"""
Day 75 — Logistic regression
=============================
    p = 1 / (1 + e^-z)     where z = X @ beta

The INSIDE is a linear model (Day 66). The logistic function squashes it
into (0,1). The `e` is Day 18's Euler's number -- it is what makes the
derivative clean, which is what makes gradient descent work here.

NO CLOSED FORM. That is why Day 72 came first.

THE INTERPRETATION TRAP: e^beta = 2 does NOT mean the probability doubles.
"""
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# 1 -- plot the logistic function. Verify the table.
def ex_01():
    z = np.linspace(-8, 8, 400)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(z, sigmoid(z)); ax.axhline(0.5, ls="--", lw=1); ax.axvline(0, ls="--", lw=1)
    ax.set_xlabel("z = X @ beta"); ax.set_ylabel("probability")
    ax.set_title("Any real number in. A probability out.")
    for v in (-5, -1, 0, 1, 5):
        print(f"  z={v:>3}  ->  p={sigmoid(v):.4f}")


# 2 -- coefficient size changes STEEPNESS; intercept changes POSITION.
def ex_02(): pass


# 3 -- WHY NOT LINEAR. Fit a line to binary data.
#      MARK where it predicts above 1 and below 0.
#      THREE REASONS LINEAR REGRESSION FAILS HERE:
#        1.
#        2.
#        3.
def ex_03(n=100): pass


# =============================================================================
# 4 -- LOG LOSS FROM SCRATCH. Show what CONFIDENT WRONGNESS costs.
# =============================================================================
def log_loss(y, p, eps=1e-15):
    p = np.clip(p, eps, 1 - eps)
    return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))

def ex_04():
    print("  truth = 1, and the model predicted:")
    for pred in (0.99, 0.70, 0.50, 0.40, 0.10, 0.01):
        print(f"    p={pred:.2f}  ->  loss {log_loss(np.array([1.0]), np.array([pred])):.4f}")
    print("  confident and wrong is punished far harder than uncertain.")
    # WHY LOG LOSS AND NOT SQUARED ERROR? TWO REASONS:


# =============================================================================
# 5 -- FIT BY GRADIENT DESCENT YOURSELF. Day 72's loop, logistic gradient.
#      gradient = (1/n) * X.T @ (sigmoid(X @ beta) - y)
#      Note how similar it is to the linear case. That is not a coincidence.
# =============================================================================
def logistic_gd(X, y, lr=0.1, iters=5000, verbose=True):
    n = len(y)
    beta = np.zeros(X.shape[1])
    for i in range(iters):
        p = sigmoid(X @ beta)
        gradient = (1 / n) * X.T @ (p - y)
        beta -= lr * gradient
        if verbose and i % 1000 == 0:
            print(f"    iter {i:>5}  log loss {log_loss(y, p):.6f}")
    return beta


# 6 -- compare with sklearn.LogisticRegression. DO THE COEFFICIENTS MATCH?
#      (set penalty=None for a fair comparison -- sklearn regularises by default)
def ex_06(): pass


# 7 -- multivariable fit -> a table of coefficient, odds ratio, and a SENTENCE.
def coefficient_table(names, beta):
    print(f"  {'feature':<24}{'beta':>10}{'odds ratio':>14}")
    for name, b in zip(names, beta):
        print(f"  {name:<24}{b:>10.4f}{np.exp(b):>14.4f}")
    # PLAIN-ENGLISH SENTENCE FOR EACH:


# =============================================================================
# 8 -- THE DOUBLING MISTAKE.
#      e^beta = 2. What happens to the PROBABILITY, starting from 0.1 / 0.5 / 0.9?
#      THREE DIFFERENT ANSWERS.
# =============================================================================
def ex_08():
    print("  odds ratio = 2.0")
    for p0 in (0.1, 0.5, 0.9):
        odds = p0 / (1 - p0) * 2
        p1 = odds / (1 + odds)
        print(f"    from p={p0:.2f}  ->  p={p1:.4f}   (change of {p1-p0:+.4f})")
    # "THE PROBABILITY DOUBLES" IS WRONG IN ALL THREE CASES.
    # WHAT I WOULD SAY INSTEAD:


# 9 -- predicted-probability distribution.
#      Clustered near 0.5, or confident? WHAT DOES EACH PATTERN SUGGEST?
def ex_09(): pass


# 10 -- fit on real data: Project 3 if it is classification,
#       otherwise Olist "was this order delivered late?"
def ex_10(): pass


# =============================================================================
# 11 -- THE THRESHOLD EXPERIMENT. 0.1 to 0.9.
#       Track accuracy AND the two error counts separately.
#       0.5 IS A CONVENTION, NOT AN ANSWER.
#
#       threshold   accuracy   false positives   false negatives
#       ...
#
#       WHICH DID I CHOOSE?
#       WHAT BUSINESS REASONING DECIDED IT?
#       WHAT WOULD HAVE TO CHANGE FOR ME TO MOVE IT?
# =============================================================================
def ex_11(y_true, probs): pass


# MINI ASSESSMENT -- 8 minutes
#   Churn model: age coefficient -0.04, support_tickets coefficient 0.31
#     1. odds ratios: age ____   tickets ____
#     2. a plain-English sentence for each (avoid the doubling mistake):
#     3. which matters more? WHAT DO I NEED TO KNOW BEFORE ANSWERING?


if __name__ == "__main__":
    print("--- ex_01 the logistic function ---"); ex_01()
    print("--- ex_04 log loss ---");              ex_04()
    print("--- ex_08 THE DOUBLING MISTAKE ---");  ex_08()

    n = 500
    x = rng.uniform(-3, 3, n)
    X = np.column_stack([np.ones(n), x])
    y = (rng.random(n) < sigmoid(0.5 + 1.8 * x)).astype(float)
    print("--- ex_05 fitting by gradient descent ---")
    beta = logistic_gd(X, y, lr=0.5, iters=5000)
    print(f"  fitted: {np.round(beta, 4)}   (true was [0.5, 1.8])")
    plt.show()
