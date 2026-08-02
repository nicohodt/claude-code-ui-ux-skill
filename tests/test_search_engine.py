"""Behavioural tests for the BM25 search engine and design system generator.

Every advertised ``--domain`` and ``--stack`` must return results; a domain that
silently returns nothing is the most common way a data edit breaks the skill.
"""

from __future__ import annotations

import json
import subprocess
import sys

import pytest

from conftest import SCRIPTS_DIR

# Representative query per domain — chosen to exercise real vocabulary rather
# than matching a single hard-coded row.
DOMAIN_QUERIES = {
    "product": "saas dashboard",
    "style": "glassmorphism",
    "typography": "elegant serif",
    "color": "fintech banking",
    "landing": "hero conversion",
    "chart": "time series dashboard",
    "ux": "accessibility contrast",
    "icons": "navigation menu",
    "react": "memo rerender performance",
    "web": "bottom navigation",
    "google-fonts": "inter",
    "gsap": "scroll reveal",
}


def test_domain_queries_cover_every_configured_domain(core) -> None:
    """Fails loudly when a new domain is added without test coverage."""
    assert set(DOMAIN_QUERIES) == set(core.CSV_CONFIG), (
        "DOMAIN_QUERIES is out of sync with core.CSV_CONFIG; "
        f"missing={set(core.CSV_CONFIG) - set(DOMAIN_QUERIES)} "
        f"extra={set(DOMAIN_QUERIES) - set(core.CSV_CONFIG)}"
    )


@pytest.mark.parametrize("domain,query", sorted(DOMAIN_QUERIES.items()))
def test_every_domain_returns_results(core, domain: str, query: str) -> None:
    result = core.search(query, domain=domain)
    assert "error" not in result, result.get("error")
    assert result["count"] > 0, (
        f"--domain {domain} returned nothing for {query!r}; "
        f"suggestions={result.get('suggestions')}"
    )
    assert result["domain"] == domain


def test_every_stack_returns_results(core) -> None:
    empty = []
    for stack in core.AVAILABLE_STACKS:
        result = core.search_stack("layout component state", stack)
        if "error" in result or result["count"] == 0:
            empty.append(stack)
    assert not empty, f"stacks returning no results: {empty}"


def test_all_22_stacks_are_registered(core) -> None:
    assert len(core.AVAILABLE_STACKS) == 22, (
        f"expected 22 advertised stacks, found {len(core.AVAILABLE_STACKS)}: "
        f"{core.AVAILABLE_STACKS}"
    )


def test_unknown_stack_reports_an_error(core) -> None:
    result = core.search_stack("anything", "not-a-real-stack")
    assert "error" in result
    assert "not-a-real-stack" in result["error"]


def test_domain_auto_detection_picks_a_sensible_domain(core) -> None:
    assert core.detect_domain("glassmorphism frosted blur") == "style"
    assert core.detect_domain("bar chart vs line chart") == "chart"
    # "font"-shaped queries may legitimately resolve to either font domain.
    assert core.detect_domain("serif heading font pairing") in {
        "typography",
        "google-fonts",
    }


def test_search_result_rows_are_non_empty(core) -> None:
    result = core.search("minimalism swiss", domain="style")
    first = result["results"][0]
    assert isinstance(first, dict) and first, "result rows must be populated dicts"


def test_empty_query_does_not_crash(core) -> None:
    result = core.search("", domain="style")
    assert "error" not in result
    assert isinstance(result["count"], int)


def test_nonsense_query_misses_cleanly(core) -> None:
    """A miss must return an empty result set with a suggestions key, not raise."""
    result = core.search("zzzzqqqqxxxx", domain="style")
    assert result["count"] == 0
    assert result["results"] == []
    assert "suggestions" in result, "a miss should always carry a suggestions key"


def test_partial_match_still_offers_suggestions(core) -> None:
    """A near-miss on real vocabulary should propose alternatives."""
    result = core.search("glassmorphis", domain="style")
    assert result["count"] == 0 or result["results"]
    if result["count"] == 0:
        assert result.get("suggestions"), "a near-miss should suggest terms"


def test_design_system_generation_is_complete(design_system) -> None:
    generated = design_system.generate_design_system(
        "beauty spa wellness", project_name="Test Spa", output_format="ascii"
    )
    assert set(generated) >= {"text", "design_system"}

    spec = generated["design_system"]
    # Every section the ASCII/Markdown renderers and the README output promise.
    for key in (
        "project_name", "category", "pattern", "style", "colors", "typography",
        "key_effects", "anti_patterns",
    ):
        assert spec.get(key), f"design system is missing the {key!r} section"

    assert spec["project_name"] == "Test Spa"
    assert generated["text"].strip(), "rendered output must not be empty"


def test_density_dial_produces_a_spacing_scale(design_system) -> None:
    """spacing_scale is only populated when the --density dial is supplied."""
    without = design_system.generate_design_system("saas dashboard", project_name="T")
    assert without["design_system"].get("spacing_scale") is None

    with_dial = design_system.generate_design_system(
        "saas dashboard", project_name="T", density=9
    )
    assert with_dial["design_system"].get("spacing_scale"), (
        "--density should override the spacing scale"
    )


@pytest.mark.parametrize(
    "query", ["fintech banking app", "healthcare analytics dashboard", "indie game portfolio"]
)
def test_design_system_generation_survives_varied_briefs(design_system, query: str) -> None:
    spec = design_system.generate_design_system(query, project_name="Test")["design_system"]
    assert spec.get("style"), f"no style resolved for {query!r}"
    assert spec.get("colors"), f"no palette resolved for {query!r}"


def test_design_system_supplies_anti_patterns(design_system) -> None:
    """Anti-patterns are the skill's main defence against generic output."""
    spec = design_system.generate_design_system("banking app", project_name="Bank")[
        "design_system"
    ]
    assert spec["anti_patterns"].strip(), "a brief must yield anti-patterns to avoid"


def test_markdown_output_format_is_supported(design_system) -> None:
    generated = design_system.generate_design_system(
        "saas dashboard", project_name="Test", output_format="markdown"
    )
    assert generated["text"].strip()


def _run_cli(*args: str) -> subprocess.CompletedProcess:
    """Invoke search.py and decode its output as UTF-8.

    ``search.py`` deliberately forces a UTF-8 stdout wrapper so its box-drawing
    output survives redirection on Windows. ``text=True`` alone would decode
    that with the *locale* codec (cp1252 on Windows runners), which raises
    UnicodeDecodeError on the box characters and hands back ``None``.
    """
    return subprocess.run(
        [sys.executable, str(SCRIPTS_DIR / "search.py"), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
    )


def test_cli_json_output_is_valid_json() -> None:
    proc = _run_cli("SaaS", "--domain", "style", "--json")
    assert proc.returncode == 0, proc.stderr
    payload = json.loads(proc.stdout)
    assert payload["count"] > 0


def test_cli_design_system_runs_end_to_end() -> None:
    proc = _run_cli("beauty spa", "--design-system", "-p", "Serenity Spa")
    assert proc.returncode == 0, proc.stderr
    assert "RECOMMENDED DESIGN SYSTEM" in proc.stdout


def test_cli_rejects_an_unknown_domain() -> None:
    proc = _run_cli("anything", "--domain", "nonsense")
    assert proc.returncode != 0, "an invalid --domain must not exit 0"
