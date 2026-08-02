# Contributing

**Welcome — genuinely.** This project exists because people keep adding what they know about design to it. If you have ever thought *"that palette is wrong for a hospital app"* or *"my framework is missing"*, you already have everything you need to contribute.

**A few promises, so you know what you're walking into:**

- 🕐 **Every PR gets a first response within 48 hours.** No silent rot.
- 📄 **No CLA, no contributor agreement, no paperwork.** MIT in, MIT out.
- 🧩 **One CSV row is a real contribution.** Small PRs are the point, not a compromise.
- 🙅 **No gatekeeping.** You don't need to be a designer, or know Python, or have contributed to open source before.
- ✅ **We fix your PR rather than close it.** If CI fails or the format is off, we'll tell you exactly what to change — or push the fix ourselves if you'd rather.
- 🏆 **Credit is automatic.** Everyone who merges a change is added to [CONTRIBUTORS.md](CONTRIBUTORS.md) and named in release notes.

---

## Table of contents

- [Your first contribution in 5 minutes](#your-first-contribution-in-5-minutes)
- [Ways to contribute](#ways-to-contribute)
- [Contribution recipes](#contribution-recipes)
- [Project structure](#project-structure)
- [Development workflow](#development-workflow)
- [Commit messages](#commit-messages)
- [Pull request guidelines](#pull-request-guidelines)
- [Reporting bugs](#reporting-bugs)
- [Getting help](#getting-help)

---

## Your first contribution in 5 minutes

**You don't need to clone anything.** The most valuable data in this project is plain CSV, and GitHub lets you edit it in the browser.

1. Open [`src/ui-ux-pro-max/data/colors.csv`](src/ui-ux-pro-max/data/colors.csv) on GitHub.
2. Click the ✏️ **pencil icon** (top right).
3. Add one row at the bottom, following the format of the row above it.
4. Scroll down, choose **"Create a new branch and start a pull request"**, and click **Propose changes**.

That's it. That's a real, creditable contribution. A maintainer will run the sync step for you if you didn't.

> **Working locally instead?** See [Development workflow](#development-workflow). The only thing to remember: edit under `src/ui-ux-pro-max/`, then run `npm run sync:assets` inside `cli/`.

---

## Ways to contribute

Ranked roughly by how much they help, not by how hard they are.

| | What | Where | Skill needed |
|---|---|---|---|
| 🌈 | **New color palette** | `data/colors.csv` | Just design sense |
| 🏭 | **New industry reasoning rule** | `data/ui-reasoning.csv` | Just domain knowledge |
| 🎨 | **New UI style** | `data/styles.csv` | Just design sense |
| 🔤 | **New font pairing** | `data/typography.csv` | Just typography taste |
| ♿ | **New UX guideline** | `data/ux-guidelines.csv` | Accessibility/UX knowledge |
| 🌍 | **Translate the README** | `README.[lang].md` | Fluency in your language |
| 📚 | **Docs, typos, examples** | anywhere | None |
| 🧱 | **New tech stack** | `data/stacks/<stack>.csv` | Knowing that framework |
| ✨ | **New motion preset** | `data/motion.csv` | GSAP |
| 📊 | **New chart guidance** | `data/charts.csv` | Data-viz knowledge |
| 🔍 | **Search engine work** | `scripts/core.py` | Python |
| 🖥️ | **CLI work** | `cli/src/` | TypeScript |
| 🧪 | **Tests** | `.claude/skills/**/tests/`, `cli/tests/` | pytest / Playwright |

All data paths are relative to `src/ui-ux-pro-max/`.

**Not sure where to start?** Browse [good first issues](https://github.com/nicohodt/claude-code-ui-ux-skill/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) or the [what-we-need-right-now list](README.md#-what-we-need-right-now).

---

## Contribution recipes

Each recipe below is self-contained. Match the existing rows in the file — the column list is the contract.

### Add a color palette

**File:** `src/ui-ux-pro-max/data/colors.csv`

```
No,Product Type,Primary,On Primary,Secondary,On Secondary,Accent,On Accent,Background,
Foreground,Card,Card Foreground,Muted,Muted Foreground,Border,Destructive,On Destructive,Ring,Notes
```

Rules of thumb:
- `On X` colors are the text/icon color placed **on** that background — they must hit **4.5:1** contrast.
- Keep `Product Type` aligned with a row in `products.csv` where possible.
- Put the reasoning in `Notes` ("Trust blue + orange CTA contrast").

### Add an industry reasoning rule

**File:** `src/ui-ux-pro-max/data/ui-reasoning.csv`

```
No,UI_Category,Recommended_Pattern,Style_Priority,Color_Mood,Typography_Mood,
Key_Effects,Decision_Rules,Anti_Patterns,Severity
```

`Anti_Patterns` is the most valuable column — it's what stops the AI producing generic output. Be specific: *"AI purple/pink gradients"*, *"dark mode"*, *"playful rounded fonts"*.

### Add a UI style

**File:** `src/ui-ux-pro-max/data/styles.csv`

```
No,Style Category,Type,Keywords,Primary Colors,Secondary Colors,Effects & Animation,
Best For,Do Not Use For,Light Mode ✓,Dark Mode ✓,Performance,Accessibility,Mobile-Friendly,
Conversion-Focused,Framework Compatibility,Era/Origin,Complexity,AI Prompt Keywords,
CSS/Technical Keywords,Implementation Checklist,Design System Variables
```

`AI Prompt Keywords` and `CSS/Technical Keywords` are what the agent actually consumes — write them as instructions, not adjectives.

### Add a font pairing

**File:** `src/ui-ux-pro-max/data/typography.csv`

```
No,Font Pairing Name,Category,Heading Font,Body Font,Mood/Style Keywords,Best For,
Google Fonts URL,CSS Import,Tailwind Config,Notes
```

Use Google Fonts so the import URL works without a license step. **Non-Latin script pairings (CJK, Arabic, Devanagari, Cyrillic) are especially wanted.**

### Add a UX guideline

**File:** `src/ui-ux-pro-max/data/ux-guidelines.csv`

```
No,Category,Issue,Platform,Description,Do,Don't,Code Example Good,Code Example Bad,Severity
```

The `Code Example Good` / `Code Example Bad` pair is what makes a guideline stick — please include both.

### Add a tech stack

**File:** `src/ui-ux-pro-max/data/stacks/<your-stack>.csv`

```
No,Category,Guideline,Description,Do,Don't,Code Good,Code Bad,Severity,Docs URL
```

Then register the stack name in `src/ui-ux-pro-max/scripts/search.py` so `--stack <your-stack>` resolves. Copy an existing file such as `react.csv` as your starting point.

### Translate the README

Copy `README.md` to `README.<lang>.md` (e.g. `README.es.md`, `README.ja.md`, `README.fr.md`) and translate. Add your language to the link row at the top of `README.md` and `README.zh.md`. Partial translations are accepted — translate what you can and open the PR.

---

## Project structure

```
claude-code-ui-ux-skill/
├── src/ui-ux-pro-max/          # ← SOURCE OF TRUTH. Edit here.
│   ├── data/                   # CSV databases
│   │   ├── styles.csv          # 84 UI styles
│   │   ├── colors.csv          # 192 color palettes
│   │   ├── typography.csv      # 74 font pairings
│   │   ├── products.csv        # 192 product types
│   │   ├── ui-reasoning.csv    # 161 industry reasoning rules
│   │   ├── ux-guidelines.csv   # 99 UX rules
│   │   ├── icons.csv, motion.csv, charts.csv, landing.csv, ...
│   │   └── stacks/             # 22 per-framework guideline files
│   ├── scripts/                # search.py (CLI), core.py (BM25 engine), design_system.py
│   └── templates/              # per-assistant skill templates
├── cli/                        # npm installer (ui-ux-pro-max-cli)
│   ├── src/                    # TypeScript CLI
│   └── assets/                 # mirror of src/ — generated, do not hand-edit
├── .claude/skills/             # Claude Code skill; data/ + scripts/ mirrored from src/
├── .github/                    # issue templates, PR template, CI workflows
├── docs/                       # documentation & GitHub Pages site
└── stack/                      # optional companion "design stack" project
```

> ⚠️ **The one rule that matters:** make changes in `src/ui-ux-pro-max/`. Everything under `cli/assets/` and `.claude/skills/ui-ux-pro-max/{data,scripts}` is a mirrored copy kept in sync by `cli/scripts/sync-assets.mjs`, and CI will fail if the copies drift. There are deliberately **no symlinks** in this repo — Git on Windows breaks them.

---

## Development workflow

### Setup

Prerequisites: **Node.js 18+**, **Python 3.x**, **Git**. (Bun is optional — the CLI build falls back to `tsc`.)

```bash
# 1. Fork on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/claude-code-ui-ux-skill.git
cd claude-code-ui-ux-skill

# 2. Track the upstream repo
git remote add upstream https://github.com/nicohodt/claude-code-ui-ux-skill.git

# 3. Install CLI dependencies
cd cli && npm install && cd ..
```

### Make a change

```bash
# 1. Branch off main
git checkout -b feat/your-feature-name

# 2. Edit files under src/ui-ux-pro-max/

# 3. Mirror your changes into cli/assets/ and .claude/skills/
cd cli
npm run sync:assets     # copies src/ -> cli/assets/ AND src/ -> .claude/skills/ui-ux-pro-max/
npm run check:assets    # verifies the mirrors match (this is what CI runs)
```

### Verify before opening the PR

```bash
# from cli/
npm run validate:csv     # CSV schema + column count check
npm run smoke:domains    # every --domain returns results
npm run smoke:stacks     # every --stack resolves
npm run typecheck        # TypeScript

# from the repo root — try your change for real
python3 src/ui-ux-pro-max/scripts/search.py "your query" --domain color
python3 src/ui-ux-pro-max/scripts/search.py "your product" --design-system
```

Python tests (only if you touched scripts):

```bash
pip install pytest
python3 -m pytest .claude/skills -v
```

### Test the CLI end to end

```bash
cd cli
npm run build
mkdir -p /tmp/uipro-test && cd /tmp/uipro-test
node /path/to/repo/cli/dist/index.js init --ai claude --offline
```

> **Can't get the tooling to run?** Open the PR anyway and say so in the description. Data-only PRs are easy for a maintainer to sync and validate.

---

## Commit messages

We use [Conventional Commits](https://www.conventionalcommits.org/) because releases are automated from them.

```
feat:     new content or capability (style, rule, palette, stack)  → minor release
fix:      bug fix                                                  → patch release
docs:     documentation only                                       → no release
refactor: code change, no behavior change                          → no release
chore:    build, dependencies, tooling                             → no release
test:     adding or fixing tests                                   → no release
feat!:    breaking change (or a BREAKING CHANGE: footer)           → major release
```

**Examples:**

```
feat: add Bauhaus Revival style to general styles
feat: add color palette for veterinary clinics
fix: correct WCAG contrast on fintech accent color
docs: translate README to Spanish
```

Got the prefix wrong? Not a problem — we squash-merge and can fix the title.

---

## Pull request guidelines

1. **One topic per PR.** Two unrelated styles in one PR is fine; a style plus a CLI refactor is not.
2. **Describe what and why.** Two sentences is plenty. If it closes an issue, write `Closes #123`.
3. **Run `npm run sync:assets`** if you touched `data/`, `scripts/` or `templates/`. If you forget, CI will tell you and we'll help.
4. **Branch, don't push to `main`.** `main` is protected.
5. **Draft PRs are welcome.** Open one early if you want feedback before finishing.

**What we will never do:** close your PR for being too small, for imperfect English, or for not matching a style guide you couldn't have known about.

---

## Reporting bugs

[Open an issue](https://github.com/nicohodt/claude-code-ui-ux-skill/issues/new/choose) with:

- Your OS and terminal
- Which AI assistant (Claude Code, Cursor, Windsurf, …)
- Your `ui-ux-pro-max-cli` version (`uipro --version`)
- The exact command or prompt
- Expected vs. actual behavior, plus any error output

For security issues, **do not open a public issue** — see [SECURITY.md](SECURITY.md).

---

## Getting help

- 💬 [**Discussions**](https://github.com/nicohodt/claude-code-ui-ux-skill/discussions) — questions, ideas, "is this a good idea before I build it?"
- 🐛 [**Issues**](https://github.com/nicohodt/claude-code-ui-ux-skill/issues) — bugs and concrete proposals
- 📖 [**CLAUDE.md**](CLAUDE.md) — architecture and sync rules in depth

Asking a question is never a bother. A question you had is a documentation gap we didn't know about.

---

By contributing you agree that your work is licensed under the [MIT License](LICENSE), and to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

**Thanks for being here. 🚀**
