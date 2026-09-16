# Day 41 — The Cleaning Pipeline

|  |  |
|:--|:--|
| **Date** | Monday, 26 October 2026 |
| **Position** | Week 6 · Month 2 · Phase 2 |
| **Budget** | **~75 min** (50 project + 25 SQL) |
| **Code files** | `project_1/src/clean.py` · `Day_41.sql` |
| **Project** | 📊 **P1 — cleaning, done properly** |

> **Why cleaning is a module and not a notebook cell.** So far your cleaning lives in scattered notebook cells, in an order only you remember. That is fine while exploring and useless afterwards: it cannot be tested, cannot be rerun on new data, and cannot be reviewed. Today it becomes `src/clean.py` — a function that takes a raw file and returns clean data plus a report of what it did.
>
> **The report is the point.** A cleaning step that silently drops 400 rows is indistinguishable from a bug. One that says "dropped 412 rows: 380 with no price, 32 with impossible dates" is evidence.

---

## 🎯 Objective

Turn exploratory cleaning into a reproducible, testable, self-documenting pipeline.

---

## 📚 Learn

### 🔴 MUST DO — the pattern

**Every step returns data *and* a record of what it did:**

```python
def clean(raw: pd.DataFrame) -> tuple[pd.DataFrame, CleaningReport]:
    report = CleaningReport(rows_in=len(raw))
    df = raw.copy()

    df, n = _standardise_columns(df);   report.log("columns renamed", n)
    df, n = _coerce_numeric(df);        report.log("prices coerced to NaN", n)
    df, n = _parse_dates(df);           report.log("dates unparseable", n)
    df, n = _canonicalise_items(df);    report.log("item names collapsed", n)
    df, n = _drop_impossible(df);       report.log("impossible rows dropped", n)
    df, n = _handle_missing(df);        report.log("missing prices filled", n)

    report.rows_out = len(df)
    return df, report
```

**Five properties this has that notebook cells do not:**

1. **Ordered** — the sequence is explicit and cannot be run out of order by accident
2. **Testable** — each `_step` is a function with an input and an output
3. **Reportable** — every decision produces a number
4. **Reproducible** — one call, from raw file to clean data
5. **Reviewable** — someone can read the order and disagree with it

### Order matters

| Step | Why here |
|:-----|:---------|
| 1. Standardise column names | Everything after depends on knowing what columns are called |
| 2. Coerce types | Cannot filter on a number that is still a string |
| 3. Parse dates | Cannot sort or resample without them |
| 4. Canonicalise categories | Must happen **before** grouping, or "Lahore" and "lahore" are two groups |
| 5. Drop impossible rows | After types — you cannot detect a negative price in a string column |
| 6. Handle missing | **Last** — earlier steps create NaN via coercion, and you want to decide about all of it at once |

Doing 6 before 2 is the classic mistake: you fill the missing values, *then* coercion creates new ones, and your "no missing data" check passes on data that has missing data.

### Raw data is immutable

```
data/raw/        <- never edited, never overwritten. Downloaded, then read-only.
data/processed/  <- output of the pipeline. Deletable and regenerable at any time.
```

If `processed/` is destroyed you rerun the pipeline. If `raw/` is destroyed you download again. **You should never be afraid to delete `processed/`** — and if you are, it means a cleaning step exists only in your head.

---

## 💻 Code

### 🔴 MUST DO — the pipeline (50 min)

Build `project_1/src/clean.py`:

1. `CleaningReport` — a small class that accumulates `(step, count, note)` and renders a readable summary. **You built exactly this class on Days 15–23** — this is that skill, on your own project.
2. `_standardise_columns` — lowercase, underscore, strip the BOM *(Day 11's `﻿`)*
3. `_coerce_numeric` — `errors="coerce"`, return how many became NaN
4. `_parse_dates` — handle the formats you actually found, count failures
5. `_canonicalise_items` — a lookup for the spellings you found on Day 39
6. `_drop_impossible` — negatives, zeros, dates outside the range. **Return the dropped rows**, not just the count, so they can be inspected.
7. `_handle_missing` — the strategy you decided on Day 33, and the reason in the docstring
8. `clean(raw)` — compose them, return `(df, report)`
9. Run it end to end. Save to `data/processed/`.
10. **Print the report.** Does every number make sense? Anything surprising is a bug or a finding.
11. **Four tests** in `tests/test_clean.py` — including one for the empty DataFrame *(Day 25's rule)*

### 🔴 MUST DO — SQL (`Day_41.sql`, 25 min)

12. Subqueries in `WHERE` — items priced above the overall average
13. Subqueries in `FROM` — a derived table
14. Correlated subquery — each item's price against its own category average
15. `EXISTS` and `NOT EXISTS`
16. **The comparison:** the same question via subquery and via `JOIN`. Which reads better?

---

## 🔬 Understanding Check

1. **Reasoning.** Why must missing-value handling come after type coercion?
2. **Application.** Why does `_drop_impossible` return the dropped rows rather than just a count?
3. **Design.** `CleaningReport` is a class you designed in the OOP block. What would this look like without it?
4. **Reasoning.** Why is raw data read-only? What does that guarantee?
5. **SQL.** What makes a correlated subquery different from a plain one? Why is it usually slower?
6. **Comparison.** Exercise 16: subquery or join? Does the answer depend on the reader or on the engine?
7. **Judgement.** Your report says 412 rows dropped out of 5,200 — 8%. Is that acceptable? What would you need to know to decide?

---

## 🎯 Expected Outcome

- [ ] A cleaning pipeline that runs from raw file to processed data in one call
- [ ] Every step reporting what it did, in numbers
- [ ] Tests covering the pipeline, including the empty case
- [ ] Subqueries written from memory

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Read the pattern | 10 min |
| Build the pipeline (1–11) | 40 min |
| **SQL: subqueries** | 25 min |
| Daily review | 5 min |
| **Total** | **~80 min** |

---

## 🧪 Mini Assessment

Delete `data/processed/` entirely. Rerun the pipeline. **Do you get identical output?** If not, a cleaning step exists only in a notebook cell — find it and move it in.

---

## 🔁 Daily Review

1. What percentage of rows did cleaning remove? Is that defensible?
2. Did anything in the report surprise me? Bug or finding?
3. Did the delete-and-rerun test pass on the first attempt?
4. Which cleaning decision am I least confident about? *(Write it in the README on Day 45 — stated uncertainty is credibility, not weakness.)*

---

## 📦 Completion Criteria

- [ ] `src/clean.py` runs end to end
- [ ] Every step reports counts
- [ ] Dropped rows are inspectable, not just counted
- [ ] Four tests pass, including the empty case
- [ ] `data/processed/` regenerable from scratch, identically
- [ ] The cleaning log written in `NOTES.md`
- [ ] Five SQL subquery exercises working
- [ ] Committed to git

---

**[← Day 40](../Day_40/Day_40.md)** · **[Day 42 →](../Day_42/Day_42.md)** · [README](../../../README.md)
