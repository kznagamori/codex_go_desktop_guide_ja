package textstats

import "testing"

func TestAnalyze(t *testing.T) {
	tests := []struct {
		name  string
		input string
		want  Stats
	}{
		{"empty", "", Stats{0, 0, 0}},
		{"ascii", "abc", Stats{3, 3, 1}},
		{"japanese", "日本語", Stats{3, 9, 1}},
		{"emoji", "A😀", Stats{2, 5, 1}},
		{"combining_mark", "e\u0301", Stats{2, 3, 1}},
		{"crlf", "a\r\nb", Stats{3, 3, 2}},
		{"cr", "a\rb", Stats{3, 3, 2}},
		{"newline_only", "\n", Stats{1, 1, 2}},
		{"trailing_newline", "a\n", Stats{2, 2, 2}},
		{"space", " ", Stats{1, 1, 1}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := Analyze(tt.input); got != tt.want {
				t.Errorf("Analyze(%q) = %+v, want %+v", tt.input, got, tt.want)
			}
		})
	}
}
