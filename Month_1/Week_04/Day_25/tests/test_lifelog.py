"""
Tests for lifelog.
==================
Rule: write the EMPTY case first for every function.
That single habit catches more real bugs than anything else here.

    pytest -v
    pytest -k streak
    pytest -x
"""
from datetime import date

import pytest

# from lifelog.models    import DailyLog
# from lifelog.sources   import ListSource, DirectorySource
# from lifelog.analysis  import LogCollection


# -----------------------------------------------------------------------------
# helper -- build a DailyLog with no file on disk.
# This is possible ONLY because of the composition design from Day 18.
# -----------------------------------------------------------------------------
def make_log(d: date, raw: str = "## 🏋️ Fitness\nsome content\n"):
    pass


# =============================================================================
# PART B -- ANALYSIS
# =============================================================================

def test_empty_collection_has_no_streak():
    """EMPTY CASE FIRST. Always."""
    pass


def test_single_log_is_a_streak_of_one():
    """A single logged day is a streak of 1, not 0. Off-by-one lives here."""
    pass


def test_gap_breaks_the_streak():
    pass


def test_all_consecutive_is_one_long_streak():
    pass


def test_duplicate_dates_do_not_inflate_the_streak():
    """Two logs on the same date must not count as two consecutive days."""
    pass


def test_unsorted_input_still_finds_the_streak():
    """longest_streak must not assume the input is sorted."""
    pass


def test_missing_dates_empty_collection():
    pass


def test_missing_dates_no_gaps():
    pass


def test_missing_dates_finds_a_one_day_gap():
    pass


def test_filter_no_matches_returns_empty_collection():
    """Must return a LogCollection, NOT a list. Assert the type."""
    pass


def test_filter_boundary_dates():
    """Are start and end inclusive? DECIDE, document it, then test it."""
    pass


def test_section_frequency_counts_repeats():
    pass


def test_len_and_contains_and_getitem():
    """Include a NEGATIVE index."""
    pass


# =============================================================================
# PART C -- PARSING
# =============================================================================

def test_from_path_rejects_a_bad_filename():
    """Right exception type, and a message that names the file."""
    pass


def test_from_path_rejects_an_impossible_date():
    """2026-09-31 is not a real date."""
    pass


def test_empty_file_is_empty():
    pass


def test_headings_with_no_body_is_empty():
    """NO RIGHT ANSWER until you choose one.
    MY DECISION:
    WHY:
    """
    pass


def test_directory_source_reports_what_it_skipped(tmp_path):
    """Two valid files, two invalid. Expect 2 loaded and 2 skipped WITH REASONS."""
    pass


# =============================================================================
# PART D -- THE PAYOFF
# =============================================================================
#  First full run:
#    tests failed : ____
#    real bugs    : ____
#
#  For each bug: WOULD I HAVE FOUND THIS WITHOUT THE TEST?
#    1.
#    2.
#
#  Then: plant a bug deliberately and confirm a test catches it.
#  A test that cannot fail is not a test.
# =============================================================================
