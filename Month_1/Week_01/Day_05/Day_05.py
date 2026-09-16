"""
Day 5 — Choosing the right data structure
==========================================
Thirteen exercises in three groups: mechanics, choosing, applied.
Exercise 7 is the one to take seriously -- measure, do not guess.
"""

import time
from collections import Counter, defaultdict

# =============================================================================
# MECHANICS
# =============================================================================

# 1 -- Remove duplicates, PRESERVE order. (Hint: a set for seen, a list for out.)
def ex_01(items=["tea", "sugar", "tea", "oil", "sugar", "flour"]):
    pass


# 2 -- Merge two dicts. On key collision, SUM the values.
def ex_02(a={"tea": 10, "sugar": 5}, b={"tea": 3, "oil": 7}):
    pass


# 3 -- Invert a dict {k: v} -> {v: k}.
#      Then answer: what happens when two keys share a value? Is your answer safe?
#      ANSWER:
def ex_03(d={"tea": 1250, "sugar": 180, "salt": 180}):
    pass


# 4 -- Frequency count BY HAND, then with Counter. Print both line counts.
def ex_04(items=["tea", "sugar", "tea", "oil", "tea"]):
    pass


# 5 -- Group rows by 'region' using defaultdict(list).
ROWS = [
    {"item": "tea",   "region": "sindh",  "qty": 4, "price": 1250.0},
    {"item": "sugar", "region": "punjab", "qty": 3, "price": 180.0},
    {"item": "tea",   "region": "punjab", "qty": 2, "price": 1250.0},
    {"item": "oil",   "region": "sindh",  "qty": 1, "price": 540.0},
]

def ex_05(rows=ROWS):
    pass


# 6 -- Read a value three levels deep WITHOUT KeyError, whatever is missing.
STUDENTS = {"gaurav": {"sem1": {"CSE110": 88}}}

def ex_06(data=STUDENTS, path=("gaurav", "sem1", "MAT265")):
    pass


# =============================================================================
# CHOOSING  -- the real lesson
# =============================================================================

# 7 -- MEASURE. Same membership test, three containers, 50,000 lookups.
#      Predict the ordering FIRST, then run it.
#      MY PREDICTION:
#      MEASURED:
def ex_07(n=50_000):
    haystack = list(range(n))
    as_list, as_set, as_dict = haystack, set(haystack), {k: True for k in haystack}
    needles = range(0, n, 97)

    for label, container in (("list", as_list), ("set", as_set), ("dict", as_dict)):
        start = time.perf_counter()
        hits = sum(1 for x in needles if x in container)
        print(f"  {label:<5} {time.perf_counter() - start:.4f}s  ({hits} hits)")


# 8 -- Aggregate by TWO keys using a tuple as the dict key.
#      Target: {('sindh', 'tea'): 5000.0, ...}
def ex_08(rows=ROWS):
    pass


# 9 -- Set operations on two customer lists. For each of union / intersection /
#      difference, write ONE sentence on what it means to the business.
SHOP_A = {"ali", "sana", "bilal", "hira"}
SHOP_B = {"sana", "hira", "usman"}

def ex_09(a=SHOP_A, b=SHOP_B):
    # union        ->
    # intersection ->
    # a - b        ->
    pass


# 10 -- Flatten a nested list. Then answer: what structure should this have
#       been in the first place, and why was it nested?
#       ANSWER:
def ex_10(nested=[[1, 2], [3, 4, 5], [], [6]]):
    pass


# =============================================================================
# APPLIED
# =============================================================================

# 11 -- Price lookup that never crashes on an unknown item.
def ex_11(prices={"tea": 1250, "sugar": 180}, item="ghee"):
    pass


# 12 -- Items in shop A's inventory but not shop B's.
def ex_12():
    pass


# 13 -- Three interview reps in one function:
#       (a) second-highest value
#       (b) the missing number from 1..N
#       (c) rotate a list left by k
def ex_13():
    pass


if __name__ == "__main__":
    print("\n--- ex_07: MEASURE, do not guess ---")
    ex_07()
