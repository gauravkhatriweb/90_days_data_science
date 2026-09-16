"""
Day 42 — Consolidation + the Project 1 scope decision
======================================================
Ten retrieval tasks, closed book, 3 minutes each. 0 / 0.5 / 1.
Then the honest scope question.
"""
import pandas as pd

# 1 (D36) -- left join, verify the row count
def t1(): pass
S1 = None

# 2 (D36) -- what does validate="many_to_one" prevent?  ANSWER:
S2 = None

# 3 (D37) -- melt wide->long, then pivot back
def t3(): pass
S3 = None

# 4 (D37) -- when does pivot raise where pivot_table does not?  ANSWER:
S4 = None

# 5 (D38) -- chart with fig, ax and all seven readability rules
def t5(): pass
S5 = None

# 6 (D39) -- two figure-level and two axes-level functions
#   figure-level:            axes-level:
S6 = None

# 7 (D40) -- IQR outlier detection. WHY NOT Z-SCORE HERE?
def t7(): pass
S7 = None

# 8 (D40) -- why correlate % changes rather than levels?  ANSWER:
S8 = None

# 9 (D41) -- a cleaning step returning (data, count)
def t9(): pass
S9 = None

# 10 (SQL) -- a correlated subquery, and what makes it correlated
#   QUERY:
#   WHAT MAKES IT CORRELATED:
S10 = None


# =============================================================================
# THE THREE-DAY TEST  -- Project 1 ships on Day 45. You have ~4 hours left.
# =============================================================================
#   [ ] cleaning pipeline runs end to end
#   [ ] at least ONE question answered with evidence
#   [ ] at least THREE charts worth keeping
#   [ ] data-quality decisions recorded WITH COUNTS
#   [ ] I could explain the finding to a non-technical person
#
#   UNTICKED: ____
#
#   IF 3 OR MORE ARE UNTICKED -> NARROW THE SCOPE TODAY.
#   One question answered properly beats three answered vaguely.
#   A reviewer reads depth as competence and breadth as padding.
#
#   MY DECISION:
#   WHAT I CUT:
#   MY ONE-SENTENCE CONCLUSION AS IT STANDS:
#
#   AM I SCOPING HONESTLY, OR HOPING THE NEXT THREE DAYS GO UNUSUALLY WELL?
# =============================================================================


if __name__ == "__main__":
    scores = [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10]
    done = [s for s in scores if s is not None]
    if done:
        print(f"Score: {sum(done)} / 10")
        print(f"Weak: {[i+1 for i, s in enumerate(scores) if s is not None and s < 1]}")
