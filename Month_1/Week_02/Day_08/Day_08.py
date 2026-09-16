"""
Day 8 — Slicing, unpacking, sorting by key  (45-min orientation day)
=====================================================================
Nine drills. Predict before you run, at least for drill 1.
"""

PRICES = [1250, 180, 2600, 540, 890]
ROWS = [
    {"item": "tea",   "region": "sindh",  "qty": 4, "price": 1250.0},
    {"item": "sugar", "region": "punjab", "qty": 3, "price": 180.0},
    {"item": "tea",   "region": "punjab", "qty": 2, "price": 1250.0},
    {"item": "oil",   "region": "sindh",  "qty": 1, "price": 540.0},
]
CSV_LINES = [
    "item,qty,price",
    "tea,4,1250",
    "sugar,3,180",
    "oil,1,540",
]


# 1 -- PREDICT each, then run.
def ex_01(p=PRICES):
    # p[1:3]   predict:
    # p[:3]    predict:
    # p[-2:]   predict:
    # p[::2]   predict:
    # p[::-1]  predict:
    # p[3:1]   predict:
    for expr in ("p[1:3]", "p[:3]", "p[-2:]", "p[::2]", "p[::-1]", "p[3:1]"):
        print(f"  {expr:<10} -> {eval(expr)}")


# 2 -- Copy with slicing. Mutate the ORIGINAL and prove the copy is untouched.
def ex_02():
    pass


# 3 -- Reverse a string, a list and a tuple with ONE idiom.
def ex_03():
    pass


# 4 -- Split the header away from the rows using starred unpacking.
#      You use exactly this on Day 11.
def ex_04(lines=CSV_LINES):
    pass


# 5 -- Swap two variables with no temporary.
def ex_05(a=1, b=2):
    pass


# 6 -- Sort ROWS by price, descending.
def ex_06(rows=ROWS):
    pass


# 7 -- Sort by region ASCENDING then price DESCENDING. One key, one sorted() call.
def ex_07(rows=ROWS):
    pass


# 8 -- Highest-revenue row using max(..., key=...). Revenue is qty * price.
def ex_08(rows=ROWS):
    pass


# 9 -- Case-insensitive sort of city names.
#      Then answer: why is key=str.lower better than lowercasing the list first?
#      ANSWER:
def ex_09(cities=["lahore", "Karachi", "hyderabad", "Islamabad"]):
    pass


if __name__ == "__main__":
    print("--- ex_01 ---"); ex_01()
    print("--- ex_04 ---"); print(ex_04())
    print("--- ex_07 ---"); print(ex_07())
    print("--- ex_08 ---"); print(ex_08())
