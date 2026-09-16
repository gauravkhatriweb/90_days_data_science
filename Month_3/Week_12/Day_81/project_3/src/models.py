"""
Project 3 — models. SIMPLEST FIRST.
====================================
Starting with a random forest and working backwards teaches you nothing
about what the features are doing.

    baseline -> linear/logistic -> single tree -> forest

TRAIN SET ONLY. The test set is touched ONCE, on Day 82.
"""
from __future__ import annotations

import time

import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier, export_text


# -----------------------------------------------------------------------------
# 11-15 -- the candidates, in order of complexity
# -----------------------------------------------------------------------------
def candidates(preprocess):
    """Return {name: pipeline}. Reuse Day 79's preprocessing for all of them."""
    return {
        # "baseline":  Pipeline([("clf", DummyClassifier(strategy="most_frequent"))]),
        # "logistic":  Pipeline([("prep", preprocess), ("clf", LogisticRegression(max_iter=1000))]),
        # "tree_d4":   Pipeline([("prep", preprocess), ("clf", DecisionTreeClassifier(max_depth=4))]),
        # "forest":    Pipeline([("prep", preprocess), ("clf", RandomForestClassifier(n_estimators=300))]),
    }


# -----------------------------------------------------------------------------
# 16 -- THE COMPARISON TABLE
#       mean, SPREAD across folds, fit time, and the GAP TO BASELINE.
#       The spread matters as much as the mean -- Day 74.
# -----------------------------------------------------------------------------
def compare(models: dict, X, y, cv, scoring: str, baseline: float) -> pd.DataFrame:
    rows = []
    for name, model in models.items():
        t0 = time.perf_counter()
        scores = cross_val_score(model, X, y, cv=cv, scoring=scoring)
        rows.append({
            "model": name,
            "mean": scores.mean(),
            "sd": scores.std(ddof=1),
            "min_fold": scores.min(),
            "max_fold": scores.max(),
            "fit_seconds": round(time.perf_counter() - t0, 2),
            "gap_to_baseline": scores.mean() - baseline,
        })
    return pd.DataFrame(rows).sort_values("mean", ascending=False)


# -----------------------------------------------------------------------------
# 14 -- PRINT THE TREE. Are the rules SENSIBLE?
#       This is a DATA check as much as a model check -- nonsense rules
#       mean a feature problem.
# -----------------------------------------------------------------------------
def inspect_tree(pipeline, feature_names):
    """ARE THE RULES SENSIBLE?  ANSWER:"""
    pass


# =============================================================================
# 17-19 -- THE HONESTY CHECK
# =============================================================================
#   BEST MODEL:                        SCORE: ____
#   BASELINE:                          ____
#   GAP:                               ____
#   DAY 80'S STATED THRESHOLD FOR "WORTH DEPLOYING": ____
#   DOES IT CLEAR IT?  ____
#
#   IS ANY SCORE SUSPICIOUSLY GOOD?
#     if the FIRST model gets 0.97, STOP and look for the leak.
#     WHAT I CHECKED:
#
#   WHAT DID NOT WORK (record this -- it goes in the README):
#
#   DID I LOOK AT THE TEST SET TODAY?  yes / no
#     (answer honestly -- if yes, that is worth knowing about yourself)
#
#   IF NO MODEL BEATS THE BASELINE:
#     that is a REAL FINDING, not a failure. "These features do not predict
#     this outcome" written up well is a stronger portfolio piece than a
#     1% improvement presented as a success.
# =============================================================================


if __name__ == "__main__":
    print("Explore train only. Build features. Simplest model first.")
