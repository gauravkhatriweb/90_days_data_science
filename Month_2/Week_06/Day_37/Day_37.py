"""
Day 37 — Reshaping: long, wide, and why it matters
===================================================
Neither shape is "correct". The right shape is the one the NEXT step needs.

  Seaborn      -> LONG
  correlation  -> WIDE
  scikit-learn -> WIDE (one column per feature)
"""
import pandas as pd


# 1 -- Is my PBS data long or wide? PRINT THE EVIDENCE.
#      ANSWER:
def ex_01(df): pass


# 2 -- melt to long. VERIFY the row count = rows x value_columns.
#      expected: ____   actual: ____
def ex_02(df): pass


# 3 -- pivot back. Confirm you recovered the original.
def ex_03(df_long): pass


# 4 -- TRIGGER pivot's duplicate error ON PURPOSE.
#      WHAT DID THE ERROR JUST TELL ME ABOUT MY DATA?
def ex_04(df_long): pass


# 5 -- pivot_table on the same duplicated data. It aggregates SILENTLY.
#      WHY IS THE ERROR MORE USEFUL THAN THE SILENCE?
def ex_05(df_long): pass


# 6 -- pivot_table with margins=True
def ex_06(df_long): pass


# 7 -- crosstab: category by month, counts then normalize="index"
#      WHAT DOES normalize="index" CHANGE THE QUESTION TO?
def ex_07(df): pass


# 8 -- groupby(["a","b"]).sum().unstack() -- cross-tab in one line
def ex_08(df): pass


# 9 -- SHAPE FOR PURPOSE. One dataset, three shapes.
def ex_09(df):
    # (a) Seaborn line plot        -> shape: ____   columns: ____
    # (b) correlation matrix       -> shape: ____   columns: ____
    # (c) scikit-learn feature X   -> shape: ____   columns: ____
    pass


# 10 -- THE THREE TIDY RULES
#       1.
#       2.
#       3.
#       WHICH DOES MY PBS DATA BREAK?
#       DOES IT MATTER FOR THIS PROJECT?


# MINI ASSESSMENT -- 5 minutes, closed book
def month_by_item(df_long) -> pd.DataFrame:
    """Wide: month x item, average price, totals row and column, 0 where absent.
    Then melt it back and confirm nothing was lost except the totals.
    """
    pass


if __name__ == "__main__":
    print("Load your PBS data, then work through 1-10.")
