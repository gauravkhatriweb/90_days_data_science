# Week 5 Review — NumPy, Pandas, and SQL Begins

|  |  |
|:--|:--|
| **Covers** | Days 29–35 · 14–20 October 2026 |
| **Topics** | Arrays · vectorisation · broadcasting · DataFrames · missing data · dtypes · groupby · SQL basics |
| **Budget** | 45–60 min |
| **Also this week** | 📊 Project 1 acquisition · 🗄️ SQL track started Day 33 |

> Closed book unless stated.

---

## ⏸️ Catch-Up Rights

| Day | Done? | If not — MUST DO only |
|:---:|:-----:|:----------------------|
| 29 · NumPy arrays | ☐ | Exercises 1, 6, 10, 11 |
| 30 · Vectorisation | ☐ | Exercises 5, 7, 8 — axis and broadcasting |
| 31 · Aggregation, masking | ☐ | Exercises 2, 5, 9 |
| 32 · Pandas + P1 acquisition | ☐ | **The acquisition. Do not skip it** — Days 39–45 all depend on having data. |
| 33 · Missing data + SQL start | ☐ | Exercises 1–6 and SQLBolt 1–4 |
| 34 · GroupBy | ☐ | Exercises 3, 4, 6 and the SQL `GROUP BY` |
| 35 · Consolidation | ☐ | The twelve retrieval tasks |

---

## 📝 Part 1 — Knowledge (closed book, 15 min)

1. Why is a NumPy array faster than a Python list? Answer in terms of memory layout.
2. State the axis rule in your own words.
3. `(3,4)` and `(3,)` do not broadcast; `(3,4)` and `(4,)` do. Explain using the rules.
4. Why is `np.nan != np.nan`, and how do you test for it?
5. Why does Pandas align Series on index rather than position?
6. `loc` vs `iloc` — two differences, including slice ends.
7. What is the difference between MCAR and MNAR, and why does it change what you may do?
8. `agg` vs `transform` — what shape does each return?
9. `WHERE` vs `HAVING` — explain from execution order.
10. When do `COUNT(*)` and `COUNT(column)` differ?

**Score: ___ / 10**

---

## 💻 Part 2 — Coding (closed book, 20 min)

**Task A — 5 min.** A `(100,5)` array with NaN: per-column means ignoring missing, plus the missing count per column, plus the row index of the maximum in column 2.

**Task B — 5 min.** Load a CSV, coerce a numeric column, parse dates, report how many values were coerced.

**Task C — 5 min.** `groupby().agg()` with three named metrics, then `transform` to add a per-group comparison column.

**Task D — 5 min.** SQL: group, aggregate, filter groups with `HAVING`, order, limit.

**Score: ___ / 4**

---

## 🧩 Part 3 — Problem Solving (open book, 10 min)

> A 400 MB CSV of daily retail transactions. `price` is a string with currency symbols and thousands separators. `date` uses two different formats. 7% of `region` values are missing, and they are **not** missing at random — one city's system failed for three weeks.
>
> Write the **plan**: load, diagnose, decide on each problem, and produce revenue per region per month. State specifically what you will do about the non-random missingness, and what you will have to say about it in the final report.

That last sentence is the whole exercise.

---

## 🔁 Part 4 — Retention Check

- [ ] I predict view-vs-copy correctly in NumPy
- [ ] I write array expressions instead of loops by default
- [ ] I can state the axis rule without looking
- [ ] I run the five-line inspection ritual on every dataset automatically
- [ ] I reach for `errors="coerce"` without thinking
- [ ] I recognise `SettingWithCopyWarning` and know both fixes
- [ ] I can write `groupby().agg()` with named outputs from memory
- [ ] I can write a `GROUP BY` with `HAVING` from memory

> Weak this week: ______________________________________________

---

## 📊 Part 5 — Project 1 Checkpoint

| | Status |
|:--|:--|
| Raw data on disk, unmodified | ☐ |
| `SOURCES.md` complete (URL, date, coverage) | ☐ |
| At least one file loads | ☐ |
| Three answerable questions written | ☐ |
| One honest limitation written | ☐ |
| Missingness classified (MCAR / MAR / MNAR) | ☐ |

**The honest question:** is this data good enough for a portfolio project? If not, **now** is the time to find more or change the question — not on Day 43.

> ______________________________________________

---

## 🗄️ Part 6 — SQL Track

| | |
|:--|:--|
| SQLBolt lessons complete | ___ / 18 |
| Can write `SELECT … WHERE … ORDER BY` from memory | ☐ |
| Can write `GROUP BY … HAVING` from memory | ☐ |
| Understand execution order well enough to explain the alias question | ☐ |

**The pace check:** 25 minutes on ~4 days a week gets you to interview-competent SQL by Day 64. Is that holding, or is SQL the block that gets dropped when the day is short? If it is being dropped, move it to the *start* of the session rather than the end.

---

## 🎓 Part 7 — University Link

- **CIS 105** covers spreadsheet analysis. Anything from this week that overlaps?
- **MAT 265:** Chapter 1 is done. Is the maths track due to resume on Day 46 as planned?
- Is the weekday budget still holding, four weeks into semester?

---

## 🔮 Part 8 — The Decision

| If… | Then… |
|:----|:------|
| Part 1 ≥ 7, Part 2 ≥ 3, data acquired | ✅ Continue. Week 6 as written. |
| Data not acquired | 🛑 **Fix this first.** Move Day 36's Pandas work to IF TIME and spend the MUST DO block on acquisition. Days 39–45 cannot start without data. |
| Part 2 ≤ 2 | ⚠️ Add a 15-minute Pandas warm-up to Days 36–38. |
| SQL being skipped | 🔧 Move SQL to the front of the session. 25 minutes at the start beats 0 minutes at the end. |
| All comfortable | ⏩ Add SQLBolt 11–12 (joins) early. |

**My decision:**

> ______________________________________________

---

## 📊 Week 5 Scorecard

| Measure | Result |
|:--------|:-------|
| Days completed | ___ / 7 |
| Part 1 — knowledge | ___ / 10 |
| Part 2 — coding | ___ / 4 |
| Day 35 retrieval | ___ / 12 |
| Retention boxes | ___ / 8 |
| SQLBolt lessons | ___ |
| P1 data acquired | ☐ |
| Honest hours | ___ h |
| **Biggest weakness** | |
| **Biggest win** | |

---

**[← Day 35](./Day_35/Day_35.md)** · **[Day 36 →](../Week_06/Day_36/Day_36.md)** · [README](../../README.md)
