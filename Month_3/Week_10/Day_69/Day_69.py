"""
Day 69 — What machine learning actually is
===========================================
"Finding a function that maps inputs to outputs, by searching for the
 parameters that minimise error on examples."

  function        -> f(x) = y            (Ch.1, Day 10)
  inputs          -> a feature matrix X  (Day 65)
  parameters      -> a weight vector B   (Day 65)
  maps            -> X @ B               (Day 66)
  minimise error  -> follow the derivative downhill (Days 25, 72)
  on EXAMPLES     -> a SAMPLE, so every score is a SAMPLE STATISTIC (Day 48)

That last line is why statistics came before ML in this plan.
"""
import numpy as np
import pandas as pd


# =============================================================================
# 1 -- REWRITE THE DEFINITION in terms of Days 65-68. No borrowed jargon.
# =============================================================================
#   MY DEFINITION:
#
#


# =============================================================================
# 2 -- CLASSIFY TEN PROBLEMS.
#      supervised-regression / supervised-classification / unsupervised / NOT ML
#      At least THREE should be "NOT ML".
# =============================================================================
PROBLEMS = [
    "Predict next month's revenue for a kiryana shop",
    "Group customers into segments nobody has defined yet",
    "Decide whether an order is fraudulent",
    "Report how many orders were late last quarter",
    "Predict how many days until a customer's next purchase",
    "Flag transactions over PKR 50,000 for manual review",
    "Recommend which products to stock next month",
    "Work out which supplier has the highest defect rate",
    "Predict whether a shop will still be using SwiftBase in six months",
    "Decide what counts as an 'active' customer",
]
#   1.                               6.
#   2.                               7.
#   3.                               8.
#   4.                               9.
#   5.                              10.
#
#   WHICH WAS HARDEST TO CLASSIFY, AND WHY?


# =============================================================================
# 3 -- BUILD THE BASELINES. Any model must beat these.
# =============================================================================
def baselines(y_regression=None, y_classification=None):
    """Regression: always predict the mean. Classification: always the majority."""
    if y_regression is not None:
        rmse = np.sqrt(((y_regression - y_regression.mean()) ** 2).mean())
        print(f"  regression baseline (predict the mean) RMSE = {rmse:.4f}")
    if y_classification is not None:
        majority = pd.Series(y_classification).value_counts(normalize=True).iloc[0]
        print(f"  classification baseline (majority class) accuracy = {majority:.4f}")
        print("  <- if this is 0.94, then '94% accurate' means LEARNED NOTHING")


# =============================================================================
# 4 -- FIND THE LEAKAGE.
#      Target: will this order be delivered LATE?
#      Mark each SAFE or LEAK, and say why.
# =============================================================================
CANDIDATE_FEATURES = [
    "order_purchase_timestamp",        #
    "customer_state",                  #
    "product_category",                #
    "seller_state",                    #
    "freight_value",                   #
    "estimated_delivery_date",         #
    "order_delivered_customer_date",   #
    "review_score",                    #
    "payment_installments",            #
    "days_late",                       #
    "seller_avg_delay_last_90d",       #
    "order_item_count",                #
]
#   THE TEST: would I actually know this value AT THE MOMENT I need the prediction?
#
#   WHICH WAS THE SUBTLEST LEAK?
#   HOW WOULD I HAVE CAUGHT IT IN REAL WORK?
#   (symptom: a score that seems too good. Treat 0.99 as a bug report.)


# =============================================================================
# 5 -- THE AVAILABILITY TEST on your own Project 2 features.
# =============================================================================
def availability_test(df):
    """For each column: known at prediction time? yes / no / depends."""
    pass


# =============================================================================
# 6 -- THREE PROBLEMS WHERE ML IS THE WRONG TOOL.
#      From LifeOS, SwiftBase, or your own experience.
# =============================================================================
#   1. PROBLEM:                     BETTER APPROACH:
#   2. PROBLEM:                     BETTER APPROACH:
#   3. PROBLEM:                     BETTER APPROACH:
#
#   A CASE WHEN a shopkeeper can read and override beats a random forest
#   nobody trusts. When is that true?


# =============================================================================
# 7 -- THE PROJECT 3 BRIEF.  (starts Day 80 -- decide it now)
# =============================================================================
#   THE QUESTION:
#
#   THE TARGET (what exactly am I predicting, and how is it defined):
#
#   THE FEATURES I WOULD ACTUALLY HAVE AT PREDICTION TIME:
#
#   THE BASELINE I MUST BEAT:
#
#   WHAT BEATING IT BY 2% WOULD BE WORTH, IN MONEY OR RISK:
#
#   WHY THIS PROBLEM AND NOT ANOTHER:
#
#   Deciding this NOW means Days 71-79 are studied with a use in mind.


# MINI ASSESSMENT -- 5 minutes
#   "Can we use AI to predict which customers will leave?"
#     what I would need:
#     the baseline:
#     what could leak:
#     ONE REASON THIS MIGHT NOT BE WORTH BUILDING:


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    baselines(y_regression=rng.normal(100, 15, 1000),
              y_classification=rng.choice([0, 1], 1000, p=[0.94, 0.06]))
