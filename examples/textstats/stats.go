// Package textstats contains GUI-independent counting rules for the tutorial.
package textstats

import (
	"strings"
	"unicode/utf8"
)

// Stats counts Unicode code points, UTF-8 bytes, and lines after LF normalization.
// Runes is not a count of user-perceived grapheme clusters.
type Stats struct {
	Runes int `json:"runes"`
	Bytes int `json:"bytes"`
	Lines int `json:"lines"`
}

// Analyze accepts text from the application's text input. It does not mutate,
// save, log, or send that text. Empty input has zero lines.
func Analyze(text string) Stats {
	normalized := strings.ReplaceAll(text, "\r\n", "\n")
	normalized = strings.ReplaceAll(normalized, "\r", "\n")
	if normalized == "" {
		return Stats{}
	}
	return Stats{
		Runes: utf8.RuneCountInString(normalized),
		Bytes: len(normalized),
		Lines: strings.Count(normalized, "\n") + 1,
	}
}
