"""LogCollection -- many logs, and the questions you can ask about them.

Contains NO formatting. Not one f-string that builds a report line.
"""
from __future__ import annotations

from datetime import date, timedelta


class LogCollection:
    """A set of DailyLog objects, with queries over them."""

    def __init__(self, logs):
        pass

    @classmethod
    def from_source(cls, source):
        """Build from any LogSource. Note it does not care which kind."""
        pass

    # --- behave like a collection -----------------------------------------
    def __len__(self): pass
    def __getitem__(self, i): pass
    def __iter__(self): pass
    def __contains__(self, d: date): pass
    def __repr__(self): pass

    # --- properties --------------------------------------------------------
    @property
    def date_range(self) -> tuple[date, date] | None:
        """(earliest, latest). None if empty."""
        pass

    @property
    def total_words(self) -> int:
        pass

    @property
    def missing_dates(self) -> list[date]:
        """Every date between first and last with no log.

        Do NOT assume the logs are sorted, or that dates are unique.
        """
        pass

    # --- queries -----------------------------------------------------------
    def longest_streak(self) -> tuple[date, date, int] | None:
        """Longest run of consecutive logged days.

        OFF-BY-ONE LIVES HERE. Hand-check one month before trusting it.
        A single logged day is a streak of 1, not 0.
        """
        pass

    def section_frequency(self) -> dict[str, int]:
        """How often each '## ' heading appears across all logs."""
        pass

    def by_weekday(self) -> dict[str, int]:
        """Logs per weekday name. Which day do you actually log?"""
        pass

    def longest(self, n=5): pass
    def shortest(self, n=5): pass

    def filter(self, start: date, end: date) -> "LogCollection":
        """Return a NEW LogCollection.

        WHY A LogCollection AND NOT A LIST?
        ANSWER:
        """
        pass
