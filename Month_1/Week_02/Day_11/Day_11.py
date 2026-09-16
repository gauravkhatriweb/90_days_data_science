"""
Day 11 — Files, and the CSV you parse yourself
===============================================
By the end you will know exactly what pd.read_csv() does for you --
and what it has to guess.

DO NOT import csv until step 8.
"""

from pathlib import Path

FIXTURE = Path("messy_sales.csv")

MESSY_CSV = '''item,qty,price
"Tea, Green",4,1250.00
Sugar,3,"1,180.00"
Oil,,540
Flour,2
Ghee,1,540,extra
"Rice, Basmati 5kg",2,2600.00
'''


# 1 -- Write the fixture using `with`.
def step_01_write():
    pass


# 2 -- Read it three ways. Comment on when each is correct.
#      read()      ->
#      readlines() ->
#      for line in f ->
def step_02_read_three_ways():
    pass


# 3 -- Naive parse. Print the rows that break and say WHY each one broke.
def step_03_naive():
    pass


# 4 -- Handle quoted fields containing commas.
#      Scan character by character. Track whether you are inside quotes.
def split_csv_line(line: str, sep: str = ",") -> list[str]:
    pass


# 5 -- Type conversion. Reuse the Day 9 idea: return None rather than raising.
def safe_float(value):
    pass

def to_record(fields: list[str], header: list[str]) -> dict:
    pass


# 6 -- Detect short and long rows. Do not crash, do not silently pad.
def validate_field_count(fields: list[str], expected: int, line_no: int):
    """Return None if fine, else (line_no, reason)."""
    pass


# 7 -- Write clean records back out, quoting any field containing the separator.
def step_07_write_clean(records: list[dict], path=Path("clean_sales.csv")):
    pass


# 8 -- NOW import csv and compare. Write down every difference you find.
#      DIFFERENCES:
def step_08_compare():
    import csv
    with open(FIXTURE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            print("  csv module:", row)


# MINI ASSESSMENT -- 10 minutes, closed book
def read_records(path=FIXTURE):
    """Return (records, problems).

    records : list[dict] with typed values
    problems: list[(line_number, reason)]
    Must not raise on any line of the fixture.
    """
    pass


if __name__ == "__main__":
    step_01_write()
    step_03_naive()
    print("\n--- csv module for comparison ---")
    step_08_compare()
    recs, probs = read_records() or ([], [])
    print(f"\nrecords={len(recs)} problems={probs}")
