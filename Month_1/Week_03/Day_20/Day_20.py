"""
Day 20 — Abstraction: design the interface first
=================================================
EXERCISE 1 IS THE POINT. Write the contract before any class.
If you start with `class DataSource(ABC):` you have skipped the lesson.
"""
from abc import ABC, abstractmethod


# =============================================================================
# 1 -- DESIGN FIRST. No code. Fill this in before scrolling down.
# =============================================================================
#
#  CONTRACT: DataSource
#
#   load()      -> returns:
#                  raises:
#                  promises:
#
#   describe()  -> returns:
#                  promises:
#
#   What must EVERY source promise, regardless of where the data comes from?
#
#   What must a source NOT be responsible for?
#
# =============================================================================


# 2-3 -- the ABC: two abstract methods, one concrete shared method
class DataSource(ABC):
    pass


# 4 -- two real implementations
class CsvSource(DataSource):
    pass

class DictSource(DataSource):
    pass


# 5 -- BREAK IT. This one is missing describe().
#      WHEN DOES THE ERROR APPEAR?
class IncompleteSource(DataSource):
    def load(self):
        return []


# 6 -- The same omission with DUCK TYPING instead of an ABC.
#      WHEN DOES *THIS* ERROR APPEAR?
#      THE DIFFERENCE, AND WHY IT MATTERS IN A TEAM:
class DuckSource:
    def load(self):
        return []
    # no describe() -- and nothing complains until someone calls it

def uses_a_source(source):
    records = source.load()
    header = source.describe()      # fails here, whenever this happens to run
    return header, records


# 7 -- a second interface
class ReportFormatter(ABC):
    @abstractmethod
    def format(self, ledger) -> str:
        """Render a ledger as text. Must not mutate the ledger."""

class TextFormatter(ReportFormatter):
    pass

class JsonFormatter(ReportFormatter):
    pass


# 8 -- the final composition: a Ledger that HAS a source and HAS a formatter
class Ledger:
    def __init__(self, name, source: DataSource, formatter: ReportFormatter):
        pass

    def report(self) -> str:
        pass


# 9 -- swap both at runtime. Then count.
#      3 sources x 2 formats
#        with COMPOSITION : ____ classes
#        with INHERITANCE : ____ classes
#      Now make it 5 sources x 4 formats. Recount.
#        COMPOSITION : ____      INHERITANCE : ____
def ex_09():
    pass


# MINI ASSESSMENT -- 8 minutes, closed book
class Notifier(ABC):
    """SwiftBase sends receipts by SMS, WhatsApp, and printed slip.

    Two abstract methods, one concrete shared method.

    WHAT SHOULD HAPPEN WHEN A NOTIFIER FAILS?
    WHOSE JOB IS IT TO DECIDE -- the notifier, or the caller?
    ANSWER:
    """
    pass


if __name__ == "__main__":
    try:
        IncompleteSource()
    except TypeError as e:
        print("ABC caught it at instantiation:\n ", e)

    print("\nDuck typing did NOT catch it at instantiation.")
    try:
        uses_a_source(DuckSource())
    except AttributeError as e:
        print("It failed later, at the call site:\n ", e)
