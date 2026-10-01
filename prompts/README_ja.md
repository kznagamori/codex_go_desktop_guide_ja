# 単独で入力できる共通プロンプト

**ドキュメントバージョン：v0.0.7**  
**更新日：2026年10月1日**

1ファイルに1つの全文入力を収録しています。外側のコードフェンスを除いた本文をコピーします。共通集・ハンズオンの全文入力と同時に重複送信しません。

ChatGPT.comはP01・P02とP33またはP37までです。生成した2文書をPCへ配置した後、CodexでC0→P04を行います。P34・P35・P38・P08はCodexです。P04は初回4テンプレート、P40は後でコピーした文書の補助的な記入です。

プロンプトの`{...}`はユーザーが送信前に置き換えます。コピー済みファイルの`{...}`は指定を受けたエージェントが更新します。承認・試験結果・未知の仕様は自動で作りません。

| ID | 依頼 | 入力先 |
|---|---|---|
| [C0](C0_prompt_ja.md) | このセッションの進め方 | Codex CLI |
| [P01](P01_prompt_ja.md) | ChatGPT.comでアイデアを整理する | ChatGPT.com |
| [P02](P02_prompt_ja.md) | アイデアを引継ぎファイルにまとめる | ChatGPT.com |
| [P03](P03_prompt_ja.md) | 質問や提案が広がったときに止める | ChatGPT.com／Codex CLI（質問を止める環境） |
| [P04](P04_prompt_ja.md) | コピー済みの初期テンプレートを実値で整える | Codex CLI |
| [P05](P05_prompt_ja.md) | アイデアの受け取りを確認する | Codex CLI |
| [P06](P06_prompt_ja.md) | 全体要求の骨格を作る | Codex CLI |
| [P07](P07_prompt_ja.md) | 文書をレビューする | Codex CLI |
| [P08](P08_prompt_ja.md) | 確認した文書を承認し、承認記録を更新する | Codex CLI |
| [P09](P09_prompt_ja.md) | 技術構成を公式情報で確認する | Codex CLI |
| [P10](P10_prompt_ja.md) | 全体設計の骨格を作る | Codex CLI |
| [P11](P11_prompt_ja.md) | 直近の作業だけ細分化する | Codex CLI |
| [P12](P12_prompt_ja.md) | 1タスクだけ実行する | Codex CLI |
| [P13](P13_prompt_ja.md) | 変更差分をレビューする | Codex CLI |
| [P14](P14_prompt_ja.md) | 指摘された範囲だけ直す | Codex CLI |
| [P15](P15_prompt_ja.md) | 途中でも保存して止める | Codex CLI |
| [P16](P16_prompt_ja.md) | 文書と実状態を照合して再開する | Codex CLI |
| [P17](P17_prompt_ja.md) | 突然終了から復旧する | Codex CLI |
| [P18](P18_prompt_ja.md) | テスト計画・実施記録を整備する | Codex CLI |
| [P19](P19_prompt_ja.md) | 採用技術に合わせたCIの計画を作る | Codex CLI |
| [P20](P20_prompt_ja.md) | リリースを準備するが公開しない | Codex CLI |
| [P21](P21_prompt_ja.md) | 人が公開に関する1操作を承認する | Codex CLI |
| [P22](P22_prompt_ja.md) | 要求変更を扱う | Codex CLI |
| [P23](P23_prompt_ja.md) | バグを再現して最小修正へつなぐ | Codex CLI |
| [P24](P24_prompt_ja.md) | 既存リポジトリの規模と正本を調べる | Codex CLI |
| [P25](P25_prompt_ja.md) | 製品全体の機能地図とリリース範囲を作る | Codex CLI |
| [P26](P26_prompt_ja.md) | 共有契約と横断的リスクを決める | Codex CLI |
| [P27](P27_prompt_ja.md) | 次の一つの小機能を実装可能にする | Codex CLI |
| [P28](P28_prompt_ja.md) | 小機能を結合して既存機能への影響を見る | Codex CLI |
| [P29](P29_prompt_ja.md) | リリース全体の完成度を証拠で評価する | Codex CLI |
| [P30](P30_prompt_ja.md) | 依存・同梱資産だけを更新する | Codex CLI |
| [P31](P31_prompt_ja.md) | 仕様・コード・試験のずれを点検する | Codex CLI |
| [P32](P32_prompt_ja.md) | 既存の文書と履歴を保持して、必要な作業管理だけを整える | Codex CLI |
| [P33](P33_prompt_ja.md) | 未決の名前について候補を作る | ChatGPT.com |
| [P34](P34_prompt_ja.md) | 名前の必要な確認だけを行う | Codex CLI |
| [P35](P35_prompt_ja.md) | 確認した正式な名前の対応表を承認する | Codex CLI |
| [P36](P36_prompt_ja.md) | 名前の実物照合と最小の反映計画を作る | Codex CLI |
| [P37](P37_prompt_ja.md) | 決定済みの名前を記録する。候補は作らない | ChatGPT.com |
| [P38](P38_sync_idea_naming_ja.md) | 承認済みのアプリ名・GitHubリポジトリ名をidea.mdへ反映する | Codex CLI |
| [P39](P39_prompt_ja.md) | 指摘に基づいて文書だけを最小修正する | Codex CLI |
| [P40](P40_prompt_ja.md) | 後の工程でコピーしたテンプレートの記入欄を整理する | Codex CLI |

[全体の使い分け](../04_prompt_templates_ja.md#naming-route)／[コピーするファイル一覧](../templates/README_ja.md)
