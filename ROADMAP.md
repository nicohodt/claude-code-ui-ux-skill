# Roadmap

What's planned, what's wanted, and what's deliberately out of scope. **Nothing here is reserved** — if an item interests you, comment on the matching issue or just open a PR.

Difficulty: 🟢 beginner · 🟡 intermediate · 🔴 advanced

---

## Now — accepting PRs today

These are concrete, scoped, and unblocked.

| Item | Why | Difficulty |
|---|---|---|
| **Raise all component text pairs to 4.5:1** | The 192 palettes clear the 3:1 floor enforced by `tests/test_wcag_contrast.py`, and body text clears 4.5:1 everywhere. The `On Primary` / `On Secondary` / `On Accent` pairs sit between the two. Raising them to full AA and tightening the test is the single highest-value accessibility contribution available. | 🟡 |
| **Document the remaining UI styles in the README tables** | `styles.csv` holds 84 styles; the README tables name 67. | 🟢 |
| **Color palettes for underserved industries** | Agriculture, logistics, public sector, education, non-profit. | 🟢 |
| **Non-Latin font pairings** | CJK, Arabic, Devanagari, Cyrillic. Currently every pairing is Latin-first, which makes the skill markedly worse outside English-language products. | 🟢 |
| **Industry rules beyond the current 161** | Government services, marketplaces, hardware/IoT, education. | 🟢 |
| **README translations** | Spanish, French, German, Japanese, Portuguese, Hindi. | 🟢 |
| **WCAG 2.2 guidelines** | `ux-guidelines.csv` predates 2.2; target size, focus appearance, and dragging movements are missing. | 🟡 |
| **New tech stacks** | Solid, Qwik, Remix, Blazor, Ionic, Lit, Kotlin Multiplatform. One CSV file each, following the shared schema enforced by `tests/test_data_integrity.py`. | 🟡 |

## Next — designed, not started

| Item | Notes |
|---|---|
| **Motion presets beyond GSAP** | Framer Motion / Motion One equivalents for the 16 existing tiers, so the motion data isn't locked to one library. |
| **Search quality: synonyms and typo tolerance** | BM25 currently misses near-misses (`glassmorphis` returns nothing). A synonym table plus edit-distance fallback in `core.py`. 🔴 |
| **Contrast checking inside the generator** | The database is verified in CI, but `design_system.py` doesn't re-check contrast when it composes a palette with a style override. |
| **Per-style example galleries** | Real before/after pages, screenshotted, to make style selection concrete. |
| **Dark-mode palette variants** | Several palettes are dark-first today; a systematic light/dark pair per product type would be better. |

## Later — wanted, needs design work first

- **Figma export** of a generated design system (tokens + styles).
- **W3C Design Token Community Group format** output alongside the current Markdown.
- **A benchmark** that measures whether the skill actually improves generated UI, rather than asserting it. This is the most valuable unbuilt thing in the project and the hardest to do honestly.
- **VS Code extension** surfacing the database without an AI assistant.

## Out of scope

Saying no keeps the project coherent:

- **A paid or "pro" tier.** Everything ships in this repository under MIT, permanently.
- **Runtime network calls.** The search engine stays offline and dependency-free — no API keys, no telemetry. This is why it's usable in restricted environments.
- **Generating images or assets.** This project decides *what a design should be*; rendering it is the assistant's job.
- **Framework-specific component libraries.** The stack files describe guidelines, not shipped components.
- **Python dependencies.** Standard library only. It's the reason `uipro init` works everywhere.

---

## Versioning

Releases are automated from [Conventional Commits](https://www.conventionalcommits.org/) via semantic-release. Adding data is a `feat:` (minor). Correcting existing data is a `fix:` (patch). Changing a CSV schema or the search API is breaking (`feat!:`).

## Proposing something

Open a [feature request](https://github.com/nicohodt/claude-code-ui-ux-skill/issues/new/choose) or a [Discussion](https://github.com/nicohodt/claude-code-ui-ux-skill/discussions). Roadmap items are added when someone makes the case for one — this list is not fixed by the maintainer alone.
