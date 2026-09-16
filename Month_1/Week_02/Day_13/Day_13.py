"""
Day 13 — Debugging  (45-min day: first day of semester)
=======================================================
Five planted bugs. For EACH one:
   1. write your hypothesis in the HYPOTHESIS comment
   2. THEN run it
   3. THEN debug it
   4. record whether your first guess was right

Tracking your hit rate is how debugging gets faster.
"""

# =============================================================================
# BUG 1 -- ZeroDivisionError. The cause is not where it crashes.
# HYPOTHESIS:
# WAS I RIGHT?
# =============================================================================
ROWS_1 = [
    {"item": "tea", "qty": "4", "price": "1250"},
    {"item": "oil", "qty": "1", "price": "540"},
]

def mean_price(rows):
    prices = [float(r["price"]) for r in rows if r["qty"].isdigit() and int(r["qty"]) > 10]
    return sum(prices) / len(prices)


# =============================================================================
# BUG 2 -- No error. Wrong answer. The dangerous kind.
# HYPOTHESIS:
# WAS I RIGHT?
# =============================================================================
def drop_invalid(rows):
    for row in rows:
        if row.get("qty", 0) <= 0:
            rows.remove(row)
    return rows

ROWS_2 = [
    {"item": "a", "qty": 0}, {"item": "b", "qty": 0},
    {"item": "c", "qty": 5}, {"item": "d", "qty": 0},
]
# Expect one row back. Count what you actually get.


# =============================================================================
# BUG 3 -- KeyError on a column that is visibly there.
# HYPOTHESIS:
# WAS I RIGHT?
# =============================================================================
HEADER_LINE = "﻿item,qty,price"     # note what is at the front

def build_header(line):
    return line.split(",")

def lookup(row_dict):
    return row_dict["item"]


# =============================================================================
# BUG 4 -- TypeError, from a None produced somewhere else entirely.
# HYPOTHESIS:
# WAS I RIGHT?
# =============================================================================
def safe_float(v):
    try:
        return float(v)
    except ValueError:
        return None

def revenue(rows):
    return sum(safe_float(r["price"]) * r["qty"] for r in rows)

ROWS_4 = [
    {"price": "1250", "qty": 4},
    {"price": "N/A",  "qty": 2},
]


# =============================================================================
# BUG 5 -- Correct on 5 rows, wrong on 5,000. Off-by-one.
# HYPOTHESIS:
# WAS I RIGHT?
# =============================================================================
def chunk(items, size):
    """Split into chunks of `size`. Test on len 5 AND len 5000."""
    out = []
    for i in range(0, len(items), size):
        out.append(items[i:i + size - 1])
    return out


if __name__ == "__main__":
    print("Write hypotheses FIRST, then uncomment one at a time.\n")
    # print(mean_price(ROWS_1))
    # print(drop_invalid(ROWS_2))
    # print(revenue(ROWS_4))
    # print(len(chunk(list(range(5000)), 10)), sum(len(c) for c in chunk(list(range(5000)), 10)))
