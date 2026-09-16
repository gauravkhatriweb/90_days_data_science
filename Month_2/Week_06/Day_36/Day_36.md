# Day 36 — Joins: Combining Tables

|  |  |
|:--|:--|
| **Date** | Wednesday, 21 October 2026 |
| **Position** | Week 6 · Month 2 · Phase 2 |
| **Budget** | **~75 min** (50 Pandas + 25 SQL) |
| **Code files** | `Day_36.py` · `Day_36.sql` |

> **Why joins get a full day in both tools at once.** Real analysis almost never happens on one table — prices are in one file, item categories in another, regional populations in a third. And joins are where analysts silently lose or duplicate rows. **Learning the same concept in Pandas and SQL on the same day makes the shared model obvious**, and the model is what stops the row-count bugs.

---

## 🎯 Objective

Combine tables correctly, and always know how many rows you should have afterwards.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Pandas](https://www.youtube.com/watch?v=QUaSmqBeR9w) · **`45:33 → 57:46`** · @1.5× | PRIMARY | 8 min | Joining datasets |
| The join-type table and the row-count rule below | REFERENCE | 15 min | The part that prevents bugs |
| [SQLBolt lessons 6–8](https://sqlbolt.com/) | **PRACTICE** | 20 min | `INNER JOIN`, `LEFT JOIN`, nulls from joins |

---

## 🧠 Core Concepts

### The four joins

| Join | Keeps | Use when |
|:-----|:------|:---------|
| `inner` | Only keys present in **both** | You need complete records — **and you must accept losing rows** |
| `left` | All of the left, matched from the right | **The default in analysis.** Keep your data, enrich it. |
| `right` | All of the right | Rare — swap the tables and use `left` |
| `outer` | Everything from both | Reconciliation: "what is in one and not the other?" |

```python
pd.merge(prices, categories, on="item", how="left")
pd.merge(a, b, left_on="item_code", right_on="code", how="left")
pd.merge(a, b, on=["item", "month"], how="left")     # composite key
a.join(b)                                             # joins on the INDEX
pd.concat([a, b], axis=0)                             # stack rows, not a join
```

**`merge` combines on values; `concat` stacks.** Reaching for `concat` when you meant `merge` produces a taller table full of NaN, and it is a surprisingly common mistake.

### The row-count rule — the most important thing on this page

**Before every join, predict the row count. After every join, check it.**

```python
before = len(prices)
merged = prices.merge(categories, on="item", how="left")
print(f"{before} -> {len(merged)}")
```

| Relationship | Expected after a left join |
|:-------------|:---------------------------|
| **one-to-one** | Exactly the same |
| **many-to-one** | Exactly the same |
| **one-to-many** | **More rows** — one per match |
| **many-to-many** | **Multiplies.** 3 matching × 4 matching = 12 rows. |

**The silent disaster:** your right-hand table has a duplicate key you did not know about. The join doubles those rows. Your revenue total is now wrong, nothing errored, and the number is plausible enough that nobody notices.

```python
categories["item"].duplicated().sum()     # check BEFORE joining
merged = prices.merge(categories, on="item", how="left", validate="many_to_one")
```

**`validate=` is the habit worth building.** It raises if the relationship is not what you claimed. `"one_to_one"`, `"one_to_many"`, `"many_to_one"`, `"many_to_many"`. One argument, and it converts a silent wrong answer into a loud error.

### `indicator=True` — how many actually matched

```python
merged = a.merge(b, on="item", how="left", indicator=True)
merged["_merge"].value_counts()
# both       1180
# left_only    60     <- 60 items had no category. Is that expected?
```

The answer to "is that expected?" is the analysis. Sixty unmatched items might be new products, or a spelling inconsistency, or a join key that is subtly wrong — and you cannot tell without looking.

### The same thing in SQL

```sql
SELECT p.item, p.price, c.category
FROM prices p
LEFT JOIN categories c ON p.item = c.item;
```

| Pandas | SQL |
|:-------|:----|
| `how="inner"` | `INNER JOIN` (or just `JOIN`) |
| `how="left"` | `LEFT JOIN` |
| `on="item"` | `ON p.item = c.item` |
| `left_on`/`right_on` | `ON a.x = b.y` |
| `indicator=True` | `WHERE c.item IS NULL` finds the non-matches |

**The `LEFT JOIN … IS NULL` pattern is worth memorising** — it answers "what is in A but not in B?" and it appears in interviews constantly.

> **Note:** SQLite supports `RIGHT JOIN` and `FULL OUTER JOIN` from version 3.39 (2022). If your build is older, swap the table order and use `LEFT JOIN`.

---

## 💻 Code

### 🔴 MUST DO — Pandas (`Day_36.py`, 35 min)

1. Build a small item→category lookup for your PBS items
2. Left join it to the price data. **Predict the row count first.**
3. Compare all four join types on the same pair; record the row count of each
4. `indicator=True` — how many items had no category? Inspect them.
5. **The duplicate-key disaster:** deliberately add a duplicate to the lookup, join, and watch the row count inflate and the total change
6. Add `validate="many_to_one"` and watch it catch the same problem loudly
7. Join on a composite key (item + month)
8. `left_on` / `right_on` with differently named columns
9. `concat` vs `merge` — do the wrong one on purpose and describe the result
10. **Tidy data:** state the three rules, then say whether your PBS data satisfies them

### 🔴 MUST DO — SQL (`Day_36.sql`, 25 min)

11. SQLBolt 6–8
12. `INNER JOIN` two tables
13. `LEFT JOIN`, and find the unmatched rows with `WHERE … IS NULL`
14. Join three tables in one query
15. `JOIN` with `GROUP BY` — revenue per category
16. **Row-count check in SQL:** count before and after, and explain any difference

---

## 🔬 Understanding Check

1. **Reasoning.** Why is `left` the usual default in analysis rather than `inner`?
2. **Debugging.** After a join your revenue total doubled. What happened, and what would have caught it?
3. **Application.** What does `validate="many_to_one"` check, and why is it better than checking afterwards?
4. **Comparison.** `merge` vs `concat` — when is each right?
5. **SQL.** Write the `LEFT JOIN … IS NULL` pattern and say what question it answers.
6. **Understanding.** Sixty items have no category after your join. Name three possible causes and how you would tell them apart.
7. **Connection.** Pandas `merge` and SQL `JOIN` — what is genuinely the same, and what differs?
8. **Project.** Do you need a join for Project 1? If yes, which tables, and what relationship?

---

## 🎯 Expected Outcome

- [ ] Choose the right join type by reasoning about what you must not lose
- [ ] Predict and verify row counts on every join
- [ ] Use `validate` and `indicator` as habits
- [ ] Write inner and left joins in SQL from memory

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians joins @1.5× | 8 min |
| Join types + the row-count rule | 15 min |
| Pandas exercises 1–10 | 27 min |
| **SQL: SQLBolt 6–8 + exercises 11–16** | 25 min |
| Daily review | 5 min |
| **Total** | **~80 min** |

---

## 🧪 Mini Assessment

Six minutes, closed book. Three tables — transactions, items, regions. Produce revenue per region per category, keeping every transaction even where the item or region lookup is missing, and report how many transactions had no match on each side.

---

## 🔁 Daily Review

1. Exercise 5: how much did the total change with the duplicate key? Would I have noticed in real work?
2. Did I predict the row count correctly on every join today?
3. Is `validate=` going to become a habit, or will I forget it? *(If the latter — write it into your project's cleaning function now.)*
4. Does Project 1 need a join?

---

## 📦 Completion Criteria

- [ ] All four join types compared with row counts recorded
- [ ] The duplicate-key disaster reproduced, and caught by `validate`
- [ ] `indicator=True` used, unmatched rows inspected
- [ ] SQLBolt 6–8 complete
- [ ] Six SQL exercises working, including `LEFT JOIN … IS NULL`
- [ ] Committed to git

---

**[← Week 5 Review](../../Week_05/Week_05_Review.md)** · **[Day 37 →](../Day_37/Day_37.md)** · [README](../../../README.md)
