"""
Day 6 — Comprehensions  (45-minute day: orientation week)
==========================================================
Eight conversions. Each loop is given. Write the comprehension beside it.
Exercise 8 is a judgement call, not a conversion.
"""

ROWS = [
    {"item": "tea",   "qty": 4, "price": 1250.0},
    {"item": "sugar", "qty": 0, "price": 180.0},
    {"item": "oil",   "qty": 1, "price": 540.0},
]
MESSY = ["  TEA  ", "Sugar\n", "  OIL"]
ITEMS = ["tea", "sugar", "oil"]
PRICES = [1250, 180, 540]


# 1 -- squares of even numbers 1..20
def loop_01():
    out = []
    for n in range(1, 21):
        if n % 2 == 0:
            out.append(n * n)
    return out

def comp_01():
    pass


# 2 -- clean messy strings
def loop_02():
    out = []
    for s in MESSY:
        out.append(s.strip().lower())
    return out

def comp_02():
    pass


# 3 -- rows with qty above 0
def loop_03():
    out = []
    for r in ROWS:
        if r["qty"] > 0:
            out.append(r)
    return out

def comp_03():
    pass


# 4 -- {item: price} from two parallel lists
def comp_04():
    pass


# 5 -- just the item names from ROWS
def comp_05():
    pass


# 6 -- flatten [[1,2],[3,4],[5]]  (nested comprehension -- note the ORDER of the fors)
def comp_06(nested=[[1, 2], [3, 4], [5]]):
    pass


# 7 -- dict comprehension filtering on the VALUE, not the key
#      From {'tea':1250,'sugar':180,'oil':540} keep only items over 500
def comp_07(d={"tea": 1250, "sugar": 180, "oil": 540}):
    pass


# 8 -- THE TRAP. Write this as a comprehension, then as a loop.
#      Task: for each row, if qty > 0 produce qty*price, else produce 0,
#            but skip rows with no 'price' key entirely.
#      Then answer: which version would you ship, and why?
#      ANSWER:
def trap_comprehension(rows=ROWS):
    pass

def trap_loop(rows=ROWS):
    pass


if __name__ == "__main__":
    print(comp_01())
    print(comp_02())
    print(comp_04())
    print(comp_07())
