"""
Day 27 — The standard library you will actually use
====================================================
Every exercise runs against your REAL LifeOS repository.
pathlib | datetime | collections | json
"""
import json
from collections import Counter, defaultdict, namedtuple
from datetime import date, datetime, timedelta
from pathlib import Path

LIFEOS = Path(__file__).resolve().parents[4]


# --- pathlib -----------------------------------------------------------------

# 1 -- every daily log across ALL month directories, in one glob. Count by month.
def ex_01():
    pass


# 2 -- build the path to PILLARS/education.md using parents[]. Confirm it exists.
def ex_02():
    pass


# 3 -- the five largest .md files in LifeOS, by size.
def ex_03():
    pass


# --- datetime ----------------------------------------------------------------

# 4 -- parse every log filename into a date. Earliest, latest, distinct months.
def ex_04():
    pass


# 5 -- THE TRAP. Run it, watch it be False, then fix the comparison.
#      WHY IS IT FALSE?
def ex_05():
    d = date(2026, 9, 16)
    dt = datetime(2026, 9, 16)
    print(f"  date == datetime : {d == dt}")
    # FIX:


# 6 -- days between today and Day 90 (2026-12-14). How many are weekends?
def ex_06():
    pass


# --- collections -------------------------------------------------------------

# 7 -- Counter over every '## ' heading across all logs.
#      WHICH SECTION DO I WRITE MOST? DOES IT MATCH MY STATED PRIORITIES?
def ex_07():
    pass


# 8 -- namedtuple for a log summary. Compare against a dict and a plain tuple.
#      WHEN IS EACH RIGHT?
LogSummary = namedtuple("LogSummary", "date words sections")

def ex_08():
    pass


# --- json --------------------------------------------------------------------

# 9 -- export a summary as JSON. HIT THE DATE ERROR ON PURPOSE, then fix it.
#      WHY DOES json.dumps REFUSE A date?
def ex_09():
    payload = {"generated": date.today(), "logs": 116}
    try:
        print(json.dumps(payload))
    except TypeError as e:
        print("  expected failure:", e)
    # FIX:


# 10 -- ensure_ascii True vs False with Urdu text. Write both, compare the files.
def ex_10():
    payload = {"item": "چائے", "price": 1250}
    print("  ascii=True :", json.dumps(payload))
    print("  ascii=False:", json.dumps(payload, ensure_ascii=False))
    # WHAT WOULD ascii=True DO TO A DATASET OF URDU PRODUCT NAMES?


# MINI ASSESSMENT -- 6 minutes, closed book
def log_stats(directory: Path) -> str:
    """JSON with: count, earliest, latest, three most common headings.

    Dates must serialise. Non-ASCII must survive.
    """
    pass


if __name__ == "__main__":
    print("--- ex_05 ---"); ex_05()
    print("--- ex_09 ---"); ex_09()
    print("--- ex_10 ---"); ex_10()
