"""
Day 17 — Class variables, classmethods, staticmethods
======================================================
Exercise 3 is the one that matters. Reproduce the bug before fixing it.
"""
from pathlib import Path


# 1-2, 5 -- class variables
class ShopLedger:
    currency = "PKR"                        # immutable class variable: fine
    VALID_REGIONS = ("sindh", "punjab")     # tuple, so it cannot be mutated
    instances_created = 0                   # a genuine shared counter

    def __init__(self, name, records=None):
        pass

    # 6 -- alternative constructor from a CSV path
    @classmethod
    def from_csv(cls, path):
        pass

    # 7 -- alternative constructor from records already in memory
    @classmethod
    def from_records(cls, records, name="unnamed"):
        pass

    # 9 -- a staticmethod. Then argue for or against it in the comment.
    #      ARGUMENT:
    @staticmethod
    def is_valid_region(region):
        pass


def ex_01_02():
    """Show the lookup order, then show that assigning via the instance
    SHADOWS rather than changes the class variable."""
    pass


# 3 -- THE BUG. Run this as written. Two ledgers will share one list.
class BuggyLedger:
    records = []                # MUTABLE class variable -- the bug

    def add(self, r):
        self.records.append(r)  # never assigns, so never creates an instance var

def ex_03():
    a, b = BuggyLedger(), BuggyLedger()
    a.add({"item": "tea"})
    print("  a.records:", a.records)
    print("  b.records:", b.records, "  <- b never added anything")
    print("  same object?", a.records is b.records)


# 4 -- Fix it, and write the connection to the Day 4 bug.
#      THE SHARED PRINCIPLE (one sentence):
class FixedLedger:
    pass


# 8 -- Subclass it. Show that from_records returns the SUBCLASS, not ShopLedger,
#      because you used `cls`. Then hardcode the name and watch it break.
class OnlineLedger(ShopLedger):
    pass

def ex_08():
    pass


# MINI ASSESSMENT -- 6 minutes, closed book
class Transaction:
    """class-level `count` | instance `amount` | from_string('tea:4:1250')"""
    pass


if __name__ == "__main__":
    print("--- ex_03: the mutable class variable bug ---")
    ex_03()
