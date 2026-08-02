# SEO & growth checklist

Everything file-based has already been done in this repo. The items below **can only be set in the GitHub UI or externally** — they're the remaining levers for ranking on searches like *"claude skill ui ux"*, *"claude code design skill"*, and *"best claude skill for design"*.

Work top to bottom; the first five matter most.

---

## 1. Repository settings (highest impact)

Google's title tag for a GitHub repo is `GitHub - owner/repo: <repo description>`. The **repo description is the single most important on-page SEO field you control**, and it isn't stored in any file.

**Settings → General, or the ⚙️ next to "About" on the repo home page:**

**Description** — paste exactly:

```
The open-source Claude skill for UI/UX design. 84 UI styles, 192 color palettes, 74 font pairings, 99 UX guidelines & 161 industry rules across 22 stacks. Works with Claude Code, Cursor & Windsurf.
```

**Website** — `https://nicohodt.github.io/claude-code-ui-ux-skill/`

**Topics** — add all of these (GitHub topic pages are indexed and drive internal discovery):

```
claude-skill  claude-code  claude-code-skill  claude-code-plugin  anthropic
ui-ux  ui-design  ux-design  design-system  design-tokens  color-palette
typography  accessibility  wcag  ai-agents  ai-coding-assistant  cursor
windsurf  github-copilot  developer-tools  hacktoberfest  good-first-issue
```

> `hacktoberfest` and `good-first-issue` are contributor-acquisition topics — people browse them specifically looking for projects to contribute to.

**Checkboxes:** enable **Issues**, **Discussions**, **Projects**, **Preserve this repository**, and **Sponsorships** (optional).

---

## 2. Social preview image

**Settings → General → Social preview → Upload an image** (1280×640px).

This is the image that appears when the repo is shared on X, LinkedIn, Reddit, Hacker News and Slack — it directly affects click-through, which affects ranking.

Put the repo name, the tagline *"The Claude skill that makes AI-generated UI actually good"*, and the headline numbers (84 styles · 192 palettes · 161 rules) on it.

Also add a real screenshot to the repo and reference it from `README.md`:

```markdown
<p align="center">
  <img src="docs/assets/design-system-output.png"
       alt="Claude Code generating a complete design system with colors, typography and a pre-delivery accessibility checklist" width="800">
</p>
```

> The previous README pointed at `screenshots/website.png`, which did not exist — that broken image has been removed. Add a real one before re-adding the tag, and keep the alt text descriptive and keyword-bearing.

---

## 3. Enable GitHub Pages

**Settings → Pages → Source: Deploy from a branch → Branch: `main` → Folder: `/docs`**

This publishes [`docs/index.html`](index.html) at `https://nicohodt.github.io/claude-code-ui-ux-skill/`. That page already ships:

- A keyword-targeted `<title>` and meta description
- Canonical URL and `hreflang` alternates for English/Chinese
- Open Graph + Twitter Card tags
- **JSON-LD structured data**: `SoftwareApplication`, `WebSite`, and an 8-question `FAQPage`

The `FAQPage` schema is what makes the listing eligible for FAQ rich results and for surfacing in "People Also Ask" — it's the reason the FAQ wording in `README.md` and `docs/index.html` is kept in sync. If you edit one, edit the other.

---

## 4. Google Search Console

1. Add `https://nicohodt.github.io/claude-code-ui-ux-skill/` as a property at [search.google.com/search-console](https://search.google.com/search-console).
2. Verify with the HTML-tag method — paste the `<meta name="google-site-verification" ...>` tag into `<head>` in `docs/index.html`.
3. Submit `https://nicohodt.github.io/claude-code-ui-ux-skill/sitemap.xml`.
4. Use **URL Inspection → Request indexing** on the Pages URL and the GitHub repo URL.
5. Check **Enhancements → FAQ** after a week to confirm the structured data validated.

> **robots.txt note:** GitHub Pages only honours `robots.txt` at the *user site root* (`nicohodt.github.io/robots.txt`), which comes from a `nicohodt.github.io` repo — not from this project's `/docs`. That's why no `robots.txt` ships here. The sitemap works regardless once submitted directly.

Validate the structured data before requesting indexing:
- [Rich Results Test](https://search.google.com/test/rich-results)
- [Schema Markup Validator](https://validator.schema.org/)

---

## 5. npm listing

`npmjs.com` package pages rank well for tool searches. Already set in `cli/package.json`: a keyword-rich `description`, 25 `keywords`, plus `homepage`, `repository` and `bugs`.

Remaining step: **`cli/README.md` is what npm renders on the package page.** It has been rewritten for this, but confirm it looks right after the next `npm publish`.

---

## 6. Off-page signals (what actually moves rankings)

Ranking for *"claude skill ui ux"* is mostly won off GitHub. In rough order of value:

| Where | What to do |
|---|---|
| **Awesome lists** | PR into `awesome-claude-code`, `awesome-claude-skills`, `awesome-ai-tools`, `awesome-design-systems`. These are high-authority backlinks *and* a direct contributor funnel. |
| **Hacker News** | Show HN post. Lead with the problem ("AI design all looks the same"), not the feature list. |
| **Reddit** | r/ClaudeAI, r/ChatGPTCoding, r/webdev, r/Frontend, r/opensource. Post the before/after, not the repo link alone. |
| **Dev.to / Hashnode / Medium** | A tutorial titled *"How to make Claude Code stop producing AI-slop UI"* — long-tail keyword traffic, canonical back to the Pages site. |
| **Product Hunt** | One launch, on a Tuesday–Thursday. |
| **X / LinkedIn** | Before/after screenshots outperform text every time. |
| **YouTube** | Even a 3-minute screen recording; video results occupy space on the SERP you can't otherwise reach. |

Each of these is also a contributor-acquisition channel — most first-time contributors arrive from a post, not from search.

---

## 7. Keyword map

Keep these phrases appearing naturally in the README H2s, the Pages headings, and any blog posts. Don't stuff them — Google penalises repetition without substance.

| Intent | Query | Where it's targeted |
|---|---|---|
| Primary | claude skill ui ux | README H1, Pages `<title>` |
| Primary | claude code ui ux skill | Repo name, description |
| Primary | claude code design skill | Pages H1, README intro |
| Comparison | best claude skill for design | FAQ ("Which Claude skill is best for UI/UX design?") |
| Problem | ai generated design looks bad / ai slop | "Why AI-generated design looks the same" section |
| How-to | how to install claude skill | "Quick start" / "Install" sections |
| Adjacent | cursor ui ux rules | "Supported AI assistants" |
| Adjacent | ai design system generator | "How the design system generator works" |
| Contributor | claude skill good first issue | Topics, badges, issue labels |

---

## 8. Ongoing

- **Ship releases regularly.** Freshness is a ranking factor, and semantic-release already generates release notes from Conventional Commits.
- **Label 10–15 issues `good first issue` and `help wanted`.** These populate GitHub's contributor discovery surfaces — repos with zero such issues never appear there. This is the highest-leverage single action for contributor count.
- **Answer every issue and PR within 48 hours.** The README promises it, and responsiveness is what turns a first-time contributor into a repeat one.
- **Keep the FAQ in `README.md` and `docs/index.html` identical.** Contradictory answers weaken the structured data.
- **Add each new contributor to `CONTRIBUTORS.md`.** Visible credit is the cheapest retention mechanism there is.
