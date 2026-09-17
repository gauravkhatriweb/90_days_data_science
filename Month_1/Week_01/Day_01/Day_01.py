"""
Day 1 — Environment check and honest baseline diagnostic
=========================================================

TWO PARTS.

PART A: environment. Run this file. If it prints "ENVIRONMENT OK" you are set.
PART B: the diagnostic. 12 tasks, rising difficulty.

RULES FOR PART B
----------------
  * Closed book. No Google, no AI, no notes, no autocomplete suggestions.
  * 50 minutes maximum.
  * If you cannot do a task, write `pass` and move on. Leaving it blank is
    the honest answer and it is genuinely useful information.
  * Score yourself at the end. Be harsh. A flattering score costs you
    three weeks of badly-calibrated curriculum.
"""

# =============================================================================
# PART A — ENVIRONMENT CHECK
# =============================================================================

def check_environment():
    """Verify every library the 90 days depend on."""
    required = [
        "numpy", "pandas", "matplotlib", "seaborn",
        "scipy", "sympy", "sklearn", "pytest",
    ]
    import importlib
    import sys

    print(f"Python {sys.version.split()[0]}")
    missing = []
    for name in required:
        try:
            importlib.import_module(name)
            print(f"  ok      {name}")
        except ImportError:
            print(f"  MISSING {name}")
            missing.append(name)

    if missing:
        print("\nInstall the missing ones:")
        print(f"  pip install {' '.join(missing)}")
        return False

    print("\nENVIRONMENT OK")
    return True


# =============================================================================
# PART B — THE DIAGNOSTIC
# =============================================================================
# Tasks 1-4 test: can you write Python at all?
# -----------------------------------------------------------------------------

# TASK 1 -- Print your name and age on one line, using an f-string.
# Expected output style:  Gaurav is 18 years old
def task_01():
    print(f"Gaurav is 10 years old!")


# TASK 2 -- Given the list below, return the sum of only the even numbers.
#           Do not use a library.
NUMBERS = [4, 9, 12, 7, 3, 20, 15, 8]

def task_02(numbers=NUMBERS):
    pass
#Idonot kown how to do this 


# TASK 3 -- Return the given sentence with the words in reverse order.
#           "data science is hard"  ->  "hard is science data"
def task_03(sentence="data science is hard"):
    pass # idk 


# TASK 4 -- Count how many times each character appears in a string.
#           Return a dictionary.  "hello" -> {'h':1,'e':1,'l':2,'o':1}
def task_04(text="hello"):
    pass#idk 


# -----------------------------------------------------------------------------
# Tasks 5-8 test: do you know Python idiom, not just programming?
# -----------------------------------------------------------------------------

# TASK 5 -- Rewrite this as a SINGLE list comprehension.
#     result = []
#     for n in range(1, 21):
#         if n % 3 == 0:
#             result.append(n * n)
def task_05():
    pass#idk


# TASK 6 -- Given a list of (name, score) tuples, return the names sorted by
#           score, highest first. Use sorted() with a key.
SCORES = [("ali", 72), ("sana", 91), ("bilal", 65), ("hira", 88)]

def task_06(scores=SCORES):
    pass#idk


# TASK 7 -- Write a function that accepts any number of positional arguments
#           and any number of keyword arguments, and returns a string
#           describing how many of each it received.
def task_07():
    pass#idk


# TASK 8 -- Open a file called 'missing_file.csv' and return its first line.
#           If the file does not exist, return the string "no file".
#           Do not let the program crash.
def task_08(path="missing_file.csv"):
    pass#idk


# -----------------------------------------------------------------------------
# Tasks 9-12 test: OOP -- the topic this plan spends the most time on.
# -----------------------------------------------------------------------------

# TASK 9 -- Write a class `Shop` with an __init__ that stores a name and an
#           empty list of sales, and a method `record(amount)` that appends
#           to that list.
class Shop:
    pass#idk


# TASK 10 -- Add a method `total()` to Shop that returns the sum of sales.
#            Then explain in a comment: why is `total()` a method rather than
#            an attribute set in __init__?
#            ANSWER:


# TASK 11 -- Write a class `OnlineShop` that inherits from `Shop`, adds a
#            `delivery_fee` attribute, and overrides `total()` to include
#            the fee once per sale.
class OnlineShop:
    pass#idk


# TASK 12 -- Give Shop a __repr__ so that printing a Shop object shows
#            something like:  Shop('Khatri Traders', 3 sales, total 4500)
#            Why is __repr__ better than writing a .show() method?
#            ANSWER:


# =============================================================================
# SCORING
# =============================================================================

def score_yourself():
    """
    One point per task you completed WITHOUT looking anything up.
    Partial credit is not a thing here -- it either ran or it did not.

      1-4   beginner          -> run Days 2-14 at full length
      5-8   idiom is the gap  -> EXPECTED. Run the plan as written, video at 1.5-2x
      9-11  OOP is the hole   -> compress Days 2-9 into 4, start OOP early
      12    not your problem  -> skip to Day 15, say why in the Week 1 review
    """
    MY_SCORE = None   # <-- put your honest number here
    return MY_SCORE#idk


if __name__ == "__main__":
    check_environment()
    print("\nNow do Part B. Closed book. 50 minutes.")
#idk how to solves these that's why i want to watch python videos 