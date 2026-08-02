#!/usr/bin/env bash
#
# Seed the contributor-facing labels and a starter set of good first issues.
#
# Why this exists: GitHub's contributor discovery surfaces — the "good first
# issue" search, the topic pages, and the Explore recommendations — only show
# repositories that actually have open, labelled, unassigned issues. A repo with
# zero of them is invisible to people looking for something to work on, no
# matter how good its README is.
#
# Requires the GitHub CLI, authenticated:  gh auth login
#
# Usage:
#   bash scripts/seed-issues.sh              # dry run — prints, creates nothing
#   bash scripts/seed-issues.sh --yes        # actually create labels + issues
#
set -euo pipefail

REPO="nicohodt/claude-code-ui-ux-skill"
APPLY=false
[[ "${1:-}" == "--yes" ]] && APPLY=true

if ! command -v gh >/dev/null 2>&1; then
  echo "error: the GitHub CLI (gh) is required. See https://cli.github.com" >&2
  exit 1
fi

if $APPLY && ! gh auth status >/dev/null 2>&1; then
  echo "error: not authenticated. Run: gh auth login" >&2
  exit 1
fi

$APPLY || echo "DRY RUN — nothing will be created. Re-run with --yes to apply."
echo "Repository: $REPO"
echo

# ---------------------------------------------------------------------------
# Labels
# ---------------------------------------------------------------------------
# name|color|description
LABELS=(
  "good first issue|7057ff|Small, well-scoped, and ready for a first-time contributor"
  "help wanted|008672|We would love someone to pick this up"
  "design-data|c2e0c6|Adding or correcting a style, palette, font pairing or rule"
  "accessibility|d4c5f9|WCAG, contrast, screen readers, keyboard navigation"
  "documentation|0075ca|README, guides, examples"
  "translation|fbca04|Translating docs into another language"
  "new stack|1d76db|Support for an additional framework or platform"
  "search engine|5319e7|BM25 ranking, matching, relevance"
  "cli|bfd4f2|The uipro installer"
  "tests|d93f0b|Test coverage and CI"
)

echo "== Labels =="
for entry in "${LABELS[@]}"; do
  IFS='|' read -r name color desc <<<"$entry"
  if $APPLY; then
    # --force updates an existing label instead of failing.
    gh label create "$name" --repo "$REPO" --color "$color" --description "$desc" --force \
      >/dev/null && echo "  ok    $name"
  else
    echo "  would create/update: $name ($color)"
  fi
done
echo

# ---------------------------------------------------------------------------
# Starter issues
# ---------------------------------------------------------------------------
# Each is genuinely useful, genuinely small, and has a concrete acceptance
# criterion. Vague issues ("improve docs") do not attract contributors.
#
# title@@labels@@body
ISSUES=(
"Add color palettes for agriculture and farming products@@good first issue,design-data@@\
The database has 192 palettes but no coverage for agriculture, farming or agritech products.

**What to do**
1. Add one or more rows to \`src/ui-ux-pro-max/data/colors.csv\`.
2. Match the existing column order exactly (see \`CONTRIBUTING.md\` → *Add a color palette*).
3. Every \`On X\` colour must reach at least 4.5:1 against its background — \`tests/test_wcag_contrast.py\` enforces this.

**Done when** the new palette(s) are in \`colors.csv\`, \`npm run validate:csv\` passes in \`cli/\`, and the test suite is green.

You can do this entirely in the GitHub web editor — see [your first contribution in 5 minutes](https://github.com/nicohodt/claude-code-ui-ux-skill/blob/main/CONTRIBUTING.md#your-first-contribution-in-5-minutes)."

"Add CJK font pairings (Chinese, Japanese, Korean)@@good first issue,design-data@@\
All 74 font pairings in \`typography.csv\` are Latin-first, which makes the skill noticeably worse for CJK products.

**What to do**
Add pairings to \`src/ui-ux-pro-max/data/typography.csv\` using Google Fonts so the import URL works without a licence step. Good candidates: Noto Sans JP, Noto Serif JP, Zen Kaku Gothic, Noto Sans SC/TC, Noto Sans KR.

**Done when** the rows are added with a valid \`https://fonts.googleapis.com/\` URL (enforced by \`tests/test_data_integrity.py\`) and the suite passes.

Native reading knowledge of the script is genuinely valuable here — please say in the PR which language you're covering."

"Document the remaining UI styles in the README tables@@good first issue,documentation@@\
\`styles.csv\` contains 84 styles. The README tables name 67 of them, so 17 are undocumented.

**What to do**
1. Diff the style names in \`src/ui-ux-pro-max/data/styles.csv\` against the tables in \`README.md\`.
2. Add the missing rows to the correct \`<details>\` table with a short \"Best For\".
3. Mirror the change into \`README.zh.md\` if you can; English-only is still accepted.

**Done when** every style in the CSV appears in the README, and the note about 67 vs 84 is removed.

No code required — pure documentation."

"Add WCAG 2.2 success criteria to the UX guidelines@@help wanted,accessibility@@\
\`ux-guidelines.csv\` predates WCAG 2.2. The criteria added in 2.2 are missing entirely.

**What to do**
Add rows covering at least: 2.4.11 Focus Not Obscured, 2.5.7 Dragging Movements, 2.5.8 Target Size (Minimum), 3.2.6 Consistent Help, 3.3.7 Redundant Entry.

Each row needs \`Do\`, \`Don't\` and both \`Code Example Good\` / \`Code Example Bad\` — the code pair is what makes a guideline land.

**Done when** the criteria are present with runnable examples and the suite passes.

Requires some accessibility knowledge, so it's marked help-wanted rather than good-first-issue."

"Raise all component text pairs to WCAG AA 4.5:1@@help wanted,accessibility@@\
Body text (\`Background\`/\`Foreground\`, \`Card\`/\`Card Foreground\`) clears 4.5:1 in all 192 palettes, and every pair now clears the 3:1 floor. The \`On Primary\` / \`On Secondary\` / \`On Accent\` / \`Muted Foreground\` pairs still sit between 3:1 and 4.5:1 in many palettes.

**What to do**
1. Adjust the \`On *\` foregrounds — or darken the backing colour — so each pair reaches 4.5:1, without wrecking the palette's character.
2. Tighten \`COMPONENT_TEXT_PAIRS\` in \`tests/test_wcag_contrast.py\` from 3.0 to 4.5 once they pass.
3. Note the change in the \`Notes\` column, following the existing convention.

This is tracked on the [roadmap](https://github.com/nicohodt/claude-code-ui-ux-skill/blob/main/ROADMAP.md) as the highest-value accessibility contribution available. Partial PRs covering a subset of palettes are welcome."

"Add support for a new tech stack@@good first issue,new stack@@\
The skill ships guidelines for 22 stacks. Frequently requested and still missing: **Solid, Qwik, Remix, Blazor, Ionic, Lit, Kotlin Multiplatform**.

**What to do**
1. Copy \`src/ui-ux-pro-max/data/stacks/react.csv\` to \`stacks/<your-stack>.csv\` and rewrite the rows.
2. Keep the shared 10-column schema exactly — \`tests/test_data_integrity.py\` enforces it across every stack file.
3. Register the stack in \`src/ui-ux-pro-max/scripts/search.py\` so \`--stack <name>\` resolves.
4. Run \`npm run sync:assets\` in \`cli/\`.

**Done when** \`--stack <your-stack>\` returns results and \`bash scripts/smoke-stacks.sh\` passes.

Pick one stack per PR. Comment here to say which you're taking so we don't duplicate."

"Translate the README into your language@@good first issue,translation,documentation@@\
Docs exist in English and Simplified Chinese. Wanted: **Spanish, French, German, Japanese, Portuguese, Hindi** — or any other language.

**What to do**
1. Copy \`README.md\` to \`README.<lang>.md\` (e.g. \`README.es.md\`).
2. Translate it. **Partial translations are accepted** — translate what you can.
3. Add your language to the link row at the top of \`README.md\` and \`README.zh.md\`.

**Done when** the file exists and is linked.

Keep the numbers (84 styles, 192 palettes, …) accurate — \`tests/test_advertised_counts.py\` checks the English and Chinese phrasings, and we'll add a pattern for yours."

"Add typo tolerance to the search engine@@help wanted,search engine@@\
A near-miss returns nothing at all: searching \`glassmorphis\` (one character short of \`glassmorphism\`) yields zero results, and the suggestion fallback is empty for anything sufficiently off.

**What to do**
Add an edit-distance fallback in \`src/ui-ux-pro-max/scripts/core.py\`: when BM25 returns no hits, retry against the vocabulary within a small Levenshtein distance. **Standard library only** — the project has no Python dependencies and that constraint is deliberate.

**Done when** \`core.search(\"glassmorphis\", domain=\"style\")\` returns the Glassmorphism row, and \`tests/test_search_engine.py::test_partial_match_still_offers_suggestions\` is tightened to assert it.

The most technically interesting open issue in the project."
)

echo "== Issues =="
for entry in "${ISSUES[@]}"; do
  title="${entry%%@@*}"
  rest="${entry#*@@}"
  labels="${rest%%@@*}"
  body="${rest#*@@}"

  if $APPLY; then
    # Skip if an open issue with this exact title already exists.
    existing=$(gh issue list --repo "$REPO" --state open --search "\"$title\" in:title" \
      --json title --jq 'length' 2>/dev/null || echo 0)
    if [[ "$existing" != "0" ]]; then
      echo "  skip  (already open) $title"
      continue
    fi
    gh issue create --repo "$REPO" --title "$title" --label "$labels" --body "$body" >/dev/null
    echo "  ok    $title"
  else
    echo "  would create: [$labels]"
    echo "                $title"
  fi
done

echo
if $APPLY; then
  echo "Done. Check https://github.com/$REPO/issues"
  echo "Leave these unassigned — assigned issues are hidden from GitHub's"
  echo "good-first-issue discovery surfaces."
else
  echo "Dry run complete. Re-run with --yes to create them."
fi
