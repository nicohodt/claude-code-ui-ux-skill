# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

UI UX Pro Max is an AI-powered design intelligence toolkit providing searchable databases of UI styles, color palettes, font pairings, chart types, and UX guidelines. It works as a skill/workflow for AI coding assistants (Claude Code, Windsurf, Cursor, etc.).

## Search Command

```bash
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain> [-n <max_results>]
```

**Domain search:**
- `product` - Product type recommendations (SaaS, e-commerce, portfolio)
- `style` - UI styles (glassmorphism, minimalism, brutalism) + AI prompts and CSS keywords
- `typography` - Font pairings with Google Fonts imports
- `color` - Color palettes by product type
- `landing` - Page structure and CTA strategies
- `chart` - Chart types and library recommendations
- `ux` - Best practices and anti-patterns
- `icons` - Icon recommendations with import code (Phosphor, Heroicons, Lucide)
- `react` - React/Next.js performance patterns
- `web` - App interface guidelines (iOS/Android/React Native)
- `google-fonts` - Individual Google Fonts lookup
- `gsap` - GSAP animation skeletons by intensity tier (hover, scroll reveal, stagger, page transition, parallax, loading)

**Design dials (optional, only with `--design-system`):**
```bash
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --design-system --variance <1-10> --motion <1-10> --density <1-10>
```
`--variance` biases style selection (centered/minimal → bold/asymmetric), `--motion` attaches a matching GSAP snippet from `motion.csv`, `--density` overrides the spacing-scale tokens (spacious → dense/dashboard). Any dial left unset behaves exactly as before.

**Stack search:**
```bash
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --stack <stack>
```
Available stacks: `html-tailwind` (default), `react`, `nextjs`, `astro`, `vue`, `nuxtjs`, `nuxt-ui`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`, `jetpack-compose`, `threejs`, `angular`, `laravel`, `javafx`, `wpf`, `winui`, `avalonia`, `uno`, `uwp`

## Architecture

```
src/ui-ux-pro-max/                # Source of Truth
├── data/                         # Canonical CSV databases
│   ├── products.csv, styles.csv, colors.csv, typography.csv, ...
│   └── stacks/                   # Stack-specific guidelines
├── scripts/
│   ├── search.py                 # CLI entry point
│   ├── core.py                   # BM25 + regex hybrid search engine
│   └── design_system.py          # Design system generation
└── templates/
    ├── base/                     # Base templates (skill-content.md, quick-reference.md)
    └── platforms/                # Platform configs (claude.json, cursor.json, ...)

cli/                              # CLI installer (ui-ux-pro-max-cli on npm)
├── src/
│   ├── commands/init.ts          # Install command with template generation
│   └── utils/template.ts         # Template rendering engine
├── scripts/sync-assets.mjs       # Mirrors src/ -> cli/assets/ AND src/ -> .claude/skills/ui-ux-pro-max/
└── assets/                       # Bundled assets (~564KB)
    ├── data/                     # Copy of src/ui-ux-pro-max/data/
    ├── scripts/                  # Copy of src/ui-ux-pro-max/scripts/
    └── templates/                # Copy of src/ui-ux-pro-max/templates/

.claude/skills/ui-ux-pro-max/     # Claude Code skill: hand-authored SKILL.md +
                                   # data/, scripts/ mirrored from src/ (see Sync Rules)
.claude-plugin/                   # Claude Marketplace publishing
```

The search engine uses BM25 ranking combined with regex matching. Domain auto-detection is available when `--domain` is omitted.

## Sync Rules

**Source of Truth:** `src/ui-ux-pro-max/`

There are no symlinks in this repo (git-on-Windows checks them out as plain
text files pointing at a path, which silently breaks the skill) -- every
mirrored copy below is a real, independently-committed file kept in sync by
`cli/scripts/sync-assets.mjs`, enforced by the "Check asset sync" CI workflow.

When modifying files:

1. **Data & Scripts** - Edit in `src/ui-ux-pro-max/`:
   - `data/*.csv` and `data/stacks/*.csv`
   - `scripts/*.py`
   - Then run the sync below -- changes are NOT automatically reflected anywhere else.

2. **Templates** - Edit in `src/ui-ux-pro-max/templates/`:
   - `base/skill-content.md` - Common SKILL.md content
   - `base/quick-reference.md` - Quick reference section (Claude only)
   - `platforms/*.json` - Platform-specific configs

3. **Sync before publishing / committing data or script changes:**
   ```bash
   cd cli
   npm run sync:assets   # mirrors src/ -> cli/assets/ AND src/ -> .claude/skills/ui-ux-pro-max/{data,scripts}
   npm run check:assets  # verify, no npm install required
   ```
   `.claude/skills/ui-ux-pro-max/SKILL.md` itself is hand-authored, not
   mirrored or template-generated -- edit it directly.

4. **Reference Folders** - No manual sync needed. The CLI generates these from templates during `uipro init`.

5. **Sub-skills** - The six sibling skills (`design`, `design-system`, `brand`,
   `banner-design`, `slides`, `ui-styling`) have their source of truth in
   `.claude/skills/<name>/` and are mirrored into `cli/assets/skills/<name>/` by the
   same `npm run sync:assets`. Edit them under `.claude/skills/`, never under
   `cli/assets/`. They ship with `uipro init`, so anything user-visible in them
   (frontmatter `author`, demo/sample content) is public-facing.

## Project Identity

- **Repo:** `nicohodt/claude-code-ui-ux-skill` · **Maintainer:** [@nicohodt](https://github.com/nicohodt) · **MIT**
- **npm package:** `ui-ux-pro-max-cli` (binary stays `uipro`)
- **Claude marketplace id:** `claude-code-ui-ux-skill` — install is
  `/plugin install ui-ux-pro-max@claude-code-ui-ux-skill`. The id must match
  `.claude-plugin/marketplace.json` `name`/`id` and both READMEs.
- The project is **fully open source with no paid or premium tier**. Don't
  reintroduce upsell sections, donation links, or cross-promotion of other
  products — the contributor pitch in both READMEs depends on that being true.

## Documentation & SEO

- `README.md` (English) and `README.zh.md` (Chinese) are **parallel documents**.
  A change to structure, counts, or the FAQ in one belongs in the other.
- `docs/index.html` is the GitHub Pages landing page. Its JSON-LD `FAQPage` block
  duplicates the README FAQ **verbatim by design** — if you edit an FAQ answer,
  edit it in all three places or the structured data contradicts the page.
- `docs/SEO-CHECKLIST.md` tracks the steps that can only be done in the GitHub UI
  (repo description, topics, social preview, enabling Pages) plus off-page work.
- `CONTRIBUTORS.md` is the credit list. Every merged PR should add its author.
- The README promises a **48-hour first response on issues and PRs**. If that
  stops being true, change the promise rather than leaving it stale.

## Testing

```bash
pip install pytest
pytest                     # 192 tests; config lives in pytest.ini
```

Tests live in `tests/` at the repo root and run against the **source of truth**
(`src/ui-ux-pro-max/`), never the mirrors. They cover:

- `test_data_integrity.py` — ragged rows, duplicate columns, sequential `No`
  identifiers, the shared 10-column stack schema, severity vocabularies
- `test_wcag_contrast.py` — 4.5:1 for body text, 3:1 for component text, across
  all 192 palettes. **This is the project's core promise; do not weaken these
  thresholds to make a palette pass — fix the palette.**
- `test_search_engine.py` — every domain and stack returns results, design
  system generation, CLI JSON output
- `test_advertised_counts.py` — the numbers in the docs must equal the rows in
  the CSVs. If you add data, update the docs (or vice versa) or this fails.

Adding a row to a CSV can break `test_advertised_counts.py` by design. That is
the mechanism that stopped "98 UX guidelines" from drifting from a database that
actually held 99.

## Prerequisites

Python 3.x (no external dependencies required). `pytest` is needed only to run
the test suite.

**Note:** On Windows, use `python` instead of `python3` to run the scripts.

## Git Workflow

Never push directly to `main`. Always:

1. Create a new branch: `git checkout -b feat/...` or `fix/...`
2. Commit changes
3. Push branch: `git push -u origin <branch>`
4. Create PR: `gh pr create`
