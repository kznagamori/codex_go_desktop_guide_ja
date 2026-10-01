// Package loadgate demonstrates rejecting stale asynchronous load results.
// It does not cancel work, read files, manage watchers, or implement a Wails DTO.
package loadgate

import (
	"errors"
	"sync"
)

var (
	ErrEmptyDocument = errors.New("document ID must not be empty")
	ErrExhausted     = errors.New("request generation exhausted")
)

// Token identifies one in-process request. Fields deliberately are not exported:
// this is not a wire DTO or an authentication/authorization mechanism.
type Token struct {
	documentID string
	generation uint64
}

// View is a consistent copy of state. Content belongs to ShowingDocument,
// which can differ from PendingDocument while the new document is loading.
type View struct {
	ShowingDocument string
	Content         string
	PendingDocument string
	Loading         bool
	ErrorCode       string
}

// Gate's zero value is usable. Do not copy a Gate after first use.
type Gate struct {
	mu         sync.Mutex
	generation uint64
	pending    Token
	view       View
}

// Begin invalidates any previous pending request, including one for the same ID.
// It preserves the last successfully displayed content while loading.
func (g *Gate) Begin(documentID string) (Token, error) {
	if documentID == "" {
		return Token{}, ErrEmptyDocument
	}
	g.mu.Lock()
	defer g.mu.Unlock()
	// Never wrap and accidentally reuse an old generation.
	if g.generation == ^uint64(0) {
		return Token{}, ErrExhausted
	}
	g.generation++
	g.pending = Token{documentID: documentID, generation: g.generation}
	g.view.PendingDocument = documentID
	g.view.Loading = true
	g.view.ErrorCode = ""
	return g.pending, nil
}

// Complete accepts a result at most once, and only for the latest live request.
func (g *Gate) Complete(t Token, content string) bool {
	g.mu.Lock()
	defer g.mu.Unlock()
	if !g.current(t) {
		return false
	}
	g.view = View{ShowingDocument: t.documentID, Content: content}
	return true
}

// Fail only affects the current request and preserves the last successful view.
// The caller supplies a stable non-sensitive code, not raw file contents/paths.
func (g *Gate) Fail(t Token, errorCode string) bool {
	g.mu.Lock()
	defer g.mu.Unlock()
	if !g.current(t) {
		return false
	}
	if errorCode == "" {
		errorCode = "LOAD_FAILED"
	}
	g.view.PendingDocument = ""
	g.view.Loading = false
	g.view.ErrorCode = errorCode
	return true
}

// Close clears the view and rejects pending results. A later Begin creates a
// fresh generation. It does not stop any goroutine; lifecycle control is separate.
func (g *Gate) Close() {
	g.mu.Lock()
	defer g.mu.Unlock()
	g.view = View{}
	g.pending = Token{}
}

// Snapshot returns state without exposing a mutable shared object.
func (g *Gate) Snapshot() View {
	g.mu.Lock()
	defer g.mu.Unlock()
	return g.view
}

// Caller holds mu. Checking and updating must occur within the same lock.
func (g *Gate) current(t Token) bool {
	return g.view.Loading && t == g.pending
}
