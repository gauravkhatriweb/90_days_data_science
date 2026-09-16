"""
Project 1 — the final charts.
==============================
Exploratory charts were for you. These are for a stranger with ten seconds.

RULE: if you cannot write the ONE SENTENCE the chart must make the reader
realise, cut the chart.

Each function takes ax=None so it works standalone OR inside a grid --
the axes-level pattern from Day 39, applied to your own code.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid", palette="colorblind", context="talk")


# 1 -- THE SEQUENCE. One sentence per chart. Write these BEFORE coding.
#
#   context_chart    ->
#   headline_chart   ->
#   comparison_chart ->
#   nuance_chart     ->
#
#   WHICH DID I CUT, AND WHY?


def context_chart(df: pd.DataFrame, ax: plt.Axes | None = None) -> plt.Axes:
    """The overall picture. What was happening generally?"""
    pass


def headline_chart(df: pd.DataFrame, ax: plt.Axes | None = None) -> plt.Axes:
    """THE chart this project exists for.

    This one goes at the top of the README and on LinkedIn.
    Spend disproportionate time on it.

      [ ] title states the FINDING
      [ ] axes labelled with units
      [ ] the point is ANNOTATED
      [ ] passes the ten-second test with a real person
    """
    pass


def comparison_chart(df: pd.DataFrame, ax: plt.Axes | None = None) -> plt.Axes:
    """The finding against its comparison. This is what makes it MEAN something."""
    pass


def nuance_chart(df: pd.DataFrame, ax: plt.Axes | None = None) -> plt.Axes:
    """Where it varies, or where it does not hold."""
    pass


def save_all(df: pd.DataFrame, outdir: Path = Path("figures")) -> None:
    """Regenerate every figure. dpi >= 150 -- a blurry chart reads as carelessness."""
    pass


# =============================================================================
# THE TEN-SECOND TEST -- do this with an ACTUAL PERSON
# =============================================================================
#   Who I showed it to:
#   EXACTLY what they said:
#
#   Was that my finding?          yes / no
#   What did they get wrong?
#   What I changed as a result:
# =============================================================================


if __name__ == "__main__":
    print("Write the sentences first. Then build the charts. Then test them on a human.")
