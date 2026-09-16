"""
Day 70 — Linear algebra consolidation. Closed book.
====================================================
Ten tasks, 3 minutes each. 0 / 0.5 / 1.
Task 11 is the one that matters.
"""
import numpy as np

# 1 (D65) -- a row of a dataset is ____ ; the dataset is ____
S1 = None

# 2 (D65) -- span and linear dependence, WITHOUT the word "correlated"
S2 = None

# 3 (D65) -- why does one-hot encoding create a dependency?
S3 = None

# 4 (D66) -- what do the columns of a matrix tell you?
S4 = None

# 5 (D66) -- X is (1000,8). weights must be ____ . predictions are ____
S5 = None

# 6 (D67) -- the four equivalent statements, and why they are ONE:
#   a)            b)            c)            d)
#   THE ONE IDEA:
S6 = None

# 7 (D67) -- fit a regression with solve(X.T @ X, X.T @ y)
def t7():
    rng = np.random.default_rng(0)
    X = np.column_stack([np.ones(200), rng.random(200) * 50])
    y = X @ np.array([3.0, 1.5]) + rng.normal(0, 2, 200)
    # your line here
S7 = None

# 8 (D67) -- why solve() and not inv() @ b?  TWO reasons:
S8 = None

# 9 (D68) -- what is an eigenvector, geometrically? NO FORMULA.
S9 = None

# 10 (D68) -- why are the covariance matrix's eigenvectors the directions
#             of greatest variance?
S10 = None


# =============================================================================
# 11 -- THE INTEGRATION PARAGRAPH. From memory. No notes.
# =============================================================================
#
#   A dataset is ________________________________________________
#
#   A model is __________________________________________________
#
#   Fitting is __________________________________________________
#
#   Multicollinearity is ________________________________________
#
#   ...and it breaks fitting because ____________________________
#
#   WHICH LINK WAS WEAKEST?
#   (that is exactly what to re-read tonight)
# =============================================================================


if __name__ == "__main__":
    scores = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]
    done = [s for s in scores if s is not None]
    if done:
        print(f"Score: {sum(done)} / 10")
        print(f"Weak: {[i+1 for i, s in enumerate(scores) if s is not None and s < 1]}")
        if sum(done) < 7:
            print("Below 7 -> rewatch the four 3Blue1Brown chapters in Week 11's IF TIME.")
