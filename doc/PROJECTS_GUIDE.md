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

👉 テンプレートの選択ルールについては 「[📋 Issue テンプレート運用方針](#-issue-テンプレート運用方針why)」を参照

---

## 🧪 CI テストワークフロー

このプロジェクトでは、GitHub Actions を利用した CI テスト環境を構築しています。
開発ブランチや Pull Request に対して、Python テストが自動的に実行されます。

### ✅ ワークフロー定義

- ファイル: `.github/workflows/test.yml`
- 実行タイミング:
  - push / pull_request / 手動（workflow_dispatch）
- テスト内容:
  - Python 3.13 にて `uv pip install --group dev` を実行し、依存パッケージをインストール
  - `uv run pytest` によりテストスイートを実行

### 🔧 今後の拡張予定

- Bats（Bash Automated Testing System）による CLI スクリプトの自動テスト（[Issue #5](https://github.com/linuxfirstMint/package_migration_tools/issues/5)）
- キャッシュの導入による高速化
- テスト結果の通知やブロッカー設定の追加

---

## 🔖 コミットメッセージのプレフィックス運用ルール

このプロジェクトでは、明確な目的と分類に基づいて以下のプレフィックスを使用しています。
`cz-git` と `commitlint` により、補完・自動チェックが行われます。

| プレフィックス | 用途                                           | emoji |
| -------------- | ---------------------------------------------- | ----- |
| `feat`         | 新機能の追加                                   | ✨    |
| `fix`          | バグ修正                                       | 🐛    |
| `docs`         | ドキュメント整備（README やテンプレートなど）  | 📝    |
| `style`        | コード整形、エディタ設定など（意味に影響なし） | 💄    |
| `refactor`     | 機能追加・バグ修正を含まないリファクタリング   | ♻️    |
| `test`         | テスト追加や修正（unit, integration, bats 等） | ✅    |
| `build`        | ビルド設定や依存パッケージ変更                 | 📦️   |
| `ci`           | GitHub Actions 等 CI 構成                      | 🎡    |
| `config`       | commitlint, ruff, editorconfig などの設定変更  | ⚙️    |
| `tool`         | 補助スクリプトや開発ツールの追加・整備         | 🛠     |
| `infra`        | GitHub Projects や環境構築スクリプト関連       | 🧱    |
| `revert`       | 過去のコミットの取り消し                       | ⏪️   |

🚫 **`chore:` は使用しません**。すべての変更は具体的なプレフィックスで分類されます。

---

## 📋 Issue テンプレート運用方針（Why）

現在の開発フェーズでは、すべての issue を `task_template.md` に統一しています。
機能提案も「実装タスク」として `task` ラベルで管理されます。

将来的に運用の拡張状況に合わせて、`feature_request.md`,`bug_report.md` を復活させることを想定しています。

👉 運用パターンについては 「[🧰 運用パターン](#-運用パターン)」を参照

---

## 🔺 備考

- 運用ガイドは階段的に最適化します
- 階層化した歴史が残るので、指針を追加しやすくなります
