"""
Day 39 — Seaborn
=================
Seaborn wants LONG data. If a call is fighting you, your data is probably wide.

AXES-LEVEL  : histplot boxplot scatterplot lineplot   -- accept ax=
FIGURE-LEVEL: displot catplot relplot pairplot lmplot -- create their own figure,
                                                          and ax= RAISES.
"""
import matplotlib.pyplot as plt
import seaborn as sns


# 1 -- theme once, at the top. colorblind costs nothing.
sns.set_theme(style="whitegrid", palette="colorblind", context="notebook")


# 2 -- histplot with hue + kde, then the same data as an ecdfplot.
#      WHY CAN AN ECDF NOT MISLEAD THE WAY A HISTOGRAM CAN?
def ex_02(df): pass


# 3 -- boxplot vs violinplot, side by side.
#      FIND A CASE WHERE THE VIOLIN SHOWS SOMETHING THE BOX HIDES.
#      WHAT WAS IT?  WHY DOES IT MATTER?
def ex_03(df): pass


# 4 -- barplot default vs estimator="sum".
#      NAME A BUSINESS QUESTION WHERE READING THE DEFAULT AS A TOTAL
#      WOULD BE BADLY WRONG:
def ex_04(df): pass


# 5 -- correlation heatmap. annot=True, center=0.
#      WHY DOES center=0 MATTER ON A DIVERGING SCALE?
def ex_05(df_wide): pass


# 6 -- pairplot on FIVE columns.
#      WHY WOULD I NOT DO THIS ON FIFTY?
def ex_06(df): pass


# 7 -- THE ERROR. Call a figure-level function with ax=. Read the message.
#      THE ERROR SAID:
#      THE FIX:
def ex_07(df):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    # sns.displot(data=df, x="price", ax=axes[0])   # <- raises. Why?
    # fix: use the axes-level twin
    pass


# 8 -- relplot with col="item" -- faceting, one panel per item
def ex_08(df): pass


if __name__ == "__main__":
    print("Seaborn mechanics first (~20 min), then the project notebook.")
