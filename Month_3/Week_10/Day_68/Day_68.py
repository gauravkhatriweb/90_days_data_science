"""
Day 68 — Eigenvectors, and why PCA works
=========================================
AN EIGENVECTOR IS A DIRECTION THE TRANSFORMATION DOES NOT TURN.

The eigenvectors of the COVARIANCE MATRIX are the directions your data
varies most along. That is all PCA is.

Exercise 1 first: find them BY EYE before computing them.
"""
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)

A        = np.array([[3, 1], [0, 2]])
ROT90    = np.array([[0, -1], [1, 0]])
SCALE    = np.array([[2, 0], [0, 2]])
SHEAR    = np.array([[1, 1], [0, 1]])
COLLAPSE = np.array([[1, 2], [2, 4]])


# 1 -- THE VISUAL. Apply A to many unit vectors. Which ones did NOT rotate?
#      MY GUESS (by eye): ____ and ____
def ex_01():
    angles = np.linspace(0, 2 * np.pi, 60, endpoint=False)
    unit = np.vstack([np.cos(angles), np.sin(angles)])
    out = A @ unit

    fig, ax = plt.subplots(figsize=(7, 7))
    for i in range(unit.shape[1]):
        ax.plot([0, unit[0, i]], [0, unit[1, i]], lw=0.4, alpha=0.4)
        ax.plot([0, out[0, i]], [0, out[1, i]], lw=0.8, alpha=0.6)
    vals, vecs = np.linalg.eig(A)
    for i in range(len(vals)):
        v = vecs[:, i] * 3
        ax.plot([-v[0], v[0]], [-v[1], v[1]], "k--", lw=2)
    ax.set_aspect("equal"); ax.grid(True)
    ax.set_title("Dashed lines: the directions that do NOT rotate")
    print(f"  eigenvalues : {np.round(vals, 4)}")
    print(f"  eigenvectors:\n{np.round(vecs, 4)}")


# 2 -- verify A @ v == lambda * v for each eigenvector
def ex_02():
    vals, vecs = np.linalg.eig(A)
    for i in range(len(vals)):
        v = vecs[:, i]
        print(f"  A@v = {np.round(A @ v, 4)}   lambda*v = {np.round(vals[i] * v, 4)}")


# 3 -- interesting structures.
#      rotation: WHY NO REAL EIGENVECTORS?
#      scale   : WHY IS EVERY VECTOR AN EIGENVECTOR?
#      shear   : WHY ONLY ONE?
def ex_03():
    for name, M in [("rotate 90", ROT90), ("scale", SCALE), ("shear", SHEAR)]:
        vals, _ = np.linalg.eig(M)
        print(f"  {name:<10} eigenvalues = {np.round(vals, 4)}")


# 4 -- THE COLLAPSE. One eigenvalue is zero.
#      CONNECT IT TO det = 0 AND TO YESTERDAY'S FOUR STATEMENTS:
def ex_04():
    vals, _ = np.linalg.eig(COLLAPSE)
    print(f"  eigenvalues: {np.round(vals, 6)}")
    print(f"  product    : {np.prod(vals):.6f}")
    print(f"  det        : {np.linalg.det(COLLAPSE):.6f}   <- the SAME number")


# =============================================================================
# BUILDING PCA
# =============================================================================

# 5 -- correlated 2-D data. GUESS the direction of greatest variance BY EYE.
#      MY GUESS: roughly ____ degrees
def make_data(n=500):
    x = rng.normal(0, 1, n)
    y = 0.8 * x + rng.normal(0, 0.4, n)
    return np.column_stack([x, y])


# 6 -- covariance matrix -> eigenvectors -> PLOT THEM ON THE DATA.
#      DID MY GUESS MATCH?
def ex_06():
    data = make_data()
    centred = data - data.mean(axis=0)
    cov = np.cov(centred.T)
    vals, vecs = np.linalg.eig(cov)
    order = np.argsort(vals)[::-1]
    vals, vecs = vals[order], vecs[:, order]

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(centred[:, 0], centred[:, 1], s=6, alpha=0.4)
    for i in range(2):
        v = vecs[:, i] * np.sqrt(vals[i]) * 3
        ax.plot([0, v[0]], [0, v[1]], lw=3, label=f"PC{i+1} ({vals[i]/vals.sum():.0%})")
    ax.set_aspect("equal"); ax.legend(); ax.grid(True)
    ax.set_title("The eigenvectors of the covariance matrix ARE the principal components")
    print(f"  explained variance: {np.round(vals / vals.sum(), 4)}")


# 7 -- project onto PC1. How much variance is retained?  ____%
def ex_07(): pass


# 8 -- compare with sklearn.decomposition.PCA.
#      SAME DIRECTIONS?  (signs may flip -- WHY IS THAT FINE?)
def ex_08(): pass


# =============================================================================
# THE CAUTIONS
# =============================================================================

# 9 -- PCA WITHOUT SCALING. One feature in thousands, one in tens.
#      WATCH PC1 BECOME "THE BIG FEATURE".
#      PC1 loadings unscaled: ____
#      PC1 loadings scaled  : ____
#      WHY IS THIS THE MOST COMMON PCA MISTAKE?
def ex_09(n=500):
    spend = rng.normal(5000, 1500, n)
    age = rng.normal(35, 8, n)
    X = np.column_stack([spend, age])
    cov = np.cov((X - X.mean(0)).T)
    vals, vecs = np.linalg.eig(cov)
    print(f"  UNSCALED PC1 loadings: {np.round(vecs[:, np.argmax(vals)], 4)}")
    Xs = (X - X.mean(0)) / X.std(0)
    covs = np.cov(Xs.T)
    v2, ve2 = np.linalg.eig(covs)
    print(f"  SCALED   PC1 loadings: {np.round(ve2[:, np.argmax(v2)], 4)}")


# 10 -- PCA on YOUR Project 2 feature matrix.
#       explained variance ratio plot
#       COMPONENTS FOR 90% VARIANCE: ____
#       WOULD I ACTUALLY USE IT HERE? ARGUE BOTH SIDES, THEN DECIDE:
#         FOR:
#         AGAINST:
#         DECISION:
def ex_10(): pass


# MINI ASSESSMENT -- 8 minutes
#   Explain PCA to someone who knows what a scatter plot is and nothing else.
#   No matrices. No eigenvectors. Just the picture and the trade-off.
#
#   MY EXPLANATION:
#
#   WHEN I WOULD NOT USE IT:


if __name__ == "__main__":
    print("--- ex_01 find them by eye first ---"); ex_01()
    print("--- ex_02 verify ---");                 ex_02()
    print("--- ex_03 special cases ---");          ex_03()
    print("--- ex_04 the collapse ---");           ex_04()
    print("--- ex_06 PCA from scratch ---");       ex_06()
    print("--- ex_09 the scaling mistake ---");    ex_09()
    plt.show()
