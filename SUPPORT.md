# Getting help

Every question gets an answer. There is no such thing as a question that is too basic here — if you had it, the documentation has a gap.

## Where to go

| I want to… | Go here |
|---|---|
| Ask how to use the skill | [Discussions → Q&A](https://github.com/nicohodt/claude-code-ui-ux-skill/discussions) |
| Report something broken | [Open a bug report](https://github.com/nicohodt/claude-code-ui-ux-skill/issues/new/choose) |
| Suggest a style, palette, or rule | [Design data issue](https://github.com/nicohodt/claude-code-ui-ux-skill/issues/new/choose) — or [add it yourself in 5 minutes](CONTRIBUTING.md#your-first-contribution-in-5-minutes) |
| Propose a feature | [Feature request](https://github.com/nicohodt/claude-code-ui-ux-skill/issues/new/choose) |
| Get unstuck on a pull request | Comment on your own PR and say so — that's what it's for |
| Report a security issue | **Not** a public issue → [SECURITY.md](SECURITY.md) |

## Response times

- **Issues and pull requests:** first response within **48 hours**
- **Discussions:** usually within a few days

This is a volunteer-maintained project, so these are honest targets rather than guarantees. If something has gone quiet for longer than that, a polite bump on the thread is welcome and will not annoy anyone.

## Before you open an issue

A quick check that resolves most reports:

```bash
# 1. Are you on the current CLI?
npm install -g ui-ux-pro-max-cli@latest
uipro --version

# 2. Does Python work?
python3 --version           # use `python` on Windows

# 3. Does the search engine itself work?
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "saas" --domain style
```

If step 3 prints results, the skill is installed correctly and the problem is likely in how your AI assistant is loading it — mention which assistant you're using in the issue.

## Commercial support

There isn't any, and there is no paid tier. This project is MIT licensed and maintained in the open. If you need something specific built, the fastest route is to [open a feature request](https://github.com/nicohodt/claude-code-ui-ux-skill/issues/new/choose) or send a pull request.
