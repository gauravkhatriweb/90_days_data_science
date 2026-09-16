"""Output. Contains NO analysis -- every number comes from LogCollection."""
from __future__ import annotations

from abc import ABC, abstractmethod


class Formatter(ABC):
    """Contract: render(collection) -> str, and must not mutate the collection."""

    @abstractmethod
    def render(self, collection) -> str:
        ...


class TextFormatter(Formatter):
    """A human report. Aim for something you would actually want to read."""

    def render(self, collection) -> str:
        pass


class JsonFormatter(Formatter):
    """The same FACTS, machine-readable.

    If this is missing a fact the text version has, analysis has leaked
    into presentation. Fix the boundary, not the formatter.
    """

    def render(self, collection) -> str:
        pass
