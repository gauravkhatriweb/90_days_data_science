"""
Day 35 — Consolidation. Closed book.
=====================================
Twelve tasks, 3 minutes each. Score 0 / 0.5 / 1.
Task 13 is the one that teaches something new.
"""
import numpy as np
import pandas as pd

# 1 (D29) -- Why is an array faster than a list? Answer in MEMORY terms.
#   ANSWER:
S1 = None

# 2 (D29) -- slice, modify, predict the original.  PREDICTION:
def t2(): pass
S2 = None

# 3 (D30) -- the axis rule, in my words, applied to a (4,6) array
#   RULE:
def t3(): pass
S3 = None

# 4 (D30) -- does (3,4) + (3,) broadcast? If not, fix it.
def t4(): pass
S4 = None

# 5 (D30) -- replace a loop-with-an-if using np.where
def t5(): pass
S5 = None

# 6 (D31) -- mean over data containing NaN, correctly
def t6(): pass
S6 = None

# 7 (D31) -- compound boolean mask with correct precedence
def t7(): pass
S7 = None

# 8 (D32) -- the five-line ritual, FROM MEMORY
#   1.  2.  3.  4.  5.
S8 = None

# 9 (D32) -- loc vs iloc, same selection, plus the slice-end difference
def t9(): pass
S9 = None

# 10 (D33) -- to_numeric(errors='coerce') and count what it caught
def t10(): pass
S10 = None

# 11 (D34) -- groupby().agg() with NAMED outputs
def t11(): pass
S11 = None

# 12 (D34) -- transform: each row vs its group mean
def t12(): pass
S12 = None


# =============================================================================
# 13 -- ONE QUESTION, THREE TOOLS
# "Average price per item, for items seen more than 20 times."
# =============================================================================

def in_pure_python(rows):
    """Day 12 style. No libraries."""
    pass
# LINES: ____

def in_pandas(df):
    pass
# LINES: ____

SQL = """
-- write it here
"""
# LINES: ____

#   WHICH WOULD I CHOOSE FOR 1,000 ROWS?       WHY?
#   WHICH FOR 50 MILLION ROWS?                 WHY?
#   WHAT DID WRITING ALL THREE REVEAL?


if __name__ == "__main__":
    scores = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12]
    done = [s for s in scores if s is not None]
    if done:
        print(f"Score: {sum(done)} / 12")
        print(f"Weak: {[i+1 for i, s in enumerate(scores) if s is not None and s < 1]}")
