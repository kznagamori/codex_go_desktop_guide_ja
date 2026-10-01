# 公式資料・確認対象・技術プロファイル

**ドキュメントバージョン：v0.0.7**  
**更新日：2026年10月1日**

**引き継いだ技術情報の確認基準日：2026年9月25日・30日（各項目を参照）**

## 1. 確認記録の扱い

v0.0.6は文書・入力例の整合性を点検した版です。この章の外部URL、依存版、CLIの導入・実行結果を新たに確認した版ではありません。各項目の過去の確認日と、利用時に行う採用確認を区別してください。

v0.0.3では命名に関するS36〜S42を2026年10月1日に追加確認しました。個別候補の検索・名前の取得可否の実証はしていません。

この章のS01〜S34は、v0.0.1以前から引き継いだ公式資料の参照先と確認記録です。技術情報の確認基準日は各項目に記載しています。**v0.0.2ではMarkdownによるプロンプト構造化についてS35だけを新たに確認しました。固定タグ、依存版、全Actionsタグ、その他のURLの再調査はしていません。** 過去の確認記録を今回新たに検証した事実として扱いません。

本番の採用版は、導入する時点の公式資料、CLIヘルプ、固定タグ、生成物、実ビルドで照合します。演習の固定環境を「利用時点の最新」と読み替えません。固定版が利用できない、説明と現物が異なるなどの場合は、変更を別タスクとして承認してから修正します。

特定のアプリ・リポジトリの構成、文書数、試験件数は本ガイドの要求にしていません。規模の説明は一般的な機能群・状態共有・配布要件に置き換えています。Go、Codex CLI、Wailsなどは実際の操作に必要な技術名として残します。

## 2. 三つのプロファイル

| 項目 | 本番の共通手順 | Markdownビューア発展演習 | 文字数カウンター基礎演習 |
|---|---|---|---|
| 目的 | 複数機能を持つアプリを段階開発 | 複数機能の結合練習 | CLI・小タスクの基本練習 |
| GUI | 要求と既存構成で決定 | Wails v2.15.0候補 | Wails v3.0.0-beta.25固定 |
| Go | 現物の依存を満たす版を承認 | 1.27.1候補、実ビルドで確認 | 基礎演習の固定版1.27.1 |
| frontend build | なし／ありを明記 | なし | Node.js 24.21.0と標準vanilla |
| Linux | 採用GUIによる | GTK3/WebKitGTK4.1 | GTK4/WebKitGTK6.0標準構成 |
| CLI／出力 | 現物を確認 | wails／build/bin | wails3／bin |
| CPU | 利用者の要求に合わせる | amd64 | amd64 |

本番の技術構成は利用者の要求と既存資産から決定します。演習の依存版・CPU・機能範囲を自動採用しません。

引き継いだ2026年9月30日の確認記録では、Wails v3はBetaです。v2とv3ではCLI・Linux標準依存が異なります。[S07](#s07) [S32](#s32)

## 3. ガイド独自の運用

質問8問／初期12問通算、命名質問3問をその内数で管理、候補10案・確認3案・見直し1回5案、1タスク、直近3〜5作業、10〜30分の停止枠、同一原因の修正2回、文書配置・承認ゲートは本ガイドの提案です。OpenAIの上限や公式推奨値ではなく、品質・所要時間・完成の保証でもありません。

S31の実行計画からは、永続する進捗・決定・検証・再開情報の考え方を参考にしました。記事中の「次のマイルストーンへ自律的に継続」「頻繁なcommit」といった運用を、そのまま採用していません。本ガイドでは利用者の希望に合わせ、1タスクで止まり、Gitの書込み操作は明示承認に限定します。

## 4. 基礎演習で参照する公式資料 S01〜S30

<a id="s01"></a>

### S01. Codex CLI

[Codex CLI](https://developers.openai.com/codex/cli/)

確認した点：導入、起動、ChatGPTアカウントによるサインイン。開発者向け旧URLからlearn.chatgpt.comへリダイレクトされる場合がある。

<a id="s02"></a>

### S02. Codex CLI：コマンド・スラッシュコマンド

[Codex CLI：コマンド・スラッシュコマンド](https://learn.chatgpt.com/docs/developer-commands?surface=cli)

確認した点：sandbox/approval、resume、/plan、/statusなど。本番手順は少数のコマンドに絞る。ChatGPT.comのコマンドとCLIのコマンドは別。実際の版のヘルプも確認する。

<a id="s03"></a>

### S03. AGENTS.md

[AGENTS.md](https://developers.openai.com/codex/guides/agents-md/)

確認した点：指示の探索、優先関係、サイズ制限。通常のdocsがすべて自動読込みされるという意味ではない。

<a id="s04"></a>

### S04. Codex best practices

[Codex best practices](https://developers.openai.com/codex/learn/best-practices)

確認した点：明確な依頼、関連コンテキスト、検証、再利用できるリポジトリ指示。質問数や時間枠の数値は本ガイド独自。

<a id="s05"></a>

### S05. Codex Windows sandbox

[Codex Windows sandbox](https://developers.openai.com/codex/windows/)

確認した点：Windowsネイティブのsandbox。elevated設定は作業を常時管理者・無制限で実行する指定ではない。

<a id="s06"></a>

### S06. Codex on WSL

[Codex on WSL](https://learn.chatgpt.com/docs/windows/wsl)

確認した点：WSLでのCLI利用。ネイティブWindows側の設定・実行環境とは分けて扱う。

<a id="s07"></a>

### S07. Wails v3 status / roadmap

[Wails v3 status / roadmap](https://v3.wails.io/status/)

確認した点：確認時点はBeta。GTK4/WebKitGTK 6.0が標準。Go 1.25+の案内。

<a id="s08"></a>

### S08. Wails releases

[Wails releases](https://github.com/wailsapp/wails/releases)

基礎演習の固定版v3.0.0-beta.25を文字数カウンター教材に保持する。2026-09-30時点の最新リリースと断定するための記録ではない。stableと表現しない。

<a id="s09"></a>

### S09. Wails v3 installation

[Wails v3 installation](https://v3.wails.io/getting-started/installation/)

確認した点：Windows WebView2、Linux依存関係、doctor。確認ページの更新日は2026-09-22。

<a id="s10"></a>

### S10. Wails beta.25 go.mod

[Wails beta.25 go.mod](https://raw.githubusercontent.com/wailsapp/wails/v3.0.0-beta.25/v3/go.mod)

確認した点：固定タグのgo.modにgo 1.25.0。最低版は一般記事より実際の固定依存を優先して照合。

<a id="s11"></a>

### S11. Wails first app

[Wails first app](https://v3.wails.io/getting-started/your-first-app/)

確認した点：生成プロジェクト、Taskfile、frontend、buildディレクトリ。

<a id="s12"></a>

### S12. Wails v3 CLI reference

[Wails v3 CLI reference](https://v3.wails.io/reference/cli/)

確認した点：wails3 init、vanillaテンプレート、wails3 version、task、出力先bin。

<a id="s13"></a>

### S13. Wails building

[Wails building](https://v3.wails.io/guides/build/building/)

確認した点：build/dev/package、GOOS/GOARCH。生成済みTaskfileが具体的な処理を定義する。

<a id="s14"></a>

### S14. Wails Linux build / packaging

[Wails Linux build / packaging](https://v3.wails.io/guides/build/linux/)

確認した点：Linuxのビルド・配布・ランタイム依存。アーカイブ配布と完全同梱配布を混同しない。

<a id="s15"></a>

### S15. Wails service tutorial

[Wails service tutorial](https://v3.wails.io/tutorials/01-creating-a-service/)

確認した点：Goサービス登録とフロントエンドへの公開。実際の生成バインディングを参照する。

<a id="s16"></a>

### S16. Go downloads

[Go downloads](https://go.dev/dl/)

確認した点：調査時点の安定版Go 1.27.1。ハンズオンのtoolchainに採用。

<a id="s17"></a>

### S17. Node.js releases

[Node.js releases](https://nodejs.org/en/about/previous-releases)

確認した点：調査時点でNode 24がLTS、Latest LTS表記は24.21.0。Node 26 Currentと混同しない。

<a id="s18"></a>

### S18. GitHub-hosted runners

[GitHub-hosted runners](https://docs.github.com/en/actions/reference/runners/github-hosted-runners)

確認した点：windows-2025、ubuntu-24.04、ubuntu-26.04のラベル。Windows runnerはWindows 11デスクトップ実機ではない。

<a id="s19"></a>

### S19. actions/checkout

[actions/checkout](https://github.com/actions/checkout)

確認した点：確認時点のメジャー例v7。実運用では完全なcommit SHAへ固定する。

<a id="s20"></a>

### S20. actions/setup-go

[actions/setup-go](https://github.com/actions/setup-go)

確認した点：確認時点のメジャー例v7。go-version-file、キャッシュ。

<a id="s21"></a>

### S21. actions/setup-node

[actions/setup-node](https://github.com/actions/setup-node)

確認した点：確認時点のメジャー例v7。node-version-fileと依存ロックのキャッシュ。

<a id="s22"></a>

### S22. actions/upload-artifact

[actions/upload-artifact](https://github.com/actions/upload-artifact)

確認した点：確認時点のメジャー例v7。成果物名、ファイル不在時失敗、アーカイブ化による権限保持。

<a id="s23"></a>

### S23. GitHub Actions secure use

[GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use)

確認した点：最小権限、完全SHA固定、信頼しないコードとsecretの分離。

<a id="s24"></a>

### S24. gh release create

[gh release create](https://cli.github.com/manual/gh_release_create)

確認した点：--draft、--prerelease、--verify-tag。指定タグがないまま作成する挙動を避ける。

<a id="s25"></a>

### S25. WSL GUI applications

[WSL GUI applications](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)

確認した点：WSL2でLinux GUIを実行する構成。通常のUbuntuデスクトップでの受入試験とは区別。

<a id="s26"></a>

### S26. Go unicode/utf8

[Go unicode/utf8](https://pkg.go.dev/unicode/utf8)

確認した点：RuneCountInString。コードポイント数と見た目の文字数は異なる。

<a id="s27"></a>

### S27. Go vulnerability management

[Go vulnerability management](https://go.dev/doc/security/vuln/)

確認した点：govulncheck等による脆弱性確認。検出なしが安全性全体の保証ではない。

<a id="s28"></a>

### S28. gh run download

[gh run download](https://cli.github.com/manual/gh_run_download)

確認した点：run ID・artifact名・出力先を指定して、特定のCI実行の成果物を取得する。

<a id="s29"></a>

### S29. Wails beta.25：Apt依存パッケージ定義

[固定タグのapt.go](https://raw.githubusercontent.com/wailsapp/wails/v3.0.0-beta.25/v3/internal/doctor/packagemanager/apt.go)

確認した点：標準のlibgtk-4-dev、libwebkitgtk-6.0-dev、build-essential、pkg-config。GTK3/4.1はlegacy/optional。npmはaptパッケージとして判定するため、バージョン管理ツールで導入したnpmは実コマンドでも確認する。

<a id="s30"></a>

### S30. Ubuntu 24.04：WebKitGTK 6.0ランタイム

[Ubuntu packages：libwebkitgtk-6.0-4](https://packages.ubuntu.com/noble/libwebkitgtk-6.0-4)

確認した点：Ubuntu 24.04でのランタイムパッケージ名と関連依存。-devを必要とする開発環境とは区別する。バージョンはセキュリティ更新されるため、このランタイムを古い版へ固定する運用にはしない。


## 5. 共通の作業管理・発展演習で参照する公式資料

<a id="s31"></a>
### S31. 永続的な実行計画

[OpenAI Cookbook: Using PLANS.md for multi-hour problem solving](https://developers.openai.com/cookbook/articles/codex_exec_plans)

引き継いだ確認日：2026-09-30。作業の目的、進捗、発見、決定、検証、再開可能な記録の扱いを参照。ファイル名だけで特殊機能が働くという意味ではない。本ガイドは独自の短時間・承認付き運用へ適用する。

<a id="s32"></a>
### S32. Wails v2の導入

[Wails v2 Installation](https://wails.io/docs/gettingstarted/installation/)

引き継いだ確認日：2026-09-30。Go経由のCLI導入、doctor、WebView2、LinuxのGTK3とWebKitGTK、Ubuntu 24.04の4.1系と`-tags webkit2_41`の注意を確認。ページの最低Go版だけで採用依存すべてがビルド可能と判断しない。

<a id="s33"></a>
### S33. Wails v2のCLI

[Wails v2 CLI](https://wails.io/docs/reference/cli/)

引き継いだ確認日：2026-09-30。ページ表示版v2.15.0。`wails init`の名前・生成先・テンプレート、`wails build`などの実コマンドを確認。v3のCLIをこのプロジェクトへ混ぜない。

<a id="s34"></a>
### S34. Wails v2の設定

[Wails v2 Project Config](https://wails.io/docs/reference/project-config/)

引き継いだ確認日：2026-09-30。wails.json、frontend導入/ビルド/dev設定、assetdir等を確認。設定を空にしただけで埋込み対象や古いdistが自動的に正しくなるわけではなく、実コードのembedと配信経路を一致させる。


<a id="s35"></a>
### S35. Markdownでプロンプトの区切りを示す

[OpenAI API: Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)

v0.0.2での確認日：2026-09-30。Markdownの見出しとリストが、プロンプト内の区切りや階層を示し、開発時の読みやすさにも役立つという説明を確認しました。本文の指示と参照する内容を分ける考え方を、本ガイドの実入力文へ適用しています。

これは一般的なプロンプト設計の説明です。Codex CLIに専用のMarkdownモードがある、特定の書式だけが必須、Markdownが他の形式より必ず高精度、という根拠にはしません。このガイド独自の質問予算・停止枠・承認ルールは変更しません。v0.0.2の編集では、旧本文の指示を保持した構造化を検査しており、モデルの応答品質を比較する実験は行っていません。

## 6. v0.0.3の命名工程で追加確認した公式資料

以下の確認日は**2026年10月1日**です。S01〜S35の依存版・導入コマンドを再検証したことを意味しません。また、候補の実際の空き・同名ソフト・商標を本資料の作成時に調べた記録ではありません。

<a id="s36"></a>
### S36. GitHub：リポジトリの作成と名前の条件

[Creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)

所有者、リポジトリ名、公開範囲、初期ファイルの選択を確認しました。名前は100文字以内で、ASCII英字・数字・`.`・`-`・`_`を使用します。既存のローカルリポジトリを取り込む場合は、GitHub側でREADME等を事前生成しない案内も参照しました。命名の承認と、作成・公開範囲の決定を本ガイドでは分離します。

<a id="s37"></a>
### S37. GitHub：リポジトリの検索

[Searching for repositories](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)

`in:name`、`user:`、`org:`、`repo:owner/name`の検索範囲を確認しました。検索結果と作成時の可否判定は別に記録し、見つからないことを名前の予約や権利上の使用可能性の根拠にしません。

<a id="s38"></a>
### S38. GitHub：リポジトリの改名

[Renaming a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository)

改名後のリダイレクト、ローカルremote更新、PagesのURL、改名対象リポジトリで公開したActionへの参照の例外を確認しました。旧名を再利用するとリダイレクトが失われる注意も参照しています。公開済みの名前は一括文字列置換だけで移行済みとしません。

<a id="s39"></a>
### S39. Go：module名とソース位置

[Managing dependencies — Naming a module](https://go.dev/doc/modules/managing-dependencies#naming-a-module)

moduleパスがimportパスの接頭辞となること、可能ならリポジトリ位置を使うこと、公開位置が未定の場合の扱いを確認しました。本ガイドの`github.com/{owner}/{repo}`はGitHubのルートに単一moduleを置く新規v0/v1の例です。アプリ表示名・実行ファイル名とmoduleパスを同じものとして扱いません。

<a id="s40"></a>
### S40. Microsoft：Windowsのファイル・パス命名

[Naming Files, Paths, and Namespaces](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file)

Windowsの予約名・予約文字・末尾の空白やピリオド、大小文字の扱いを確認しました。`CON`等は拡張子を付けても予約名です。これは実行ファイル名とフォルダー名の確認に使用し、GUIの表示名へ同じ制限を機械的に適用しません。

<a id="s41"></a>
### S41. GitHub：404はリポジトリ不在の証明ではない

[Troubleshooting the REST API](https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api)

適切に認証されていない非公開リソースへのアクセスでも404が返る説明を確認しました。名前候補の調査では、APIの404や閲覧不能をそのまま空き判定に使用しません。

<a id="s42"></a>
### S42. WIPO：商標の検索範囲と追加確認

[Global Brand Database](https://www.wipo.int/en/web/global-brand-database)

収録する商標情報と、国・地域の登録簿の検索や専門家への相談も検討するという案内を確認しました。一般Web検索や一つのデータベースだけで、世界中での名称の未使用・法的な安全を保証しません。本資料は商標の個別評価や登録代行を行うものではありません。

## 7. v0.0.5で確認したファイルの受け渡し・編集

確認日：**2026年10月1日**。この追加確認は文書の受け渡し・保存の説明のためであり、既存のGo・Wails・Node・Actions等の版を再調査・更新した記録ではありません。

<a id="s43"></a>
### S43. ChatGPTのファイルアップロード

[File Uploads FAQ](https://help.openai.com/en/articles/8555545-file-uploads-faq)

会話へ文書をアップロードして内容を扱う方法を確認しました。本ガイドでは同じチャットの明示したidea.md、実際に添付した最新版、または貼り付けた本文を使います。ローカル編集用の接続は使わず、ChatGPTの更新出力をユーザーがPCへ保存・再読込みする手順です。PCのパスを文章に書くだけで内容を渡したことにはしません。プラン別の上限やUI位置を固定した案内にはしていません。

### S01・S03の補足確認

[Codex CLI](https://developers.openai.com/codex/cli/)と[AGENTS.md](https://developers.openai.com/codex/guides/agents-md/)を確認しました。Codexの作業ディレクトリ内でのファイル調査・編集と適用指示を前提に、対象ファイル・変更範囲・保存確認を指定します。権限のある環境で実際に保存できたかは実ファイルと差分で確認します。

DRAFT／REVIEW／APPROVEDやP08/P35、承認履歴の書式は**このガイドの文書管理ルール**です。OpenAI製品の組み込み状態遷移・認証・電子署名を示す名称ではありません。エージェントが独自判断でAPPROVEDにすることを、公式機能として説明しません。

## 8. 個別プロジェクトの情報を記録する場所

実際の開発対象を調べるときは、そのプロジェクトの`docs/workflow/repo-map.md`へリポジトリ、対象コミット、確認した範囲を記録し、`docs/research/toolchain.md`へ採用版と公式根拠を残します。一般的な手順書へ特定のアプリの構成を固定せず、対象プロジェクト側で根拠を管理してください。

個別の候補・正式名称・確認したURL・日時・未確認・人の承認は、そのプロジェクトの`docs/ideas/naming.md`（または既存の正本）へ記録します。

READMEに書かれていること、実装を読んで確認したこと、CIに定義されていること、実際に動かして合格したことは、それぞれ区別します。外部情報の確認を省略した場合は「未確認」と記録します。

## 9. v0.0.7で再確認したCodexの実ファイル操作と指示の読込み

確認日：2026年10月1日。今回確認したのは次の操作範囲で、Go・Wails・Node・Actionsの採用版やライブラリの再調査ではありません。

<a id="s45"></a>
### S45. Codex CLIとAGENTS.mdの読込み時点

[Codex CLI](https://developers.openai.com/codex/cli/)／[Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md/)

公式CLI資料では、指定ディレクトリを作業場所にしてローカルのコードを読み、変更し、コマンドを実行する流れを説明しています。AGENTS.md資料では、作業開始前に指示を読み、起動時に指示の連なりを構築する説明があります。P04でコピーしたAGENTS.mdを変更した場合、このガイドは新規セッションを同じ作業ルートで開始し、C0を再入力してから次へ進む運用にしました。resumeで続行することと、新しい指示読込みを同一視しません。

テンプレートのP04/P40、DRAFT／REVIEW／APPROVED、引継ぎ手順は本ガイド独自の運用です。公式の自動承認機能や署名を示しません。権限不足や入力不足で保存できない場合は、未保存として止めます。
