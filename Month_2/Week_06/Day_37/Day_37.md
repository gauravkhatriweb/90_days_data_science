# Day 37 — Reshaping: Long, Wide, and Why It Matters

|  |  |
|:--|:--|
| **Date** | Thursday, 22 October 2026 |
| **Position** | Week 6 · Month 2 · Phase 2 |
| **Budget** | **~75 min** (50 Pandas + 25 SQL) |
| **Code files** | `Day_37.py` · `Day_37.sql` |

> **Why reshaping is a real skill, not an API detail.** Your PBS data almost certainly arrives **wide** — one row per item, one column per week. Every plotting library, every statistical test and every machine learning model wants it **long** — one row per observation. Knowing how to move between the two, and *why* each shape exists, saves hours of confusion in every project from here to Day 90.

---

## 🎯 Objective

Move between long and wide formats deliberately, and know which shape each downstream task needs.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Pandas](https://www.youtube.com/watch?v=QUaSmqBeR9w) · **`1:08:02 → 1:17:20`** · @1.5× | PRIMARY | 6 min | Pivot tables and crosstabs |
| The long/wide section below | REFERENCE | 18 min | The reasoning |
| [SQLBolt lessons 11–12](https://sqlbolt.com/) | PRACTICE | 20 min | Queries with expressions, and `INSERT`/`UPDATE` |

---

## 🧠 Core Concepts

### Long versus wide

**Long (tidy)** — one row per observation:

| date | item | price |
|:--|:--|--:|
| 2026-01-07 | tea | 1250 |
| 2026-01-07 | sugar | 180 |
| 2026-01-14 | tea | 1265 |

**Wide** — one row per subject, one column per variable:

| date | tea | sugar |
|:--|--:|--:|
| 2026-01-07 | 1250 | 180 |
| 2026-01-14 | 1265 | 185 |

| | Long is better for | Wide is better for |
|:--|:--|:--|
| | Plotting (Seaborn wants long) | Human reading |
| | Statistical tests | Correlation matrices |
| | Machine learning | Row-wise arithmetic across variables |
| | Adding a new item without adding a column | Compact display |

**Neither is correct in the abstract.** The right shape is the one the next step needs — which means you will convert repeatedly, and that is normal rather than a sign you got it wrong earlier.

### The four operations

```python
df.melt(id_vars=["date"], var_name="item", value_name="price")   # wide -> long
df.pivot(index="date", columns="item", values="price")            # long -> wide
df.pivot_table(index="date", columns="item", values="price",
               aggfunc="mean", fill_value=0, margins=True)        # pivot + aggregate
pd.crosstab(df.region, df.category)                                # frequency table
```

**`pivot` vs `pivot_table`:** `pivot` raises if `(index, columns)` is not unique. `pivot_table` aggregates duplicates instead. **The error from `pivot` is useful** — it is telling you your data has duplicates you did not know about. Reaching straight for `pivot_table` hides that.

### `stack` and `unstack` — the index versions

```python
df.stack()      # columns -> index rows  (wider to longer)
df.unstack()    # index rows -> columns  (longer to wider)
```

These operate on the *index* rather than on columns, which makes them the natural partners of a MultiIndex from `groupby(["a","b"])`. `groupby(["region","item"]).sum().unstack()` produces a region-by-item table in one line.

### The three rules of tidy data

1. Each **variable** is a column
2. Each **observation** is a row
3. Each **type of observational unit** is a table

Rule 3 is the one people break. If your table has both item-level and region-level attributes repeated down every row, those are two units and should be two tables joined when needed. *(This is exactly the same reasoning as database normalisation — which is why SQL and tidy data agree.)*

### Where this bites you later

| Day | Needs |
|:---:|:------|
| 39 | Seaborn: long |
| 40 | Correlation matrix: wide |
| 44 | Multi-line time chart: long |
| 74 | scikit-learn: wide, one column per feature |

Knowing which shape each wants — before you start — saves the loop of plotting, getting something wrong, and reshaping.

---

## 💻 Code

### 🔴 MUST DO — Pandas (`Day_37.py`, 35 min)

1. Establish whether your PBS data is long or wide. Print the evidence.
2. `melt` it to long. Verify the row count: `rows × value_columns`.
3. `pivot` it back. Confirm you recovered the original.
4. **Trigger `pivot`'s duplicate error on purpose.** What did it just tell you about your data?
5. `pivot_table` with `aggfunc="mean"` on the same duplicated data — see it aggregate silently instead
6. `pivot_table` with `margins=True` for row and column totals
7. `crosstab` — item category by month, with counts, then with `normalize="index"`
8. `groupby(["a","b"]).sum()` then `.unstack()` — one line to a cross-tabulated table
9. **Shape for purpose:** take one dataset to the exact shape needed for (a) a Seaborn line plot, (b) a correlation matrix, (c) a scikit-learn feature matrix. Three shapes, one dataset.
10. Apply the three tidy rules to your PBS data and state which it breaks

### 🔴 MUST DO — SQL (`Day_37.sql`, 25 min)

11. SQLBolt 11–12
12. `CASE WHEN` — bucket prices into low / medium / high
13. Conditional aggregation — `SUM(CASE WHEN … THEN 1 ELSE 0 END)` as a pivot in SQL
14. `CAST` and date functions — extract year and month
15. `COALESCE` to handle nulls in an aggregation
16. **The comparison:** produce a month-by-item pivot in SQL, then in Pandas. Which was easier, and why?

---

## 🔬 Understanding Check

1. **Comparison.** Long vs wide — name two things each is better for.
2. **Reasoning.** Why is `pivot`'s duplicate error more useful than `pivot_table`'s silent aggregation?
3. **Application.** Exercise 9: which shape does each of the three consumers want, and why?
4. **Understanding.** State the three tidy rules. Which does your PBS data break?
5. **SQL.** How does conditional aggregation work as a pivot? Why is it more awkward than Pandas?
6. **Reasoning.** Why do SQL's normalisation rules and tidy data's rules agree?
7. **Project.** What shape does your PBS data need to be in for Day 39's charts? Is it there yet?

---

## 🎯 Expected Outcome

- [ ] Convert between long and wide in either direction without looking it up
- [ ] Choose `pivot` or `pivot_table` deliberately
- [ ] State which shape each downstream tool needs
- [ ] Pivot in SQL with conditional aggregation

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians pivots @1.5× | 6 min |
| Long/wide + tidy data | 18 min |
| Pandas exercises 1–10 | 28 min |
| **SQL: SQLBolt 11–12 + exercises 12–16** | 25 min |
| Daily review | 5 min |
| **Total** | **~82 min** |

---

## 🧪 Mini Assessment

Five minutes, closed book. From long PBS data produce a wide table of **month × item showing the average price**, with a totals row and column, zeros where there is no data — then melt it back and confirm you lost nothing except the totals.

---

## 🔁 Daily Review

1. Exercise 4: what did the `pivot` error reveal about my data?
2. Which of the three shapes in exercise 9 was hardest to get to?
3. Which tidy rule does my PBS data break, and does that matter for this project?
4. Is my data in the right shape for Day 39? If not, that is tomorrow's IF TIME.

---

## 📦 Completion Criteria

- [ ] Ten Pandas exercises on real data
- [ ] The `pivot` duplicate error triggered and understood
- [ ] All three shapes from exercise 9 produced
- [ ] SQLBolt 11–12 complete
- [ ] A SQL pivot via conditional aggregation working
- [ ] Tidy-rule assessment written in `NOTES.md`
- [ ] Committed to git

---

**[← Day 36](../Day_36/Day_36.md)** · **[Day 38 →](../Day_38/Day_38.md)** · [README](../../../README.md)
