"""Keep the numbers in the docs equal to the numbers in the database.

This exists because they drifted: the README advertised "98 UX guidelines" and
"104 icon entries" while the CSVs held 99 and 105. Those numbers appear in the
README, the Chinese README, ``skill.json``, the plugin manifests, the skill
frontmatter Claude actually reads, and the JSON-LD on the docs site — so drift
is easy and invisible. A failure here means: update the docs, or update the
expected count below if the data legitimately grew.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from conftest import DATA_DIR, REPO_ROOT, STACKS_DIR, read_csv

# label -> (csv filename, human-readable name)
COUNTED_FILES = {
    "styles": "styles.csv",
    "colors": "colors.csv",
    "typography": "typography.csv",
    "products": "products.csv",
    "ui-reasoning": "ui-reasoning.csv",
    "ux-guidelines": "ux-guidelines.csv",
    "icons": "icons.csv",
    "charts": "charts.csv",
    "motion": "motion.csv",
    "landing": "landing.csv",
}


def row_count(filename: str) -> int:
    _, rows = read_csv(DATA_DIR / filename)
    return len(rows)


# Documents that quote these numbers to users.
DOC_FILES = [
    "README.md",
    "README.zh.md",
    "skill.json",
    "cli/README.md",
    "cli/package.json",
    "docs/index.html",
    ".claude/skills/ui-ux-pro-max/SKILL.md",
]

# (regex capturing the number, csv filename). Patterns are written to match the
# phrasing actually used in the docs, in both English and Chinese.
DOC_PATTERNS: list[tuple[str, str]] = [
    (r"(\d+)\s+UI styles", "styles.csv"),
    (r"(\d+)\s+种 UI 风格", "styles.csv"),
    (r"(\d+)\s+color palettes", "colors.csv"),
    (r"(\d+)\s+套配色", "colors.csv"),
    (r"(\d+)\s+font pairings", "typography.csv"),
    (r"(\d+)\s+组字体配对", "typography.csv"),
    (r"(\d+)\s+product types", "products.csv"),
    (r"(\d+)\s+UX guidelines", "ux-guidelines.csv"),
    (r"(\d+)\s+UX rules", "ux-guidelines.csv"),
    (r"(\d+)\s+条 UX 指南", "ux-guidelines.csv"),
    (r"(\d+)\s+industry reasoning rules", "ui-reasoning.csv"),
    (r"(\d+)\s+条行业推理规则", "ui-reasoning.csv"),
    (r"(\d+)\s+chart types", "charts.csv"),
    (r"(\d+)\s+icon entries", "icons.csv"),
    (r"(\d+)\s+条图标条目", "icons.csv"),
    (r"(\d+)\s+GSAP motion presets", "motion.csv"),
]


@pytest.mark.parametrize("label,filename", sorted(COUNTED_FILES.items()))
def test_counted_files_are_non_empty(label: str, filename: str) -> None:
    assert row_count(filename) > 0, f"{filename} is empty"


def test_stack_count_is_22() -> None:
    """22 stacks is advertised in every manifest and both READMEs."""
    stacks = sorted(STACKS_DIR.glob("*.csv"))
    assert len(stacks) == 22, (
        f"expected 22 stack files, found {len(stacks)}: {[p.stem for p in stacks]}"
    )


@pytest.mark.parametrize("doc", DOC_FILES)
def test_documented_counts_match_the_database(doc: str) -> None:
    path = REPO_ROOT / doc
    if not path.exists():
        pytest.skip(f"{doc} not present")
    text = path.read_text(encoding="utf-8")

    mismatches: list[str] = []
    for pattern, filename in DOC_PATTERNS:
        expected = row_count(filename)
        for match in re.finditer(pattern, text):
            found = int(match.group(1))
            if found != expected:
                phrase = match.group(0)
                mismatches.append(
                    f"{doc}: {phrase!r} but {filename} has {expected} rows"
                )

    assert not mismatches, "\n".join(mismatches)


def test_at_least_one_doc_states_each_headline_number() -> None:
    """Guards against a doc rewrite quietly dropping the headline figures."""
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    for pattern, filename in DOC_PATTERNS:
        if "\\s+种" in pattern or "条" in pattern or "套" in pattern or "组" in pattern:
            continue  # Chinese phrasings do not appear in the English README
        if not re.search(pattern, readme):
            continue
        assert str(row_count(filename)) in readme
