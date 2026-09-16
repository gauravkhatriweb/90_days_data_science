"""
Project 1 — the cleaning pipeline.
===================================
Every step returns DATA and a RECORD OF WHAT IT DID.
A step that silently drops 400 rows is indistinguishable from a bug.

ORDER MATTERS:
  1 columns -> 2 types -> 3 dates -> 4 categories -> 5 impossible -> 6 missing

  Missing LAST, because coercion in step 2 CREATES missing values. Handling
  them in step 1 means your "no missing data" check passes on data that
  still has missing data.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd


@dataclass
class CleaningReport:
    """Accumulates what each step did. This is the evidence, not the log."""

    rows_in: int = 0
    rows_out: int = 0
    steps: list[tuple[str, int, str]] = field(default_factory=list)
    dropped: pd.DataFrame | None = None

    def log(self, step: str, count: int, note: str = "") -> None:
        pass

    def render(self) -> str:
        """A readable summary. This text goes in the README on Day 45."""
        pass


# -----------------------------------------------------------------------------
# 1 -- column names.  Strip the BOM: Day 11's '﻿'.
# -----------------------------------------------------------------------------
def _standardise_columns(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    pass


# -----------------------------------------------------------------------------
# 2 -- numeric coercion.  errors="coerce". Count what became NaN.
# -----------------------------------------------------------------------------
def _coerce_numeric(df: pd.DataFrame, cols: list[str]) -> tuple[pd.DataFrame, int]:
    pass


# -----------------------------------------------------------------------------
# 3 -- dates. Handle the formats you ACTUALLY found. Count failures.
# -----------------------------------------------------------------------------
def _parse_dates(df: pd.DataFrame, col: str) -> tuple[pd.DataFrame, int]:
    pass


# -----------------------------------------------------------------------------
# 4 -- item names. MUST be before grouping, or 'Lahore' and 'lahore' are two groups.
# -----------------------------------------------------------------------------
ITEM_CANONICAL: dict[str, str] = {
    # fill from what you found on Day 39
}

def _canonicalise_items(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    pass


# -----------------------------------------------------------------------------
# 5 -- impossible rows. RETURN THE DROPPED ROWS, not just a count.
#      A number you cannot inspect is a number you cannot defend.
# -----------------------------------------------------------------------------
def _drop_impossible(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    pass


# -----------------------------------------------------------------------------
# 6 -- missing values. LAST.
# -----------------------------------------------------------------------------
def _handle_missing(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    """Strategy decided on Day 33.

    STRATEGY:
    WHY:
    WHAT I AM ASSUMING:
    """
    pass


# -----------------------------------------------------------------------------
# the pipeline
# -----------------------------------------------------------------------------
def clean(raw: pd.DataFrame) -> tuple[pd.DataFrame, CleaningReport]:
    pass


def load_and_clean(path: Path) -> tuple[pd.DataFrame, CleaningReport]:
    pass


if __name__ == "__main__":
    df, report = load_and_clean(Path("data/raw/spi.xlsx"))
    print(report.render())
    # DOES EVERY NUMBER MAKE SENSE?
    # ANYTHING SURPRISING IS EITHER A BUG OR A FINDING. WHICH?
