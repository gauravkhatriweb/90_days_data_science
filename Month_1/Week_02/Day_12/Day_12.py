"""
shopsummary -- Day 12 entry point
==================================
Your first real tool. No third-party libraries.

    python Day_12.py messy_sales.csv --top 3 --group region

Build order:
  1. shoptools/__init__.py
  2. shoptools/parsing.py    <- Day 11 parser
  3. shoptools/cleaning.py   <- Day 7 text work
  4. shoptools/analysis.py   <- Day 4 helpers + your own median
  5. this file               <- argv handling + output formatting
"""

import sys

# from shoptools.parsing  import read_records
# from shoptools.cleaning import clean_text
# from shoptools.analysis import total_revenue, top_n, summarise, group_totals, median


def parse_args(argv):
    """Return (path, top_n, group_by). Defaults: top=3, group='region'.

    Handle a missing path with a usage message, not a traceback.
    """
    pass


def format_pkr(amount) -> str:
    """1250.0 -> 'PKR 1,250.00'   |   None -> 'PKR --'"""
    pass


def render(path, records, problems, *, top, group_by) -> str:
    """Build the whole report as ONE string, then return it.

    Returning a string instead of printing means you can test this function.
    That is the Day 4 lesson about pure functions, applied.
    """
    pass


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    # path, top, group_by = parse_args(argv)
    # records, problems = read_records(path)
    # print(render(path, records, problems, top=top, group_by=group_by))
    pass


if __name__ == "__main__":
    main()


# =============================================================================
# CHECKS BEFORE YOU CALL THIS DONE
# =============================================================================
#  [ ] runs on messy_sales.csv without crashing
#  [ ] rejected rows show line number AND reason
#  [ ] median is correct for an EVEN number of values  <- the usual bug
#  [ ] deleting shoptools/__init__.py breaks it, and you know why
#  [ ] render() returns a string; main() does the printing
