# 文書テンプレート：コピー先と記入欄の更新方法

**ドキュメントバージョン：v0.0.8**  
**更新日：2026年10月1日**

**コピー元の`templates/`は編集しません。リポジトリに置いたコピー先を、明示指示を受けたCodex CLIが更新します。** ChatGPT.comで生成したidea.mdとnaming.mdは未承認のまま渡せます。承認はコピー後にCodexで行います。

## 1. 初回は6ファイルだけを配置する

| コピー元（資料または保存した2文書） | リポジトリ内のコピー先 | 今行うこと |
|---|---|---|
| 保存済みの`idea.md` | `docs/ideas/idea.md` | ChatGPTが生成した案をそのまま配置。空の雛形で上書きしない。 |
| 保存済みの`naming.md` | `docs/ideas/naming.md` | ChatGPTが生成した案をそのまま配置。承認前でも配置する。 |
| `templates/AGENTS.md` | `AGENTS.md` | 規約の雛形。本文の規約は保持する。 |
| `templates/docs/workflow/state.md` | `docs/workflow/state.md` | コピー直後は記入欄を残してよい。P04で更新。 |
| `templates/docs/workflow/questions.md` | `docs/workflow/questions.md` | P04で既存質問履歴を引継ぐ。不明を0にしない。 |
| `templates/docs/workflow/repo-map.md` | `docs/workflow/repo-map.md` | P04で実在文書の索引に更新。 |

`templates/README_ja.md`は本説明書です。リポジトリのREADMEへコピーしません。参考コード・ガイド全文・全仕様雛形を一括で置く操作も不要です。具体的な操作と補助スクリプトは[全工程のコピー手順](../02_workflow_ja.md#template-setup)、新規作業の一巡は[開始手順](../03_quickstart_ja.md)にあります。

## 2. 各ファイルをいつ、どこへ置いて、何で記入するか

コピー元はすべてこの`templates/`からの相対パスです。`TEMPLATE.md`は指定例のIDを機械的に使うのではなく、実在する計画に合わせた未使用のID名へコピーします。元のTEMPLATEは残します。同等の文書がある場合は新しい正本を作らず、その文書へ対応させます。

| コピー元 | コピー先 | 時点 | 内容を作成する入力 | 記入欄の扱い |
|---|---|---|---|---|
| AGENTS.md | AGENTS.md | 開始時 | P04 | 元の規約を維持。記入欄なしなら対象欄なし。由来のみ整える。 |
| docs/workflow/state.md | docs/workflow/state.md | 開始時 | P04 | 日時・実際のGit・現在工程。未作成taskは未作成。 |
| docs/workflow/questions.md | docs/workflow/questions.md | 開始時 | P04 | 履歴を出典付きで引継ぎ、重複排除。未知の回数は不明。 |
| docs/workflow/repo-map.md | docs/workflow/repo-map.md | 開始時 | P04 | 実在パス・版・状態。予定パスは未作成と明記。 |
| docs/ideas/idea.md | docs/ideas/idea.md | 生成済みならコピーしない | P02／P38 | 通常はChatGPTで生成した本文を配置。雛形で上書きしない。 |
| docs/ideas/naming.md | docs/ideas/naming.md | 生成済みならコピーしない | P33／P37／P34 | 通常は生成済み案を配置。P35だけが人の名称承認を記録。 |
| docs/specs/requirements.md | docs/specs/requirements.md | 全体要求 | P06 | 承認済みideaの目的・範囲・受入条件を使う。 |
| docs/specs/feature-map.md | docs/specs/feature-map.md | 機能の全体整理 | P25 | 実要求と機能ID・依存。機能数を削らない。 |
| docs/research/toolchain.md | docs/research/toolchain.md | 技術調査 | P09 | 実際の公式確認と版・コマンド。最新を推測しない。 |
| docs/specs/design.md | docs/specs/design.md | 共通設計 | P10 | 承認済み要求・採用済み構成。状態・責務を設計する。 |
| docs/specs/interfaces.md | docs/specs/interfaces.md | 共通契約 | P26 | 必要なAPI・型・状態所有。未検証の契約は案。 |
| docs/specs/nonfunctional.md | docs/specs/nonfunctional.md | 非機能の具体化 | P26 | 性能条件・保存・通信。数値の根拠と測定方法を分ける。 |
| docs/specs/features/TEMPLATE.md | docs/specs/features/F-001.md等 | 該当機能の詳細化 | P27 | 既存IDと衝突しない実際のF-IDへ改名。対象機能だけ記入。 |
| docs/workflow/slices/TEMPLATE.md | docs/workflow/slices/S-01.md等 | 小機能の計画 | P27 | 実際のS-ID、完了形、依存、結合条件。実装済みにしない。 |
| docs/workflow/tasks/TEMPLATE.md | docs/workflow/tasks/T-001.md等 | 直近タスクの計画 | P11 | 実際のT-ID。開始時刻・試験ログは未実施のまま。 |
| docs/specs/traceability.md | docs/specs/traceability.md | 追跡表の作成 | P40で根拠を転記、P31で不一致を点検 | 実在するID・文書・証拠へ対応。証拠がなければ未実施。 |
| docs/tests/test-plan.md | docs/tests/test-plan.md | 試験計画 | P18（計画のみ） | ケース・期待値・環境を定義。実行した扱いにしない。 |
| docs/tests/results.md | docs/tests/results.md | 試験の実施時 | P18（実行／結果記録） | 日時・環境・SHA・exit codeは実測だけ。未実施はNOT_RUN。 |
| docs/workflow/backlog.md | docs/workflow/backlog.md | 保留・将来案が出た時 | P22／P25 | 要求ID・保留理由。移すだけで必須範囲を削らない。 |
| docs/workflow/decisions.md | docs/workflow/decisions.md | 判断・変更がある時 | P22 | 仮説と人の決定を分け、未承認案を承認済みにしない。 |
| docs/bugs/TEMPLATE.md | docs/bugs/BUG-001.md等 | 不具合記録時 | P23 | 実際の再現・対象版と証拠。未調査の原因は仮説。 |
| docs/releases/release-checklist.md | docs/releases/release-checklist.md | 公開準備 | P20 | 実際のゲート・候補版。公開許可は別のP21。 |

**P06/P10/P11等に文書の作成を頼む場合は、その入力に対象・根拠・保存先が含まれています。** それで記入まで行うならP40を重ねて実行する必要はありません。内容を作る前に、コピー済み欄の事実部分だけを整えたい場合にP40を使います。P40を実行しただけで仕様完成にはしません。

## 3. `{...}`には2種類ある

| 種類・欄 | 誰が何をするか | 書き方の例 |
|---|---|---|
| **送信するプロンプト**の`{対象版}`・`{承認者}` | 人が送信前に記入する。承認はAIへ委任しない。 | 実際に読んだ版`r2`と自分の識別名。 |
| **コピー先の文書**の名前・OS・目的 | エージェントがidea/namingを読み、出典・状態を付けて転記する。 | `採用予定の所有者/名前（naming r1、未承認）`。 |
| Gitルート・ブランチ・HEAD・現在日時 | エージェントがコマンドで確認する。 | `初回コミット前（HEAD未作成）`は正当な値。 |
| 質問使用数 | 送信履歴から集計し、前の記録を引き継ぐ。 | 情報が足りなければ`不明（引継ぎ履歴不足）`。 |
| 未決の要求・技術・実行コマンド | 勝手に選ばない。決める工程を記録する。 | `未決（技術調査P09で決定）`。 |
| 未作成の仕様・タスク・コード | 存在を捏造しない。 | `未作成（要求工程P06で作成予定）`。 |
| 承認・試験・公開・過去の日時 | 穴埋めによる自動作成は禁止。 | `未承認`、`NOT_RUN`、`未実施`。 |
| `{ID}`・`{日時}`など同じ文字列 | それぞれの欄の意味を読んで別々に処理する。 | 要求ID、タスクID、リリースIDを同じ値にしない。 |
| `${{ ... }}`、Go/JSONの`{}`、正規表現の`{1,3}` | 構文であって記入欄ではない。保持する。 | 波括弧全体の検索置換をしない。 |

後続テンプレートをコピーする例（通常ユーザーのPowerShell、リポジトリのルートで実行）：

```powershell
$GuideRoot = 'C:\work\guides\codex_go_desktop_guide_ja_v0.0.8'
$Source = Join-Path $GuideRoot 'templates/docs/specs/requirements.md'
$Target = Join-Path (Get-Location).Path 'docs/specs/requirements.md'
if (-not (Test-Path -LiteralPath $Source -PathType Leaf)) { throw 'コピー元がありません。' }
if (Test-Path -LiteralPath $Target) { throw '既存ファイルは上書きしません。既存の要求仕様を使います。' }
[IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($Target)) | Out-Null
[IO.File]::Copy($Source, $Target, $false)
```

コピー後はP06の全文で要求仕様を作成します。コピー元をCodexから読めることを前提にせず、必要な文書を先にコピー先へ置きます。すでに要求仕様があれば、このコピー操作ではなくP39の最小修正を使用します。

## 4. コピー先の版と状態

資料の`ドキュメントバージョン：v0.0.8`は**使用テンプレートの版**へ表記を改め、プロジェクト文書版・状態は別にします。例は`使用テンプレート：開発ガイドv0.0.8（2026年10月1日）`、`プロジェクト文書版：r1`、`文書状態：REVIEW`、`承認記録：未承認`です。

初回4件のAGENTS/state/questions/repo-mapは規約・索引・台帳なので、すべてにDRAFTやAPPROVEDを一律に追加する必要はありません。仕様・設計・計画のAPPROVEDは人が対象版を確認し、CodexへP08（命名ならP35）で保存を指示したときだけです。

一部承認は承認履歴に節・範囲を残し、文書全体はREVIEWに留めます。P38に必要なのは名称3項目が承認範囲に含まれることです。形式だけで名称文書全体をAPPROVEDへ変える必要はありません。

## 5. P04・P40の終了時に見るもの

`docs/workflow/template-check.md`にファイル・欄・更新前後・根拠・未決事項と解決工程・残す記入欄の理由を保存させます。人は実ファイル・差分を確認します。未追跡ファイルはGit差分だけでは確認できないことがあるため本文も開きます。

初回のidea/namingは保護対象で、P04による穴埋め対象ではありません。名称表の内容を整えるのはP34/P39、承認はP35、ideaへの転記はP38、ideaの承認はP08です。名前を決め直したり実績を作るための一括置換は行いません。

[初回設定P04](../04_prompt_templates_ja.md#p04)／[後工程の記入P40](../04_prompt_templates_ja.md#p40)／[文書状態](../02_workflow_ja.md#document-status)
