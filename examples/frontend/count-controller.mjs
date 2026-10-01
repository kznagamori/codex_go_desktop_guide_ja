// Framework-independent latest-request guard; no DOM or Wails import.
// The UI supplies actual generated service bindings and render callbacks.
export function createCountController({analyze, showStats, showError, showPending}) {
    let revision = 0;
    return {
        async update(text) {
            const request = ++revision;
            showPending();
            try {
                const stats = await analyze(text);
                if (request === revision) showStats(stats);
            } catch {
                if (request === revision) showError('集計に失敗しました。もう一度入力してください。');
            }
        },
        clear() {
            ++revision;
            showStats({runes: 0, bytes: 0, lines: 0});
        },
    };
}
