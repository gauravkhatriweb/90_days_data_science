"""DailyLog -- one log file, parsed."""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

FILENAME_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-daily-log\.md$")


class DailyLog:
    """One daily log file.

    Attributes : date, path, raw, sections
    Properties : word_count, is_empty, weekday
    Dunders    : __repr__, __len__
    """

    def __init__(self, log_date: date, path: Path, raw: str):
        pass

    # --- alternative constructor ------------------------------------------
    @classmethod
    def from_path(cls, path: Path) -> "DailyLog":
        """Parse the date out of the filename and read the file.

        Raise ValueError with a message naming the file if the name does not
        match YYYY-MM-DD-daily-log.md, or if the date is not a real date
        (watch for 2026-09-31).

        WHY IS THIS A classmethod RATHER THAN LOGIC IN __init__?
        ANSWER:
        """
        pass

    # --- parsing ----------------------------------------------------------
    @staticmethod
    def _split_sections(raw: str) -> dict[str, str]:
        """Split on '## ' headings -> {heading_text: body}.

        Watch out: headings contain emoji, and '###' is not '##'.
        """
        pass

    # --- properties -------------------------------------------------------
    @property
    def word_count(self) -> int:
        pass

    @property
    def is_empty(self) -> bool:
        """A log with headings but no content underneath is still empty."""
        pass

    @property
    def weekday(self) -> str:
        pass

    # --- dunders ----------------------------------------------------------
    def __repr__(self) -> str:
        pass

    def __len__(self) -> int:
        pass
