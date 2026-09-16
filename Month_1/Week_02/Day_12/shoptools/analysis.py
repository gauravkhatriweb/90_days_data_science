"""Analysis helpers. Move your Day 4 functions here, then add median.

Do NOT `import statistics` for median. Write it. You need to understand
what it does before Day 48, where median is the first robust statistic
you meet -- and the reason outliers do not move it is the whole point.
"""
from __future__ import annotations


def median(numbers: list[float]) -> float | None:
    """Middle value. For an EVEN count, the mean of the two middle values.

    The even case is where almost everyone gets this wrong. Test it.
    """
    pass


def summarise(numbers: list[float]) -> dict:
    """Return count, total, mean, median, minimum, maximum in ONE pass where possible."""
    pass


def total_revenue(rows: list[dict], *, min_qty: int = 1) -> float:
    pass


def top_n(rows: list[dict], *, key: str, n: int = 3) -> list[dict]:
    pass


def group_totals(rows: list[dict], *, by: str, value: str) -> tuple[dict, int]:
    pass
