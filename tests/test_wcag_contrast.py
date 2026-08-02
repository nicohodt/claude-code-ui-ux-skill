"""WCAG contrast enforcement for the color database.

The skill's central promise is that its palettes are accessible. These tests are
what make that claim verifiable instead of aspirational, and they are the reason
a palette PR can be reviewed mechanically.

Thresholds follow WCAG 2.1:
  * 4.5:1 — normal body text (SC 1.4.3 AA)
  * 3.0:1 — large text and UI component boundaries (SC 1.4.11)
"""

from __future__ import annotations

import re

import pytest

from conftest import DATA_DIR, read_dicts

HEX_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")
# Dark-mode palettes express hairline borders as translucent white, which is a
# deliberate choice rather than a malformed hex value.
RGBA_RE = re.compile(
    r"^rgba\(\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*\d{1,3}\s*,\s*(?:0|1|0?\.\d+)\s*\)$"
)

# Foreground/background pairs that render body copy — full AA applies.
BODY_TEXT_PAIRS = [
    ("Background", "Foreground"),
    ("Card", "Card Foreground"),
]

# Text sitting on a filled component (buttons, badges, chips). Labels here are
# routinely large or semibold, so 3:1 is the enforced floor; raising these to
# 4.5:1 is tracked in ROADMAP.md.
COMPONENT_TEXT_PAIRS = [
    ("Primary", "On Primary"),
    ("Secondary", "On Secondary"),
    ("Accent", "On Accent"),
    ("Destructive", "On Destructive"),
    ("Muted", "Muted Foreground"),
]

HEX_COLUMNS = [
    "Primary", "On Primary", "Secondary", "On Secondary", "Accent", "On Accent",
    "Background", "Foreground", "Card", "Card Foreground", "Muted",
    "Muted Foreground", "Destructive", "On Destructive", "Ring",
]

# Border alone may also be an rgba() overlay.
TRANSLUCENT_COLUMNS = ["Border"]


def relative_luminance(hex_color: str) -> float:
    """WCAG 2.1 relative luminance."""
    value = hex_color.strip().lstrip("#")
    channels = [int(value[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [
        c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels
    ]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast_ratio(a: str, b: str) -> float:
    la, lb = relative_luminance(a), relative_luminance(b)
    lighter, darker = max(la, lb), min(la, lb)
    return (lighter + 0.05) / (darker + 0.05)


@pytest.fixture(scope="module")
def palettes() -> list[dict[str, str]]:
    return read_dicts(DATA_DIR / "colors.csv")


def test_every_color_is_a_six_digit_hex(palettes) -> None:
    offenders = [
        f"No.{row['No']} {row['Product Type']} -> {column}={row[column]!r}"
        for row in palettes
        for column in HEX_COLUMNS
        if not HEX_RE.match(row[column].strip())
    ]
    assert not offenders, f"malformed hex values: {offenders[:10]}"


def test_translucent_columns_are_hex_or_rgba(palettes) -> None:
    offenders = [
        f"No.{row['No']} {row['Product Type']} -> {column}={row[column]!r}"
        for row in palettes
        for column in TRANSLUCENT_COLUMNS
        if not (
            HEX_RE.match(row[column].strip()) or RGBA_RE.match(row[column].strip())
        )
    ]
    assert not offenders, f"Border must be #RRGGBB or rgba(): {offenders[:10]}"


@pytest.mark.parametrize("background,foreground", BODY_TEXT_PAIRS)
def test_body_text_meets_wcag_aa(palettes, background: str, foreground: str) -> None:
    """Body copy must clear 4.5:1 in every one of the palettes."""
    failures = [
        (row["No"], row["Product Type"], round(contrast_ratio(row[background], row[foreground]), 2))
        for row in palettes
        if contrast_ratio(row[background], row[foreground]) < 4.5
    ]
    assert not failures, (
        f"{background}/{foreground} below 4.5:1 in {len(failures)} palette(s): "
        f"{failures[:8]}"
    )


@pytest.mark.parametrize("background,foreground", COMPONENT_TEXT_PAIRS)
def test_component_text_meets_minimum_contrast(
    palettes, background: str, foreground: str
) -> None:
    """Text on filled components must clear the 3:1 non-text/large-text floor."""
    failures = [
        (row["No"], row["Product Type"], round(contrast_ratio(row[background], row[foreground]), 2))
        for row in palettes
        if contrast_ratio(row[background], row[foreground]) < 3.0
    ]
    assert not failures, (
        f"{background}/{foreground} below 3:1 in {len(failures)} palette(s): "
        f"{failures[:8]}"
    )


def test_border_is_never_invisible(palettes) -> None:
    """A border set to its own background colour renders as nothing at all.

    Subtle hairlines are a legitimate choice (the database bottoms out around
    1.06:1), so this only catches the genuinely invisible case rather than
    imposing a contrast minimum WCAG does not require for decorative borders.
    Only opaque borders are checked; an rgba() overlay composites against
    whatever sits behind it, so a static ratio is not meaningful.
    """
    failures = [
        (
            row["No"],
            row["Product Type"],
            round(contrast_ratio(row["Background"], row["Border"]), 3),
        )
        for row in palettes
        if HEX_RE.match(row["Border"].strip())
        and contrast_ratio(row["Background"], row["Border"]) < 1.03
    ]
    assert not failures, f"Border indistinguishable from Background: {failures[:8]}"


def test_contrast_helpers_match_known_values() -> None:
    """Sanity-check the maths against WCAG's documented extremes."""
    assert contrast_ratio("#000000", "#FFFFFF") == pytest.approx(21.0, abs=0.01)
    assert contrast_ratio("#FFFFFF", "#FFFFFF") == pytest.approx(1.0, abs=0.01)
    # Tailwind blue-600 on white.
    assert contrast_ratio("#2563EB", "#FFFFFF") == pytest.approx(5.17, abs=0.02)
    # Order must not matter.
    assert contrast_ratio("#FFFFFF", "#2563EB") == pytest.approx(
        contrast_ratio("#2563EB", "#FFFFFF")
    )
