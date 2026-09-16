"""
Project P0 — lifelog, build 2 of 3
===================================
Analysis layer + output layer, cleanly separated.

THE RULE: LogCollection contains zero formatting.
          Formatters contain zero analysis.
If a formatter is computing a streak, the boundary is wrong.
"""
from pathlib import Path

LIFEOS = Path(__file__).resolve().parents[4]
ALL_LOG_DIRS = sorted(LIFEOS.glob("2026/*/daily_progress_tracking"))


if __name__ == "__main__":
    from lifelog.sources import DirectorySource
    from lifelog.analysis import LogCollection
    from lifelog.formatters import TextFormatter, JsonFormatter

    logs = []
    for d in ALL_LOG_DIRS:
        logs.extend(DirectorySource(d).load())

    collection = LogCollection(logs)
    print(TextFormatter().render(collection))
    print()
    print(JsonFormatter().render(collection))

    # THE BOUNDARY TEST: do both contain the same FACTS?
    # If JSON is missing something text has, analysis has leaked into presentation.
