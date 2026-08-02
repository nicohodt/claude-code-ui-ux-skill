# Claude Code UI/UX Skill — AI Design Intelligence for Claude, Cursor & Windsurf

**The open-source Claude skill that makes AI-generated UI and UX actually good.** Instead of hoping the model guesses a decent design, this skill gives it a searchable design-intelligence database — **84 UI styles, 192 color palettes, 74 font pairings, 99 UX guidelines, 161 industry reasoning rules, and 25 chart types across 22 tech stacks** — and a generator that turns any product brief into a complete, concrete design system.

Built for **[Claude Code](https://claude.com/product/claude-code)**. Works with Cursor, Windsurf, GitHub Copilot, Codex, Gemini CLI, and 14 more AI coding assistants.

<p align="center">
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/blob/main/README.md">🇺🇸 English</a> |
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/blob/main/README.zh.md">🇨🇳 简体中文</a>
</p>

<p align="center">
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/releases"><img src="https://img.shields.io/github/v/release/nicohodt/claude-code-ui-ux-skill?style=for-the-badge&color=blue" alt="Latest release of the Claude Code UI/UX skill"></a>
  <img src="https://img.shields.io/badge/reasoning_rules-161-green?style=for-the-badge" alt="161 industry design reasoning rules">
  <img src="https://img.shields.io/badge/UI_styles-84-purple?style=for-the-badge" alt="84 UI design styles">
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/blob/main/LICENSE"><img src="https://img.shields.io/github/license/nicohodt/claude-code-ui-ux-skill?style=for-the-badge&color=green" alt="MIT licensed"></a>
</p>

<p align="center">
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/actions/workflows/tests.yml"><img src="https://img.shields.io/github/actions/workflow/status/nicohodt/claude-code-ui-ux-skill/tests.yml?branch=main&style=flat-square&label=tests" alt="Test suite status"></a>
  <img src="https://img.shields.io/badge/tests-192-brightgreen?style=flat-square" alt="192 automated tests">
  <img src="https://img.shields.io/badge/WCAG-enforced_in_CI-success?style=flat-square" alt="WCAG contrast enforced in CI">
  <a href="https://www.npmjs.com/package/ui-ux-pro-max-cli"><img src="https://img.shields.io/npm/dm/ui-ux-pro-max-cli?style=flat-square&label=npm%20downloads" alt="npm downloads per month"></a>
  <img src="https://img.shields.io/badge/dependencies-0-success?style=flat-square" alt="Zero Python runtime dependencies">
</p>

<p align="center">
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22"><img src="https://img.shields.io/github/issues/nicohodt/claude-code-ui-ux-skill/good%20first%20issue?style=flat-square&color=7057ff&label=good%20first%20issues" alt="Good first issues — open for contributors"></a>
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/pulls"><img src="https://img.shields.io/github/issues-pr/nicohodt/claude-code-ui-ux-skill?style=flat-square&color=blue&label=open%20PRs" alt="Open pull requests"></a>
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/graphs/contributors"><img src="https://img.shields.io/github/contributors/nicohodt/claude-code-ui-ux-skill?style=flat-square&label=contributors" alt="Contributors"></a>
  <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/stargazers"><img src="https://img.shields.io/github/stars/nicohodt/claude-code-ui-ux-skill?style=flat-square&logo=github" alt="GitHub stars"></a>
</p>

---

## 🙌 We want your pull request

This project is **built by its contributors** — every UI style, palette, and industry rule is a row in a CSV file that anyone can add. No design degree required, no build step to learn, no CLA to sign.

**Our promise to contributors:**

| | |
|---|---|
| ⚡ **Fast review** | Every PR gets a first response within **48 hours**. No PR rots here. |
| 📝 **No CLA, no paperwork** | MIT in, MIT out. Open a PR and you're done. |
| 🧩 **One CSV row is a real contribution** | Adding a single color palette or UX rule is a genuine, credited, merge-worthy PR. |
| 🏆 **Everyone gets credit** | All contributors are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md) and in the release notes. |
| 💬 **Questions are welcome** | Stuck on your first PR? [Open a Discussion](https://github.com/nicohodt/claude-code-ui-ux-skill/discussions) — we'd rather help than have you give up. |
| 🎁 **100% free forever** | No premium tier, no paywalled data, no "enterprise edition". Everything lives in this repo. |

**Start here:**

- 🌱 [**Good first issues**](https://github.com/nicohodt/claude-code-ui-ux-skill/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) — small, well-scoped, and waiting for you
- 🆘 [**Help wanted**](https://github.com/nicohodt/claude-code-ui-ux-skill/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) — bigger pieces we can't get to
- 📖 [**CONTRIBUTING.md**](CONTRIBUTING.md) — a 5-minute path from fork to merged PR
- 💡 [**Contribution ideas**](#-what-we-need-right-now) — a concrete wish list, below

> **New to open source?** This is a deliberately friendly first repo. The most valuable contributions are plain text in CSV files — no TypeScript, no Python, no tooling. See [your first contribution in 5 minutes](CONTRIBUTING.md#your-first-contribution-in-5-minutes).

---

## Table of contents

- [What this skill does](#what-this-skill-does)
- [Quick start](#quick-start)
- [Why use a design skill instead of just prompting?](#why-use-a-design-skill-instead-of-just-prompting)
- [Accessibility is verified, not claimed](#accessibility-is-verified-not-claimed)
- [How the design system generator works](#how-the-design-system-generator-works)
- [Features](#features)
- [Supported AI assistants](#supported-ai-assistants)
- [Supported tech stacks](#supported-tech-stacks)
- [Usage & example prompts](#usage--example-prompts)
- [Advanced: the search CLI](#advanced-the-search-cli)
- [Contributing](#-contributing)
- [What we need right now](#-what-we-need-right-now)
- [FAQ](#faq)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## What this skill does

AI coding assistants are excellent at writing components and terrible at deciding what those components should look like. Left alone, they converge on the same purple-gradient, 16px-everything, no-focus-state page — what people now call *AI slop*.

This skill fixes that by giving the agent three things it doesn't have on its own:

1. **A design knowledge base it can search.** 84 UI styles, 192 industry-matched color palettes, 74 font pairings, 99 UX guidelines and 105 icon entries, all stored locally as CSV and queried with a BM25 + regex hybrid search engine. No API calls, no network, no keys.
2. **Reasoning rules that map a product to a design.** 161 industry-specific rules that know a banking app should not use AI-purple gradients, and that a meditation app should not use a data-dense dashboard layout.
3. **A pre-delivery checklist.** Contrast ratios, focus states, touch targets, reduced-motion, responsive breakpoints — checked before the agent says "done".

Ask for *"a landing page for my beauty spa"* and the agent produces this **before** writing a line of CSS:

```
+----------------------------------------------------------------------------------------+
|  TARGET: Serenity Spa - RECOMMENDED DESIGN SYSTEM                                       |
+----------------------------------------------------------------------------------------+
|                                                                                         |
|  PATTERN: Hero-Centric + Social Proof                                                   |
|     Conversion: Emotion-driven with trust elements                                      |
|     CTA: Above fold, repeated after testimonials                                        |
|     Sections: 1. Hero  2. Services  3. Testimonials  4. Booking  5. Contact             |
|                                                                                         |
|  STYLE: Soft UI Evolution                                                               |
|     Keywords: Soft shadows, subtle depth, calming, premium feel, organic shapes         |
|     Best For: Wellness, beauty, lifestyle brands, premium services                      |
|     Performance: Excellent | Accessibility: WCAG AA                                     |
|                                                                                         |
|  COLORS:                                                                                |
|     Primary:    #E8B4B8 (Soft Pink)                                                     |
|     Secondary:  #A8D5BA (Sage Green)                                                    |
|     CTA:        #D4AF37 (Gold)                                                          |
|     Background: #FFF5F5 (Warm White)                                                    |
|     Text:       #2D3436 (Charcoal)                                                      |
|                                                                                         |
|  TYPOGRAPHY: Cormorant Garamond / Montserrat                                            |
|     Mood: Elegant, calming, sophisticated                                               |
|                                                                                         |
|  KEY EFFECTS:                                                                           |
|     Soft shadows + Smooth transitions (200-300ms) + Gentle hover states                 |
|                                                                                         |
|  AVOID (Anti-patterns):                                                                 |
|     Bright neon colors + Harsh animations + Dark mode + AI purple/pink gradients        |
|                                                                                         |
|  PRE-DELIVERY CHECKLIST:                                                                |
|     [ ] No emojis as icons (use SVG: Heroicons/Lucide)                                  |
|     [ ] cursor-pointer on all clickable elements                                        |
|     [ ] Hover states with smooth transitions (150-300ms)                                |
|     [ ] Light mode: text contrast 4.5:1 minimum                                         |
|     [ ] Focus states visible for keyboard nav                                           |
|     [ ] prefers-reduced-motion respected                                                |
|     [ ] Responsive: 375px, 768px, 1024px, 1440px                                        |
|                                                                                         |
+-----------------------------------------------------------------------------------------+
```

---

## Quick start

### Install in Claude Code (plugin marketplace)

```
/plugin marketplace add nicohodt/claude-code-ui-ux-skill
/plugin install ui-ux-pro-max@claude-code-ui-ux-skill
```

### Install with the CLI (works with every supported assistant)

```bash
npm install -g ui-ux-pro-max-cli

cd /path/to/your/project
uipro init --ai claude      # Claude Code
```

Then just ask for UI work in natural language:

```
Build a landing page for my SaaS product
```

The skill activates on its own — no slash command, no extra prompting.

### Install for another assistant

```bash
uipro init --ai cursor      # Cursor
uipro init --ai windsurf    # Windsurf
uipro init --ai copilot     # GitHub Copilot
uipro init --ai codex       # Codex CLI
uipro init --ai gemini      # Gemini CLI
uipro init --ai antigravity # Antigravity
uipro init --ai kiro        # Kiro
uipro init --ai qoder       # Qoder
uipro init --ai roocode     # Roo Code
uipro init --ai kilocode    # KiloCode
uipro init --ai trae        # Trae
uipro init --ai opencode    # OpenCode
uipro init --ai continue    # Continue
uipro init --ai codebuddy   # CodeBuddy
uipro init --ai droid       # Droid (Factory)
uipro init --ai warp        # Warp
uipro init --ai augment     # Augment
uipro init --ai codewhale   # CodeWhale
uipro init --ai all         # Every assistant at once
```

Install once for every project on your machine with `--global`:

```bash
uipro init --ai claude --global   # → ~/.claude/skills/
```

Other commands:

```bash
uipro versions              # List available versions
uipro update                # Refresh skill files from the installed CLI package
uipro uninstall             # Remove the skill (auto-detects platform)
uipro uninstall --global    # Remove the global install
```

**Prerequisites:** Python 3.x, standard library only — the search scripts install nothing and make no network calls. Check with `python3 --version`; install from [python.org](https://www.python.org/downloads/) or your package manager if missing. These steps are for **you, the human** — AI agents using this skill are instructed never to install software on your machine.

---

## Why use a design skill instead of just prompting?

| | Plain prompting | With this Claude UI/UX skill |
|---|---|---|
| **Style choice** | Whatever is statistically average — usually the same purple gradient | Matched to your industry from 84 documented styles |
| **Colors** | Invented per request, inconsistent between files | 192 palettes mapped 1:1 to product types, reused across the project |
| **Typography** | "Inter, sans-serif" every single time | 74 curated pairings with ready Google Fonts imports |
| **Accessibility** | Mentioned only if you ask | 99 UX rules enforced, WCAG AA contrast checked pre-delivery |
| **Anti-patterns** | Reproduced happily | 161 industry rules say explicitly what *not* to do |
| **Consistency across sessions** | Starts from scratch every time | `--persist` writes a `design-system/MASTER.md` the agent reads next session |
| **Cost** | Tokens spent re-explaining your design taste | Local CSV lookup, zero API calls |

---

## Accessibility is verified, not claimed

Plenty of design tools *say* they're accessible. Here it's a test that fails the build.

Every one of the 192 color palettes is checked in CI on every push:

| Check | Threshold | Status |
|---|---|---|
| Body text (`Background`/`Foreground`) | 4.5:1 — WCAG AA | ✅ all 192 palettes |
| Card text (`Card`/`Card Foreground`) | 4.5:1 — WCAG AA | ✅ all 192 palettes |
| Component text (`On Primary`, `On Secondary`, `On Accent`, `On Destructive`) | 3:1 — WCAG 1.4.11 | ✅ all 192 palettes |
| Every color is a valid hex or `rgba()` | — | ✅ enforced |
| Borders are never invisible against their background | — | ✅ enforced |

This surfaced 14 palettes shipping white text on mid-tone backgrounds at ratios as low as **2.28:1** — below even the large-text floor. They're fixed, and the test now prevents a regression.

The wider suite — **192 tests** — also covers CSV structural integrity (ragged rows, duplicate columns, sequential IDs, shared stack schema), search behaviour across all 12 domains and 22 stacks, design-system generation, and consistency between the numbers in these docs and the actual database.

```bash
pip install pytest && pytest        # run it yourself
```

Raising every component pair to the full 4.5:1 is [the top roadmap item](ROADMAP.md) and a great contribution.

---

## How the design system generator works

```
┌─────────────────────────────────────────────────────────────────┐
│  1. USER REQUEST                                                │
│     "Build a landing page for my beauty spa"                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. MULTI-DOMAIN SEARCH (5 parallel searches)                   │
│     • Product type matching (192 categories)                    │
│     • Style recommendations (84 styles)                         │
│     • Color palette selection (192 palettes)                    │
│     • Landing page patterns (34 patterns)                       │
│     • Typography pairing (74 font combinations)                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. REASONING ENGINE                                            │
│     • Match product → UI category rules                         │
│     • Apply style priorities (BM25 ranking)                     │
│     • Filter anti-patterns for industry                         │
│     • Process decision rules (JSON conditions)                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. COMPLETE DESIGN SYSTEM OUTPUT                               │
│     Pattern + Style + Colors + Typography + Effects             │
│     + Anti-patterns to avoid + Pre-delivery checklist           │
└─────────────────────────────────────────────────────────────────┘
```

### 161 industry-specific reasoning rules

| Category | Examples |
|----------|----------|
| **Tech & SaaS** | SaaS, Micro SaaS, B2B Service, Developer Tool / IDE, AI/Chatbot Platform, Cybersecurity Platform |
| **Finance** | Fintech/Crypto, Banking, Insurance, Personal Finance Tracker, Invoice & Billing Tool |
| **Healthcare** | Medical Clinic, Pharmacy, Dental, Veterinary, Mental Health, Medication Reminder |
| **E-commerce** | General, Luxury, Marketplace (P2P), Subscription Box, Food Delivery |
| **Services** | Beauty/Spa, Restaurant, Hotel, Legal, Home Services, Booking & Appointment |
| **Creative** | Portfolio, Agency, Photography, Gaming, Music Streaming, Photo/Video Editor |
| **Lifestyle** | Habit Tracker, Recipe & Cooking, Meditation, Weather, Diary, Mood Tracker |
| **Emerging Tech** | Web3/NFT, Spatial Computing, Quantum Computing, Autonomous Drone Fleet |

Each rule carries a recommended layout pattern, style priority, color mood, typography mood, key effects, and explicit anti-patterns.

> **Missing your industry?** That's [one CSV row away](CONTRIBUTING.md#add-an-industry-reasoning-rule) — and one of the most useful PRs you can send.

---

## Features

- **84 UI styles** — Glassmorphism, Claymorphism, Minimalism, Brutalism, Neumorphism, Bento Grid, Dark Mode, AI-Native UI, and more
- **192 color palettes** — industry-specific, aligned 1:1 with the 192 product types
- **74 font pairings** — curated typography combinations with Google Fonts imports
- **25 chart types** — recommendations for dashboards and analytics, with library picks
- **22 tech stacks** — stack-specific implementation guidelines
- **99 UX guidelines** — best practices, anti-patterns, and accessibility rules
- **161 reasoning rules** — industry-specific design system generation
- **16 GSAP motion presets** — hover, scroll reveal, stagger, page transition, parallax, loading
- **105 icon entries** — Phosphor, Heroicons and Lucide recommendations with import code
- **Design dials** — bias output with `--variance`, `--motion` and `--density` flags
- **Fully offline** — CSV data + Python standard library. No API keys, no telemetry, no network calls.

<details>
<summary><b>General styles (49)</b></summary>

| # | Style | Best For |
|---|-------|----------|
| 1 | Minimalism & Swiss Style | Enterprise apps, dashboards, documentation |
| 2 | Neumorphism | Health/wellness apps, meditation platforms |
| 3 | Glassmorphism | Modern SaaS, financial dashboards |
| 4 | Brutalism | Design portfolios, artistic projects |
| 5 | 3D & Hyperrealism | Gaming, product showcase, immersive |
| 6 | Vibrant & Block-based | Startups, creative agencies, gaming |
| 7 | Dark Mode (OLED) | Night-mode apps, coding platforms |
| 8 | Accessible & Ethical | Government, healthcare, education |
| 9 | Claymorphism | Educational apps, children's apps, SaaS |
| 10 | Aurora UI | Modern SaaS, creative agencies |
| 11 | Retro-Futurism | Gaming, entertainment, music platforms |
| 12 | Flat Design | Web apps, mobile apps, startup MVPs |
| 13 | Skeuomorphism | Legacy apps, gaming, premium products |
| 14 | Liquid Glass | Premium SaaS, high-end e-commerce |
| 15 | Motion-Driven | Portfolio sites, storytelling platforms |
| 16 | Micro-interactions | Mobile apps, touchscreen UIs |
| 17 | Inclusive Design | Public services, education, healthcare |
| 18 | Zero Interface | Voice assistants, AI platforms |
| 19 | Soft UI Evolution | Modern enterprise apps, SaaS |
| 20 | Neubrutalism | Gen Z brands, startups, Figma-style |
| 21 | Bento Box Grid | Dashboards, product pages, portfolios |
| 22 | Y2K Aesthetic | Fashion brands, music, Gen Z |
| 23 | Cyberpunk UI | Gaming, tech products, crypto apps |
| 24 | Organic Biophilic | Wellness apps, sustainability brands |
| 25 | AI-Native UI | AI products, chatbots, copilots |
| 26 | Memphis Design | Creative agencies, music, youth brands |
| 27 | Vaporwave | Music platforms, gaming, portfolios |
| 28 | Dimensional Layering | Dashboards, card layouts, modals |
| 29 | Exaggerated Minimalism | Fashion, architecture, portfolios |
| 30 | Kinetic Typography | Hero sections, marketing sites |
| 31 | Parallax Storytelling | Brand storytelling, product launches |
| 32 | Swiss Modernism 2.0 | Corporate sites, architecture, editorial |
| 33 | HUD / Sci-Fi FUI | Sci-fi games, space tech, cybersecurity |
| 34 | Pixel Art | Indie games, retro tools, creative |
| 35 | Bento Grids | Product features, dashboards, personal |
| 36 | Spatial UI (VisionOS) | Spatial computing apps, VR/AR |
| 37 | E-Ink / Paper | Reading apps, digital newspapers |
| 38 | Gen Z Chaos / Maximalism | Gen Z lifestyle, music artists |
| 39 | Biomimetic / Organic 2.0 | Sustainability tech, biotech, health |
| 40 | Anti-Polish / Raw Aesthetic | Creative portfolios, artist sites |
| 41 | Tactile Digital / Deformable UI | Modern mobile apps, playful brands |
| 42 | Nature Distilled | Wellness brands, sustainable products |
| 43 | Interactive Cursor Design | Creative portfolios, interactive |
| 44 | Voice-First Multimodal | Voice assistants, accessibility apps |
| 45 | 3D Product Preview | E-commerce, furniture, fashion |
| 46 | Gradient Mesh / Aurora Evolved | Hero sections, backgrounds, creative |
| 47 | Editorial Grid / Magazine | News sites, blogs, magazines |
| 48 | Chromatic Aberration / RGB Split | Music platforms, gaming, tech |
| 49 | Vintage Analog / Retro Film | Photography, music/vinyl brands |

</details>

<details>
<summary><b>Landing page styles (8)</b></summary>

| # | Style | Best For |
|---|-------|----------|
| 1 | Hero-Centric Design | Products with strong visual identity |
| 2 | Conversion-Optimized | Lead generation, sales pages |
| 3 | Feature-Rich Showcase | SaaS, complex products |
| 4 | Minimal & Direct | Simple products, apps |
| 5 | Social Proof-Focused | Services, B2C products |
| 6 | Interactive Product Demo | Software, tools |
| 7 | Trust & Authority | B2B, enterprise, consulting |
| 8 | Storytelling-Driven | Brands, agencies, nonprofits |

</details>

<details>
<summary><b>BI / analytics dashboard styles (10)</b></summary>

| # | Style | Best For |
|---|-------|----------|
| 1 | Data-Dense Dashboard | Complex data analysis |
| 2 | Heat Map & Heatmap Style | Geographic/behavior data |
| 3 | Executive Dashboard | C-suite summaries |
| 4 | Real-Time Monitoring | Operations, DevOps |
| 5 | Drill-Down Analytics | Detailed exploration |
| 6 | Comparative Analysis Dashboard | Side-by-side comparisons |
| 7 | Predictive Analytics | Forecasting, ML insights |
| 8 | User Behavior Analytics | UX research, product analytics |
| 9 | Financial Dashboard | Finance, accounting |
| 10 | Sales Intelligence Dashboard | Sales teams, CRM |

</details>

> The tables above document 67 named styles; the full `styles.csv` database ships 84. [Documenting the rest](CONTRIBUTING.md) is an open, beginner-friendly task.

---

## Supported AI assistants

**Skill mode (auto-activates, no command needed):** Claude Code, Cursor, Windsurf, Antigravity, Codex CLI, Continue, Gemini CLI, OpenCode, Qoder, CodeBuddy, Droid (Factory), KiloCode, Warp, Augment, CodeWhale

**Workflow mode (invoke with a slash command):** Kiro, GitHub Copilot, Roo Code, KiloCode

```
/ui-ux-pro-max Build a landing page for my SaaS product
```

> **Trae:** switch to **SOLO** mode first, then the skill activates on UI/UX requests.

---

## Supported tech stacks

| Category | Stacks |
|----------|--------|
| **Web (HTML)** | HTML + Tailwind (default) |
| **React ecosystem** | React, Next.js, shadcn/ui |
| **Vue ecosystem** | Vue, Nuxt.js, Nuxt UI |
| **Angular** | Angular |
| **PHP** | Laravel (Blade, Livewire, Inertia.js) |
| **Other web** | Svelte, Astro, Three.js |
| **Desktop** | JavaFX, WPF, WinUI 3, Avalonia, Uno Platform, UWP |
| **iOS** | SwiftUI |
| **Android** | Jetpack Compose |
| **Cross-platform** | React Native, Flutter |

Mention your stack in the prompt, or let it default to HTML + Tailwind.

> **Your stack missing?** Adding a stack is a self-contained CSV file and a great first PR — see [Add a tech stack](CONTRIBUTING.md#add-a-tech-stack).

---

## Usage & example prompts

```
Build a landing page for my SaaS product

Create a dashboard for healthcare analytics

Design a portfolio website with dark mode

Make a mobile app UI for e-commerce

Build a fintech banking app with dark theme

Review this page for accessibility and UX problems
```

**What happens under the hood:**

1. **You ask** for any UI/UX task — build, design, create, implement, review, fix, improve
2. **A design system is generated** by the reasoning engine before any code is written
3. **Recommendations are matched** to your product type: styles, colors, typography, motion
4. **Code is generated** with the right tokens, spacing, and stack-specific patterns
5. **Pre-delivery checks** run against the UX anti-pattern list

---

## Advanced: the search CLI

The skill is just data plus a Python script, so you can query it directly.

> If you installed for Continue, swap `.claude/skills/` for `.continue/skills/`; for Droid (Factory) use `.factory/skills/`.

```bash
# Generate a full design system (ASCII output)
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness" --design-system -p "Serenity Spa"

# Markdown output instead
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "fintech banking" --design-system -f markdown

# Search a single domain
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "glassmorphism" --domain style
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "elegant serif" --domain typography
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "dashboard" --domain chart

# Stack-specific guidelines
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "form validation" --stack react
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "responsive layout" --stack html-tailwind
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "tableview binding" --stack javafx

# Full, untruncated data
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "SaaS" --domain style --json
```

**Search domains:** `product`, `style`, `typography`, `color`, `landing`, `chart`, `ux`, `icons`, `react`, `web`, `google-fonts`, `gsap`

**Design dials** (only with `--design-system`):

```bash
python3 .../search.py "SaaS dashboard" --design-system --variance 8 --motion 6 --density 9
```

`--variance` biases style selection (centered/minimal → bold/asymmetric), `--motion` attaches a matching GSAP snippet, `--density` overrides the spacing scale (spacious → dense/dashboard).

### Persist your design system across sessions

```bash
# Write design-system/MASTER.md
python3 .../search.py "SaaS dashboard" --design-system --persist -p "MyApp"

# Add a page-specific override
python3 .../search.py "SaaS dashboard" --design-system --persist -p "MyApp" --page "dashboard"
```

```
design-system/
├── MASTER.md           # Global source of truth (colors, typography, spacing, components)
└── pages/
    └── dashboard.md    # Page-specific overrides — only the deviations
```

Page files override the master. Point the agent at them in a new session:

```
I am building the [Page Name] page. Please read design-system/MASTER.md.
Also check if design-system/pages/[page-name].md exists.
If the page file exists, prioritize its rules. If not, use the Master rules exclusively.
Now, generate the code...
```

---

## 🤝 Contributing

**Every contribution counts here, and small ones count most.** The design database is CSV — the highest-value PRs are plain text.

```bash
# 1. Fork on GitHub, then:
git clone https://github.com/YOUR_USERNAME/claude-code-ui-ux-skill.git
cd claude-code-ui-ux-skill

# 2. Edit the source of truth
#    src/ui-ux-pro-max/data/*.csv     ← styles, colors, typography, rules
#    src/ui-ux-pro-max/scripts/*.py   ← search engine & generator
#    src/ui-ux-pro-max/templates/     ← per-assistant templates

# 3. Sync + verify (only if you touched data/scripts/templates)
cd cli && npm install
npm run sync:assets && npm run check:assets
npm run validate:csv && npm run smoke:domains

# 4. Branch, commit, PR
git checkout -b feat/your-feature
git commit -m "feat: add Bauhaus Revival style"
git push -u origin feat/your-feature
gh pr create
```

| Document | What's in it |
|---|---|
| [CONTRIBUTING.md](CONTRIBUTING.md) | The five-minute path, plus a recipe and column schema for every data type |
| [ROADMAP.md](ROADMAP.md) | What's planned, what's wanted, and what's deliberately out of scope |
| [SUPPORT.md](SUPPORT.md) | Where to ask questions and what response times to expect |
| [CLAUDE.md](CLAUDE.md) | Architecture and the sync rules between source and mirrors |
| [CHANGELOG.md](CHANGELOG.md) | Release history |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community standards |
| [SECURITY.md](SECURITY.md) | How to report a vulnerability |

### 💡 What we need right now

Pick anything from this list, open a PR — no need to ask permission first.

| Area | What's needed | Difficulty |
|------|---------------|------------|
| 🎨 **UI styles** | Document the 17 styles in `styles.csv` not yet in the README tables | 🟢 Beginner |
| 🌈 **Color palettes** | Palettes for underserved industries: agriculture, logistics, public sector, education | 🟢 Beginner |
| 🔤 **Font pairings** | Non-Latin script pairings — CJK, Arabic, Devanagari, Cyrillic | 🟢 Beginner |
| 🏭 **Industry rules** | Any industry not in the 161: nonprofits, gov services, marketplaces, hardware | 🟢 Beginner |
| ♿ **UX guidelines** | WCAG 2.2 additions, cognitive accessibility, screen-reader patterns | 🟡 Intermediate |
| 🌍 **Translations** | `README.[lang].md` in your language — Spanish, French, German, Japanese, Portuguese, Hindi | 🟢 Beginner |
| 📚 **Docs & examples** | Real before/after examples of the skill improving a page | 🟢 Beginner |
| 🧱 **New tech stacks** | Solid, Qwik, Remix, Blazor, Ionic, Lit, Kotlin Multiplatform | 🟡 Intermediate |
| ✨ **GSAP presets** | More motion tiers, Framer Motion / Motion One equivalents | 🟡 Intermediate |
| 🔍 **Search engine** | Ranking quality, synonym handling, typo tolerance in `core.py` | 🔴 Advanced |
| 🖥️ **CLI** | New assistant targets, better `uipro init` diagnostics | 🟡 Intermediate |
| 🧪 **Tests** | Coverage for `search.py` domains and CLI e2e paths | 🟡 Intermediate |

Don't see your idea? [Open an issue](https://github.com/nicohodt/claude-code-ui-ux-skill/issues/new/choose) — proposals are welcome and get answered.

### Contributors

Every person who has shipped a change here is listed in **[CONTRIBUTORS.md](CONTRIBUTORS.md)**.

<a href="https://github.com/nicohodt/claude-code-ui-ux-skill/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=nicohodt/claude-code-ui-ux-skill" alt="Contributors to the Claude Code UI/UX skill" />
</a>

---

## FAQ

### What is a Claude skill?

A skill is a folder of instructions and data that [Claude Code](https://claude.com/product/claude-code) loads when it's relevant to your request. Unlike a prompt you paste each time, a skill lives in your project (or globally in `~/.claude/skills/`) and activates automatically. This one activates whenever you ask for UI, UX, design, layout, color, typography, or accessibility work.

### Which Claude skill is best for UI/UX design?

This one is the most complete open-source option: 84 UI styles, 192 color palettes, 74 font pairings, 99 UX guidelines and 161 industry reasoning rules, all searchable offline. It's MIT licensed, has no paid tier, and works in 19 AI coding assistants — not just Claude Code.

### Does this work with Cursor and Windsurf too?

Yes. Run `uipro init --ai cursor` or `uipro init --ai windsurf`. The skill also supports GitHub Copilot, Codex CLI, Gemini CLI, Antigravity, Kiro, Qoder, Roo Code, KiloCode, Trae, OpenCode, Continue, CodeBuddy, Droid, Warp, Augment and CodeWhale.

### Does it need an API key or send data anywhere?

No. The database is local CSV and the search engine is Python standard library. No network calls, no keys, no telemetry. The only optional network use is the CLI checking GitHub for new releases.

### How is this different from just telling Claude to "make it look good"?

"Make it look good" resolves to the average of the model's training data — the purple gradient, the same font, no focus states. This skill replaces that average with an explicit, industry-matched choice plus a list of anti-patterns to avoid, and then checks the result against WCAG AA contrast, touch targets and reduced-motion rules before delivery.

### Can I use it commercially?

Yes. MIT licensed — use it in commercial products, fork it, ship it. See [LICENSE](LICENSE).

### Is it really free? Is there a paid tier?

Completely free, and there is no paid tier. Everything in the database ships in this repository under MIT.

### How do I contribute a new UI style or color palette?

Add a row to the relevant CSV in `src/ui-ux-pro-max/data/`, run `npm run sync:assets` in `cli/`, and open a PR. Full instructions in [CONTRIBUTING.md](CONTRIBUTING.md#your-first-contribution-in-5-minutes) — it takes about five minutes and no prior knowledge of the codebase.

### Do I need to be a designer to contribute?

No. Most contributions are documenting a style, palette or rule that already exists in the wild. If you can describe why a fintech dashboard shouldn't use pastel gradients, you can contribute.

### Which languages is the documentation available in?

English and [简体中文](README.zh.md). Translations into other languages are actively wanted — see [Ways to contribute](CONTRIBUTING.md#ways-to-contribute).

---

## Troubleshooting

### `uipro: unknown command 'uninstall'` / `'update'`

Your CLI is outdated:

```bash
npm install -g ui-ux-pro-max-cli@latest
uipro uninstall
```

### `uipro uninstall` says "No installed AI skill directories detected"

The skill was installed somewhere else. Either:

```bash
cd /path/to/your/project && uipro uninstall   # run where you installed it
uipro uninstall --global                      # remove the global install

# or remove manually
rm -rf .claude/skills/ui-ux-pro-max     # Claude Code
rm -rf .cursor/skills/ui-ux-pro-max     # Cursor
rm -rf .windsurf/skills/ui-ux-pro-max   # Windsurf
rm -rf .agents/skills/ui-ux-pro-max     # Antigravity / Codex
```

### Marketplace install fails with "Zip file contains a symbolic link"

Known issue in versions before v2.5.1 — the repo used symlinks internally. This repository contains no symlinks; update, or install via the CLI:

```bash
npm install -g ui-ux-pro-max-cli && uipro init --ai claude
```

### `npm install -g` fails with a permission error

Use a Node version manager, or skip the global install:

```bash
npx ui-ux-pro-max-cli init --ai claude
```

### Python not found

The search scripts need Python 3.x. Install from [python.org](https://www.python.org/downloads/) or your package manager. AI agents are instructed to ask you rather than install it themselves.

### Design system output is cut off

Human-readable output truncates long fields at 300 characters. Use `--json`:

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "SaaS" --domain style --json
```

---

## Releases

Releases are automated with semantic-release and [Conventional Commits](https://www.conventionalcommits.org/):

- `dev` → beta prereleases (`2.6.0-beta.1`)
- `main` → stable releases (`2.6.0`)

Use `fix:` for patches, `feat:` for minor versions, `feat!:` or `BREAKING CHANGE:` for majors. Versions stay in sync across `skill.json`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `cli/package.json`.

---

## Star history

[![Star history chart for the Claude Code UI/UX skill](https://api.star-history.com/svg?repos=nicohodt/claude-code-ui-ux-skill&type=Date)](https://star-history.com/#nicohodt/claude-code-ui-ux-skill&Date)

---

## License

[MIT](LICENSE) — free for personal and commercial use.

## Also works with

- [Claude Code](https://claude.com/product/claude-code) — primary target
- [AdaL](https://sylph.ai/) — self-evolving AI coding agent ([docs](https://docs.sylph.ai/) · [GitHub](https://github.com/SylphAI-Inc/adal-cli))

---

<p align="center">
  <b>Maintained by <a href="https://github.com/nicohodt">@nicohodt</a> and <a href="https://github.com/nicohodt/claude-code-ui-ux-skill/graphs/contributors">everyone who sends a PR</a>.</b><br>
  <sub>If this made your AI-built UI better, a ⭐ helps other developers find it.</sub>
</p>
