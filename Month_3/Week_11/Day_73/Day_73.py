"""
Day 73 — R-squared, significance, and what a coefficient is worth
==================================================================
A coefficient is an ESTIMATE FROM A SAMPLE. It has a standard error,
a confidence interval, and a p-value -- and every Day 53 warning applies.

Exercises 2, 6 and 7 are the ones that change how you read a model summary.
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import cond, solve

rng = np.random.default_rng(42)


def fit(X, y):
    return solve(X.T @ X, X.T @ y)

def r_squared(y, pred):
    ss_res = ((y - pred) ** 2).sum()
    ss_tot = ((y - y.mean()) ** 2).sum()
    return 1 - ss_res / ss_tot


# 1 -- R-squared from scratch. Match sklearn's .score().
def ex_01(): pass


# =============================================================================
# 2 -- THE NOISE DEMONSTRATION.
#      Add 20 columns of PURE RANDOM NOISE. R-squared RISES EVERY TIME.
#      R2 with 1 feature : ____   with 21 features: ____
#      ADJUSTED R2       : ____                   : ____
#      WHY CAN R2 ONLY RISE?
# =============================================================================
def ex_02(n=100):
    x = rng.uniform(0, 50, n)
    y = 10 + 2.5 * x + rng.normal(0, 8, n)

    X = np.column_stack([np.ones(n), x])
    print(f"  {X.shape[1]-1:>2} real feature(s):  R2 = {r_squared(y, X @ fit(X, y)):.4f}")

    for k in (5, 10, 20):
        noise = rng.standard_normal((n, k))
        Xn = np.column_stack([X, noise])
        r2 = r_squared(y, Xn @ fit(Xn, y))
        p = Xn.shape[1] - 1
        adj = 1 - (1 - r2) * (n - 1) / (n - p - 1)
        print(f"  + {k:>2} NOISE columns:  R2 = {r2:.4f}   adjusted R2 = {adj:.4f}")
    print("  the noise columns contain NO information. R2 rose anyway.")


# 3 -- R2 on TRAIN vs TEST. How big is the gap?
#      train: ____   test: ____   gap: ____
#      WHAT DOES A LARGE GAP MEAN?
def ex_03(): pass


# 4 -- RMSE, MAE, MAPE on the same predictions.
#      WHERE DOES MAPE BREAK?  (hint: y near zero)
#      WHICH WOULD I REPORT TO A NON-TECHNICAL STAKEHOLDER, AND IN WHAT UNITS?
def ex_04(): pass


# 5 -- coefficient standard errors and t-statistics BY HAND.
#      Match statsmodels.OLS. 
def ex_05(): pass


# =============================================================================
# 6 -- THE MULTICOLLINEARITY EFFECT.
#      Fit with and without a CORRELATED TWIN feature.
#      Watch the standard errors INFLATE and the p-values COLLAPSE.
#
#      without twin: SE(b1) = ____   p = ____   cond(X) = ____
#      with twin   : SE(b1) = ____   p = ____   cond(X) = ____
#
#      CAN A MODEL PREDICT WELL AND STILL HAVE MEANINGLESS COEFFICIENTS?
# =============================================================================
def ex_06(n=300):
    x1 = rng.uniform(0, 50, n)
    twin = x1 + rng.normal(0, 0.5, n)             # 0.999 correlated
    y = 10 + 2.5 * x1 + rng.normal(0, 8, n)

    X_ok = np.column_stack([np.ones(n), x1])
    X_bad = np.column_stack([np.ones(n), x1, twin])
    print(f"  without twin: cond(X) = {cond(X_ok):10.2f}")
    print(f"  with twin   : cond(X) = {cond(X_bad):10.2f}   <- above 1000 = unreliable coefficients")
    print(f"  corr(x1, twin) = {np.corrcoef(x1, twin)[0,1]:.6f}")
    # now compute the standard errors for both and compare


# =============================================================================
# 7 -- THE MANY-FEATURES EFFECT. Fit on 20 PURE NOISE features.
#      HOW MANY CAME OUT "SIGNIFICANT" AT p < 0.05?  ____
#      (Day 53's exercise 9, now inside a model)
#      WHAT DOES THIS MEAN FOR SELECTING FEATURES BY p-VALUE?
# =============================================================================
def ex_07(n=200, k=20): pass


# =============================================================================
# 8 -- ANSCOMBE'S QUARTET. Identical statistics. Completely different data.
# =============================================================================
ANSCOMBE = {
    "I":   ([10,8,13,9,11,14,6,4,12,7,5], [8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]),
    "II":  ([10,8,13,9,11,14,6,4,12,7,5], [9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74]),
    "III": ([10,8,13,9,11,14,6,4,12,7,5], [7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]),
    "IV":  ([8,8,8,8,8,8,8,19,8,8,8],     [6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.50,5.56,7.91,6.89]),
}

def ex_08():
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    for ax, (name, (xs, ys)) in zip(axes, ANSCOMBE.items()):
        x, y = np.array(xs, float), np.array(ys, float)
        X = np.column_stack([np.ones(len(x)), x])
        b = fit(X, y)
        print(f"  {name}: mean_y={y.mean():.2f} var_y={y.var(ddof=1):.2f} "
              f"r={np.corrcoef(x,y)[0,1]:.3f} slope={b[1]:.3f} R2={r_squared(y, X@b):.3f}")
        ax.scatter(x, y); ax.plot(np.sort(x), (X @ b)[np.argsort(x)], "r")
        ax.set_title(name)
    fig.suptitle("Identical statistics. Look at the data.")
    fig.tight_layout()
    # WHAT WOULD I HAVE CONCLUDED ABOUT EACH FROM THE STATISTICS ALONE?


# 9 -- CONFIDENCE interval vs PREDICTION interval. Plot BOTH bands.
#      WHICH DOES A BUSINESS QUESTION USUALLY NEED? WHY?
def ex_09(): pass


# MINI ASSESSMENT -- 6 minutes
#   "R2 = 0.91, all coefficients significant at p<0.05. The model is ready."
#   FOUR QUESTIONS I WOULD ASK, and what answer would worry me:
#     1.
#     2.
#     3.
#     4.


if __name__ == "__main__":
    print("--- ex_02 R2 rises on pure noise ---"); ex_02()
    print("--- ex_06 multicollinearity ---");      ex_06()
    print("--- ex_08 Anscombe ---");               ex_08()
    plt.show()
