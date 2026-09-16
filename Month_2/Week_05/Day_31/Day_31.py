"""
Day 31 — Aggregation, masking, matrices. Last NumPy day.
=========================================================
Exercises 2, 5 and 9 are the ones that matter.
"""
import numpy as np

rng = np.random.default_rng(42)
SALES = rng.integers(0, 500, size=(100, 5))
PRODUCTS = np.array(["tea", "sugar", "oil", "flour", "ghee"])


# =============================================================================
# AGGREGATION
# =============================================================================

# 1 -- ten aggregations, with and without axis. Print shapes.
def ex_01(a=SALES):
    pass


# 2 -- THE NaN POISON. One missing value ruins the whole result.
#      Then fix it, then COUNT the NaNs.
#      WHY DOES ONE nan POISON THE WHOLE MEAN?
def ex_02():
    a = np.array([1.0, 2.0, np.nan, 4.0])
    print(f"  a.mean()       : {a.mean()}")
    print(f"  np.nanmean(a)  : {np.nanmean(a)}")
    print(f"  nan == nan     : {np.nan == np.nan}   <- this is why you use np.isnan")
    # count the NaNs:


# 3 -- argmax across an axis: which product sold most in each region?
#      Return the NAME, not the index.
def ex_03(a=SALES, names=PRODUCTS):
    pass


# =============================================================================
# MASKING
# =============================================================================

# 4 -- compound conditions with & and |
def ex_04(a=SALES):
    pass


# 5 -- THE PRECEDENCE BUG. Run it without parentheses first.
#      WHAT I EXPECTED:
#      WHAT HAPPENED:
def ex_05():
    prices = np.array([1250, 180, 2600, 540])
    qty = np.array([4, 12, 1, 25])
    try:
        bad = prices > 1000 & qty < 5      # no parentheses
        print("  no parens:", bad)
    except Exception as e:
        print("  no parens failed:", type(e).__name__, e)
    good = (prices > 1000) & (qty < 5)
    print("  with parens:", good)

    # Now try `and` instead of `&` and read the error message carefully.
    # WHAT DOES THAT ERROR ACTUALLY MEAN?


# 6 -- np.where for indices, then use them to look up names
def ex_06(a=SALES, names=PRODUCTS):
    pass


# =============================================================================
# STRUCTURE
# =============================================================================

# 7 -- vstack / hstack / concatenate / split, printing shapes at each step
def ex_07():
    pass


# 8 -- build a (1000, 3) dataset from three separate 1D arrays
def ex_08():
    pass


# =============================================================================
# MATRICES -- the preview of Days 65-68 and 71
# =============================================================================

# 9 -- `*` vs `@`. PREDICT both shapes first.
#      Then compute X @ weights -- the arithmetic inside a linear model.
#      PREDICTION for a * b :
#      PREDICTION for a @ b :
def ex_09():
    a = np.arange(6).reshape(2, 3)
    b = np.arange(6).reshape(3, 2)
    print(f"  a {a.shape}   b {b.shape}")
    print(f"  a @ b -> {(a @ b).shape}")
    try:
        print(f"  a * b -> {(a * b).shape}")
    except ValueError as e:
        print(f"  a * b -> ERROR: {e}")

    # A LINEAR MODEL, in one line:
    X = rng.random((1000, 5))          # 1000 rows, 5 features
    weights = rng.random((5, 1))       # one coefficient per feature
    predictions = X @ weights
    print(f"  X {X.shape} @ weights {weights.shape} -> {predictions.shape}")
    # On Day 74, model.predict(X) runs exactly this.


# MINI ASSESSMENT -- 7 minutes, closed book
def mini():
    marks = rng.integers(0, 100, size=(200, 6)).astype(float)
    marks[rng.random(marks.shape) < 0.05] = np.nan     # 5% missing
    # 1. subject averages ignoring missing
    # 2. missing count per subject
    # 3. students with ANY mark below 40
    # 4. best subject per student -- index, then name
    # 5. marks @ weights -- STATE THE OUTPUT SHAPE BEFORE RUNNING
    pass


if __name__ == "__main__":
    print("--- ex_02 NaN poison ---");   ex_02()
    print("--- ex_05 precedence ---");   ex_05()
    print("--- ex_09 * vs @ ---");       ex_09()
