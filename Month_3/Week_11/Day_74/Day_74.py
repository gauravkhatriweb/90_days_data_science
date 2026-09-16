"""
Day 74 — Validation: the day that separates real from tutorial
===============================================================
LEAKAGE is any information in training that would not exist at prediction time.

You are going to BUILD four leaks deliberately, get beautiful scores, and
then find them. That experience is the point -- afterwards you will
recognise the FEELING of a score that is too good.

THE RULE: treat an unexpectedly good score as a BUG REPORT.
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import (KFold, TimeSeriesSplit, cross_val_score,
                                     train_test_split)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

rng = np.random.default_rng(42)


def make_data(n=500):
    x1 = rng.uniform(0, 50, n)
    x2 = rng.uniform(0, 10, n)
    y = 10 + 2.5 * x1 - 1.2 * x2 + rng.normal(0, 8, n)
    return np.column_stack([x1, x2]), y


# 1 -- split, fit, compare train and test. MEASURE THE GAP.
#      train R2: ____   test R2: ____   gap: ____
def ex_01():
    X, y = make_data()
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    m = LinearRegression().fit(Xtr, ytr)
    print(f"  train R2 {m.score(Xtr, ytr):.4f}   test R2 {m.score(Xte, yte):.4f}")


# =============================================================================
# 2 -- HOW MUCH DOES THE "TEST SCORE" MOVE BY LUCK ALONE?
#      20 different random_states. Plot the spread.
#      min: ____   max: ____   spread: ____
#      WHAT DOES THAT MEAN FOR REPORTING A SINGLE NUMBER?
# =============================================================================
def ex_02(n_splits=20):
    X, y = make_data(n=150)                 # small n -> more variation
    scores = []
    for seed in range(n_splits):
        Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=seed)
        scores.append(LinearRegression().fit(Xtr, ytr).score(Xte, yte))
    scores = np.array(scores)
    print(f"  min {scores.min():.4f}   max {scores.max():.4f}   spread {scores.ptp():.4f}")
    print(f"  mean {scores.mean():.4f}  sd {scores.std(ddof=1):.4f}")
    print("  the 'test score' is itself a random variable.")


# 3 -- 5-fold cross-validation. Compare the MEAN with a single split.
#      LOOK AT THE SPREAD, not just the mean.
def ex_03():
    X, y = make_data(n=150)
    s = cross_val_score(LinearRegression(), X, y, cv=5)
    print(f"  fold scores: {np.round(s, 4)}")
    print(f"  mean {s.mean():.4f}  sd {s.std(ddof=1):.4f}")
    # ANY FOLD THAT WENT BADLY? THAT IS WORTH INVESTIGATING.


# =============================================================================
# 4 -- OVERFITTING. Polynomial degrees 1..15. Plot train AND test error.
#      THEY DIVERGE AT DEGREE ____
#      WHAT IS HAPPENING THERE?
# =============================================================================
def ex_04(max_degree=15):
    n = 60
    x = rng.uniform(-3, 3, n)
    y = x**2 + rng.normal(0, 2, n)
    X = x.reshape(-1, 1)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)

    tr, te = [], []
    for d in range(1, max_degree + 1):
        m = Pipeline([("poly", PolynomialFeatures(d)), ("lr", LinearRegression())])
        m.fit(Xtr, ytr)
        tr.append(1 - m.score(Xtr, ytr))
        te.append(1 - m.score(Xte, yte))

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(range(1, max_degree + 1), tr, "o-", label="train error")
    ax.plot(range(1, max_degree + 1), te, "s-", label="test error")
    ax.set_yscale("log"); ax.set_xlabel("polynomial degree"); ax.set_ylabel("error (log)")
    ax.set_title("Train error always falls. Test error turns around. That turn is overfitting.")
    ax.legend(); fig.tight_layout()


# 5 -- LEARNING CURVES: performance vs training-set SIZE, simple vs complex.
#      WHICH MODEL WOULD MORE DATA HELP?  HOW CAN I TELL FROM THE CURVES?
#      (this decides between COLLECTING MORE DATA and CHANGING THE MODEL --
#       a real, expensive decision)
def ex_05(): pass


# =============================================================================
# LEAKAGE -- build each one, get a beautiful score, then find it
# =============================================================================

# 6 -- TARGET LEAKAGE. Add a feature derived from the target. R2 > 0.99.
#      R2 WITH THE LEAK: ____   WITHOUT: ____
#      WOULD I HAVE NOTICED WITHOUT LOOKING?
def ex_06(n=500):
    X, y = make_data(n)
    leak = y + rng.normal(0, 0.5, n)                 # derived from the target
    X_leaky = np.column_stack([X, leak])
    Xtr, Xte, ytr, yte = train_test_split(X_leaky, y, test_size=0.2, random_state=0)
    print(f"  WITH leak   : test R2 = {LinearRegression().fit(Xtr, ytr).score(Xte, yte):.6f}")
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)
    print(f"  without leak: test R2 = {LinearRegression().fit(Xtr, ytr).score(Xte, yte):.6f}")


# 7 -- PREPROCESSING LEAKAGE. Scale BEFORE splitting vs inside a Pipeline.
#      It feels harmless. EXPLAIN EXACTLY WHAT CROSSES THE BOUNDARY:
#      inflated by: ____
def ex_07(n=80):
    X, y = make_data(n)
    # WRONG: scaler sees the test rows
    Xs = StandardScaler().fit_transform(X)
    Xtr, Xte, ytr, yte = train_test_split(Xs, y, test_size=0.3, random_state=0)
    wrong = LinearRegression().fit(Xtr, ytr).score(Xte, yte)

    # RIGHT: the scaler is fitted inside each training fold only
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
    right = Pipeline([("sc", StandardScaler()), ("lr", LinearRegression())]) \
        .fit(Xtr, ytr).score(Xte, yte)
    print(f"  scaled before split (WRONG): {wrong:.6f}")
    print(f"  scaled inside pipeline     : {right:.6f}")


# 8 -- TEMPORAL LEAKAGE. Random split on TIME-ORDERED data vs TimeSeriesSplit.
#      HOW MUCH BETTER DID THE WRONG ONE LOOK? ____
#      WHAT WOULD HAVE HAPPENED IN PRODUCTION?
def ex_08(n=400):
    t = np.arange(n)
    trend = 0.05 * t
    y = trend + np.sin(t / 20) * 3 + rng.normal(0, 1, n)
    X = np.column_stack([t, np.sin(t / 20)])

    random_score = cross_val_score(LinearRegression(), X, y, cv=KFold(5, shuffle=True, random_state=0)).mean()
    time_score = cross_val_score(LinearRegression(), X, y, cv=TimeSeriesSplit(5)).mean()
    print(f"  random KFold (WRONG)  : {random_score:.4f}   <- trained on the future")
    print(f"  TimeSeriesSplit       : {time_score:.4f}")


# 9 -- GROUP LEAKAGE. Duplicate entities across the split. Watch it inflate.
def ex_09(): pass


# =============================================================================
# DOING IT RIGHT
# =============================================================================

# 10 -- the correct sequence: split -> Pipeline -> cross-validate -> test ONCE
def ex_10(): pass

# 11 -- TimeSeriesSplit on your Project 2 data
def ex_11(): pass

# =============================================================================
# 12 -- AUDIT PROJECT 3.
# =============================================================================
#   THE AVAILABILITY TEST on every planned feature:
#     feature                    known at prediction time?   verdict
#     ______                     ____                        safe / LEAK
#
#   MY SPLIT STRATEGY:            (random / stratified / time / group -- and WHY)
#
#   WHICH OF THE SEVEN LEAKAGE FORMS AM I MOST AT RISK OF?
#   MY DEFENCE:
#
#   Write this NOW, not on Day 81.


# MINI ASSESSMENT -- 10 minutes
#   Someone hands you a model with test R2 = 0.96 predicting next-month spend.
#   THE SEVEN CHECKS, IN ORDER, AND WHAT EACH WOULD CATCH:
#     1.                                    5.
#     2.                                    6.
#     3.                                    7.
#     4.


if __name__ == "__main__":
    print("--- ex_01 ---");                    ex_01()
    print("--- ex_02 the test score varies ---"); ex_02()
    print("--- ex_03 cross validation ---");    ex_03()
    print("--- ex_06 TARGET LEAKAGE ---");      ex_06()
    print("--- ex_07 PREPROCESSING LEAKAGE ---"); ex_07()
    print("--- ex_08 TEMPORAL LEAKAGE ---");    ex_08()
    ex_04(); plt.show()
