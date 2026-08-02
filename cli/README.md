# ui-ux-pro-max-cli

**Installer for the [Claude Code UI/UX Skill](https://github.com/nicohodt/claude-code-ui-ux-skill) — the open-source Claude skill that makes AI-generated UI and UX actually good.**

One command drops a searchable design-intelligence database into your project: **84 UI styles, 192 color palettes, 74 font pairings, 99 UX guidelines, 161 industry reasoning rules and 25 chart types across 22 tech stacks** — for Claude Code, Cursor, Windsurf, GitHub Copilot, Codex, Gemini CLI and 13 more assistants.

Runs fully offline. No API keys, no telemetry, no network calls at query time.

- 📖 **Docs & full README:** <https://github.com/nicohodt/claude-code-ui-ux-skill>
- 🌐 **Website:** <https://nicohodt.github.io/claude-code-ui-ux-skill/>
- 🤝 **Contributing:** [we merge small PRs, fast](https://github.com/nicohodt/claude-code-ui-ux-skill/blob/main/CONTRIBUTING.md)

## Installation

```bash
npm install -g ui-ux-pro-max-cli
```

Or without installing:

```bash
npx ui-ux-pro-max-cli init --ai claude
```

## Usage

```bash
# Install for a specific AI assistant
uipro init --ai claude      # Claude Code
uipro init --ai cursor      # Cursor
uipro init --ai windsurf    # Windsurf
uipro init --ai antigravity # Antigravity
uipro init --ai copilot     # GitHub Copilot
uipro init --ai kiro        # Kiro
uipro init --ai codex       # Codex (Skills)
uipro init --ai roocode     # Roo Code
uipro init --ai qoder       # Qoder
uipro init --ai gemini      # Gemini CLI
uipro init --ai trae        # Trae
uipro init --ai opencode    # OpenCode
uipro init --ai continue    # Continue (Skills)
uipro init --ai all         # All assistants

# Options
uipro init --global         # Install for every project (~/.claude/skills/ etc.)
uipro init --offline        # Compatibility flag; installs bundled templates
uipro init --force          # Overwrite existing files

# Other commands
uipro versions              # List available versions
uipro update                # Update the global CLI to the latest release
uipro uninstall             # Remove the skill (auto-detects platform)
```

Then just ask your assistant for UI work in plain language — the skill activates on its own:

```
Build a landing page for my SaaS product
```

**Requires Python 3.x** for the search scripts (standard library only).

## GitHub Authentication

GitHub's unauthenticated API allows 60 requests/hour per IP. If you hit rate limits, provide a GitHub Personal Access Token (PAT) to raise the limit to 5,000 requests/hour.

**Options (in order of precedence):**

```bash
# 1. Pass directly as a flag (one-off use)
uipro init --token ghp_yourtoken
uipro versions --token ghp_yourtoken
uipro update --token ghp_yourtoken

# 2. Set as a project-scoped environment variable (recommended)
export UI_PRO_MAX_GITHUB_TOKEN=ghp_yourtoken
uipro init

# 3. Fallback: GITHUB_TOKEN is also read if UI_PRO_MAX_GITHUB_TOKEN is not set
export GITHUB_TOKEN=ghp_yourtoken
uipro init
```

**Creating a token:** Go to <https://github.com/settings/tokens>, click **Generate new token (classic)**, and select **no scopes** — public repo access requires no permissions. Copy the token and store it as an environment secret; never hardcode it in source files.

> **Warning:** `GITHUB_TOKEN` is automatically injected by GitHub Actions with broad repo permissions. Prefer `UI_PRO_MAX_GITHUB_TOKEN` in CI to avoid accidentally attaching workflow credentials to release download requests.

## How It Works

`uipro init` generates assistant-specific files from the templates bundled with the installed CLI package. To get newer templates and data, update the package, then regenerate:

```bash
uipro update                   # updates the global CLI to the latest release
uipro init --ai codex --force  # regenerate skill files from the new package
```

`uipro update` runs `npm install -g ui-ux-pro-max-cli@latest` for you (it shells out to `npm` only on Windows, where `npm` is a `.cmd`). You can still run that command manually if you prefer. When the CLI is already current, `uipro update` just refreshes the installed skill files.

## Development

```bash
# Install dependencies
bun install          # or: npm install

# Run locally
bun run src/index.ts --help

# Build
npm run build

# Sync bundled CLI assets from the source skill
npm run sync:assets

# Verify bundled assets are current before publishing
npm run check:assets
```

## Contributing

**Pull requests are very welcome, including small ones.** Most of the design database is plain CSV you can edit in the GitHub web editor — no clone, no build step, no CLA, and every PR gets a first response within 48 hours.

👉 [Start here](https://github.com/nicohodt/claude-code-ui-ux-skill/blob/main/CONTRIBUTING.md) · [Good first issues](https://github.com/nicohodt/claude-code-ui-ux-skill/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

## License

[MIT](https://github.com/nicohodt/claude-code-ui-ux-skill/blob/main/LICENSE) — free for personal and commercial use.
