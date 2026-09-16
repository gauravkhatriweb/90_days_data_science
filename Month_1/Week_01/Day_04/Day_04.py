"""
Day 4 — Functions that do one thing
====================================
You are building a small toolkit, not doing scattered exercises.
You will import from this file on Days 11 and 12.

Requirements for every function below:
  * one job
  * a documented return contract (including the empty / invalid case)
  * options are KEYWORD-ONLY -- put a bare `*` in the signature
"""

from __future__ import annotations


# -----------------------------------------------------------------------------
# 1 -- clean_text
# -----------------------------------------------------------------------------
def clean_text(raw: str) -> str:
    """Strip, lowercase, and collapse runs of internal whitespace.

    '  SURF  EXCEL   2KG \\n'  ->  'surf excel 2kg'
    Returns '' for None or empty input.
    """
    pass


# -----------------------------------------------------------------------------
# 2 -- to_number
# -----------------------------------------------------------------------------
def to_number(value, *, default=None):
    """Convert to int if whole, else float. Return `default` if impossible.

    '42' -> 42     '42.5' -> 42.5     'abc' -> default     '' -> default
    """
    pass


# -----------------------------------------------------------------------------
# 3 -- parse_row
# -----------------------------------------------------------------------------
def parse_row(line: str, *, sep: str = ",") -> dict:
    """Parse 'item,qty,price' into a typed dict.

    Returns {} if the line does not have exactly 3 fields.
    """
    pass


# -----------------------------------------------------------------------------
# 4 -- total_revenue  (write the FULL docstring; this is the model for the rest)
# -----------------------------------------------------------------------------
def total_revenue(rows: list[dict], *, min_qty: int = 1) -> float:
    """

    """
    pass


# -----------------------------------------------------------------------------
# 5 -- top_n  (generic -- must not hardcode a key name)
# -----------------------------------------------------------------------------
def top_n(rows: list[dict], *, key: str, n: int = 3) -> list[dict]:
    pass


# -----------------------------------------------------------------------------
# 6 -- summarise  (ONE pass over the data, not five)
# -----------------------------------------------------------------------------
def summarise(numbers: list[float]) -> tuple:
    """Return (count, total, mean, minimum, maximum).

    Decide and DOCUMENT what happens for an empty list.
    """
    pass


# -----------------------------------------------------------------------------
# 7 -- validate_rows  (Day 3 ex_10, now with a contract)
# -----------------------------------------------------------------------------
def validate_rows(rows: list[dict]) -> tuple[list[dict], list[tuple[int, str]]]:
    pass


# -----------------------------------------------------------------------------
# 8 -- the mutable default trap
# -----------------------------------------------------------------------------
def buggy_add(row, rows=[]):
    """Leave this broken. It is the demonstration."""
    rows.append(row)
    return rows

def fixed_add(row, rows=None):
    pass

def demonstrate_mutable_default():
    """Call buggy_add twice, print both results, then show fixed_add behaving."""
    pass


# -----------------------------------------------------------------------------
# 9 -- safe_divide  (choose a strategy and say why in the docstring)
# -----------------------------------------------------------------------------
def safe_divide(a: float, b: float):
    """

    Strategy chosen:
    Why:
    """
    pass


# -----------------------------------------------------------------------------
# MINI ASSESSMENT -- closed book, 20 minutes
# -----------------------------------------------------------------------------
def group_totals(rows: list[dict], *, by: str, value: str) -> tuple[dict, int]:
    """Group rows by `by` and sum `value`. Return ({group: total}, skipped_count).

    Skip any row missing either key or whose `value` is not numeric.
    Document what is returned for an empty `rows`.

    You are hand-writing pandas .groupby().sum() -- you meet the one-liner on Day 34.
    """
    pass


SAMPLE = [
    {"item": "tea",   "region": "sindh",  "qty": 4, "price": 1250.0},
    {"item": "sugar", "region": "punjab", "qty": 3, "price": 180.0},
    {"item": "tea",   "region": "punjab", "qty": 2, "price": 1250.0},
    {"item": "oil",   "region": "sindh",  "qty": 1, "price": 540.0},
    {"item": "flour", "region": "sindh"},
]

if __name__ == "__main__":
    print(clean_text("  SURF  EXCEL   2KG \n"))
    print(to_number("42.5"), to_number("abc", default=0))
    print(parse_row("tea,4,1250.00"))
    print(total_revenue(SAMPLE))
    print(summarise([4, 9, 12, 7]))
    demonstrate_mutable_default()
    print(group_totals(SAMPLE, by="region", value="qty"))
