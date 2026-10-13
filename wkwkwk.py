"""Fail-Closed Comedy Engineering: a tiny, honest laughter helper."""

from __future__ import annotations

from typing import Any


def wkwkwk(
    topik: Any = "kehidupan",
    level: Any = 3,
    fail_closed: bool = True,
) -> dict[str, Any]:
    """Print a laugh and return a structured result.

    This function is a comedy helper, not an audit engine. It never certifies
    tests, Git state, production readiness, or any external system as passing.
    Invalid levels fall back to 3 and produce a warning code.
    """
    warnings: list[str] = []

    try:
        normalized_level = int(level)
    except (ValueError, TypeError, OverflowError):
        normalized_level = 3
        warnings.append("LEVEL_INVALID_FALLBACK_3")

    normalized_level = max(1, min(normalized_level, 20))

    print(f"{'WK' * normalized_level} 😂")
    print(f"Topik: {topik}")
    print("Kesimpulan ilmiah: perlu ngopi dulu.")

    if fail_closed:
        print("AUDIT: NOT_VERIFIED")
        print("PASS: DILARANG TANPA BUKTI")

    return {
        "status": "NOT_VERIFIED",
        "topic": topik,
        "level": normalized_level,
        "pass_allowed": False,
        "coffee_required": True,
        "fail_closed": bool(fail_closed),
        "warnings": warnings,
        "evidence": None,
    }


if __name__ == "__main__":
    wkwkwk()
    wkwkwk("Qweny dan filesystem", 8)
    wkwkwk("Bug yang berubah jadi fitur", "QWENY")
