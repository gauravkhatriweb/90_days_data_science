"""
Day 71 — Linear regression
===========================
You already fitted one on Day 67:  beta = solve(X.T @ X, X.T @ y)
Today that line gets its name, its justification, and its ASSUMPTIONS.

Exercise 7 is the one that matters: the residual plot catches more
problems than any test statistic, and it takes ten seconds.
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import solve

rng = np.random.default_rng(42)


# 1 -- generate a known relationship. DRAW A LINE BY EYE FIRST.
#      MY EYEBALLED SLOPE: ____   INTERCEPT: ____
def make_data(n=100, slope=2.5, intercept=10, noise=8):
    x = rng.uniform(0, 50, n)
    y = intercept + slope * x + rng.normal(0, noise, n)
    return x, y


# 2 -- residuals for the eyeballed line vs the fitted line.
#      SSE eyeballed: ____   SSE fitted: ____
def ex_02(): pass


# 3 -- WHY SQUARED. Sum of RAW residuals for a deliberately terrible model.
#      It is near ZERO. Then do the same with squares.
def ex_03():
    x, y = make_data()
    terrible = np.full_like(y, y.mean())          # predicts the mean, always
    raw = (y - terrible).sum()
    squared = ((y - terrible) ** 2).sum()
    print(f"  sum of RAW residuals     : {raw:12.6f}   <- near zero. Useless.")
    print(f"  sum of SQUARED residuals : {squared:12.2f}   <- honest")
    # NAME A COST OF CHOOSING SQUARED ERROR:


# 4 -- fit by the CLOSED FORM. Compare with the eyeball guess.
def ex_04():
    x, y = make_data()
    X = np.column_stack([np.ones(len(x)), x])
    beta = solve(X.T @ X, X.T @ y)
    print(f"  intercept {beta[0]:.4f}   slope {beta[1]:.4f}")
    return beta


# 5 -- compare with sklearn.LinearRegression.
#      AGREE TO HOW MANY DECIMAL PLACES? ____
def ex_05(): pass


# 6 -- BREAK IT. Add a perfectly collinear column.
#      solve() FAILS. sklearn DOES NOT.
#      WHAT DID SKLEARN SILENTLY DO?  IS THAT GOOD OR DANGEROUS?
def ex_06(n=200):
    x1 = rng.uniform(0, 50, n)
    x2 = x1 * 3.0                                  # perfectly collinear
    y = 10 + 2.5 * x1 + rng.normal(0, 5, n)
    X = np.column_stack([np.ones(n), x1, x2])
    print(f"  rank {np.linalg.matrix_rank(X)} of {X.shape[1]} columns")
    try:
        solve(X.T @ X, X.T @ y)
    except np.linalg.LinAlgError as e:
        print("  my solver:", e)
    # now fit sklearn on the SAME X and print its coefficients.
    # WHAT DID IT RETURN? WHY DID IT NOT ERROR?


# 7 -- THE RESIDUAL PLOT. Fit a LINE to genuinely CURVED data.
#      THE CURVE IS OBVIOUS IN THE RESIDUALS AND INVISIBLE IN R-SQUARED.
def ex_07(n=200):
    x = rng.uniform(0, 10, n)
    y = 3 + 2 * x + 0.8 * x**2 + rng.normal(0, 3, n)     # quadratic truth
    X = np.column_stack([np.ones(n), x])
    beta = solve(X.T @ X, X.T @ y)
    fitted = X @ beta
    resid = y - fitted

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    axes[0].scatter(x, y, s=8); axes[0].plot(np.sort(x), (X @ beta)[np.argsort(x)], "r")
    axes[0].set_title("Looks like a reasonable fit")
    axes[1].scatter(fitted, resid, s=8); axes[1].axhline(0, color="k", lw=1)
    axes[1].set_xlabel("fitted"); axes[1].set_ylabel("residual")
    axes[1].set_title("The residual plot says it is not")
    fig.tight_layout()
    ss_res, ss_tot = (resid**2).sum(), ((y - y.mean())**2).sum()
    print(f"  R-squared = {1 - ss_res/ss_tot:.4f}   <- looks fine, and the model is wrong")


# 8 -- HETEROSCEDASTICITY. Build it, then see the fan in the residual plot.
def ex_08(): pass


# 9 -- Fit on YOUR Project 3 data.
#      INTERPRET ONE COEFFICIENT IN A FULL SENTENCE:
#
#      "A one-unit increase in ______ is associated with a ______ change in
#       ______, HOLDING ALL OTHER FEATURES CONSTANT."
#
#      WHAT DOES "HOLDING CONSTANT" ASSUME HERE, AND IS IT REALISTIC?
#
#      WHY IS "CAUSES" THE WRONG WORD?
def ex_09(): pass


# MINI ASSESSMENT -- 6 minutes
#   price = 12000 + 3200*area - 850*age
#     1. interpret each coefficient, in full sentences:
#     2. what does the intercept mean? is it meaningful here?
#     3. one thing this model CANNOT tell you that someone will ask it to:


if __name__ == "__main__":
    print("--- ex_03 why squared ---");   ex_03()
    print("--- ex_04 closed form ---");   ex_04()
    print("--- ex_06 breaking it ---");   ex_06()
    print("--- ex_07 residual plot ---"); ex_07()
    plt.show()
