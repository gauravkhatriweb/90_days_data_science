"""
Project 3 — dataset construction.
==================================
NO MODELLING IN THIS FILE.

Order:
  1. load and join
  2. CHECK THE GRAIN
  3. availability test -> drop the leaks IN CODE, with a comment
  4. split -- BEFORE anything else
  5. baselines
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

RAW = Path("data/raw")
PROCESSED = Path("data/processed")


# -----------------------------------------------------------------------------
# 1-2 -- load, join, and CHECK THE GRAIN
# -----------------------------------------------------------------------------
def build_dataset() -> pd.DataFrame:
    """One row per ______ .

    GRAIN:
    HOW I VERIFIED IT:
    """
    pass


# -----------------------------------------------------------------------------
# 3 -- THE AVAILABILITY TEST. Drop the leaks here, with reasons.
# -----------------------------------------------------------------------------
LEAKING_COLUMNS = {
    # "column_name": "why it would not exist at prediction time",
}

def drop_leaks(df: pd.DataFrame) -> pd.DataFrame:
    """Every drop needs a reason in LEAKING_COLUMNS.

    THE TEST: would I know this value AT THE MOMENT I need the prediction?
    THE HARDEST CALL WAS:
    """
    pass


# -----------------------------------------------------------------------------
# 4 -- SPLIT. Before EDA, before scaling, before anything.
# -----------------------------------------------------------------------------
def split(df: pd.DataFrame):
    """STRATEGY:            random / stratified / time-ordered / grouped
    WHY:
    WHAT THE WRONG ONE WOULD HAVE DONE:

    The test set is saved separately and touched ONCE, on Day 82.
    """
    pass


# -----------------------------------------------------------------------------
# 5 -- BASELINES. Compute these before any model exists.
# -----------------------------------------------------------------------------
def baselines(y_train) -> dict:
    """
    majority class / predict-the-mean : ____
    current business rule             : ____
    THE HONEST COMPARISON             : ____

    Every later number gets compared with these.
    """
    pass


if __name__ == "__main__":
    df = build_dataset()
    # df = drop_leaks(df)
    # train, test = split(df)
    # print(baselines(train["target"]))
    print("No modelling today. Infrastructure only.")
