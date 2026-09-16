# Day 55 — SQL Deep Day

|  |  |
|:--|:--|
| **Date** | Monday, 9 November 2026 |
| **Position** | Week 8 · Month 2 · Phase 3 |
| **Budget** | **~150 min** — 🇵🇰 **Iqbal Day. Public holiday, no classes.** |
| **Code file** | `Day_55.sql` |

> **Why today is a SQL day and not a rest day.** You have a free weekday, which happens twice in ninety days. The SQL track has been running 25 minutes at a time since Day 33 — good for retention, not enough for the harder constructs. Today consolidates it and takes you to the level Project 2 needs, starting Day 58.
>
> **This is also the most directly employable block in the challenge.** Entry-level analyst interviews are, more often than not, a SQL screen.

---

## 🎯 Objective

Write multi-step SQL with CTEs and window functions comfortably, and solve interview-style problems without help.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians SQL](https://www.youtube.com/watch?v=p1epCuYb5OQ) · **`3:42:24 → 5:02:00`** · @1.75× | PRIMARY | 45 min | Relationships, joins in depth, views |
| The CTE and pattern sections below | REFERENCE | 20 min | Structuring a query |
| [PostgreSQL Exercises](https://pgexercises.com/) — Joins and Aggregates | **PRACTICE** | 35 min | Harder than SQLBolt, real schema |

**Skip** `0:00 → 0:31` (PostgreSQL installation — you are on SQLite) and `5:09:46 → end` (stored procedures — a database-administration topic, not an analyst one).

### 🟢 IF TIME

- [DataLemur](https://datalemur.com/) free tier — real interview questions from real companies.

---

## 🧠 Core Concepts

### CTEs — how to write a query someone can read

```sql
WITH weekly AS (
    SELECT item, week, AVG(price) AS avg_price
    FROM prices
    GROUP BY item, week
),
with_change AS (
    SELECT *,
           LAG(avg_price) OVER (PARTITION BY item ORDER BY week) AS prev,
           avg_price - LAG(avg_price) OVER (PARTITION BY item ORDER BY week) AS change
    FROM weekly
)
SELECT item, week, avg_price, change
FROM with_change
WHERE change > 0
ORDER BY change DESC;
```

**Three reasons CTEs beat nested subqueries:**

1. **Read top to bottom** instead of inside out. A three-level nested subquery has to be read from the middle.
2. **Each step is named**, so the name documents the intent.
3. **Each step can be tested** — run just the first CTE to check it.

**The rule:** more than one level of nesting, use a CTE. Query readability is not cosmetic — an unreadable query is one the next person rewrites instead of trusting.

### The patterns that come up constantly

**1. Top N per group**
```sql
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY category ORDER BY sales DESC) AS rn
    FROM products
)
SELECT * FROM ranked WHERE rn <= 3;
```

**2. Period-on-period change** — `LAG` over an ordered partition.

**3. Running total**
```sql
SUM(amount) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
```

**4. Find the gaps** — `LEFT JOIN ... WHERE right.id IS NULL`.

**5. Pivot** — conditional aggregation with `CASE WHEN`.

**6. Deduplicate, keeping the latest**
```sql
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY updated_at DESC) AS rn
    FROM customers
)
SELECT * FROM ranked WHERE rn = 1;
```

**These six cover a large share of real analyst SQL and a large share of interview questions.** Being able to write them without thinking is a genuine, marketable skill.

### The things that will trip you up

| Trap | What happens |
|:-----|:-------------|
| `NULL` comparisons | `NULL = NULL` is **not true** — it is `NULL`. Use `IS NULL`. |
| `NOT IN` with a NULL in the list | Returns **no rows at all**. Use `NOT EXISTS`. |
| Aggregates ignore NULLs | `AVG` over 10 values with 3 nulls divides by 7, not 10 |
| `COUNT(*)` vs `COUNT(col)` | Day 34 — they differ whenever there are nulls |
| Integer division | `5/2 = 2` in many engines. Cast one side. |
| `WHERE` on a window function | Not allowed — `SELECT` runs after `WHERE`. Wrap it in a CTE. |

**The `NOT IN` NULL trap is the nastiest**, because it returns an empty result rather than an error and looks like "there is no such data".

---

## 💻 Code

### 🔴 MUST DO — `Day_55.sql` (85 min)

**Consolidation (1–6)** — the six patterns, on your PBS database
1. Top 3 most expensive weeks per item
2. Week-on-week change with `LAG`
3. Running total of the price index over time
4. Items with no observations in a given month — the gap pattern
5. Month-by-band pivot with `CASE WHEN`
6. Deduplicate, keeping the latest observation per item-week

**The traps (7–10)** — reproduce each, then fix it
7. `NULL = NULL` returning nothing
8. `NOT IN` with a NULL — the empty result
9. `AVG` silently skipping NULLs — compare with `COALESCE`
10. Integer division producing 0

**Interview problems (11–15)** — closed book, timed
11. *(5 min)* The second-highest price per item
12. *(8 min)* Items whose price rose for three consecutive weeks
13. *(8 min)* The share each item contributes to total spend, per month
14. *(10 min)* The largest week-on-week jump per item, with the week it happened
15. *(10 min)* A cohort table: by first-observation month, how many items are still present N months later

**Question 15 is the hardest and the most useful** — cohort retention is the single most common analytics question in a real product company, and it is Project 2's core.

### 🟢 IF TIME

- Three DataLemur problems
- Read one of your queries from Day 44 and rewrite it with CTEs

---

## 🔬 Understanding Check

1. **Reasoning.** Name three ways a CTE beats a nested subquery.
2. **Debugging.** Your `NOT IN` returned nothing and you expected rows. What happened, and what is the fix?
3. **Understanding.** Why can you not filter on a window function in `WHERE`? Answer with execution order.
4. **Comparison.** `ROW_NUMBER` vs `RANK` vs `DENSE_RANK` — which for "top 3, no ties"?
5. **Application.** Which of the six patterns will Project 2 need? Name at least three.
6. **Judgement.** `AVG` skipping nulls — when is that what you want, and when is it a silent bug?
7. **Interview.** Explain a window function to someone who knows `GROUP BY` but not windows. 45 seconds.
8. **Self-assessment.** Which of questions 11–15 could you not finish in time? That is your gap.

---

## 🎯 Expected Outcome

- [ ] Structure a multi-step query with CTEs
- [ ] Write all six patterns without reference
- [ ] Recognise the NULL traps
- [ ] Solve an interview-style problem under time pressure

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians SQL `3:42:24 → 5:02:00` @1.75× | 45 min |
| CTEs and patterns | 20 min |
| Consolidation + traps (1–10) | 45 min |
| **Interview problems (11–15), timed** | 40 min |
| Daily review | 5 min |
| **Total** | **~155 min** |

---

## 🧪 Mini Assessment

Questions 11–15, closed book and timed. **Three out of five inside their limits is interview-ready for an entry-level analyst screen.**

---

## 🔁 Daily Review

1. Score on 11–15: ___ / 5. Which ran over?
2. Which of the six patterns is least automatic?
3. Which NULL trap would have cost me the most in real work?
4. **Project 2 starts in three days.** Is my SQL at the level it needs?

---

## 📦 Completion Criteria

- [ ] All six patterns written against real data
- [ ] All four traps reproduced and fixed
- [ ] Questions 11–15 attempted closed-book and timed, scored
- [ ] pgexercises Joins and Aggregates sections complete
- [ ] Committed to git

---

**[← Day 54](../Day_54/Day_54.md)** · **[Day 56 →](../Day_56/Day_56.md)** · [README](../../../README.md)
