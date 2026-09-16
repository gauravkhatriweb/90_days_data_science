"""
Day 67 — Determinants, inverses, and solving systems
=====================================================
THE FOUR STATEMENTS THAT ARE ONE STATEMENT:

    det(A) = 0
    A has no inverse
    A's columns are linearly dependent        <- Day 65
    A collapses space to fewer dimensions     <- Day 66
    Ax = b has no unique solution

They are five views of "the columns carry no independent information."

Exercises 10-11 are the point of the day: you will fit a linear regression
from first principles, and then break it on purpose.
"""
import time

import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import cond, det, inv, matrix_rank, solve

rng = np.random.default_rng(42)

ROT90   = np.array([[0, -1], [1, 0]])
STRETCH = np.array([[2, 0], [0, 1]])
COLLAPSE = np.array([[1, 2], [2, 4]])


# 1 -- apply A then B by hand, then (B @ A) at once. Identical?
def ex_01():
    v = np.array([3, 2])
    print(f"  B@(A@v) = {STRETCH @ (ROT90 @ v)}")
    print(f"  (B@A)@v = {(STRETCH @ ROT90) @ v}")


# 2 -- A@B != B@A, VISUALLY. rotate-then-stretch vs stretch-then-rotate.
def ex_02():
    G = np.mgrid[-2:2.5:0.5, -2:2.5:0.5].reshape(2, -1)
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    for ax, (M, title) in zip(axes, [
        (STRETCH @ ROT90, "rotate, THEN stretch"),
        (ROT90 @ STRETCH, "stretch, THEN rotate"),
    ]):
        out = M @ G
        ax.scatter(out[0], out[1], s=6)
        ax.set_title(title); ax.set_aspect("equal"); ax.grid(True)
    fig.tight_layout()
    # THEY ARE DIFFERENT. THAT IS WHY MATRIX MULTIPLICATION IS NOT COMMUTATIVE.


# 3 -- compose three. Predict the combined effect first.  PREDICTION:
def ex_03(): pass


# 4 -- determinants of the Day 66 matrices. Connect each to what you SAW.
def ex_04():
    for name, M in [("identity", np.eye(2)), ("scale x2", 2*np.eye(2)),
                    ("rotate 90", ROT90), ("stretch x", STRETCH),
                    ("shear", np.array([[1,1],[0,1]])), ("COLLAPSE", COLLAPSE)]:
        print(f"  {name:<12} det = {det(M):7.3f}   rank = {matrix_rank(M)}")
    # WHICH ONE PRESERVES AREA?  WHICH DESTROYS IT?


# 5 -- THE AREA PROOF. Transform a unit square, measure the output area.
#      measured area: ____   determinant: ____   MATCH?
def ex_05(): pass


# 6 -- a NEGATIVE determinant. Visualise the flip.
def ex_06(): pass


# 7 -- invert an invertible matrix. Confirm A @ A_inv == I.
def ex_07():
    A = np.array([[2, 1], [1, 3]])
    print(f"  A @ inv(A) =\n{np.round(A @ inv(A), 10)}")


# 8 -- TRY TO INVERT THE COLLAPSED MATRIX. Read the error.
#      CONNECT IT TO THE FOUR STATEMENTS:
def ex_08():
    print(f"  det(COLLAPSE) = {det(COLLAPSE)}")
    try:
        inv(COLLAPSE)
    except np.linalg.LinAlgError as e:
        print("  expected failure:", e)


# 9 -- solve vs inv @ b. Time both, compare ACCURACY on a bad system.
#      WHY NEVER USE inv?  TWO REASONS:
def ex_09(n=500):
    A = rng.random((n, n)) + np.eye(n) * 0.001      # deliberately ill-conditioned
    b = rng.random(n)
    t = time.perf_counter(); x1 = solve(A, b);     t_solve = time.perf_counter() - t
    t = time.perf_counter(); x2 = inv(A) @ b;      t_inv = time.perf_counter() - t
    print(f"  cond(A)  = {cond(A):.2e}")
    print(f"  solve    : {t_solve:.4f}s   residual {np.linalg.norm(A @ x1 - b):.2e}")
    print(f"  inv @ b  : {t_inv:.4f}s   residual {np.linalg.norm(A @ x2 - b):.2e}")


# =============================================================================
# 10 -- FIT A LINEAR REGRESSION FROM FIRST PRINCIPLES.
#       beta = solve(X.T @ X, X.T @ y)      <- the normal equations
#       Compare with sklearn. THEY SHOULD MATCH.
# =============================================================================
def ex_10(n=500):
    X = np.column_stack([np.ones(n), rng.random(n) * 100, rng.random(n) * 10])
    true_beta = np.array([5.0, 2.5, -1.2])
    y = X @ true_beta + rng.normal(0, 3, n)

    beta_hat = solve(X.T @ X, X.T @ y)
    print(f"  true       : {true_beta}")
    print(f"  my fit     : {np.round(beta_hat, 4)}")
    print(f"  det(X'X)   : {det(X.T @ X):.4e}")
    print(f"  cond(X)    : {cond(X):.2f}")
    # NOW COMPARE WITH sklearn.linear_model.LinearRegression -- do they match?
    # WHAT IS "LEARNING" IN MACHINE LEARNING, THEN?


# =============================================================================
# 11 -- NOW BREAK IT. Add a collinear column.
#       det(X'X) before: ____   after: ____
#       cond(X)  before: ____   after: ____
#       WHAT HAPPENED TO THE COEFFICIENTS?
#       WHY IS THIS DANGEROUS EVEN WHEN NOTHING ERRORS?
# =============================================================================
def ex_11(n=500):
    x1 = rng.random(n) * 100
    x2 = rng.random(n) * 10
    X_ok = np.column_stack([np.ones(n), x1, x2])
    X_bad = np.column_stack([np.ones(n), x1, x2, (x1 + x2) / 2])   # collinear

    y = X_ok @ np.array([5.0, 2.5, -1.2]) + rng.normal(0, 3, n)

    for label, X in [("clean", X_ok), ("collinear", X_bad)]:
        print(f"  {label:<10} det(X'X)={det(X.T @ X):>12.4e}   cond(X)={cond(X):>12.2f}")

    # Then: cond(X) on MY OWN Project 2 feature matrix = ____
    # SHOULD I TRUST ITS COEFFICIENTS?


# MINI ASSESSMENT -- 8 minutes
#   X has four columns; one is the MEAN of two others.
#     1. det(X'X) = ____
#     2. can I fit a regression? what happens?
#     3. cond(X) roughly = ____
#     4. which column would I drop, and how would I decide?


if __name__ == "__main__":
    print("--- ex_01 composition ---"); ex_01()
    print("--- ex_04 determinants ---"); ex_04()
    print("--- ex_07 inverse ---");      ex_07()
    print("--- ex_08 singular ---");     ex_08()
    print("--- ex_09 solve vs inv ---"); ex_09()
    print("--- ex_10 regression from scratch ---"); ex_10()
    print("--- ex_11 breaking it ---");  ex_11()
    ex_02(); plt.show()
