"""
Day 49 — Statistics consolidation. Closed book.
================================================
Ten tasks, 3 minutes each. 0 / 0.5 / 1.
Task 11 is the one that takes judgement.
"""
import numpy as np
from scipy.stats import beta

rng = np.random.default_rng(42)

# 1 -- the four probability operations and their formulas
#   P(A and B) =            (independent)
#   P(A and B) =            (always)
#   P(A or B)  =
#   P(A | B)   =
S1 = None

# 2 -- why does the union rule subtract the joint?  ANSWER:
S2 = None

# 3 -- Bayes on a NEW problem, formula from memory.
#   A factory's 2% of parts are defective. A scanner catches 95% of defects
#   and false-alarms on 3% of good parts. A part is flagged. P(defective)?
def t3(): pass
S3 = None

# 4 -- P(A|B) != P(B|A) with a FRESH example
#   P(A|B) means:        P(B|A) means:
S4 = None

# 5 -- binomial when ____________ ; beta when ____________
S5 = None

# 6 -- 95% credible interval from 12 successes in 40 trials
def t6(): pass
S6 = None

# 7 -- explain n-1 WITHOUT algebra
#   ANSWER:
S7 = None

# 8 -- when is the median the honest choice?  ANSWER:
S8 = None

# 9 -- np.std vs pd.Series.std defaults
#   np.std default ddof = ____    pandas default ddof = ____
S9 = None

# 10 -- a sampling bias in a dataset I have ACTUALLY used
#   DATASET:        BIAS:        CONSEQUENCE:
S10 = None


# =============================================================================
# 11 -- THE COMPOUND QUESTION
# A: 240 / 3000 clicked.   B: 280 / 3000 clicked.
# =============================================================================
def experiment():
    a_s, a_f = 240, 3000 - 240
    b_s, b_f = 280, 3000 - 280
    a = rng.beta(a_s, a_f, 200_000)
    b = rng.beta(b_s, b_f, 200_000)
    print(f"  A: {a_s/3000:.4f}   95% CI {beta.ppf([.025,.975], a_s, a_f)}")
    print(f"  B: {b_s/3000:.4f}   95% CI {beta.ppf([.025,.975], b_s, b_f)}")
    print(f"  P(B > A) = {(b > a).mean():.4f}")
    print(f"  median lift = {np.median(b - a):.5f}")

#   WHAT I TELL THE TEAM:
#
#   WHAT I REFUSE TO TELL THEM:
#   (e.g. that B "causes" more clicks; that the lift will hold at scale;
#    that this justifies a permanent change on one week of data)


if __name__ == "__main__":
    print("--- task 11 ---"); experiment()
    scores = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]
    done = [s for s in scores if s is not None]
    if done:
        print(f"\nScore: {sum(done)} / 10")
        print(f"Weak: {[i+1 for i, s in enumerate(scores) if s is not None and s < 1]}")
