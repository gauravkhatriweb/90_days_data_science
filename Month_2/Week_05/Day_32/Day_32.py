"""
Day 32 — Pandas mechanics
==========================
Twelve exercises, then Project 1 acquisition.

THE RITUAL -- run these five on EVERY dataset you ever load, in this order:
    df.shape        what size is it, really
    df.info()       dtypes and non-null counts
    df.head()       does it look like what you expected
    df.isna().sum() how much is missing, and where
    df.describe()   do the numbers make sense
Thirty seconds. Catches hours of confusion.
"""
import numpy as np
import pandas as pd

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 20)


# 1 -- build a Series three ways. Inspect .index and .values.
def ex_01():
    pass


# 2 -- INDEX ALIGNMENT. Predict the result BEFORE running.
#      MY PREDICTION:
def ex_02():
    a = pd.Series([1, 2, 3], index=["x", "y", "z"])
    b = pd.Series([10, 20, 30], index=["z", "y", "x"])
    print(a + b)
    # WHY DOES PANDAS ALIGN ON LABEL RATHER THAN POSITION?
    # WHAT BUG DOES THAT PREVENT?


# 3 -- DataFrame from a dict, from a list of dicts, from a NumPy array
def ex_03():
    pass


# 4 -- read_csv with index_col, parse_dates, usecols, dtype
def ex_04():
    pass


# 5 -- THE RITUAL on a real file
def ritual(df: pd.DataFrame, name="dataset"):
    print(f"\n=== {name} ===")
    print(f"shape: {df.shape}")
    df.info()
    print(df.head())
    print("\nmissing per column:\n", df.isna().sum())
    print("\n", df.describe())


# 6 -- loc vs iloc. Same selection both ways, then show the slice-end difference.
#      loc slice end is ________ , iloc slice end is ________
def ex_06():
    pass


# 7 -- df["col"] vs df[["col"]]. Print type() of each.
def ex_07():
    pass


# 8 -- boolean filtering: single, compound with &, then the same via .query()
def ex_08():
    pass


# 9 -- set_index / reset_index / sort_index / sort_values
def ex_09():
    pass


# 10 -- nlargest / value_counts / nunique / sample
def ex_10():
    pass


# 11 -- add a computed column THREE ways. Time each.
#       FASTEST: ______   SLOWEST: ______   WHY:
def ex_11():
    pass


# 12 -- read_excel on a REAL PBS file.
#       WHAT I HAD TO PASS TO MAKE IT LOAD:
#         header=
#         skiprows=
#         usecols=
#         sheet_name=
#       WHAT read_excel HAD TO HANDLE THAT read_csv DID NOT:
def ex_12(path="project_1/data/raw/spi.xlsx"):
    pass


if __name__ == "__main__":
    ex_02()
