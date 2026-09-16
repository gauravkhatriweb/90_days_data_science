"""
Day 30 — Vectorisation and broadcasting
========================================
The mental switch: DESCRIBE the transformation, do not manage the iteration.

Exercises 5 and 7 require PREDICTIONS before running. Write them down.
"""
import time

import numpy as np

QTY = np.array([4, 12, 1, 25, 7, 30])
PRICE = np.array([1250.0, 180.0, 2600.0, 540.0, 890.0, 120.0])
GRID = np.arange(1, 25).reshape(4, 6)


# =============================================================================
# VECTORISATION
# =============================================================================

# 1 -- rewrite three Day 3 loops as array expressions. TIME BOTH.
def ex_01():
    pass


# 2 -- np.where: tiered discount, no loop.
#      qty > 20 -> 20% off | qty > 10 -> 10% off | else full price
def ex_02(qty=QTY, price=PRICE):
    pass


# 3 -- chain five operations into ONE expression. Compare speed AND readability.
#      WHICH IS MORE READABLE? BE HONEST.
def ex_03():
    pass


# 4 -- normalise: (x - mean) / std, vectorised
def ex_04(a=PRICE):
    pass


# =============================================================================
# AXIS -- predict the SHAPE before running
# =============================================================================

# 5 -- six aggregations on a (4,6) array.
#      PREDICT EACH RESULT SHAPE FIRST.
def ex_05(a=GRID):
    ops = [
        ("a.sum()",          lambda: a.sum()),          # predicted shape:
        ("a.sum(axis=0)",    lambda: a.sum(axis=0)),    # predicted shape:
        ("a.sum(axis=1)",    lambda: a.sum(axis=1)),    # predicted shape:
        ("a.mean(axis=0)",   lambda: a.mean(axis=0)),   # predicted shape:
        ("a.max(axis=1)",    lambda: a.max(axis=1)),    # predicted shape:
        ("a.argmax(axis=0)", lambda: a.argmax(axis=0)), # predicted shape:
    ]
    for label, fn in ops:
        r = np.asarray(fn())
        print(f"  {label:<20} shape {str(r.shape):<8} {r}")


# 6 -- the axis rule IN MY OWN WORDS, then verified on a 3D array.
#      MY RULE:
def ex_06():
    a = np.arange(24).reshape(2, 3, 4)
    for ax in (0, 1, 2):
        print(f"  shape {a.shape}  axis={ax}  ->  {a.sum(axis=ax).shape}")


# =============================================================================
# BROADCASTING
# =============================================================================

# 7 -- PREDICT the result shape (or "error") for each pair. THEN run.
#      SCORE: ___ / 8
SHAPE_PAIRS = [
    ((3, 4), (4,)),      # predict:
    ((3, 4), (3,)),      # predict:
    ((3, 4), (3, 1)),    # predict:
    ((3, 1), (1, 4)),    # predict:
    ((5,),   (5, 1)),    # predict:
    ((2, 3, 4), (4,)),   # predict:
    ((2, 3, 4), (3, 4)), # predict:
    ((2, 3, 4), (2, 4)), # predict:
]

def ex_07():
    for s1, s2 in SHAPE_PAIRS:
        try:
            result = (np.ones(s1) + np.ones(s2)).shape
        except ValueError:
            result = "ERROR"
        print(f"  {str(s1):<12} + {str(s2):<10} -> {result}")


# 8 -- THE TRAP. Add a per-row value to a (3,4) array.
#      Run it, get the error, understand it, then fix it TWO ways.
def ex_08():
    grid = np.ones((3, 4))
    per_row = np.array([10, 20, 30])          # shape (3,) -- will fail
    try:
        print(grid + per_row)
    except ValueError as e:
        print("  expected failure:", e)
    # FIX A (reshape):
    # FIX B (np.newaxis):
    # WHY DOESN'T NUMPY JUST GUESS WHAT I MEANT?


# =============================================================================
# JUDGEMENT -- vectorisation is not always the answer
# =============================================================================

# 9 -- find the CROSSOVER. Loop vs vectorised at n = 10, 100, 1000, 100000.
#      CROSSOVER AT n ≈ ____
#      WHAT DOES THIS SAY ABOUT OPTIMISING SMALL DATA?
def ex_09():
    for n in (10, 100, 1_000, 100_000):
        a = np.random.rand(n)
        t = time.perf_counter()
        for _ in range(100):
            [x * 2 for x in a]
        loop = time.perf_counter() - t
        t = time.perf_counter()
        for _ in range(100):
            a * 2
        vec = time.perf_counter() - t
        print(f"  n={n:>7}  loop {loop:.5f}s  vec {vec:.5f}s  ratio {loop/vec:>6.1f}x")


# 10 -- running total, both ways. Which would you ship?
#       ARGUMENT:
def ex_10(a=QTY):
    pass


# MINI ASSESSMENT -- 6 minutes, closed book, ZERO loops
def mini():
    sales = np.random.randint(0, 100, size=(50, 4))
    # 1. total revenue per product
    # 2. each day's sales as a % of that day's total
    # 3. days where ANY product sold > 2x its own average
    # 4. normalised per product (subtract product mean, divide by product std)
    pass


if __name__ == "__main__":
    print("--- ex_05 axis ---");          ex_05()
    print("--- ex_06 3D axis ---");       ex_06()
    print("--- ex_07 broadcasting ---");  ex_07()
    print("--- ex_08 the trap ---");      ex_08()
    print("--- ex_09 crossover ---");     ex_09()
