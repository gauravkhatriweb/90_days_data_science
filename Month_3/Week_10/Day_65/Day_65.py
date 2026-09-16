"""
Day 65 — Vectors
=================
A ROW OF YOUR DATASET IS A VECTOR.
YOUR DATASET IS A CLOUD OF POINTS IN FEATURE-SPACE.

Once that is a fact rather than a metaphor, machine learning stops being
a library you call.

PLOT EVERYTHING. The geometry is the point.
"""
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)

# one customer = one point in 4-D space
CUSTOMER = np.array([34, 12, 4500, 2])      # age, orders, spend, returns


# 1 -- add, scale, negate. Plot each step.
def ex_01():
    a, b = np.array([2, 1]), np.array([1, 3])
    fig, ax = plt.subplots(figsize=(6, 6))
    for v, label in [(a, "a"), (b, "b"), (a + b, "a+b"), (3 * a, "3a"), (-a, "-a")]:
        ax.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1)
        ax.annotate(label, v)
    ax.set_xlim(-4, 8); ax.set_ylim(-4, 8); ax.grid(True); ax.set_aspect("equal")


# 2 -- a+b and b+a land in the same place. Show it geometrically.
def ex_02(): pass


# 3 -- LINEAR COMBINATION: reach a target with two given vectors.
#      FIND THE COEFFICIENTS.  (hint: np.linalg.solve)
def ex_03():
    a, b = np.array([2, 1]), np.array([1, 3])
    target = np.array([7, 8])
    # solve  c1*a + c2*b = target
    pass


# 4 -- SPAN. Independent vectors fill the plane. Dependent ones collapse to a line.
def ex_04(n=2000):
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    for ax, (v1, v2, title) in zip(axes, [
        (np.array([2, 1]), np.array([1, 3]), "independent -> spans the plane"),
        (np.array([2, 1]), np.array([4, 2]), "DEPENDENT  -> collapses to a line"),
    ]):
        c = rng.uniform(-3, 3, (n, 2))
        pts = c @ np.vstack([v1, v2])
        ax.scatter(pts[:, 0], pts[:, 1], s=2, alpha=0.3)
        ax.set_title(title); ax.set_aspect("equal")
    fig.tight_layout()
    # WHAT DOES THE SECOND ONE MEAN FOR A DATASET WITH TWO SUCH COLUMNS?


# 5 -- BUILD MULTICOLLINEARITY ON PURPOSE.
#      RANK BEFORE: ____   RANK AFTER: ____
#      WHY DOES A DEFICIENT RANK BREAK A REGRESSION?
def ex_05(n=500):
    price_pkr = rng.uniform(100, 5000, n)
    area = rng.uniform(50, 500, n)
    price_usd = price_pkr / 280.0                   # an exact linear dependence

    X_ok = np.column_stack([price_pkr, area])
    X_bad = np.column_stack([price_pkr, area, price_usd])
    print(f"  X_ok  shape {X_ok.shape}   rank {np.linalg.matrix_rank(X_ok)}")
    print(f"  X_bad shape {X_bad.shape}   rank {np.linalg.matrix_rank(X_bad)}  <- 3 columns, rank 2")
    print(f"  corr(price_pkr, price_usd) = {np.corrcoef(price_pkr, price_usd)[0,1]:.6f}")


# 6 -- THE ONE-HOT TRAP.
#      Encode 3 categories into 3 columns. Show the dependency. Then drop one.
#      WHY IS THE THIRD COLUMN REDUNDANT?
#      WHY DOES drop_first=True EXIST?  (you meet it on Day 79)
def ex_06(n=100):
    cats = rng.integers(0, 3, n)
    onehot = np.eye(3)[cats]
    print(f"  3 columns -> rank {np.linalg.matrix_rank(onehot)}")
    print(f"  row sums are always {onehot.sum(axis=1)[:5]}  <- the dependency")
    print(f"  dropping one -> rank {np.linalg.matrix_rank(onehot[:, 1:])} of 2 columns")


# 7 -- DISTANCE with and without scaling.
#      WHICH FEATURE DOMINATES UNSCALED?  WHY?
def ex_07():
    a = np.array([34, 12, 4500, 2])
    b = np.array([52, 11, 4600, 3])
    print(f"  unscaled distance: {np.linalg.norm(a - b):.2f}")
    # now scale each feature to mean 0, sd 1 and recompute
    # WHICH FEATURE WAS THE WHOLE DISTANCE?


# 8 -- COSINE SIMILARITY vs nearest-by-distance.
#      ARE THE MOST SIMILAR PAIR AND THE NEAREST PAIR THE SAME?
def ex_08(): pass


# 9 -- ONE REAL ROW from Project 2, as a vector.
#      DIMENSIONS: ____
#      DOES ITS LENGTH MEAN ANYTHING? WHY OR WHY NOT?
def ex_09(): pass


# MINI ASSESSMENT -- 5 minutes
#   Three columns, the third = col1 + col2.
#     1. rank = ____
#     2. what happens fitting a linear regression on all three?
#     3. which column to drop, and how would I decide?


if __name__ == "__main__":
    print("--- ex_05 multicollinearity ---"); ex_05()
    print("--- ex_06 the one-hot trap ---");  ex_06()
    print("--- ex_07 distance ---");          ex_07()
    ex_04(); plt.show()
