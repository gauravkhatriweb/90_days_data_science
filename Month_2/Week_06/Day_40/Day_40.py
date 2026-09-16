"""
Day 40 — How to actually explore data
======================================
THE LOOP:  ask -> PREDICT -> compute -> compare -> follow the surprise
Step 2 is the one everyone skips, and it is the one that makes it work.
"""
import numpy as np
import pandas as pd


# 1 -- Write FIVE questions about your data. Grade each. Rewrite the bad ones.
#     A good question is one where a specific answer would CHANGE WHAT YOU SAY.
#
#     Q1:                                          good / bad ->  rewrite:
#     Q2:                                          good / bad ->  rewrite:
#     Q3:                                          good / bad ->  rewrite:
#     Q4:                                          good / bad ->  rewrite:
#     Q5:                                          good / bad ->  rewrite:


# 2 -- IQR vs z-score on the same column. Do they agree?
#      WHERE DO THEY DIFFER, AND WHY?
def ex_02(s: pd.Series):
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    iqr_out = s[(s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)]
    z = (s - s.mean()) / s.std()
    z_out = s[z.abs() > 3]
    print(f"  IQR flags {len(iqr_out)},  z-score flags {len(z_out)}")
    # WHY DOES THE Z-SCORE METHOD STRUGGLE WHEN OUTLIERS ARE EXTREME?


# 3 -- Classify TEN real outliers from your data.
#      data error / real and important / real but out of scope
#       1.                      6.
#       2.                      7.
#       3.                      8.
#       4.                      9.
#       5.                     10.
#      REMOVED: ____   KEPT: ____   (these counts go in the README)


# 4 -- THE CONFOUNDING DEMONSTRATION.
#      Correlate raw price LEVELS, then correlate PERCENTAGE CHANGES.
#      Compare the two heatmaps.
#      NAIVE (levels)  mean correlation: ____
#      CHANGES         mean correlation: ____
#      WHAT WOULD I HAVE WRONGLY CONCLUDED FROM THE FIRST ONE?
def ex_04(df_wide):
    levels  = df_wide.corr()
    changes = df_wide.pct_change().corr()
    print("  levels  mean corr:", round(levels.values[np.triu_indices_from(levels, 1)].mean(), 3))
    print("  changes mean corr:", round(changes.values[np.triu_indices_from(changes, 1)].mean(), 3))


# 5 -- Decompose one series: rolling mean for trend, then the residual.
#      IS THERE VISIBLE SEASONALITY? WHAT PERIOD?
def ex_05(s: pd.Series):
    pass


# 6 -- THE SPURIOUS CORRELATION DEMONSTRATION.
#      20 PURELY RANDOM series. 190 pairs. How many exceed |0.5| by chance?
#      COUNT: ____
#      WHAT DOES THIS TEACH ME ABOUT TESTING MANY HYPOTHESES?
def ex_06(n_series=20, n_points=50, seed=0):
    rng = np.random.default_rng(seed)
    data = pd.DataFrame(rng.standard_normal((n_points, n_series)))
    c = data.corr().values
    upper = c[np.triu_indices_from(c, 1)]
    print(f"  pairs: {len(upper)}")
    print(f"  |r| > 0.3 : {(abs(upper) > 0.3).sum()}")
    print(f"  |r| > 0.5 : {(abs(upper) > 0.5).sum()}")
    print("  ...and every one of these series is pure noise.")


# =============================================================================
# MINI ASSESSMENT -- three sentences on question one.
# =============================================================================
#   WHAT I FOUND:
#
#   THE EVIDENCE:
#
#   WHAT WOULD HAVE TO BE TRUE FOR ME TO BE WRONG:
#   (this third one is the sentence most people cannot write)
# =============================================================================


if __name__ == "__main__":
    print("--- ex_06: spurious correlations in pure noise ---")
    ex_06()
