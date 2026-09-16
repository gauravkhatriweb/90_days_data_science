"""
Day 72 — Gradient descent
==========================
    compute the slope -> step downhill -> repeat

That is the whole algorithm. The slope is a DERIVATIVE -- Day 19.
The gradient is a set of PARTIAL derivatives, one per parameter -- also Day 19.
The update is a MATRIX MULTIPLICATION -- Day 66.

Every idea in this plan converges on the five lines in ex_01.
WRITE IT YOURSELF before importing anything.
"""
import time

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)


def make_data(n=200, slope=2.5, intercept=10, noise=8):
    x = rng.uniform(0, 50, n)
    y = intercept + slope * x + rng.normal(0, noise, n)
    return np.column_stack([np.ones(n), x]), y


# =============================================================================
# 1 -- GRADIENT DESCENT FROM SCRATCH. Five lines.
# =============================================================================
def gradient_descent(X, y, lr=0.0001, iters=5000, verbose=True):
    n = len(y)
    beta = np.zeros(X.shape[1])
    history = []
    for i in range(iters):
        predictions = X @ beta
        error = predictions - y
        cost = (error ** 2).mean()
        gradient = (2 / n) * X.T @ error          # dMSE/dbeta
        beta -= lr * gradient
        history.append(cost)
        if verbose and i % 1000 == 0:
            print(f"    iter {i:>6}  cost {cost:12.4f}  beta {np.round(beta, 4)}")
    return beta, history


# 2 -- COMPARE WITH THE CLOSED FORM.
#      SAME ANSWER TO ____ DECIMAL PLACES
#      ITERATIONS NEEDED: ____
def ex_02():
    X, y = make_data()
    closed = np.linalg.solve(X.T @ X, X.T @ y)
    descended, _ = gradient_descent(X, y, lr=0.0005, iters=20000, verbose=False)
    print(f"  closed form      : {np.round(closed, 6)}")
    print(f"  gradient descent : {np.round(descended, 6)}")


# 3 -- THE LEARNING-RATE EXPERIMENT. Plot all five cost curves.
#      WHICH DIVERGED? ____
#      WHAT DID ITS CURVE DO?
def ex_03():
    X, y = make_data()
    fig, ax = plt.subplots(figsize=(10, 5))
    for lr in (0.00001, 0.0001, 0.0005, 0.001, 0.002):
        try:
            _, hist = gradient_descent(X, y, lr=lr, iters=400, verbose=False)
            ax.plot(hist, label=f"lr={lr}")
        except (OverflowError, FloatingPointError):
            print(f"  lr={lr} exploded")
    ax.set_yscale("log"); ax.set_xlabel("iteration"); ax.set_ylabel("cost (log)")
    ax.set_title("Too small: slow. Too large: oscillates, then diverges.")
    ax.legend(); fig.tight_layout()


# 4 -- PLOT THE PATH across the error surface (contour plot).
def ex_04(): pass


# 5 -- FEATURE SCALING. Unscaled vs scaled. Compare ITERATION COUNTS.
#      unscaled: ____ iterations   scaled: ____ iterations
#      EXPLAIN IT WITH THE SHAPE OF THE ERROR SURFACE:
#      (this is the real reason StandardScaler exists -- Day 79)
def ex_05(n=500):
    spend = rng.uniform(1000, 50000, n)          # thousands
    age = rng.uniform(18, 70, n)                 # tens
    y = 5 + 0.002 * spend + 1.5 * age + rng.normal(0, 3, n)

    X_raw = np.column_stack([np.ones(n), spend, age])
    Xs = np.column_stack([np.ones(n),
                          (spend - spend.mean()) / spend.std(),
                          (age - age.mean()) / age.std()])
    print(f"  cond(X) unscaled = {np.linalg.cond(X_raw):.1f}")
    print(f"  cond(X) scaled   = {np.linalg.cond(Xs):.1f}")
    # run gradient descent on both and count iterations to the same tolerance


# 6 -- STOCHASTIC gradient descent. One row per step. Compare the cost curve.
#      WHAT DOES THE NOISE LOOK LIKE?  WHY IS IT USEFUL?
def sgd(X, y, lr=0.0005, epochs=50):
    pass


# 7 -- MINI-BATCH at sizes 1, 32, 256, all. Compare time and smoothness.
def ex_07(): pass


# =============================================================================
# 8 -- THE CHAIN RULE CONNECTION.  This is why Day 25 mattered.
# =============================================================================
#
#   error depends on the PREDICTION:      E = (pred - y)^2
#   prediction depends on BETA:           pred = X @ beta
#
#   So, by the chain rule:
#
#       dE/dbeta  =  dE/dpred  x  dpred/dbeta
#                 =  2(pred - y)  x  X
#                 =  2 X^T (X beta - y)
#
#   WRITE THAT OUT IN YOUR OWN WORDS:
#
#
#   THIS IS BACKPROPAGATION IN MINIATURE. In a neural network the chain is
#   longer -- one link per layer -- but it is the SAME RULE.
#
#   WHY DOES THIS MATTER BEYOND LINEAR REGRESSION?
# =============================================================================


# MINI ASSESSMENT -- 8 minutes, closed book.
# Gradient descent for y = mx + c. TWO parameters, a loop, NO matrix shortcuts.
# Does it converge to the same answer as np.polyfit?
def mini(x, y, lr=0.0001, iters=10000):
    m, c = 0.0, 0.0
    # your loop here
    return m, c


if __name__ == "__main__":
    X, y = make_data()
    print("--- ex_01 from scratch ---")
    gradient_descent(X, y, lr=0.0005, iters=5000)
    print("--- ex_02 vs closed form ---"); ex_02()
    print("--- ex_05 scaling ---");         ex_05()
    ex_03(); plt.show()
