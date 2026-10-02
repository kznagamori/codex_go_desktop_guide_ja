# v0.0.7の文書監査記録

**ドキュメントバージョン：v0.0.9**  
**更新日：2026年10月2日**

## 1. 対象と結論

v0.0.6の全80件のMarkdownを、今回の入力場所・コピー・記入欄・承認保存という観点で点検しました。すべての技術記述を新しい依存版で動作確認したという意味ではありません。P35失敗の実行ログは未提供のため、特定モデルの不具合や再現結果を断定しません。

主な変更は、ChatGPTの承認入力を廃して2文書生成後にCodexへ移すこと、6ファイルを配置してP04へ記入を依頼すること、全22テンプレートの使用時点を明示することです。後工程の補助P40を追加しました。候補一覧を承認用の正式表にしたことにせず、P34で対応表を保存してからP35へ進めます。

## 2. 確認したファイル

| v0.0.6から確認したファイル | 今回の点検・処置 |
|---|---|
| `00_README_ja.md` | 今回の変更・参照・検証範囲を更新。過去履歴は過去の記録として保持。 |
| `01_scale_review_ja.md` | 役割・参照の整合を確認。教材固有の仕様は維持。 |
| `02_workflow_ja.md` | 引継ぎ・環境切替・コピー・記入欄・承認保存を本文と全文入力で修正。 |
| `03_quickstart_ja.md` | 引継ぎ・環境切替・コピー・記入欄・承認保存を本文と全文入力で修正。 |
| `04_prompt_templates_ja.md` | 引継ぎ・環境切替・コピー・記入欄・承認保存を本文と全文入力で修正。 |
| `05_hands_on_text_counter_ja.md` | 引継ぎ・環境切替・コピー・記入欄・承認保存を本文と全文入力で修正。 |
| `06_hands_on_markdown_viewer_ja.md` | 引継ぎ・環境切替・コピー・記入欄・承認保存を本文と全文入力で修正。 |
| `07_official_sources_ja.md` | 今回の変更・参照・検証範囲を更新。過去履歴は過去の記録として保持。 |
| `08_validation_ja.md` | 今回の変更・参照・検証範囲を更新。過去履歴は過去の記録として保持。 |
| `09_revision_history_ja.md` | 今回の変更・参照・検証範囲を更新。過去履歴は過去の記録として保持。 |
| `examples/README_ja.md` | 役割・参照の整合を確認。教材固有の仕様は維持。 |
| `examples/idea_text_counter.md` | 役割・参照の整合を確認。教材固有の仕様は維持。 |
| `examples/markdown_viewer/S-05.md` | 役割・参照の整合を確認。教材固有の仕様は維持。 |
| `examples/markdown_viewer/T-014.md` | 役割・参照の整合を確認。教材固有の仕様は維持。 |
| `examples/markdown_viewer/idea.md` | 役割・参照の整合を確認。教材固有の仕様は維持。 |
| `prompts/C0_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P01_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P02_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P03_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P04_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P05_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P06_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P07_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P08_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P09_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P10_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P11_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P12_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P13_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P14_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P15_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P16_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P17_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P18_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P19_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P20_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P21_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P22_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P23_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P24_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P25_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P26_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P27_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P28_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P29_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P30_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P31_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P32_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P33_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P34_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P35_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P36_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P37_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P38_sync_idea_naming_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/P39_prompt_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `prompts/README_ja.md` | 対応する共通本文から再出力。入力先・記入欄・保存方法を照合。 |
| `templates/AGENTS.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/README_ja.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/bugs/TEMPLATE.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/ideas/idea.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/ideas/naming.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/releases/release-checklist.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/research/toolchain.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/specs/design.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/specs/feature-map.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/specs/features/TEMPLATE.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/specs/interfaces.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/specs/nonfunctional.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/specs/requirements.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/specs/traceability.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/tests/results.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/tests/test-plan.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/workflow/backlog.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/workflow/decisions.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/workflow/questions.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/workflow/repo-map.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/workflow/slices/TEMPLATE.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/workflow/state.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `templates/docs/workflow/tasks/TEMPLATE.md` | 初回／後工程の分類、コピー先と記入の担当、承認・未知値を確認。 |
| `validation/review_v0.0.6_ja.md` | 過去監査として保持。現行手順と区別。 |

## 3. 新しい資料と検査

P40単独プロンプト、コピー補助と説明、この監査記録を追加しています。現在のMarkdown件数・入力数・内部リンク・フェンス等は`document-check.json`、破損を検出する負試験は`negative-check-v0.0.7.json`を参照してください。検査スクリプトの成功は、モデルが同じ動作をする保証ではありません。

PowerShellのコピー補助は実行していません。コピー元・先6項目、上書き拒否・PlanOnly・UTF-8・hash照合の実装をテキストとして確認したのみです。実アプリ10ファイルのバイト一致を維持しています。利用者のリポジトリ・GitHubには変更を行っていません。
