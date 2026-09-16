"""
Day 78 — Trees and forests
===========================
A tree is a sequence of IF-STATEMENTS, learned rather than written.
That is its advantage: a shallow tree can be PRINTED and handed to a person.

A single tree overfits badly. A forest averages many decorrelated trees
and the variance falls -- Day 74's trade-off, exploited deliberately.

Exercise 9 is the one to remember: feature importance can rank PURE NOISE
as important.
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

rng = np.random.default_rng(42)


def make_data(n=2000):
    x1 = rng.uniform(0, 10, n)
    x2 = rng.uniform(0, 10, n)
    y = ((x1 * x2 > 25) ^ (rng.random(n) < 0.08)).astype(int)   # non-linear + noise
    return np.column_stack([x1, x2]), y


# 1 -- depth-2 tree. PRINT IT AS TEXT AND READ THE RULES ALOUD.
def ex_01():
    X, y = make_data()
    t = DecisionTreeClassifier(max_depth=2, random_state=0).fit(X, y)
    print(export_text(t, feature_names=["x1", "x2"]))
    # COULD I HAND THESE RULES TO A SHOPKEEPER? THAT IS THE ADVANTAGE.


# =============================================================================
# 2 -- WATCH IT OVERFIT. Depths 1..20. Train and test accuracy.
#      THEY DIVERGE AT DEPTH ____
# =============================================================================
def ex_02():
    X, y = make_data()
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
    depths = range(1, 21)
    tr = [DecisionTreeClassifier(max_depth=d, random_state=0).fit(Xtr, ytr).score(Xtr, ytr) for d in depths]
    te = [DecisionTreeClassifier(max_depth=d, random_state=0).fit(Xtr, ytr).score(Xte, yte) for d in depths]
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(depths, tr, "o-", label="train"); ax.plot(depths, te, "s-", label="test")
    ax.set_xlabel("max_depth"); ax.set_ylabel("accuracy"); ax.legend()
    ax.set_title("Train keeps climbing. Test turns over. That turn is overfitting.")
    fig.tight_layout()
    print(f"  best test accuracy at depth {list(depths)[int(np.argmax(te))]}")


# 3 -- unlimited depth: train 1.0, test much lower
def ex_03():
    X, y = make_data()
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
    t = DecisionTreeClassifier(random_state=0).fit(Xtr, ytr)
    print(f"  train {t.score(Xtr, ytr):.4f}   test {t.score(Xte, yte):.4f}   <- memorised")


# 4 -- control it: max_depth / min_samples_leaf / min_samples_split.
#      WHICH HELPED MOST? ____
def ex_04(): pass


# 5 -- forest vs single tree. COMPARE THE TRAIN-TEST GAP.
def ex_05():
    X, y = make_data()
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
    for name, m in [("single tree", DecisionTreeClassifier(random_state=0)),
                    ("forest",      RandomForestClassifier(n_estimators=200, random_state=0))]:
        m.fit(Xtr, ytr)
        gap = m.score(Xtr, ytr) - m.score(Xte, yte)
        print(f"  {name:<12} train {m.score(Xtr,ytr):.4f}  test {m.score(Xte,yte):.4f}  gap {gap:.4f}")
    # WHY DOES AVERAGING DECORRELATED TREES REDUCE VARIANCE?


# 6 -- n_estimators 1..500. WHERE DOES TEST PERFORMANCE FLATTEN? ____
def ex_06(): pass


# 7 -- built-in .feature_importances_
def ex_07(): pass


# 8 -- PERMUTATION IMPORTANCE. Compare with the built-in.
#      WHERE DO THEY DISAGREE? WHICH DO I BELIEVE, AND WHY?
def ex_08(): pass


# =============================================================================
# 9 -- THE CARDINALITY BIAS.
#      Add a PURE NOISE column with MANY UNIQUE VALUES.
#      WATCH IT RANK AS IMPORTANT.
#      built-in importance of the noise column: ____
#      permutation importance of the same column: ____
#      WHAT DOES THIS TEACH ME ABOUT READING AN IMPORTANCE PLOT?
# =============================================================================
def ex_09(n=2000):
    X, y = make_data(n)
    noise = rng.random(n)                       # pure noise, all unique values
    X_plus = np.column_stack([X, noise])
    Xtr, Xte, ytr, yte = train_test_split(X_plus, y, test_size=0.3, random_state=0)
    rf = RandomForestClassifier(n_estimators=300, random_state=0).fit(Xtr, ytr)

    print("  built-in importances:")
    for name, imp in zip(["x1", "x2", "PURE NOISE"], rf.feature_importances_):
        print(f"    {name:<12} {imp:.4f}")

    perm = permutation_importance(rf, Xte, yte, n_repeats=10, random_state=0)
    print("  permutation importances (on the TEST set):")
    for name, imp in zip(["x1", "x2", "PURE NOISE"], perm.importances_mean):
        print(f"    {name:<12} {imp:.4f}")


# MINI ASSESSMENT -- 5 minutes
#   Forest: 0.89 test accuracy. Logistic regression: 0.86.
#   The business must explain every decision to customers.
#   WHICH DO I SHIP?
#   WHAT DO I SAY ABOUT THE 3%?


if __name__ == "__main__":
    print("--- ex_01 read the rules ---"); ex_01()
    print("--- ex_03 memorisation ---");   ex_03()
    print("--- ex_05 forest vs tree ---"); ex_05()
    print("--- ex_09 THE CARDINALITY BIAS ---"); ex_09()
    ex_02(); plt.show()
