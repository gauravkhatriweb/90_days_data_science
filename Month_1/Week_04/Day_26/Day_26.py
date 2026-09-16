"""
Day 26 — Assessment + generators
=================================
PART A IS CLOSED BOOK AND TIMED. Do it before reading anything else.
No notes. No AI. No docs. No accepting autocomplete.
If a task overruns, STOP and move on. Score honestly.
"""
import itertools
import sys
import time

# =============================================================================
# PART A -- THE ASSESSMENT  (75 minutes)
# =============================================================================

# 1 (8 min) -- parse a messy CSV line with a quoted comma into a typed dict
def task_01(line='"Tea, Green",4,"1,250.00"'):
    pass
SCORE_01 = None

# 2 (8 min) -- group by TWO keys, sum a third. State your structure and why.
#    STRUCTURE:     WHY:
def task_02(rows):
    pass
SCORE_02 = None

# 3 (10 min) -- class with __init__, cached @property, invalidating mutator, __repr__
class Task03:
    pass
SCORE_03 = None

# 4 (10 min) -- an ABC, two implementations, one function that uses both
SCORE_04 = None

# 5 (8 min) -- return (results, failures) over rows that break three different ways
def task_05(rows):
    pass
SCORE_05 = None

# 6 (7 min) -- multi-level sort, then top-N per group
def task_06(rows, n=2):
    pass
SCORE_06 = None

# 7 (7 min) -- one list comprehension and one dict comprehension, both with conditions
def task_07(rows):
    pass
SCORE_07 = None

# 8 (10 min) -- four pytest tests for task_06, INCLUDING the empty case
SCORE_08 = None

# 9 (7 min) -- find and fix three bugs below
def buggy(rows=[], seen={}):                    # bug 1
    total = 0
    for r in rows:
        if r["qty"] > 0:
            rows.remove(r)                      # bug 2
        total += r["price"] * r["qty"]
    return total / len(rows)                    # bug 3
#   BUG 1:
#   BUG 2:
#   BUG 3:
SCORE_09 = None


def score_part_a():
    scores = [SCORE_01, SCORE_02, SCORE_03, SCORE_04, SCORE_05,
              SCORE_06, SCORE_07, SCORE_08, SCORE_09]
    done = [s for s in scores if s is not None]
    if not done:
        return print("Fill in SCORE_01..SCORE_09 after the timed run.")
    total = sum(done)
    weak = [i + 1 for i, s in enumerate(scores) if s is not None and s < 1]
    print(f"PART A: {total} / 9    weak tasks: {weak}")
    if   total >= 8: print("  -> Python is no longer the obstacle. Month 2 as written.")
    elif total >= 6: print("  -> Solid with gaps. Month 2 IF TIME goes to the weak tasks.")
    elif total >= 4: print("  -> Shaky. Add a 20-min Python warm-up to Days 29-35.")
    else:            print("  -> Repeat Days 15-21 in Week 5's IF TIME. Start NumPy anyway.")


# =============================================================================
# PART B -- GENERATORS   (only after Part A is scored)
# =============================================================================

# 10 -- convert DirectorySource.load() to iter_logs() using yield


# 11 -- a three-stage LAZY pipeline. Prove nothing runs until consumed.
def ex_11():
    def read(n):
        for i in range(n):
            print(f"    read {i}")      # proof of laziness
            yield i
    pass


# 12 -- THE EXHAUSTION TRAP. Wrong answer, no error.
def ex_12():
    rows = (r for r in [{"qty": 2}, {"qty": 3}])
    total = sum(r["qty"] for r in rows)
    count = len(list(rows))              # 0 -- already exhausted
    print(f"  total={total} count={count}   <- count should be 2")
    # FIX A (materialise once):
    # FIX B (iterate twice):
    # WHICH WOULD I SHIP, AND WHY:


# 13 -- islice over an infinite generator
def ex_13():
    def naturals():
        n = 0
        while True:
            yield n
            n += 1
    pass


# 14 -- itertools.groupby over logs by month.
#       PRECONDITION: it only groups ADJACENT equal keys.
#       WHAT HAPPENS IF THE INPUT IS UNSORTED?
def ex_14():
    pass


# 15 -- measure the memory difference over 1,000,000 items
def ex_15(n=1_000_000):
    as_list = [i for i in range(n)]
    as_gen  = (i for i in range(n))
    print(f"  list      : {sys.getsizeof(as_list):>12,} bytes")
    print(f"  generator : {sys.getsizeof(as_gen):>12,} bytes")


if __name__ == "__main__":
    score_part_a()
    print("\n--- ex_12: the exhaustion trap ---"); ex_12()
    print("\n--- ex_15: memory ---");              ex_15()
