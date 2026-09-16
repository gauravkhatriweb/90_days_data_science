"""
Day 9 — Errors are information  (45-min orientation day)
=========================================================
Rule 1: never write a bare `except:`
Rule 2: keep the try block small
Rule 3: fail loudly at the edges, quietly in the middle
"""

# 1 -- safe_float: return None instead of raising.
#      Comment: WHY is returning None right here, when Day 4 said to be deliberate?
#      ANSWER:
def safe_float(value):
    pass


# 2 -- Catch FileNotFoundError. The message must name the path it tried.
def ex_02(path="does_not_exist.csv"):
    pass


# 3 -- Catch ValueError and TypeError in ONE except, keeping the exception object.
def ex_03(value=None):
    pass


# 4 -- Use `else` so the try block contains exactly one line.
def ex_04(raw="42.5"):
    pass


# 5 -- Prove `finally` runs even when the exception is NOT caught.
def ex_05():
    pass


# 6 -- Your own exception, with an actionable message.
class DataQualityError(Exception):
    """Raised when input data fails validation."""

def ex_06(rows=[]):
    pass


# 7 -- THE ANTI-PATTERN.
#      Run buggy_version() -- it contains a typo (`pric` not `price`).
#      Watch the bare except swallow it completely.
#      Then write fixed_version() that lets the typo surface.
def buggy_version(row={"item": "tea", "price": 1250}):
    try:
        return row["item"], row["pric"] * 2     # typo, on purpose
    except:
        return None                              # and it vanishes

def fixed_version(row={"item": "tea", "price": 1250}):
    pass


# 8 -- THE REAL ONE.
# Process every row. Return (processed, failures) where each failure is
# (index, exception_type_name, message). Nothing should stop the batch.
BROKEN_ROWS = [
    {"item": "tea",   "qty": 4,     "price": "1250.00"},
    {"item": "sugar", "qty": "3",   "price": "N/A"},
    {"item": "oil",                 "price": "540"},
    {"item": "flour", "qty": 2,     "price": ""},
    {"item": "ghee",  "qty": 0,     "price": "1900"},
    {"item": "rice",  "qty": 5,     "price": "890.50"},
]

def ex_08(rows=BROKEN_ROWS):
    pass


# MINI ASSESSMENT -- 3 minutes, closed book
def parse_price(raw):
    """'1,250.00' -> 1250.0 | 'N/A' -> None | '' -> None | None -> None"""
    pass


if __name__ == "__main__":
    print("buggy :", buggy_version())
    processed, failures = ex_08() or ([], [])
    print(f"processed={len(processed)} failures={failures}")
    for v in ("1,250.00", "540", "N/A", "", None):
        print(f"  {v!r:<12} -> {parse_price(v)}")
