"""
Day 76 — Why accuracy lies
===========================
PRECISION = TP / (TP + FP) = P(actually positive | predicted positive)

That is Day 46's P(disease | positive test), with new words on it.
A 99%-accurate test for a 0.1% disease gave 9%. Same arithmetic.

THE QUESTION IS NEVER "which metric is better".
IT IS "which mistake costs more" -- and that is a business question.
"""
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)


def confusion(y_true, y_pred):
    """Return (tn, fp, fn, tp) computed by hand."""
    tp = int(((y_true == 1) & (y_pred == 1)).sum())
    tn = int(((y_true == 0) & (y_pred == 0)).sum())
    fp = int(((y_true == 0) & (y_pred == 1)).sum())
    fn = int(((y_true == 1) & (y_pred == 0)).sum())
    return tn, fp, fn, tp


def metrics(y_true, y_pred):
    tn, fp, fn, tp = confusion(y_true, y_pred)
    acc = (tp + tn) / len(y_true)
    prec = tp / (tp + fp) if (tp + fp) else float("nan")
    rec = tp / (tp + fn) if (tp + fn) else float("nan")
    f1 = 2 * prec * rec / (prec + rec) if prec and rec else float("nan")
    spec = tn / (tn + fp) if (tn + fp) else float("nan")
    return dict(accuracy=acc, precision=prec, recall=rec, f1=f1, specificity=spec)


# 1-3 -- build it by hand, match sklearn, LABEL EVERY CELL.
#        sklearn puts ACTUALS on rows and PREDICTIONS on columns.
#        Many textbooks do the opposite. CHECK BEFORE READING ANYONE'S MATRIX.
def ex_01_03(): pass


# =============================================================================
# 4 -- THE 99% MODEL. 1% fraud. Predict "no" for everything.
# =============================================================================
def ex_04(n=10_000, fraud_rate=0.01):
    y = (rng.random(n) < fraud_rate).astype(int)
    always_no = np.zeros(n, dtype=int)
    m = metrics(y, always_no)
    print(f"  fraud rate           : {y.mean():.4f}")
    print(f"  accuracy             : {m['accuracy']:.4f}   <- looks excellent")
    print(f"  recall (caught)      : {m['recall']:.4f}     <- caught NOTHING")
    print(f"  frauds missed        : {y.sum()}")
    print("  never report accuracy on imbalanced data without the class balance beside it.")


# 5 -- three models on all five metrics: a real one, always-negative, random.
#      WHICH METRIC SEPARATES THEM?
def ex_05(): pass


# =============================================================================
# 6 -- THE DAY 46 CONNECTION.
#      precision IS P(actually positive | predicted positive).
#      Show the same arithmetic both ways.
# =============================================================================
def ex_06(n=100_000, base_rate=0.001, sensitivity=0.99, fpr=0.01):
    has = (rng.random(n) < base_rate).astype(int)
    flagged = np.where(has == 1,
                       rng.random(n) < sensitivity,
                       rng.random(n) < fpr).astype(int)
    m = metrics(has, flagged)
    tn, fp, fn, tp = confusion(has, flagged)
    print(f"  TP {tp}   FP {fp}   ->  precision = {tp}/{tp+fp} = {m['precision']:.4f}")
    print(f"  Bayes (Day 46) gave ~0.09 for the same setup.")
    print("  SAME CALCULATION. Different vocabulary.")


# =============================================================================
# 7 -- SWEEP THE THRESHOLD. Plot precision and recall together.
#      WHERE DO THEY CROSS?  WHAT DOES THAT POINT MEAN?
# =============================================================================
def ex_07(y_true=None, probs=None):
    if y_true is None:
        n = 5000
        y_true = (rng.random(n) < 0.08).astype(int)
        probs = np.clip(rng.beta(2, 5, n) + y_true * 0.35, 0, 1)
    ts = np.linspace(0.01, 0.99, 99)
    precs, recs = [], []
    for t in ts:
        m = metrics(y_true, (probs >= t).astype(int))
        precs.append(m["precision"]); recs.append(m["recall"])
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(ts, precs, label="precision"); ax.plot(ts, recs, label="recall")
    ax.set_xlabel("threshold"); ax.legend()
    ax.set_title("They move against each other. 0.5 is a convention, not an answer.")
    fig.tight_layout()
    return y_true, probs


# =============================================================================
# 8 -- THE COST-BASED THRESHOLD.  FP costs 500. FN costs 8,000.
#      total cost = FP*500 + FN*8000. FIND THE MINIMUM.
#      COST-MINIMISING THRESHOLD: ____
#      F1-MAXIMISING THRESHOLD  : ____
#      THEY WILL DIFFER. WHICH WOULD I USE, AND WHY?
# =============================================================================
def ex_08(y_true, probs, fp_cost=500, fn_cost=8000):
    ts = np.linspace(0.01, 0.99, 99)
    costs, f1s = [], []
    for t in ts:
        tn, fp, fn, tp = confusion(y_true, (probs >= t).astype(int))
        costs.append(fp * fp_cost + fn * fn_cost)
        m = metrics(y_true, (probs >= t).astype(int))
        f1s.append(0 if np.isnan(m["f1"]) else m["f1"])
    best_cost = ts[int(np.argmin(costs))]
    best_f1 = ts[int(np.argmax(f1s))]
    print(f"  cost-minimising threshold: {best_cost:.2f}  (cost {min(costs):,.0f})")
    print(f"  F1-maximising threshold  : {best_f1:.2f}")
    print("  the costs, not the metric name, are the answer.")


# 9 -- class_weight=None vs "balanced". WHAT CHANGES, AND WHAT DOES NOT?
def ex_09(): pass


# =============================================================================
# 10 -- APPLY IT TO YOUR OWN PROBLEM.
#       Project 3, or Olist "was this order delivered late?"
#
#       WHAT A FALSE POSITIVE COSTS, IN WORDS:
#       WHAT A FALSE NEGATIVE COSTS, IN WORDS:
#       PUT NUMBERS ON BOTH:        FP = ____    FN = ____
#       THEREFORE MY METRIC IS:     ____
#       AND MY THRESHOLD IS:        ____
#
#       WHEN IS THE CORRECT RESPONSE TO IMBALANCE TO DO NOTHING ABOUT IT?
# =============================================================================


# MINI ASSESSMENT -- 6 minutes
#   200 flagged. 30 genuinely fraudulent. 50 frauds in total. 10,000 transactions.
#     1. the confusion matrix:
#     2. accuracy ____  precision ____  recall ____
#     3. IS THIS MODEL USEFUL? Answer with COSTS, not metrics.


if __name__ == "__main__":
    print("--- ex_04 the 99% model ---");        ex_04()
    print("--- ex_06 precision IS Bayes ---");   ex_06()
    print("--- ex_07 the trade-off ---")
    y, p = ex_07()
    print("--- ex_08 cost-based threshold ---"); ex_08(y, p)
    plt.show()
