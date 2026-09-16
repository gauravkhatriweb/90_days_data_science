"""
Day 14 — Consolidation. Closed book. No scrolling back.
========================================================
Fourteen tasks, one per day so far. 2-4 minutes each.
If you cannot do one in 4 minutes: STOP, mark it 0, move on.
The mark is worth more than the answer.

Score: 0 = could not | 0.5 = needed a hint | 1 = clean
"""

# 1 (Day 1) -- Four analytics types, one example each. Write them as a comment.
#   descriptive :
#   diagnostic  :
#   predictive  :
#   prescriptive:
SCORE_01 = None

# 2 (Day 2) -- "  1,250.00 PKR " -> 1250.0  in one chained expression.
def task_02(raw="  1,250.00 PKR "):
    pass
SCORE_02 = None

# 3 (Day 2) -- Predict bool() for: []  [0]  ""  " "  0.0  {}
#   PREDICTIONS:
SCORE_03 = None

# 4 (Day 3) -- Iterate items and prices together WITH a 1-based index available.
def task_04(items=["tea", "oil"], prices=[1250, 540]):
    pass
SCORE_04 = None

# 5 (Day 3) -- Guard-clause version of this:
#   if row: 
#       if "qty" in row:
#           if row["qty"] > 0:
#               return row["qty"]
def task_05(row):
    pass
SCORE_05 = None

# 6 (Day 4) -- Function with keyword-only args, a docstring, and type hints.
SCORE_06 = None

# 7 (Day 4) -- Reproduce the mutable-default bug, then fix it.
SCORE_07 = None

# 8 (Day 5) -- Aggregate revenue by (region, item). State your structure and why.
#   STRUCTURE:  
#   WHY:
def task_08(rows):
    pass
SCORE_08 = None

# 9 (Day 5) -- Cost of `x in container`:  list = ____   set = ____
SCORE_09 = None

# 10 (Day 6) -- Dict comprehension: {item: revenue} for rows where qty > 0.
def task_10(rows):
    pass
SCORE_10 = None

# 11 (Day 7) -- The six-step cleaning sequence, in order:
#   1.  2.  3.  4.  5.  6.
SCORE_11 = None

# 12 (Day 8) -- Sort rows by region ascending, revenue descending. One key.
def task_12(rows):
    pass
SCORE_12 = None

# 13 (Day 9) -- Batch-process rows, return (processed, failures). No crashes.
def task_13(rows):
    pass
SCORE_13 = None

# 14 (Day 11) -- Parse:  'Tea, Green",4,1250'  -- wait, that is malformed.
#     Parse this correctly:  '"Tea, Green",4,1250'
def task_14(line='"Tea, Green",4,1250'):
    pass
SCORE_14 = None


if __name__ == "__main__":
    scores = [SCORE_01, SCORE_02, SCORE_03, SCORE_04, SCORE_05, SCORE_06, SCORE_07,
              SCORE_08, SCORE_09, SCORE_10, SCORE_11, SCORE_12, SCORE_13, SCORE_14]
    done = [s for s in scores if s is not None]
    if done:
        print(f"Score: {sum(done)} / 14")
        weak = [i + 1 for i, s in enumerate(scores) if s is not None and s < 1]
        print(f"Weak: tasks {weak}")
    else:
        print("Fill in the SCORE_ variables after attempting each task.")
