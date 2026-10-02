# ハンズオンの参考ファイル

**ドキュメントバージョン：v0.0.8**  
**更新日：2026年10月1日**

> **参考記入例で、実入力プロンプトではありません。** 記載されたID・版・承認・試験結果を実在の記録とみなさず、対象リポジトリの文書と対応させて使います。

本資料の識別子`go_text_counter`／`go_markdown_viewer`は一般的な教材例で、利用者の正式名やGitHubで使用可能な名前を確定したものではありません。[命名工程](../02_workflow_ja.md#naming)で確認・記録し、別名への反映は[P36](../04_prompt_templates_ja.md#p36)で対象を計画します。v0.0.6では参考コード・スクリプト・workflowの実装は変更していません。

## 1. 発展演習：Markdownビューア

[発展ハンズオン](../06_hands_on_markdown_viewer_ja.md)用の記入例と限定的な参考コードです。

| ファイル | 使い方 |
|---|---|
| [markdown_viewer/idea.md](markdown_viewer/idea.md) | 承認前の引継ぎ例。実際の回答・承認を別途記録する。 |
| [markdown_viewer/S-05.md](markdown_viewer/S-05.md) | 監視を検索・履歴・文書切替と結合する小機能計画。 |
| [markdown_viewer/T-014.md](markdown_viewer/T-014.md) | 古い読込結果の拒否を扱う1作業。 |
| [loadgate/gate.go](loadgate/gate.go) | Go標準ライブラリのみの要求世代の判定例。 |
| [loadgate/gate_test.go](loadgate/gate_test.go) | 古い成功・失敗、同一文書再要求、終了、並行性など9テスト。 |

loadgateはWails DTOや認可の仕組みではありません。実I/Oの中止・監視の解除・UI接続は実装していません。コードのテスト合格とMarkdownビューア全体の動作確認を混同しません。

## 2. 基礎演習：文字数カウンター専用

**以下のworkflowsとpackage scriptsはWails v3／文字数カウンター専用です。** Wails v2などの異なる技術構成や、発展演習のMarkdownビューアへそのままコピーしません。特にCLI、Nodeビルド、Linux依存、出力bin名が違います。

これは完成済みGUIアプリではありません。[ハンズオン](../05_hands_on_text_counter_ja.md)で、自分のリポジトリに生成・実装し、実行結果を確認するための資料です。

| ファイル | コピー先／用途 |
|---|---|
| [idea_text_counter.md](idea_text_counter.md) | `docs/ideas/idea.md`。演習用の引継ぎ例。利用者の承認は未取得。 |
| [textstats/stats.go](textstats/stats.go) | `internal/textstats/stats.go`。GUIに依存しない計数ロジック参考解。 |
| [textstats/stats_test.go](textstats/stats_test.go) | `internal/textstats/stats_test.go`。10ケースの参考テスト。 |
| [workflows/ci.yml](workflows/ci.yml) | `.github/workflows/ci.yml`。実装・配布文書が揃った段階の参考例。 |
| [workflows/release.yml](workflows/release.yml) | `.github/workflows/release.yml`。タグから再利用CIを呼び、Draftを作成。 |
| [scripts/package-linux.sh](scripts/package-linux.sh) | `scripts/package-linux.sh`。binの実行ファイルと必要文書をtar.gz化。 |
| [scripts/package-windows.ps1](scripts/package-windows.ps1) | `scripts/package-windows.ps1`。PowerShell 7でZIP化。 |

## フロントエンドの小さな回帰試験

[frontend/count-controller.mjs](frontend/count-controller.mjs)と[対応テスト](frontend/count-controller.test.mjs)は、`frontend/src/`へ配置する参考例です。Node標準のテスト機能を使い、GUIやWailsを起動せず、応答順序・クリア・エラーを確認します。画面側の入力欄のクリアとDOM更新、実際のWails接続は別途実装・確認が必要です。

## 参考CIを適用する前提

アプリ識別子とbin名は`go_text_counter`、CPUはamd64です。名前を変える場合は生成Taskfile、パッケージスクリプト、artifact名を一緒に確認してください。

リポジトリに`.go-version`、`.node-version`、`.wails-version`、go.mod/go.sum、frontend/package-lock.json、内部ロジックとテスト、生成Wails Taskfileが必要です。パッケージングには`README.md`、利用者が確認した`LICENSE`、実依存に基づく`THIRD_PARTY_NOTICES.md`、`docs/user-guide.md`が必要です。Draft Releaseには`docs/releases/notes.md`も必要です。

依存導入は`npm ci`を使うよう生成タスクを確認・必要最小限修正します。`wails3 build`が、その後に`npm install`でlockfileを書き換える設定を残さないでください。Go moduleとCLIのWails版も一致させます。

最初のGUI生成直後にこの完成形CIをそのまま入れると、まだ存在しない内部テストや配布文書で失敗します。最初はcheckout、固定版導入、依存、ビルドだけのCIで確認し、H18で完成形へ拡張します。

## Actionsの版と権限

例の`@v7`は確認した公式メジャー版を示す教育用の可変タグです。そのまま公開用の最終固定値にはしません。CodexのP19で公式リポジトリとタグのcommitを照合して固定案を記録し、人の承認後にP12のCIタスクで完全SHAと版コメントを反映します。SHAを推測して書いてはいけません。[S19〜S23](../07_official_sources_ja.md#s19)

通常の検査はread権限です。release.ymlのDraft作成jobだけにcontents:writeとactions:readを与えます。個人PATを例として埋め込んでいません。タグpushによりGitHub側のビルドとDraft作成が開始されますが、公開は自動化していません。

`gh run download`ではrun IDとartifact名を指定します。「最新の成功ビルド」を無条件に使いません。`gh release create --verify-tag --draft`で既存タグを確認し、既存Releaseがある場合は上書きせず止めます。[S24](../07_official_sources_ja.md#s24) [S28](../07_official_sources_ja.md#s28)

## スクリプトの注意

両スクリプトはアプリのルートから実行します。環境変数`BUILD_VERSION`を設定します。配布に必要なファイルがない場合と、同名のアーカイブが既にある場合は失敗します。既存成果物の削除を自動化していません。

Linuxスクリプトが削除するのは、自分で作った一時ステージングディレクトリだけです。Windowsスクリプトも同様です。生成したアーカイブはdistに残ります。

Linux tar.gzは実行権限を保持します。Windows ZIPはPowerShell 7を想定します。アーカイブにバイナリ、利用説明、ライセンス、依存通知、VERSION.txtだけを入れ、リポジトリや秘密情報一式を添付しません。

固定版・ロックファイル・Actions SHAは環境変動を減らすためのものです。OSパッケージやrunnerイメージ等も変わるため、ここではビット単位の再現可能ビルドを保証していません。

## 作成時点の検証

純粋なGo計数ロジック、文書構造、参照スクリプトの確認結果は、同梱の[検証記録](../08_validation_ja.md)を参照してください。**Wails GUI全体、Windows実行、GitHub Actions実行は資料作成環境では未実施**です。参考YAMLがパースできることは、GitHub上で完走したことではありません。
