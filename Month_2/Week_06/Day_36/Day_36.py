"""
Day 36 — Joins
===============
THE RULE: predict the row count before. Check it after.

merge  -> combines on VALUES
concat -> STACKS
Using concat when you meant merge gives a taller table full of NaN.
"""
import pandas as pd


# 1 -- build an item -> category lookup for your PBS items
def ex_01(df): pass


# 2 -- LEFT JOIN. PREDICT THE ROW COUNT FIRST.
#      PREDICTED: ____    ACTUAL: ____
def ex_02(prices, categories):
    pass


# 3 -- all four join types on the same pair. Record every row count.
#      inner: ____   left: ____   right: ____   outer: ____
def ex_03(a, b):
    pass


# 4 -- indicator=True. How many items had no category? INSPECT them.
#      left_only count: ____     ARE THESE EXPECTED?
def ex_04(a, b):
    pass


# 5 -- THE DUPLICATE-KEY DISASTER.
#      Add a duplicate to the lookup, join, watch the rows inflate
#      AND the revenue total change. Nothing errors.
#      rows before: ____   rows after: ____   total before: ____   total after: ____
#      WOULD I HAVE NOTICED THIS IN REAL WORK?
def ex_05(prices, categories):
    pass


# 6 -- validate="many_to_one" catches the same thing LOUDLY.
#      WHY IS AN ERROR BETTER THAN A CHECK AFTERWARDS?
def ex_06(prices, categories):
    pass


# 7 -- composite key: join on item AND month
def ex_07(a, b): pass

# 8 -- left_on / right_on with differently named columns
def ex_08(a, b): pass


# 9 -- concat vs merge. Do the WRONG one on purpose.
#      WHAT DID concat PRODUCE WHEN I MEANT merge?
def ex_09(a, b): pass


# 10 -- TIDY DATA. State the three rules, then judge your own data.
#       1.
#       2.
#       3.
#       DOES MY PBS DATA SATISFY THEM?  WHICH RULE DOES IT BREAK?


# MINI ASSESSMENT -- 6 minutes, closed book
def revenue_by_region_category(transactions, items, regions):
    """Keep EVERY transaction. Report unmatched counts on each side."""
    pass


if __name__ == "__main__":
    print("Build your lookup table, then work through 1-10.")
