import { defineConfig } from "cz-git";

export default defineConfig({
  rules: {
    // コミットメッセージのルール設定
    // @see: https://commitlint.js.org/#/reference-rules
  },
  prompt: {
    alias: {
      fd: "docs: タイポ修正",
    },
    messages: {
      type: "コミットの種類を選択してください:",
      scope: "変更のスコープを指定してください（任意）: ",
      customScope: "変更のスコープを指定してください:",
      subject: "変更の短い、命令形の説明を入力してください:\n",
      body: '変更の詳細な説明を入力してください（任意）。新しい行を作る場合は"|"\nを使用:\n',
      breaking:
        'BREAKING CHANGESを列挙してください（任意）。新しい行を作る場合は"|"\nを使用:\n',
      footerPrefixesSelect:
        "変更に関連するISSUESの種類を選択してください（任意）: ",
      customFooterPrefix: "カスタムISSUESプレフィックスを入力:",
      footer: "この変更に関連するISSUESを列挙してください。例： #31, #34:\n",
      generatingByAI: "コミットメッセージを生成中...",
      generatedSelectByAI: "適切なサブジェクトをAIが生成したものから選択:",
      confirmCommit: "上記のコミット内容で進めていいですか？",
    },
    types: [
      { value: "feat", name: "feat:     ✨  新機能追加", emoji: "✨" },
      { value: "fix", name: "fix:      🐛  バグ修正", emoji: "🐛" },
      {
        value: "docs",
        name: "docs:     📝  ドキュメントのみの変更",
        emoji: "📝",
      },
      {
        value: "style",
        name: "style:    💄  コードの意味に影響しない変更",
        emoji: "💄",
      },
      {
        value: "refactor",
        name: "refactor: ♻️   機能の追加やバグ修正以外のコード変更",
        emoji: "♻️",
      },
      {
        value: "perf",
        name: "perf:     ⚡️  パフォーマンス改善",
        emoji: "⚡️",
      },
      {
        value: "test",
        name: "test:     ✅  テストの追加または既存テストの修正",
        emoji: "✅",
      },
      {
        value: "build",
        name: "build:    📦️   ビルドシステムまたは外部依存関係の変更",
        emoji: "📦️",
      },
      {
        value: "ci",
        name: "ci:       🎡  CI構成ファイルとスクリプトの変更",
        emoji: "🎡",
      },
      {
        value: "chore",
        name: "chore:    🔨  ソースやテストファイル以外の変更",
        emoji: "🔨",
      },
      {
        value: "revert",
        name: "revert:   ⏪️  前のコミットの取り消し",
        emoji: "⏪️",
      },
    ],
    useEmoji: true,
    emojiAlign: "center",
    useAI: true,
    aiNumber: 1,
    themeColorCode: "",
    scopes: [],
    allowCustomScopes: true,
    allowEmptyScopes: true,
    customScopesAlign: "bottom",
    customScopesAlias: "custom",
    emptyScopesAlias: "empty",
    upperCaseSubject: false,
    markBreakingChangeMode: false,
    allowBreakingChanges: ["feat", "fix"],
    breaklineNumber: 100,
    breaklineChar: "|",
    skipQuestions: [],
    issuePrefixes: [{ value: "closed", name: "closed:   処理済みISSUES" }],
    customIssuePrefixAlign: "top",
    emptyIssuePrefixAlias: "skip",
    customIssuePrefixAlias: "custom",
    allowCustomIssuePrefix: true,
    allowEmptyIssuePrefix: true,
    confirmColorize: true,
    scopeOverrides: undefined,
    defaultBody: "",
    defaultIssues: "",
    defaultScope: "",
    defaultSubject: "",
  },
});
