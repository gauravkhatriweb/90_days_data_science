"""
Day 3 — Control flow and loops, the Python way
===============================================
Ten exercises. Target: at most ONE of your solutions uses an index.
"""

# EX 1 -- FizzBuzz that RETURNS rather than prints.
#         Why does returning matter? Because you can test a return value.
def ex_01_fizzbuzz(n=20):
    pass


# EX 2 -- Rewrite each of these WITHOUT an index.
def ex_02():
    names = ["ali", "sana", "bilal"]
    scores = [72, 91, 65]

    # (a) for i in range(len(names)): print(names[i])
    # (b) for i in range(len(names)): print(i + 1, names[i])
    # (c) for i in range(len(names)): print(names[i], scores[i])
    pass


# EX 3 -- Build {item: price} from two parallel lists using zip.
ITEMS = ["tea", "sugar", "flour", "oil"]
PRICES = [1250, 180, 2600, 540]

def ex_03(items=ITEMS, prices=PRICES):
    pass


# EX 4 -- Print a numbered receipt starting at 1, right-aligned numbers.
def ex_04(items=ITEMS):
    pass


# EX 5 -- Second largest number, WITHOUT sorting and without a library.
#         One pass. Track two values.
def ex_05(numbers=[4, 9, 12, 7, 12, 3, 20, 15]):
    pass


# EX 6 -- Refactor into guard clauses. Keep the behaviour identical.
def ex_06_nested(row):
    if row is not None:
        if "qty" in row:
            if row["qty"] > 0:
                if row.get("price", 0) > 0:
                    return row["qty"] * row["price"]
    return None

def ex_06_guarded(row):
    pass


# EX 7 -- A converging while loop. Halve `value` until it drops below
#         `threshold`. Return (final_value, number_of_steps).
#         This is the shape of gradient descent -- you meet it again on Day 72.
def ex_07(value=1000.0, threshold=1.0):
    pass


# EX 8 -- One pass over the text. Return (vowels, consonants, digits).
def ex_08(text="Gaurav Khatri, 2026, NIT Lahore"):
    pass


# EX 9 -- Print a right-aligned triangle of '*' with `height` rows.
def ex_09(height=5):
    pass


# EX 10 -- THE ONE THAT MATTERS.
# Validate transaction rows. Return (valid_rows, rejections)
# where `rejections` is a list of (row_index, reason) so a human can fix them.
# Reasons to reject: missing key, non-numeric qty/price, qty <= 0, price <= 0.
ROWS = [
    {"item": "tea",    "qty": 4,     "price": 1250.0},
    {"item": "sugar",  "qty": 0,     "price": 180.0},
    {"item": "flour",  "qty": 2,     "price": -1},
    {"item": "oil",    "qty": "two", "price": 540.0},
    {"item": "rice"},
    {"item": "ghee",   "qty": 1,     "price": 1900.0},
]

def ex_10(rows=ROWS):
    pass


if __name__ == "__main__":
    print(ex_01_fizzbuzz())
    ex_02(); print(ex_03()); ex_04()
    print("second largest:", ex_05())
    print("guarded:", ex_06_guarded({"qty": 3, "price": 100}))
    print("converged:", ex_07())
    print("counts:", ex_08())
    ex_09()
    valid, rejected = ex_10() or ([], [])
    print(f"valid={len(valid)} rejected={rejected}")
