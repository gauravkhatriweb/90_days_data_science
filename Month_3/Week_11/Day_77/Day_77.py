"""
Day 77 — ROC, AUC, and consolidation
=====================================
AUC = the probability that a randomly chosen POSITIVE is scored higher
      than a randomly chosen NEGATIVE.  It measures RANKING, not calibration,
      and it says nothing about which threshold to use.

Exercise 4 is the one to take seriously: on imbalanced data the ROC curve
flatters a model that the precision-recall curve exposes.
"""
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)


def rates(y_true, probs, t):
    pred = (probs >= t).astype(int)
    tp = ((y_true == 1) & (pred == 1)).sum()
    fp = ((y_true == 0) & (pred == 1)).sum()
    fn = ((y_true == 1) & (pred == 0)).sum()
    tn = ((y_true == 0) & (pred == 0)).sum()
    tpr = tp / (tp + fn) if (tp + fn) else 0.0
    fpr = fp / (fp + tn) if (fp + tn) else 0.0
    prec = tp / (tp + fp) if (tp + fp) else 1.0
    return tpr, fpr, prec


# 1 -- BUILD AN ROC CURVE BY HAND. Match sklearn.roc_curve.
def roc_by_hand(y_true, probs, n_points=200):
    ts = np.linspace(1.0, 0.0, n_points)
    pts = [rates(y_true, probs, t)[:2] for t in ts]
    tpr = np.array([p[0] for p in pts]); fpr = np.array([p[1] for p in pts])
    return fpr, tpr


# 2 -- AUC by hand, trapezoidal rule. Match roc_auc_score.
def auc_by_hand(fpr, tpr):
    return np.trapezoid(tpr, fpr) if hasattr(np, "trapezoid") else np.trapz(tpr, fpr)


# =============================================================================
# 3 -- VERIFY THE INTERPRETATION.
#      Sample random positive/negative PAIRS. How often does the positive
#      score higher? IT SHOULD EQUAL THE AUC.
# =============================================================================
def ex_03(y_true, probs, n_pairs=200_000):
    pos = probs[y_true == 1]; neg = probs[y_true == 0]
    a = rng.choice(pos, n_pairs); b = rng.choice(neg, n_pairs)
    empirical = (a > b).mean() + 0.5 * (a == b).mean()
    fpr, tpr = roc_by_hand(y_true, probs)
    print(f"  AUC by area        : {auc_by_hand(fpr, tpr):.4f}")
    print(f"  by sampling pairs  : {empirical:.4f}")
    print("  AUC IS that probability.")


# =============================================================================
# 4 -- THE IMBALANCE DEMONSTRATION. 1% positives.
#      ROC looks good. Precision-recall does not.
#      WHY? -- the FPR denominator is enormous, so hundreds of false alarms
#      barely move it.
# =============================================================================
def ex_04(n=50_000, rate=0.01):
    y = (rng.random(n) < rate).astype(int)
    probs = np.clip(rng.beta(2, 8, n) + y * 0.30, 0, 1)

    fpr, tpr = roc_by_hand(y, probs)
    ts = np.linspace(1.0, 0.0, 200)
    pr = [rates(y, probs, t) for t in ts]
    recall = [p[0] for p in pr]; precision = [p[2] for p in pr]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].plot(fpr, tpr); axes[0].plot([0, 1], [0, 1], "k--", lw=1)
    axes[0].set_title(f"ROC — AUC {auc_by_hand(fpr, tpr):.3f}  (looks good)")
    axes[0].set_xlabel("false positive rate"); axes[0].set_ylabel("recall")
    axes[1].plot(recall, precision)
    axes[1].axhline(rate, ls="--", lw=1)
    axes[1].set_title("Precision-Recall — the same model, honestly")
    axes[1].set_xlabel("recall"); axes[1].set_ylabel("precision")
    fig.tight_layout()
    print(f"  base rate {rate:.1%}. The dashed line is what random achieves.")
    # RULE: balanced -> ROC/AUC.  Imbalanced -> precision-recall.


# 5 -- SAME AUC, DIFFERENT SHAPES. Which would I deploy, and why?
def ex_05(): pass


# =============================================================================
# RETRIEVAL -- closed book, 3 minutes each. 0 / 0.5 / 1
# =============================================================================
# 1 (D71) -- why square residuals? ONE COST of that choice:
R1 = None
# 2 (D72) -- gradient descent in five lines, FROM MEMORY:
R2 = None
# 3 (D72) -- why do gradient methods need scaled features?
R3 = None
# 4 (D73) -- why can R2 only rise when you add features?
R4 = None
# 5 (D74) -- four leakage forms + the test that catches most of them:
R5 = None
# 6 (D74) -- why is scaling before splitting a leak? what crosses the boundary?
R6 = None
# 7 (D75) -- interpret a logistic coefficient of 0.69, CORRECTLY:
R7 = None
# 8 (D76) -- why does accuracy lie on imbalanced data?
R8 = None


# INTEGRATION -- Week 11 in one paragraph:
#   What is a model?
#   How is it fitted?
#   How do I know whether to believe it?


if __name__ == "__main__":
    n = 5000
    y = (rng.random(n) < 0.3).astype(int)
    probs = np.clip(rng.beta(2, 5, n) + y * 0.35, 0, 1)
    print("--- ex_03 what AUC means ---"); ex_03(y, probs)
    print("--- ex_04 the imbalance demonstration ---"); ex_04()
    scores = [R1, R2, R3, R4, R5, R6, R7, R8]
    done = [s for s in scores if s is not None]
    if done:
        print(f"\nRetrieval: {sum(done)} / 8")
    plt.show()
