# Applying to open-source support programs

Working notes for applying to OSS credit/funding programs, plus the verified project facts an application asks for.

> **Verify the terms yourself before applying.** Program eligibility, amounts and application windows change frequently, and the details below are not guaranteed to be current. Treat the links as the source of truth and this page as preparation.

---

## The programs

| Program | What it is | Link |
|---|---|---|
| **OpenAI — Codex for OSS** | Application form offering Codex access/credits to open-source maintainers. | <https://openai.com/form/codex-for-oss/> |
| **Anthropic — Claude for open source** | Anthropic has run credit programs for OSS maintainers and for projects building on Claude. Check the current offering before applying. | <https://www.anthropic.com/> · <https://support.claude.com/> |
| **GitHub Sponsors** | Recurring or one-off funding directly from users. Already wired up in [`.github/FUNDING.yml`](../.github/FUNDING.yml) — you must still enable it on your account. | <https://github.com/sponsors> |
| **GitHub Accelerator / Secure Open Source Fund** | Periodic cohort programs for maintainers. Cohort-based, so timing matters. | <https://github.com/accelerator> |
| **thanks.dev / Open Collective** | Dependency-graph-based and fiscal-host funding respectively. Worth adding once there are dependents. | <https://thanks.dev> · <https://opencollective.com> |

### One thing to get right first

Enable **GitHub Sponsors** on the `nicohodt` account. `.github/FUNDING.yml` already points at it, but GitHub *silently hides* the Sponsor button when the account isn't enrolled — no error, it just doesn't render. Several programs also check whether a project has a funding path already set up.

---

## Verified project facts

Every number below is checked by the test suite (`tests/test_advertised_counts.py`), so it is safe to quote in an application. Re-run `pytest` before submitting if time has passed.

**What it is:** an open-source skill/plugin that gives AI coding assistants a searchable design-intelligence database, so their UI output is grounded in explicit design rules rather than the statistical average of their training data.

| | |
|---|---|
| **License** | MIT |
| **Language** | Python (standard library only — zero runtime dependencies) + TypeScript CLI |
| **Distribution** | npm (`ui-ux-pro-max-cli`), Claude Code plugin marketplace, and 19 assistant integrations |
| **Database** | 84 UI styles · 192 color palettes · 192 product types · 74 font pairings · 99 UX guidelines · 161 industry reasoning rules · 105 icon entries · 25 chart types · 16 GSAP motion presets · 22 tech-stack guides |
| **Tests** | 192 tests across data integrity, WCAG contrast, search behaviour and docs/data consistency |
| **CI** | Python 3.9/3.11/3.13 on Linux, 3.13 on macOS and Windows; CSV validation; domain and stack smoke tests; CLI typecheck, build and end-to-end install; Playwright e2e |
| **Docs** | English + Simplified Chinese README, contributing guide, roadmap, support policy, security policy, code of conduct |
| **Privacy** | Fully offline at query time. No API keys, no telemetry, no network calls. |

### Answers to questions these forms usually ask

**What problem does it solve?**
AI coding assistants generate plausible components but have no basis for design decisions, so they converge on one look — the purple-gradient hero, one typeface at every size, missing focus states, unchecked contrast. This project supplies the missing layer: an offline, searchable database of design rules plus 161 industry-specific reasoning rules that state explicitly what *not* to do for a given product type, and a pre-delivery checklist covering contrast, focus states, touch targets and reduced motion.

**Why does it matter?**
Accessibility defects introduced by AI-generated UI scale with the tooling's adoption. This project encodes WCAG requirements as data an assistant consults automatically rather than guidance a developer must remember to ask for — and it enforces those requirements in CI, so the accessibility claim is verified rather than asserted.

**How would credits be used?**
Concretely, against the [roadmap](../ROADMAP.md): raising all 192 palettes from the 3:1 floor to full WCAG AA 4.5:1; adding non-Latin typography (CJK, Arabic, Devanagari, Cyrillic), which currently makes the tool markedly worse outside English-language products; expanding the 161 industry rules; and building an honest benchmark that measures whether the skill actually improves generated UI rather than assuming it does.

**What is the maintenance situation?**
Single maintainer, actively seeking contributors. Contribution is deliberately low-friction: the design database is CSV editable in the browser, there is no CLA, and the project commits to a first response on any issue or PR within 48 hours.

---

## Before you submit

Applications are usually reviewed by a person who opens the repository and forms an impression in about thirty seconds. In rough order of impact:

- [ ] **CI is green.** A red badge undoes everything else. Push to a branch and confirm the workflows pass before applying.
- [ ] **Repository description and topics are set.** See [SEO-CHECKLIST.md](SEO-CHECKLIST.md) §1 — this is also what makes the project findable.
- [ ] **Sponsors enabled**, so the funding path is live.
- [ ] **Open, labelled `good first issue`s exist.** Run `bash scripts/seed-issues.sh --yes`. Reviewers read this as evidence a project wants a community; GitHub's discovery surfaces also require it.
- [ ] **Discussions enabled**, so questions have somewhere to go.
- [ ] **A real screenshot in the README.** The single biggest thirty-second-impression lever, and currently missing.
- [ ] **Some release history.** Ship a release so the project doesn't look like a single commit.
- [ ] **Be straight about scale.** If the project is early, say so and show the trajectory. These programs fund promising early work; overstating adoption is the fastest way to lose credibility, and it is trivially checkable from the repo insights.

---

## What genuinely strengthens an application

Ranked by effect, and none of it is cosmetic:

1. **Real contributors.** More than any other signal. Everything in the contributor tooling here — the five-minute path, the seeded issues, the welcome workflow, the credit list — exists to produce this.
2. **Evidence of use.** npm download counts, stars over time, issues filed by strangers.
3. **The accessibility angle.** A design tool that enforces WCAG in CI is a substantially stronger story than a design tool that merely mentions accessibility, and it is unusual enough to be memorable. It is also true here, which matters.
4. **Being a good ecosystem citizen.** Getting listed in `awesome-claude-code` and similar lists is both a backlink and third-party validation.
5. **A benchmark.** Nobody has convincingly measured whether design skills improve AI output. Building that measurement would make this project the reference implementation rather than one of several options — it is on the roadmap for exactly that reason.
