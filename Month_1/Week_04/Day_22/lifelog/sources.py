"""Where logs come from. Swappable -- that is the whole design."""
from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from .models import DailyLog


class LogSource(ABC):
    """Any source of DailyLog objects.

    Contract:
      load()   -> list[DailyLog], possibly empty, never None
      skipped  -> list[(name, reason)] for anything it could not parse
    """

    @abstractmethod
    def load(self) -> list[DailyLog]:
        ...

    @property
    @abstractmethod
    def describe(self) -> str:
        """One line naming where the data came from, for the report header."""


class DirectorySource(LogSource):
    """Every *-daily-log.md in a directory.

    Must NOT crash on a bad filename or an unreadable file.
    Must RECORD what it skipped and why -- silence is the Day 9 anti-pattern.
    """

    def __init__(self, directory: Path):
        pass

    def load(self) -> list[DailyLog]:
        pass

    @property
    def describe(self) -> str:
        pass


class ListSource(LogSource):
    """DailyLog objects handed in directly. Exists so tests need no files.

    This is the concrete payoff of composition from Day 18 -- on Day 25 you
    will test the whole pipeline without touching the filesystem.
    """

    def __init__(self, logs: list[DailyLog]):
        pass

    def load(self) -> list[DailyLog]:
        pass

    @property
    def describe(self) -> str:
        pass
