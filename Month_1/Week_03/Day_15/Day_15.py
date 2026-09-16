"""
Day 15 — Why objects exist
===========================
DO NOT WRITE A CLASS UNTIL EXERCISE 3.

Exercises 1-2 are the whole point of today. If you skip them and go
straight to the syntax, this block will fail the way previous attempts
at OOP failed.
"""

# =============================================================================
# 1 -- THE DIAGNOSIS.  Open your Day 12 shopsummary. Find these four symptoms
#      IN YOUR OWN CODE and write the line references.
# =============================================================================
#
#  Symptom 1 -- the same argument threaded through every function
#      where in my code:
#
#  Symptom 2 -- data in one place, the functions that operate on it in another
#      where in my code:
#
#  Symptom 3 -- a derived value recomputed or passed around
#      where in my code:
#
#  Symptom 4 -- a second input source would mean duplicating functions
#      where in my code:
#
# =============================================================================
# 2 -- THE SENTENCE.  Complete it from what you just found.
# =============================================================================
#
#  "Functions became awkward in shopsummary when ______________________________"
#
# =============================================================================


# 3 -- NOW the syntax. __init__ stores the records; count() returns how many.
class SalesData:
    pass


# 4 -- Two instances, two different record lists. Show they do not interfere.
RECORDS_A = [
    {"item": "tea",   "region": "sindh",  "qty": 4, "price": 1250.0},
    {"item": "oil",   "region": "sindh",  "qty": 1, "price": 540.0},
]
RECORDS_B = [
    {"item": "sugar", "region": "punjab", "qty": 3, "price": 180.0},
]

def ex_04():
    pass


# 5 -- Add total() and mean() to SalesData. Both read self.records.
#      (Go back and edit the class above.)


# 6 -- Show that these two lines do the same thing:
#         data.count()
#         SalesData.count(data)
#      Then explain `self` in your own words, in the comment below.
#      MY EXPLANATION OF self:
def ex_06():
    pass


# 7 -- THE COUNTER-EXAMPLE.
#      Write a class that SHOULD have been a plain function.
#      Then say exactly why it is not justified.
#      Hint: a class with one method and no state that survives between calls.
#      WHY THIS IS NOT JUSTIFIED:
class BadExample:
    pass


# MINI ASSESSMENT -- 5 minutes, closed book
class Inventory:
    """item -> quantity, with add() and low_stock(threshold).

    WHY IS THIS BETTER AS A CLASS THAN AS TWO FUNCTIONS PLUS A DICT?
    ANSWER:
    """
    pass


if __name__ == "__main__":
    ex_04()
    ex_06()
