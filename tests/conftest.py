"""Shared fixtures for the UI/UX Pro Max test suite.

Tests run against the source of truth (``src/ui-ux-pro-max/``), not the mirrored
copies under ``cli/assets/`` or ``.claude/skills/``. The mirrors are verified
separately by the "Check asset sync" workflow.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = REPO_ROOT / "src" / "ui-ux-pro-max"
SCRIPTS_DIR = SKILL_ROOT / "scripts"
DATA_DIR = SKILL_ROOT / "data"
STACKS_DIR = DATA_DIR / "stacks"

# The search engine imports its siblings by bare module name.
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def read_csv(path: Path) -> tuple[list[str], list[list[str]]]:
    """Return ``(header, rows)`` for a CSV file, preserving raw cell text."""
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        return [], []
    return rows[0], rows[1:]


def read_dicts(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def all_data_csvs() -> list[Path]:
    """Every runtime CSV, top-level plus per-stack files."""
    return sorted(DATA_DIR.glob("*.csv")) + sorted(STACKS_DIR.glob("*.csv"))


@pytest.fixture(scope="session")
def data_dir() -> Path:
    return DATA_DIR


@pytest.fixture(scope="session")
def colors() -> list[dict[str, str]]:
    return read_dicts(DATA_DIR / "colors.csv")


@pytest.fixture(scope="session")
def core():
    import core as core_module  # noqa: PLC0415 - path is set up above

    return core_module


@pytest.fixture(scope="session")
def design_system():
    import design_system as ds_module  # noqa: PLC0415

    return ds_module
