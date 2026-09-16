"""
Day 38 — Charts that answer a question
=======================================
RULE: write the one-sentence FINDING before you draw the chart.
If you cannot state it, it is the wrong chart.

Use `fig, ax = plt.subplots()`. Never bare plt.plot().
"""
import matplotlib.pyplot as plt
import pandas as pd

OUT = "charts"      # save everything; Day 44 reuses the good ones


# 1 -- LINE: one item over time
#      FINDING:
def chart_01(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    # ax.plot(...)
    # ax.set_title("<the finding, not the contents>")
    # ax.set_xlabel("...");  ax.set_ylabel("Price (PKR/kg)")
    pass


# 2 -- LINE: four items, DIRECT-LABELLED at the line ends. No legend.
#      FINDING:
def chart_02(df): pass


# 3 -- BAR: average price by item. SORTED. ZERO-BASED.
#      FINDING:
def chart_03(df): pass


# 4 -- HISTOGRAM at 10, 30 and 100 bins, side by side.
#      HOW DID THE STORY CHANGE?
#      WHAT DOES THAT SAY ABOUT "LETTING THE DATA SPEAK"?
def chart_04(df): pass


# 5 -- BOX PLOT: price distribution per item
#      FINDING:
def chart_05(df): pass


# 6 -- SCATTER: two items against each other. Use alpha for overplotting.
#      FINDING:
def chart_06(df): pass


# 7 -- subplots(2,2): four related views, one shared title
def chart_07(df): pass


# 8 -- ANNOTATE the largest single price jump.
#      ax.annotate("+34% in one week", xy=(x, y), xytext=(x2, y2),
#                  arrowprops=dict(arrowstyle="->"))
def chart_08(df): pass


# 9 -- THE REWRITE. Take chart_03 and fix it properly.
#      Save BEFORE and AFTER. Put them side by side.
#      WHAT SPECIFICALLY MADE IT BETTER?
#        1.
#        2.
#        3.
def chart_09(df): pass


# 10 -- THE BAD CHART. Make a misleading one on purpose.
#       Truncate the y-axis, or use a dual axis.
#       WHAT DOES IT IMPLY THAT IS NOT TRUE?
#       HOW WOULD I CATCH THIS IN SOMEONE ELSE'S WORK?
def chart_10(df): pass


# =============================================================================
# THE READABILITY CHECKLIST -- run it on every chart before saving
# =============================================================================
#  [ ] title states the FINDING, not the contents
#  [ ] both axes labelled, with units
#  [ ] categorical bars sorted by value
#  [ ] direct labels instead of a legend where there are few series
#  [ ] the point being made is annotated
#  [ ] no chart junk, no 3D, no decorative colour
#  [ ] colour encodes something, and is not the ONLY encoding
# =============================================================================


if __name__ == "__main__":
    print("Load your PBS data. Write the finding first. Then draw.")
