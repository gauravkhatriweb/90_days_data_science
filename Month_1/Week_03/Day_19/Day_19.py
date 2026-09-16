"""
Day 19 — Encapsulation, properties, dunder methods, polymorphism
=================================================================
One class, built up twelve steps. By the end it behaves like a built-in type.

Watch for exercise 8: implementing __getitem__ gives you iteration for free.
Work out WHY before you read the answer anywhere.
"""


class ShopLedger:
    """Sales records for one shop.

    Internals are prefixed with _ . They are not private -- they are a promise.
    """

    def __init__(self, name, records=None, delivery_fee=0.0):
        pass

    # --- 3: @property -----------------------------------------------------
    # Convert total() and mean() to properties. Then check: did ANY caller
    # elsewhere in this file need to change?  ANSWER:

    # --- 4: a setter that validates at the boundary -----------------------
    # delivery_fee must reject negatives AT ASSIGNMENT.
    # WHY IS FAILING HERE BETTER THAN FAILING IN total()?  ANSWER:

    # --- 5: __repr__ ------------------------------------------------------
    # Make it useful in a traceback: class name, shop name, record count, total.

    # --- 6: __str__ -------------------------------------------------------
    # A human one-liner. Show WHERE each of repr/str is used.

    # --- 7: __len__ -------------------------------------------------------

    # --- 8: __getitem__ ---------------------------------------------------
    # After this, `for r in ledger` works even though you wrote no __iter__.
    # WHY?  ANSWER:

    # --- 9: __eq__ and __hash__ -------------------------------------------
    # Compare by content. Then put two ledgers in a set.
    # What happens if you define __eq__ WITHOUT __hash__?  ANSWER:

    # --- 10: __lt__ -------------------------------------------------------
    # sorted(ledgers) should order by total.

    # --- 11: __contains__ -------------------------------------------------
    # "tea" in ledger  ->  True if any record has that item.
    # What does Python fall back to if you DON'T define this?  ANSWER:


# 1 -- Access an underscore attribute from outside. Nothing stops you.
def ex_01():
    pass


# 2 -- __ name mangling. Show the mangled name via vars() or dir().
#      WHY IS THIS NOT "PRIVATE"?  ANSWER:
class Mangled:
    def __init__(self):
        self.__secret = 42

def ex_02():
    pass


# 12 -- POLYMORPHISM with no inheritance at all.
#       Three unrelated classes sharing only a method NAME.
class CsvSource:
    def load(self): return [{"item": "tea", "qty": 4, "price": 1250.0}]

class ApiSource:
    def load(self): return [{"item": "oil", "qty": 1, "price": 540.0}]

class FakeSource:
    """Exists only for tests. No files, no network. This is why composition wins."""
    def load(self): return []

def load_all(sources):
    """Works on ANY object with .load(). Python never checks the class.
    WHAT IS PYTHON ACTUALLY CHECKING?  ANSWER:
    """
    pass


# MINI ASSESSMENT -- 12 minutes, closed book
class PriceList:
    """{item: price} with len(), [], in, iteration, __repr__, and .average

    .average must be a PROPERTY, not a method.
    Missing key -> KeyError with a message that names the item.
    """
    pass


if __name__ == "__main__":
    ex_01(); ex_02()
    print(load_all([CsvSource(), ApiSource(), FakeSource()]))
