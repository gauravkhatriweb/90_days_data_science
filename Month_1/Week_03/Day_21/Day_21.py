"""
Day 21 — Build from memory
===========================
PART C. Closed book. Do not open Days 15-20.
20 minutes. If you have to look something up, note WHICH thing -- that is the
result of this exercise, not the class itself.
"""


class Inventory:
    """Stock for one shop.

    Required:
      __init__(shop_name, items=None)   -- declare EVERY attribute
      add(item, qty, price)             -- mutator, invalidates the cache
      remove(item)                      -- mutator, invalidates the cache
      total_value                       -- @property, cached
      low_stock(threshold)              -- query
      from_csv(path)                    -- @classmethod using cls
      __repr__  __len__  __getitem__  __contains__  __eq__
      _cache                            -- underscore-internal
    """
    pass


class TrackedInventory(Inventory):
    """Records every change to the stock.

    SHOULD THIS HAVE BEEN INHERITANCE OR COMPOSITION?
    Apply the "is a" test. Then apply the substitutability test.
    ANSWER:
    """
    pass


# =============================================================================
# THINGS I HAD TO LOOK UP  (this list is the real output of today)
# =============================================================================
#   1.
#   2.
#   3.
#
# PART A SCORE: ___ / 10
# ACTION FROM THE TABLE:
# =============================================================================


if __name__ == "__main__":
    inv = Inventory("Khatri Traders")
    print(repr(inv))
