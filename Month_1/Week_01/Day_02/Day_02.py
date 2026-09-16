"""
Day 2 — Python idiom: the translation layer
============================================
Nine exercises. The first five translate habits you already have.
The last four are the traps.

Run this file after each exercise. Do not write all nine then run once.
"""

# -----------------------------------------------------------------------------
# EX 1 -- f-strings
# -----------------------------------------------------------------------------
# TODO: Print:  "Gaurav has 3 projects, averaging 2.5 days each"
#       Compute the 2.5 INSIDE the f-string braces. Do not precompute it.
NAME, PROJECTS, TOTAL_DAYS = "Gaurav", 3, 7.5

def ex_01():
    pass


# -----------------------------------------------------------------------------
# EX 2 -- implicit conversion does not exist here
# -----------------------------------------------------------------------------
# Each line below raises TypeError. Fix each one with an EXPLICIT conversion.
def ex_02():
    # a = "5" + 5
    # b = "Total: " + 199.5
    # c = int("12.7")          # this one raises ValueError -- why?
    # d = [1, 2] + (3, 4)
    pass


# -----------------------------------------------------------------------------
# EX 3 -- truthiness
# -----------------------------------------------------------------------------
# PREDICT each result in the comment BEFORE running. Then run and compare.
TRUTHY_TESTS = [
    [],          # predict:
    [0],         # predict:
    "",          # predict:
    " ",         # predict:
    0.0,         # predict:
    {},          # predict:
]

def ex_03():
    for value in TRUTHY_TESTS:
        print(f"{value!r:<8} -> {bool(value)}")


# -----------------------------------------------------------------------------
# EX 4 -- `is` vs `==`
# -----------------------------------------------------------------------------
# TODO: create two lists with identical contents. Show that `==` is True
#       and `is` is False. Then show a case where `is` is the right choice.
def ex_04():
    pass


# -----------------------------------------------------------------------------
# EX 5 -- the .sort() trap
# -----------------------------------------------------------------------------
# TODO: demonstrate that list.sort() returns None while sorted() returns a list.
#       Then answer in a comment: why did the language designers do it this way?
#       ANSWER:
def ex_05():
    pass


# -----------------------------------------------------------------------------
# EX 6 -- string method chaining (this IS data cleaning)
# -----------------------------------------------------------------------------
# TODO: turn "  SURF  EXCEL   2KG \n" into "surf excel 2kg"
#       Chain methods. Handle the doubled internal spaces too.
MESSY = "  SURF  EXCEL   2KG \n"

def ex_06(raw=MESSY):
    pass


# -----------------------------------------------------------------------------
# EX 7 -- parse a CSV line by hand
# -----------------------------------------------------------------------------
# TODO: turn the line into a dict with the right TYPES:
#       {'item': 'tea', 'qty': 4, 'price': 1250.0, 'in_stock': True}
LINE = "tea,4,1250.00,yes"

def ex_07(line=LINE):
    pass


# -----------------------------------------------------------------------------
# EX 8 -- the conditional expression
# -----------------------------------------------------------------------------
# TODO: write "discounted if qty > 10 else standard" three ways:
#       (a) a normal if/else block
#       (b) a one-line conditional expression
#       (c) a dictionary lookup
#       Then comment on which you would use in real code and why.
#       ANSWER:
def ex_08(qty=12):
    pass


# -----------------------------------------------------------------------------
# EX 9 -- a helper you will reuse this week
# -----------------------------------------------------------------------------
# TODO: format_pkr(1250.0) -> "PKR 1,250.00"
#       format_pkr(None)   -> "PKR --"
#       Use an f-string format spec for the thousands separator.
def format_pkr(amount):
    pass


if __name__ == "__main__":
    for fn in (ex_01, ex_02, ex_03, ex_04, ex_05, ex_06, ex_07, ex_08):
        print(f"\n--- {fn.__name__} ---")
        fn()
    print("\n--- format_pkr ---")
    print(format_pkr(1250.0), "|", format_pkr(None))
