"""
Day 16 — Instances and state
=============================
Build ShopLedger: the object version of Day 12's shopsummary.

Exercise 5 is the important one. Do NOT skip it -- meeting the
stale-cache bug deliberately is worth more than avoiding it.
"""
import time


# 1-4 -- ShopLedger
class ShopLedger:
    """Sales records for ONE shop.

    Rules being practised here:
      * every attribute is declared in __init__, even as None
      * mutators change state and return None
      * queries report and change nothing
      * any cached value is invalidated by every mutator
    """

    def __init__(self, shop_name, records=None):
        # Declare EVERY attribute here. Include the cache.
        # Careful with the default for `records` -- Day 4 taught you why.
        pass

    # --- mutators -------------------------------------------------------
    def add(self, record):
        """Append a record. Must invalidate the cache."""
        pass

    # --- queries --------------------------------------------------------
    def count(self):
        pass

    def total(self):
        """Sum of qty * price. Caches the result."""
        pass

    def mean(self):
        pass


# 5 -- THE CACHE BUG.
#      Step 1: comment out the cache invalidation inside add().
#      Step 2: run this. Watch total() return the stale answer.
#      Step 3: restore the invalidation. Run again.
#      WHAT I SAW:
#      THE RULE THAT PREVENTS THIS:
def ex_05():
    ledger = ShopLedger("Khatri Traders")
    ledger.add({"item": "tea", "qty": 4, "price": 1250.0})
    print("  total before add :", ledger.total())
    ledger.add({"item": "oil", "qty": 1, "price": 540.0})
    print("  total after  add :", ledger.total())
    print("  expected         : 5540.0")


# 6 -- Three shops, three ledgers. Prove their state is independent.
def ex_06():
    pass


# 7 -- Attach an attribute from OUTSIDE the class. It will work.
#      Then say why it is a bad habit.
#      WHY IT IS A BAD HABIT:
def ex_07():
    pass


# 8 -- Move three more shopsummary functions in as methods:
#      top_n, group_totals, validate.  Note what each signature LOSES.
#      WHAT THE SIGNATURES LOST:


# MINI ASSESSMENT -- 6 minutes, closed book
class Basket:
    """add(item, qty, price) | remove(item) | total() | item_count()

    total() caches. BOTH mutators invalidate.
    """
    pass


if __name__ == "__main__":
    print("--- ex_05: the cache bug ---")
    ex_05()
