"""
Day 66 — Matrices as transformations
=====================================
A MATRIX IS A FUNCTION THAT MOVES SPACE.

Its COLUMNS say where the basis vectors land. That is the whole content.
Everything else -- the multiplication rule, determinants, eigenvectors --
follows from it.
"""
import matplotlib.pyplot as plt
import numpy as np

# a grid of points, to watch space move
G = np.mgrid[-3:3.5:0.5, -3:3.5:0.5].reshape(2, -1)

MATRICES = {
    "identity":     np.array([[1, 0], [0, 1]]),
    "scale x2":     np.array([[2, 0], [0, 2]]),
    "stretch x":    np.array([[2, 0], [0, 1]]),
    "rotate 90":    np.array([[0, -1], [1, 0]]),
    "shear":        np.array([[1, 1], [0, 1]]),
    "COLLAPSE":     np.array([[1, 2], [2, 4]]),     # dependent columns
}


# 1 -- apply each matrix to the grid. Plot before and after.
def ex_01():
    fig, axes = plt.subplots(2, 3, figsize=(14, 9))
    for ax, (name, M) in zip(axes.ravel(), MATRICES.items()):
        out = M @ G
        ax.scatter(G[0], G[1], s=4, alpha=0.2, label="before")
        ax.scatter(out[0], out[1], s=4, alpha=0.6, label="after")
        ax.set_title(f"{name}\nrank {np.linalg.matrix_rank(M)}")
        ax.set_aspect("equal"); ax.grid(True)
    fig.tight_layout()


# 2 -- READ THE COLUMNS. Predict where i-hat and j-hat land, BEFORE computing.
#      identity  : i -> ____   j -> ____
#      scale x2  : i -> ____   j -> ____
#      rotate 90 : i -> ____   j -> ____
#      shear     : i -> ____   j -> ____
#      COLLAPSE  : i -> ____   j -> ____
def ex_02():
    i, j = np.array([1, 0]), np.array([0, 1])
    for name, M in MATRICES.items():
        print(f"  {name:<12} i->{M @ i}   j->{M @ j}   (= the columns of M)")


# 3 -- Verify BY HAND: A @ v == v1*col1 + v2*col2
#      WHY IS THIS THE ONLY RULE THAT COULD WORK?
def ex_03():
    A = np.array([[2, 1], [0, 3]])
    v = np.array([3, 2])
    by_rule = A @ v
    by_hand = v[0] * A[:, 0] + v[1] * A[:, 1]
    print(f"  A @ v        = {by_rule}")
    print(f"  3*col1+2*col2 = {by_hand}")


# 4 -- THE COLLAPSE. The plane becomes a line.
#      RANK: ____
#      WHAT DOES A LOWER RANK MEAN FOR INFORMATION?
#      CONNECT: collapses space -> no inverse -> regression fails with collinear features
def ex_04():
    M = MATRICES["COLLAPSE"]
    out = M @ G
    print(f"  rank {np.linalg.matrix_rank(M)}, det {np.linalg.det(M):.6f}")
    print(f"  every output point lies on one line -- information was destroyed")


# 5 -- a rotation matrix for an arbitrary angle, applied to real 2-D data
def ex_05(theta_deg=30): pass


# 6 -- TRIGGER THE SHAPE ERROR on purpose. Read it. Fix it two ways.
def ex_06():
    X = np.ones((100, 5))
    w = np.ones(3)                 # wrong length
    try:
        X @ w
    except ValueError as e:
        print("  expected failure:", e)
    # WHAT ARE THE TWO SHAPES?  ____ and ____
    # FIX A:
    # FIX B:


# 7 -- X @ weights on a real feature matrix.
#      STATE EVERY SHAPE BEFORE RUNNING.
#      X: (____, ____)   weights: (____, ____)   predictions: (____, ____)
def ex_07():
    rng = np.random.default_rng(0)
    X = rng.random((1000, 5))
    weights = rng.random((5, 1))
    print(f"  {X.shape} @ {weights.shape} -> {(X @ weights).shape}")
    # EVERY LINEAR MODEL IS THIS LINE.


# 8 -- COMPOSITION. Apply A then B, vs applying (B @ A) at once.
#      SAME RESULT? WHY?
#      Then: does A @ B == B @ A?  GIVE A GEOMETRIC REASON.
def ex_08():
    A = MATRICES["rotate 90"]
    B = MATRICES["stretch x"]
    v = np.array([3, 2])
    print(f"  B @ (A @ v) = {B @ (A @ v)}")
    print(f"  (B @ A) @ v = {(B @ A) @ v}")
    print(f"  A @ B == B @ A?  {np.allclose(A @ B, B @ A)}")
    # GEOMETRIC REASON:


# MINI ASSESSMENT -- 5 minutes, NO COMPUTATION
#   A = [[3, 0], [0, 0.5]]
#     1. i -> ____   j -> ____
#     2. what it does to the plane, in words:
#     3. does it have an inverse? how do I know?
#     4. what happens to the area of a unit square? ____


if __name__ == "__main__":
    print("--- ex_02 read the columns ---"); ex_02()
    print("--- ex_03 the rule ---");         ex_03()
    print("--- ex_04 the collapse ---");     ex_04()
    print("--- ex_06 shape error ---");      ex_06()
    print("--- ex_07 a linear model ---");   ex_07()
    print("--- ex_08 composition ---");      ex_08()
    ex_01(); plt.show()
