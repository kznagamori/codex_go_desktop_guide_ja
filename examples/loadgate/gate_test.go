package loadgate

import (
	"errors"
	"sync"
	"testing"
)

func begin(t *testing.T, g *Gate, id string) Token {
	t.Helper()
	token, err := g.Begin(id)
	if err != nil {
		t.Fatal(err)
	}
	return token
}

func TestLatestSuccessWins(t *testing.T) {
	var g Gate
	a := begin(t, &g, "A")
	b := begin(t, &g, "B")
	if !g.Complete(b, "new B") || g.Complete(a, "old A") {
		t.Fatal("must accept B and reject late A")
	}
	if got := g.Snapshot(); got.ShowingDocument != "B" || got.Content != "new B" || got.Loading {
		t.Fatalf("unexpected view: %+v", got)
	}
}

func TestOldFailureDoesNotCancelNewRequest(t *testing.T) {
	var g Gate
	a := begin(t, &g, "A")
	b := begin(t, &g, "B")
	if g.Fail(a, "READ_FAILED") {
		t.Fatal("old error accepted")
	}
	if got := g.Snapshot(); !got.Loading || got.PendingDocument != "B" || got.ErrorCode != "" {
		t.Fatalf("old error changed pending B: %+v", got)
	}
	if !g.Complete(b, "B") {
		t.Fatal("current B was rejected")
	}
}

func TestSameDocumentGetsNewGeneration(t *testing.T) {
	var g Gate
	old := begin(t, &g, "same.md")
	fresh := begin(t, &g, "same.md")
	if old == fresh || g.Complete(old, "old") {
		t.Fatal("same document must not reuse request identity")
	}
	if !g.Complete(fresh, "fresh") || g.Snapshot().Content != "fresh" {
		t.Fatal("new result missing")
	}
}

func TestCloseRejectsLateResultsAndAllowsReopen(t *testing.T) {
	var g Gate
	old := begin(t, &g, "A")
	g.Close()
	if g.Complete(old, "late") || g.Fail(old, "late error") || g.Snapshot() != (View{}) {
		t.Fatal("closed view was changed")
	}
	fresh := begin(t, &g, "A")
	if old == fresh || g.Complete(old, "late again") || !g.Complete(fresh, "fresh") {
		t.Fatal("reopen did not invalidate old request")
	}
}

func TestCurrentFailurePreservesPreviousContent(t *testing.T) {
	var g Gate
	a := begin(t, &g, "A")
	g.Complete(a, "content A")
	b := begin(t, &g, "B")
	if !g.Fail(b, "READ_FAILED") {
		t.Fatal("current error rejected")
	}
	got := g.Snapshot()
	want := View{ShowingDocument: "A", Content: "content A", ErrorCode: "READ_FAILED"}
	if got != want {
		t.Fatalf("got %+v, want %+v", got, want)
	}
}

func TestResultIsAcceptedAtMostOnce(t *testing.T) {
	var g Gate
	a := begin(t, &g, "A")
	if !g.Complete(a, "first") || g.Complete(a, "second") || g.Fail(a, "late error") {
		t.Fatal("duplicate completion/error accepted")
	}
	if g.Snapshot().Content != "first" {
		t.Fatal("first result changed")
	}
}

func TestInvalidBeginDoesNotChangeState(t *testing.T) {
	var g Gate
	a := begin(t, &g, "A")
	before := g.Snapshot()
	if _, err := g.Begin(""); !errors.Is(err, ErrEmptyDocument) {
		t.Fatalf("got %v, want ErrEmptyDocument", err)
	}
	if g.Snapshot() != before || !g.Complete(a, "still valid") {
		t.Fatal("invalid input changed active request")
	}
}

func TestConcurrentCalls(t *testing.T) {
	var g Gate
	var wg sync.WaitGroup
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			tok, err := g.Begin("doc")
			if err != nil {
				t.Error(err)
				return
			}
			g.Complete(tok, "text")
			_ = g.Snapshot()
		}()
	}
	wg.Wait()
	if got := g.Snapshot(); got.Loading || got.ShowingDocument != "doc" || got.Content != "text" {
		t.Fatalf("unexpected final state: %+v", got)
	}
}

func TestGenerationDoesNotWrap(t *testing.T) {
	var g Gate
	g.generation = ^uint64(0)
	before := g.Snapshot()
	if _, err := g.Begin("A"); !errors.Is(err, ErrExhausted) {
		t.Fatalf("got %v, want ErrExhausted", err)
	}
	if g.Snapshot() != before {
		t.Fatal("generation exhaustion changed state")
	}
}
