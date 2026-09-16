"""
Day 29 — NumPy: why arrays are not lists
=========================================
Exercises 1, 6, 10 and 11 are the ones that matter.
MEASURE things. Do not take the speedup on trust.
"""
import sys
import time

import numpy as np


# =============================================================================
# WHY ARRAYS
# =============================================================================

# 1 -- MEASURE the speedup. Record the real ratio.
#     MY RATIO: ____x
def ex_01(n=1_000_000):
    as_list = list(range(n))
    as_array = np.arange(n)

    t = time.perf_counter(); sum(as_list);      list_time  = time.perf_counter() - t
    t = time.perf_counter(); as_array.sum();    array_time = time.perf_counter() - t

    print(f"  list  : {list_time:.4f}s")
    print(f"  numpy : {array_time:.4f}s")
    print(f"  ratio : {list_time / array_time:.1f}x")


# 2 -- memory. sys.getsizeof for the list, .nbytes for the array.
def ex_02(n=1_000_000):
    pass


# 3 -- mixed types. Inspect the dtype. WHAT WAS LOST?
#     ANSWER:
def ex_03():
    a = np.array([1, "two", 3.0])
    print(f"  dtype: {a.dtype}")


# =============================================================================
# ANATOMY
# =============================================================================

# 4 -- array, zeros, ones, arange, linspace, random.rand
#      Print shape / ndim / size / dtype for each.
def ex_04():
    pass


# 5 -- reshape 1..12 into (3,4), (4,3), (2,2,3).
#      WHAT DOES -1 MEAN IN reshape?
def ex_05():
    pass


# 6 -- THE OVERFLOW. Run it. Note there is no error.
#      WHY DOES NUMPY ALLOW THIS?
#      TWO FIXES:
def ex_06():
    a = np.array([2_000_000_000, 2_000_000_000], dtype=np.int32)
    print(f"  int32 sum : {a.sum()}    <- should be 4,000,000,000")


# =============================================================================
# INDEXING
# =============================================================================

GRID = np.arange(1, 13).reshape(3, 4)

# 7 -- one element, one row, one COLUMN, a sub-block
def ex_07(a=GRID):
    pass

# 8 -- boolean mask: values above the mean, and how many
def ex_08(a=GRID):
    pass

# 9 -- fancy indexing: pull out coordinates (0,1), (1,3), (2,0)
def ex_09(a=GRID):
    pass


# =============================================================================
# THE TRAP
# =============================================================================

# 10 -- THE VIEW BUG. Predict the output BEFORE running.
#       MY PREDICTION:
def ex_10():
    a = np.array([1, 2, 3, 4, 5])
    b = a[1:4]
    b[0] = 999
    print(f"  a after modifying b: {a}")
    # now with .copy():


# 11 -- VIEW OR COPY? Determine experimentally with np.shares_memory.
#       Fill in the table.
#
#         basic slice  a[1:4]        -> ____
#         boolean mask a[a > 3]      -> ____
#         fancy index  a[[0,2]]      -> ____
#         reshape                     -> ____
#         transpose    a.T            -> ____
#         ravel                       -> ____
#
#       WHY DO MASKS COPY WHILE SLICES VIEW?
def ex_11():
    a = np.arange(10)
    tests = {
        "basic slice":  a[1:4],
        "boolean mask": a[a > 3],
        "fancy index":  a[[0, 2]],
        "reshape":      a.reshape(2, 5),
        "transpose":    a.reshape(2, 5).T,
        "ravel":        a.ravel(),
    }
    for name, result in tests.items():
        kind = "VIEW" if np.shares_memory(a, result) else "COPY"
        print(f"  {name:<14} -> {kind}")


# MINI ASSESSMENT -- 5 minutes, closed book
def mini():
    scores = np.random.randint(40, 100, size=(100, 5))
    # 1. mean per subject
    # 2. students whose average > 80
    # 3. highest score in subject 3, and which student
    # 4. an INDEPENDENT copy of the first ten students
    pass


if __name__ == "__main__":
    print("--- ex_01 speed ---");  ex_01()
    print("--- ex_03 mixed ---");  ex_03()
    print("--- ex_06 overflow ---"); ex_06()
    print("--- ex_10 view bug ---"); ex_10()
    print("--- ex_11 view or copy ---"); ex_11()
