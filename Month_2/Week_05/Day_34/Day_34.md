# Day 34 — GroupBy: The Operation You Will Use Most

|  |  |
|:--|:--|
| **Date** | Monday, 19 October 2026 |
| **Position** | Week 5 · Month 2 · Phase 2 |
| **Budget** | **~75 min** (50 Pandas + 25 SQL) |
| **Code files** | `Day_34.py` · `Day_34.sql` |

> **Why groupby gets its own day.** Split-apply-combine is the single most common operation in analytics, and you have now met it three times under three names: `itertools.groupby` on Day 26, `pandas.groupby` today, and `GROUP BY` in SQL in the same session. **One concept, three syntaxes.** Learning it once, deliberately, is worth more than meeting it three times accidentally.

---

## 🎯 Objective

Aggregate by group fluently in both Pandas and SQL, and recognise that they are the same operation.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Pandas](https://www.youtube.com/watch?v=QUaSmqBeR9w) · **`57:46 → 1:08:02`** · @1.5× | PRIMARY | 7 min | GroupBy operations |
| The split-apply-combine section below | REFERENCE | 12 min | The model |
| [SQLBolt lessons 9–10](https://sqlbolt.com/) | **PRACTICE** | 15 min | `GROUP BY`, `HAVING`, aggregates |

---

## 🧠 Core Concepts

### Split — apply — combine

```python
df.groupby("region")["revenue"].sum()
```

1. **Split** the rows into groups by `region`
2. **Apply** `sum` to `revenue` within each group
3. **Combine** the results into one Series, indexed by region

That is the whole model. Everything else is variation.

```python
df.groupby("region")["revenue"].sum()                      # one column, one function
df.groupby("region")[["revenue", "qty"]].mean()            # several columns
df.groupby(["region", "item"])["revenue"].sum()            # several keys -> MultiIndex
df.groupby("region").agg(
    total=("revenue", "sum"),
    avg_price=("price", "mean"),
    n=("item", "count"),
)                                                           # named aggregation
df.groupby("region")["revenue"].transform("mean")           # BROADCAST BACK to rows
df.groupby("region").filter(lambda g: len(g) > 10)          # keep whole groups
```

### `agg` vs `transform` vs `filter` — the distinction people miss

| | Returns | Use for |
|:--|:--|:--|
| `agg` | **One row per group** | "Total revenue per region" |
| `transform` | **Same shape as the input** | "This row's revenue as a share of its region's total" |
| `filter` | A subset of the original rows | "Only regions with more than 10 transactions" |

**`transform` is the one worth internalising.** Comparing each row against its own group's statistic — a price against its region's average, a student against their class mean — is an extremely common question, and without `transform` people write a merge or a loop.

```python
df["vs_region_avg"] = df["price"] - df.groupby("region")["price"].transform("mean")
```

One line. No merge. This is also exactly what a SQL window function does — and you meet those on Day 52.

### Two behaviours that cause bugs

**`dropna=True` is the default.** Rows where the grouping key is `NaN` are **silently dropped**. If 8% of your rows have no region, they vanish from a regional breakdown and the totals will not add up. Pass `dropna=False` when you want to see them.

**`as_index=True` is the default.** The grouping key becomes the index, not a column. That is why `df.groupby("region").sum()["region"]` raises `KeyError` — region is the index now. Either use `.reset_index()` or pass `as_index=False`.

### The same thing in SQL

```sql
SELECT region, SUM(revenue) AS total
FROM sales
GROUP BY region
HAVING SUM(revenue) > 100000
ORDER BY total DESC;
```

| Pandas | SQL |
|:-------|:----|
| `df[df.qty > 0]` before grouping | `WHERE qty > 0` |
| `.groupby("region")` | `GROUP BY region` |
| `.agg(total=("revenue","sum"))` | `SUM(revenue) AS total` |
| `.query("total > 100000")` after | `HAVING SUM(revenue) > 100000` |

**`WHERE` filters rows before grouping; `HAVING` filters groups after.** That is the whole difference, it follows directly from Day 33's execution order, and it is asked in most SQL interviews.

### The `COUNT` trap

```sql
COUNT(*)           -- every row in the group
COUNT(column)      -- rows where `column` IS NOT NULL
COUNT(DISTINCT c)  -- distinct non-null values
```

`COUNT(*)` and `COUNT(column)` differ whenever the column has nulls — and that difference has produced a lot of wrong dashboards.

---

## 💻 Code

### 🔴 MUST DO — Pandas (`Day_34.py`, 35 min)

1. Group PBS data by item; get mean, min, max and count of price
2. Group by two keys; then flatten the MultiIndex with `reset_index`
3. Named aggregation — build a summary table with four differently-named metrics
4. `transform` — add a column comparing each price to its item's average
5. `filter` — keep only items with at least 40 observations
6. **The `dropna` trap:** group on a column with NaN keys. Compare `dropna=True` and `False`. Check whether the totals still add up.
7. **The `as_index` trap:** trigger the `KeyError`, then fix it two ways
8. Group by a time period — `df.groupby(df.date.dt.to_period("M"))`
9. `agg` with a custom lambda: the range (max − min) per item
10. `value_counts` versus `groupby().size()` — produce the same answer both ways and say when you would use each

### 🔴 MUST DO — SQL (`Day_34.sql`, 25 min)

11. SQLBolt lessons 9–10
12. `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` over your prices table
13. `GROUP BY` one column, then two
14. `HAVING` — groups above a threshold
15. **`WHERE` vs `HAVING`:** write a query needing both, and explain in a comment why each clause is where it is
16. **The `COUNT` trap:** `COUNT(*)` vs `COUNT(column)` on a column with nulls. Explain the difference.
17. **The comparison:** the same group-and-aggregate question in Pandas and SQL, side by side

---

## 🔬 Understanding Check

1. **Understanding.** Explain split-apply-combine in one sentence, without using the words "group by".
2. **Comparison.** `agg` vs `transform` — what shape does each return, and when do you want each?
3. **Debugging.** Your regional totals do not add up to the overall total. What is the most likely cause?
4. **Debugging.** `df.groupby("region").sum()["region"]` raises `KeyError`. Why?
5. **SQL.** `WHERE` vs `HAVING` — state the difference, and connect it to Day 33's execution order.
6. **SQL.** When do `COUNT(*)` and `COUNT(column)` differ? Give a case where using the wrong one produces a wrong business number.
7. **Connection.** `itertools.groupby` (Day 26), `pandas.groupby`, SQL `GROUP BY`. What do all three share, and what does `itertools.groupby` require that the other two do not?
8. **Project.** What does grouping your PBS data by item and by month reveal that the raw table did not?

---

## 🎯 Expected Outcome

- [ ] Group, aggregate and name the results without looking it up
- [ ] Choose between `agg`, `transform` and `filter` correctly
- [ ] Avoid the `dropna` and `as_index` traps
- [ ] Write `GROUP BY` with `HAVING` and explain the execution order

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians GroupBy @1.5× | 7 min |
| Split-apply-combine | 12 min |
| Pandas exercises 1–10 | 30 min |
| **SQL: SQLBolt 9–10 + exercises 11–17** | 25 min |
| Daily review | 6 min |
| **Total** | **~80 min** |

---

## 🧪 Mini Assessment

Six minutes, closed book. From your PBS data produce one table with, per item: mean price, price range, number of observations, and the percentage change from the first to the last period — and **exclude items with fewer than 20 observations.**

Then write the same thing in SQL.

---

## 🔁 Daily Review

1. Exercise 6: did the totals still add up with `dropna=True`? How would I have caught that in real work?
2. Which of `agg` / `transform` / `filter` do I most expect to forget? Write its shape down.
3. `WHERE` vs `HAVING` — can I explain it from execution order rather than from memory?
4. Grouping my PBS data by month: what did I see?

---

## 📦 Completion Criteria

- [ ] Ten Pandas exercises on real PBS data
- [ ] Both traps reproduced and fixed
- [ ] SQLBolt 9–10 complete
- [ ] Seven SQL exercises working
- [ ] The `COUNT` difference demonstrated on real nulls
- [ ] Mini assessment done in both tools
- [ ] Committed to git

---

**[← Day 33](../Day_33/Day_33.md)** · **[Day 35 →](../Day_35/Day_35.md)** · [README](../../../README.md)
