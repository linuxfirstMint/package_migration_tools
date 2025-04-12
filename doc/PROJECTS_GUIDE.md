# GitHub Projects 運用ガイド

このドキュメントは、本リポジトリで使用する GitHub Projects v2 の運用ルールをまとめたものです。

---

## 📌 目的

- タスクの可視化と優先順付け
- issue/プルリクエス と連携した進捗管理
- CLI ツールとの連携による省力化

---

## 🧬 カードの流れとステータス

| ステータス  | 意味                                            |
| ----------- | ----------------------------------------------- |
| Backlog     | 構想中・未着手の候補タスク (未 issue 化でも OK) |
| Todo        | issue 化された実行タスク (着手前)               |
| In Progress | 実装中のタスク (PR や ブランチと連動)           |
| Done        | 完了済みのタスク (PR マージ、レビュー終了)      |

---

## 🏷 カスタムフィールド

### Priority

- High / Medium / Low

### Type

- Task (実装・整備タスク)
- Docs (ドキュメント依存)
- Bug / Feature (拡張用)

---

## 📂 命名規則

- issue タイトルは `[task]`, `[bug]`, `[feature]` などのプリフィックスを付ける
- 複数単語はケバブケース or 空白区切り OK

---

## 🔁 自動化/スクリプト連携

- `.github/scripts/` 配下の `gh-project-scripts` を submodule として利用する
- `project-create.sh` `project-fields.sh` `project-delete.sh` などが用意されている

---

## 🧰 運用パターン

1. `task_template.md` から issue を作成
2. Projects の `Todo` にカード登録
3. Status を使って進捗管理
4. 完了後 `Done` に移動、クローズ

---

## 🔺 備考

- 運用ガイドは階段的に最適化します
- 階層化した歴史が残るので、指針を追加しやすくなります
