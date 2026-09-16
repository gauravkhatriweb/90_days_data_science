"""
Day 33 — Missing data, dtypes, text, and the SQL track begins
==============================================================
This is where analysts actually spend their time.

THE FIRST QUESTION IS NEVER "how do I fill this?"
IT IS "why is this missing?"  The answer changes what you are allowed to do.
"""
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

RAW = Path("project_1/data/raw")


# =============================================================================
# MISSING DATA
# =============================================================================

# 1 -- counts, percentages, and the per-ROW missing distribution
def ex_01(df):
    pass


# 2 -- dropna four ways. Report how many rows EACH removes.
def ex_02(df):
    #   dropna()                    -> removed ____
    #   dropna(subset=['price'])    -> removed ____
    #   dropna(thresh=5)            -> removed ____
    #   dropna(axis=1)              -> removed ____ columns
    pass


# 3 -- fillna: mean / median / constant / ffill.
#      COMPARE THE RESULTING MEANS. The choice changes your answer.
#      mean-filled   mean: ____
#      median-filled mean: ____
#      ffill-ed      mean: ____
#      WHAT DOES THIS SAY ABOUT REPORTING A MEAN FROM IMPUTED DATA?
def ex_03(df):
    pass


# 4 -- Classify YOUR PBS missingness.
#      MCAR / MAR / MNAR:
#      JUSTIFICATION:
#      WHAT AM I THEREFORE ALLOWED TO DO?


# 5 -- THE INT-TO-FLOAT SURPRISE. One NaN turns ids into 1001.0
def ex_05():
    s = pd.Series([1001, 1002, 1003])
    print(f"  clean  dtype: {s.dtype}")
    s2 = pd.Series([1001, 1002, np.nan])
    print(f"  one NaN dtype: {s2.dtype}   values: {s2.tolist()}")
    # FIX with the nullable Int64 dtype (capital I):


# =============================================================================
# DTYPES
# =============================================================================

# 6 -- to_numeric(errors='coerce'). COUNT what it turned into NaN, then INSPECT those rows.
#      WHY IS coerce BETTER THAN LETTING IT RAISE?
def ex_06(df):
    pass


# 7 -- parse dates, including a column with TWO different formats
def ex_07(df):
    pass


# 8 -- convert a repeated string column to 'category'. Measure memory both ways.
#      before: ____ KB    after: ____ KB
def ex_08(df):
    pass


# =============================================================================
# TEXT -- Day 7, vectorised
# =============================================================================

# 9 -- chain .str methods to clean PBS item names
def ex_09(df):
    pass


# 10 -- .str.contains with and without na=False. See the failure.
#       WHAT ERROR DOES na=True GIVE, AND WHY?
def ex_10(df):
    pass


# 11 -- .str.split(expand=True) to break a combined field into columns
def ex_11(df):
    pass


# =============================================================================
# THE TRAP
# =============================================================================

# 12 -- SettingWithCopyWarning. Reproduce it, then fix it twice.
#       HOW DOES THIS CONNECT TO DAY 29's VIEW-VS-COPY?
def ex_12(df):
    subset = df[df["price"] > 1000]
    subset["flag"] = True                 # the warning fires here
    # FIX A -- explicit .copy():
    # FIX B -- df.loc[mask, col] = value:
    pass


# =============================================================================
# SQL -- build the database, then use Day_33.sql
# =============================================================================

def build_db(df, path="project_1/prices.db"):
    con = sqlite3.connect(path)
    df.to_sql("prices", con, if_exists="replace", index=False)
    print(f"  wrote {len(df)} rows to {path}")
    return con


# 16 -- THE COMPARISON. Same question, both tools.
#       WHICH READS BETTER?
#       WOULD THAT CHANGE AT 50 MILLION ROWS?
def ex_16(df, con):
    pass


# MINI ASSESSMENT -- 10 minutes. The seed of Day 41's pipeline.
def load_and_clean(path) -> tuple[pd.DataFrame, dict]:
    """Load, coerce numerics, parse dates, clean item names.

    Returns (clean_df, report) where report states:
      - how many values were coerced to NaN, per column
      - how many rows were dropped, and why
      - what was left alone, and why
    """
    pass


if __name__ == "__main__":
    ex_05()
