"""
Project P0 — lifelog, build 1 of 3
===================================
Parse your own LifeOS daily logs. ~116 real files. Standard library only.

STEP 1 IS THE DESIGN. Do not write a class until it is filled in.
"""

# =============================================================================
# STEP 1 -- DESIGN.  No code below this until every blank is filled.
# =============================================================================
#
#  CLASSES AND THEIR RESPONSIBILITIES
#    DailyLog        ->
#    LogSource (ABC) ->
#    DirectorySource ->
#    ListSource      ->
#    LogCollection   ->
#    Formatter (ABC) ->
#
#  RELATIONSHIPS
#    "is a" :
#    "has a":
#
#  CONTRACTS
#    LogSource.load()  returns:
#                      raises:
#    Formatter.render() returns:
#                       must not:
#
#  DailyLog HOLDS:
#  DailyLog COMPUTES:
#
#  ERROR POLICY
#    caught and reported  :
#    allowed to propagate :
#
#  If I had to read from a DATABASE instead of a directory,
#  how many classes would change?  ____   (if more than 1, redesign)
#
# =============================================================================

from pathlib import Path

LOG_DIR = Path(__file__).resolve().parents[4] / "2026" / "september" / "daily_progress_tracking"


if __name__ == "__main__":
    from lifelog.models import DailyLog          # noqa
    from lifelog.sources import DirectorySource  # noqa

    source = DirectorySource(LOG_DIR)
    logs = source.load()
    print(f"parsed : {len(logs)}")
    print(f"skipped: {source.skipped}")
    for log in logs[:3]:
        print(" ", repr(log))
