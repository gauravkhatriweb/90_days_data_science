"""
Day 34 — GroupBy
=================
Split -> apply -> combine.

agg       -> ONE ROW PER GROUP
transform -> SAME SHAPE AS INPUT      <- the one people forget
filter    -> A SUBSET OF ORIGINAL ROWS
"""
import pandas as pd


# 1 -- group by item: mean, min, max, count of price
def ex_01(df): pass

# 2 -- group by TWO keys, then flatten the MultiIndex
def ex_02(df): pass

# 3 -- named aggregation: four differently-named metrics in one table
def ex_03(df):
    # df.groupby("item").agg(
    #     avg_price=("price", "mean"),
    #     ...
    # )
    pass

# 4 -- TRANSFORM: each price compared to its item's average, in one line
def ex_04(df):
    # df["vs_item_avg"] = df["price"] - df.groupby("item")["price"].transform("mean")
    pass

# 5 -- FILTER: keep only items with >= 40 observations
def ex_05(df): pass


# 6 -- THE dropna TRAP. Group on a column containing NaN keys.
#      Compare dropna=True and dropna=False.
#      DO THE GROUP TOTALS STILL ADD UP TO THE OVERALL TOTAL?
#      HOW WOULD I CATCH THIS IN REAL WORK?
def ex_06(df):
    pass


# 7 -- THE as_index TRAP. Trigger the KeyError, then fix it two ways.
#      WHY DOES IT HAPPEN?
def ex_07(df):
    # df.groupby("region").sum()["region"]   -> KeyError
    # FIX A: .reset_index()
    # FIX B: as_index=False
    pass


# 8 -- group by month using .dt.to_period("M")
def ex_08(df): pass

# 9 -- agg with a lambda: the range (max - min) per item
def ex_09(df): pass

# 10 -- value_counts vs groupby().size(). Same answer, both ways.
#       WHEN WOULD I USE EACH?
def ex_10(df): pass


# MINI ASSESSMENT -- 6 minutes, closed book
def summary_table(df) -> pd.DataFrame:
    """Per item: mean price, price range, n observations, % change first->last.
    Exclude items with fewer than 20 observations.
    """
    pass


if __name__ == "__main__":
    print("Load your PBS data, then work through 1-10.")
