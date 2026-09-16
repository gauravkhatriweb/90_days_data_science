"""
Day 79 — Feature engineering and leak-proof pipelines
======================================================
FEATURES MATTER MORE THAN MODEL CHOICE.

And this is where leakage most often enters, because every transformation
LEARNS something. Pipeline makes leakage structurally impossible rather
than something you have to remember not to do at 11pm.

THE MOST PRODUCTIVE QUESTION:
    what would a human who knows this business look at?
"""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

rng = np.random.default_rng(42)


# =============================================================================
# 1 -- FIVE FEATURES A HUMAN WOULD LOOK AT. Write these BEFORE coding.
# =============================================================================
#   Target:
#
#   1. FEATURE:                  WHAT IT CAPTURES:              COULD IT LEAK?
#   2. FEATURE:                  WHAT IT CAPTURES:              COULD IT LEAK?
#   3. FEATURE:                  WHAT IT CAPTURES:              COULD IT LEAK?
#   4. FEATURE:                  WHAT IT CAPTURES:              COULD IT LEAK?
#   5. FEATURE:                  WHAT IT CAPTURES:              COULD IT LEAK?
#
#   WHICH DO I PREDICT WILL BE MOST USEFUL?


# 2 -- ratios and differences. Build three.
def ex_02(df): pass


# 3 -- time features: day of week, month, is_weekend, days_since
def ex_03(df): pass


# =============================================================================
# 4 -- AN AGGREGATE FEATURE, DONE SAFELY.
#      seller_avg_delay is a strong feature -- AND computing it on the whole
#      dataset LEAKS, because the average includes the rows you are predicting.
#
#      SAFE OPTION A: compute inside the training fold only (custom transformer)
#      SAFE OPTION B: compute from a STRICTLY EARLIER time window
#
#      WHICH DID I USE, AND WHY?
#      WHAT WOULD THE UNSAFE VERSION HAVE DONE TO MY SCORE?
# =============================================================================
def safe_seller_average(df, date_col, group_col, value_col):
    """Expanding mean over earlier rows only -- never the current row."""
    pass


# 5 -- one-hot with and without drop="first". CHECK THE RANK BOTH WAYS.
#      rank without drop: ____   with drop: ____
#      WHY drop="first" FOR LINEAR MODELS BUT NOT FOR TREES?  (Day 65)
def ex_05(): pass


# 6 -- StandardScaler IS the z-score from Day 50.
#      Verify that the fitted mean and scale come from TRAINING ONLY.
def ex_06():
    X = rng.normal(50, 12, (100, 1))
    Xtr, Xte = train_test_split(X, test_size=0.3, random_state=0)
    sc = StandardScaler().fit(Xtr)
    print(f"  scaler mean  {sc.mean_[0]:.4f}   train mean {Xtr.mean():.4f}")
    print(f"  scaler scale {sc.scale_[0]:.4f}   train sd   {Xtr.std():.4f}")
    print(f"  test mean is {Xte.mean():.4f} and the scaler NEVER SAW IT")


# =============================================================================
# 7 -- THE FULL PIPELINE. Leak-proof by construction.
# =============================================================================
def build_pipeline(numeric_cols, categorical_cols, model=None):
    numeric = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scale", StandardScaler()),
    ])
    categorical = Pipeline([
        ("impute", SimpleImputer(strategy="most_frequent")),
        ("encode", OneHotEncoder(handle_unknown="ignore")),   # new categories WILL appear
    ])
    preprocess = ColumnTransformer([
        ("num", numeric, numeric_cols),
        ("cat", categorical, categorical_cols),
    ])
    return Pipeline([("prep", preprocess),
                     ("clf", model or LogisticRegression(max_iter=1000))])
# cross_val_score REFITS THE WHOLE PIPELINE ON EACH TRAINING FOLD.
# The imputer's median, the scaler's mean, the encoder's categories --
# all learned from that fold's TRAINING ROWS ONLY.


# =============================================================================
# 8 -- THE PROOF. Scale OUTSIDE the pipeline vs INSIDE.
#      inflated by: ____
#      This is Day 74 exercise 7, now with a tool that prevents it.
# =============================================================================
def ex_08(): pass


# 9 -- all features vs FIVE well-chosen ones.
#      all: ____   chosen five: ____
#      IS THE DIFFERENCE WORTH THE COMPLEXITY? WHAT WOULD I SHIP?
def ex_09(): pass


# =============================================================================
# 10 -- PROJECT 3'S REAL PIPELINE. Build the one you will use tomorrow.
# =============================================================================
#   numeric columns    :
#   categorical columns:
#   model              :
#   split strategy     :          (from Day 74's audit)
#   cross-validation   :
#   metric             :          (from Day 76's cost reasoning)
#
#   LEAKAGE AUDIT APPLIED?  ☐
#   ANYTHING STILL UNDECIDED?


# MINI ASSESSMENT -- 6 minutes
#   Predict: will this customer buy again within 90 days? (from an orders table)
#     feature 1:            captures:            could it leak?
#     feature 2:            captures:            could it leak?
#     feature 3:            captures:            could it leak?
#     feature 4:            captures:            could it leak?
#     feature 5:            captures:            could it leak?


if __name__ == "__main__":
    print("--- ex_06 the scaler never sees the test set ---"); ex_06()
