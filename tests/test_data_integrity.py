"""Structural integrity of the CSV design database.

These guard the contract every contributor's PR touches: a malformed row silently
degrades search results rather than raising, so it has to fail here instead.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from conftest import DATA_DIR, STACKS_DIR, all_data_csvs, read_csv, read_dicts

CSV_FILES = all_data_csvs()
CSV_IDS = [p.name for p in CSV_FILES]

# Every per-stack guideline file shares one schema so `--stack <name>` can treat
# them interchangeably.
STACK_HEADER = [
    "No",
    "Category",
    "Guideline",
    "Description",
    "Do",
    "Don't",
    "Code Good",
    "Code Bad",
    "Severity",
    "Docs URL",
]


def test_data_directory_is_populated() -> None:
    assert len(CSV_FILES) >= 30, "expected the full CSV database to be present"


@pytest.mark.parametrize("path", CSV_FILES, ids=CSV_IDS)
def test_csv_parses_and_has_header(path: Path) -> None:
    header, rows = read_csv(path)
    assert header, f"{path.name} has no header row"
    assert rows, f"{path.name} has no data rows"
    assert all(col.strip() for col in header), f"{path.name} has an empty column name"
    assert len(header) == len(set(header)), f"{path.name} has duplicate column names"


@pytest.mark.parametrize("path", CSV_FILES, ids=CSV_IDS)
def test_no_ragged_rows(path: Path) -> None:
    """Every row must have exactly as many cells as the header.

    A short row shifts every later column, so the search engine would index the
    wrong field without ever erroring.
    """
    header, rows = read_csv(path)
    ragged = [
        (i, len(row)) for i, row in enumerate(rows, start=2) if len(row) != len(header)
    ]
    assert not ragged, (
        f"{path.name}: {len(ragged)} row(s) have the wrong cell count "
        f"(header has {len(header)}); first offenders: {ragged[:5]}"
    )


@pytest.mark.parametrize("path", CSV_FILES, ids=CSV_IDS)
def test_id_column_is_sequential_and_unique(path: Path) -> None:
    header, rows = read_csv(path)
    if header[0] != "No":
        pytest.skip(f"{path.name} has no 'No' identifier column")
    ids = [row[0].strip() for row in rows]
    assert all(v.isdigit() for v in ids), f"{path.name} has a non-numeric 'No' value"
    numbers = [int(v) for v in ids]
    assert numbers == list(range(1, len(numbers) + 1)), (
        f"{path.name}: 'No' column must run 1..{len(numbers)} with no gaps or "
        "duplicates — renumber after inserting a row"
    )


@pytest.mark.parametrize(
    "path", sorted(STACKS_DIR.glob("*.csv")), ids=lambda p: p.name
)
def test_stack_files_share_one_schema(path: Path) -> None:
    header, _ = read_csv(path)
    assert header == STACK_HEADER, (
        f"{path.name} deviates from the shared stack schema.\n"
        f"expected: {STACK_HEADER}\nactual:   {header}"
    )


def test_product_types_are_unique() -> None:
    products = read_dicts(DATA_DIR / "products.csv")
    names = [row["Product Type"].strip().lower() for row in products]
    duplicates = {n for n in names if names.count(n) > 1}
    assert not duplicates, f"duplicate product types: {sorted(duplicates)}"


def test_every_palette_maps_to_a_product_type() -> None:
    """colors.csv is advertised as aligned 1:1 with products.csv."""
    products = {
        row["Product Type"].strip().lower()
        for row in read_dicts(DATA_DIR / "products.csv")
    }
    palettes = [row["Product Type"].strip() for row in read_dicts(DATA_DIR / "colors.csv")]
    orphans = [p for p in palettes if p.lower() not in products]
    assert not orphans, (
        f"{len(orphans)} palette(s) reference a product type that is not in "
        f"products.csv: {orphans[:5]}"
    )


def test_typography_google_fonts_urls_are_well_formed() -> None:
    rows = read_dicts(DATA_DIR / "typography.csv")
    bad = [
        row["Font Pairing Name"]
        for row in rows
        if not row["Google Fonts URL"].startswith("https://fonts.googleapis.com/")
    ]
    assert not bad, f"font pairings with a malformed Google Fonts URL: {bad}"


def test_no_severity_typos() -> None:
    """Severity drives rule ordering, so an unrecognised value silently downranks.

    Two vocabularies are in use: the four-level scale used by the guideline and
    stack files, and the banded scale used by ``react-performance.csv``.
    """
    allowed = {
        "CRITICAL", "HIGH", "MEDIUM", "LOW",
        "MEDIUM-HIGH", "LOW-MEDIUM",
    }
    offenders: list[str] = []
    for path in CSV_FILES:
        header, rows = read_csv(path)
        if "Severity" not in header:
            continue
        idx = header.index("Severity")
        for i, row in enumerate(rows, start=2):
            value = row[idx].strip().upper()
            if value and value not in allowed:
                offenders.append(f"{path.name}:{i} -> {row[idx]!r}")
    assert not offenders, f"unrecognised Severity values: {offenders[:10]}"
