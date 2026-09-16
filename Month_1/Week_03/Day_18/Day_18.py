"""
Day 18 — Inheritance vs composition
====================================
Part A: inheritance, including two deliberate breakages.
Part B: composition.
Exercise 10 is the assessment -- build the same feature both ways and choose.
"""
import json
from pathlib import Path


# =============================================================================
# PART A -- INHERITANCE
# =============================================================================

# 1 -- the base class
class Ledger:
    def __init__(self, name, records=None):
        pass

    def total(self):
        pass

    def summary(self):
        return f"{self.name}: {len(self.records)} records, total {self.total()}"


# 2 -- OnlineLedger. super() in BOTH __init__ and the override.
class OnlineLedger(Ledger):
    pass


# 3 -- THE super() BUG.
#      Delete super().__init__(...) from BrokenLedger, then call .total().
#      WHERE DID THE ERROR APPEAR?
#      WHERE WAS THE ACTUAL MISTAKE?
class BrokenLedger(Ledger):
    def __init__(self, name, records=None, fee=0.0):
        self.fee = fee          # note: no super().__init__() call


# 4 -- RetailLedger, plus ONE function that works on all three.
#      That function working on all three IS substitutability.
class RetailLedger(Ledger):
    pass

def print_report(ledger):
    """Accepts ANY ledger. Must not know which subclass it got."""
    pass


# 5 -- BREAK substitutability on purpose: return a string from total().
#      Run print_report() on it. Then restore it.
#      WHAT BROKE:
#      THE RULE THIS VIOLATES, IN MY WORDS:
class BadLedger(Ledger):
    def total(self):
        return f"PKR {sum(r['qty'] * r['price'] for r in self.records)}"


# =============================================================================
# PART B -- COMPOSITION
# =============================================================================

# 6 -- two sources, same interface: a load() that returns records
class CsvSource:
    def __init__(self, path): self.path = Path(path)
    def load(self): pass

class DictSource:
    def __init__(self, records): self.records = records
    def load(self): pass


# 7 -- Ledger that HAS A source rather than BEING a kind of reader
class ComposedLedger:
    def __init__(self, name, source):
        pass

    def reload(self):
        """Re-read from the current source."""
        pass

    def total(self):
        pass


# 8 -- swap the source at runtime, then reload. Show the records changed.
def ex_08():
    pass


# 9 -- add a THIRD source. Count how many existing lines you had to change.
#      LINES CHANGED:
class JsonSource:
    def __init__(self, path): self.path = Path(path)
    def load(self): pass


# 10 -- THE COMPARISON.
# Requirement: a ledger that reads from CSV and formats output as JSON.
# Implement both ways. Count the classes each approach needs.
#
#   INHERITANCE  -- classes needed: ____   names:
#   COMPOSITION  -- classes needed: ____   names:
#
#   Now add a THIRD source and a SECOND format. Recount.
#   INHERITANCE  -- classes needed: ____
#   COMPOSITION  -- classes needed: ____
#
#   WHICH WOULD I SHIP, AND WHY:


if __name__ == "__main__":
    print("Work through Part A, then Part B, then exercise 10.")
