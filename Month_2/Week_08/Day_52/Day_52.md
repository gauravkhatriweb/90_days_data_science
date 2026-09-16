# Day 52 — Confidence Intervals, and Window Functions

|  |  |
|:--|:--|
| **Date** | Friday, 6 November 2026 |
| **Position** | Week 8 · Month 2 · Phase 3 |
| **Budget** | **~75 min** (50 stats + 25 SQL) |
| **Code files** | `Day_52.py` · `Day_52.sql` |
| **Reading** | 📐 **Essential Math Ch. 3, pp. 92–95** |

> **Why confidence intervals matter more than the numbers they surround.** A point estimate is a guess presented as a fact. An interval is an honest statement of what you know. **Reporting intervals is the single habit that most separates a careful analyst from a careless one** — and almost nobody does it.
>
> The SQL half introduces window functions, which are the most useful thing in SQL beyond joins and the thing that most often appears in analyst interviews.

---

## 🎯 Objective

Compute confidence intervals, state precisely what they do and do not mean, and write SQL window functions.

---

## 📚 Learn — Track 1: Confidence intervals (≈ 35 min)

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 3, pp. 92–95** | **PRIMARY** · reading + code | 22 min | Confidence intervals |
| The interpretation section below | REFERENCE | 13 min | What it actually means |

---

## 🧠 Core Concepts

### The construction

```
CI = x̄ ± (critical value) × (σ / √n)
```

Yesterday's standard error, multiplied by how many of them you want to reach out:

| Confidence | z | Meaning |
|:----------:|:--|:--------|
| 90% | 1.645 | narrower, less certain |
| 95% | **1.960** | the convention |
| 99% | 2.576 | wider, more certain |

```python
from scipy import stats
stats.norm.interval(0.95, loc=mean, scale=sem)           # known sigma, large n
stats.t.interval(0.95, df=n-1, loc=mean, scale=sem)      # unknown sigma  <- usually this
```

**You almost always want the t version**, because you almost never know the true σ. Day 54 explains why the t-distribution exists.

### What a 95% confidence interval actually means

**Correct:** *"If I repeated this sampling procedure many times and built an interval each time, about 95% of those intervals would contain the true value."*

**Wrong:** *"There is a 95% probability the true value is in this interval."*

The difference is not pedantry. In the frequentist framework the true value is **fixed** — it is not random, so it has no probability of being anywhere. What is random is **your interval**, because it depends on which sample you happened to draw. The confidence is a property of the *procedure*, not of the particular interval on your screen.

**The honest working interpretation:** *"My method produces intervals that capture the truth 95% of the time, and this is one of them."*

*(The credible interval you computed on Day 47 from the beta distribution **does** support the probability statement — that is the Bayesian framework, and the difference between the two is one of the oldest arguments in statistics. Knowing there are two frameworks, and which one you are in, is worth more than picking a side.)*

### What changes the width

| Change | Effect | Why |
|:-------|:-------|:----|
| More data | **Narrower**, as √n | The SE shrinks |
| More variable data | Wider | Larger σ |
| Higher confidence | Wider | You must reach further to be more sure |

**You cannot have narrow and highly confident on a small sample.** Anyone offering both is doing something wrong, and spotting that is a genuinely useful skill.

### Where you will use it constantly

| Situation | The interval |
|:----------|:-------------|
| "Average order is PKR 2,400" | 2,400 ± 200 — and now it is a claim |
| "The model is 94% accurate" | 94% ± 3% on 400 test cases — **Day 76** |
| "B converts better than A" | Do the intervals overlap? — **Day 54** |
| "Prices rose 11%" | With what uncertainty? |

**The overlap check is the practical one.** If two intervals overlap substantially, you cannot claim a difference. That single check prevents most of the false conclusions in business analytics.

---

## 🗄️ Learn — Track 2: Window functions (25 min)

The most useful SQL beyond joins, and a standard interview topic.

```sql
SELECT
    item, week, price,
    AVG(price)  OVER (PARTITION BY item)                      AS item_avg,
    LAG(price)  OVER (PARTITION BY item ORDER BY week)        AS prev_week,
    ROW_NUMBER() OVER (PARTITION BY item ORDER BY price DESC) AS rank_in_item,
    AVG(price)  OVER (PARTITION BY item ORDER BY week
                      ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS rolling_4wk
FROM prices;
```

**The key difference from `GROUP BY`: a window function does not collapse rows.** `GROUP BY` gives one row per group; a window function keeps every row and adds the group's statistic alongside it.

**That is exactly what `pandas.transform` does** — Day 34. Same concept, different syntax. Noticing that now means you learned it once.

| Function | Gives |
|:---------|:------|
| `ROW_NUMBER()` | 1, 2, 3 — no ties |
| `RANK()` | 1, 2, 2, 4 — ties share, then skip |
| `DENSE_RANK()` | 1, 2, 2, 3 — ties share, no skip |
| `LAG(col, n)` / `LEAD(col, n)` | The value n rows back / forward |
| `SUM/AVG/COUNT OVER (...)` | Running or windowed aggregate |
| `NTILE(4)` | Quartile buckets |

**`LAG` is the one you will use most** — period-on-period change becomes one line instead of the self-join you wrote on Day 44.

---

## 💻 Code

### 🔴 MUST DO — statistics (`Day_52.py`, 35 min)

1. CI for the mean of your PBS prices at 90%, 95% and 99%. Record the widths.
2. **The empirical proof:** simulate 1,000 samples, build a 95% CI from each, and **count how many contain the true mean.** It should be about 950. *(This is what "95%" actually means.)*
3. Vary *n* at 10, 50, 200, 1,000 — plot how the width shrinks
4. `norm.interval` vs `t.interval` at n=10 and n=1,000. **When does the difference matter?**
5. **The overlap check:** two groups from your data. Do their intervals overlap? What can you claim?
6. **Write the interpretation sentence** for one of your intervals — correctly. Then write the wrong version and say what is wrong with it.
7. Add a confidence interval to one number in your Project 1 README. **Does it change the claim?**

### 🔴 MUST DO — SQL (`Day_52.sql`, 25 min)

8. `AVG() OVER (PARTITION BY ...)` — each row beside its item's average
9. `LAG` — week-on-week change in one line. **Compare with Day 44's self-join.**
10. `ROW_NUMBER`, `RANK`, `DENSE_RANK` on tied data — see all three differ
11. A rolling 4-week average with a `ROWS BETWEEN` frame
12. Top 3 per item using `ROW_NUMBER` in a CTE
13. **The connection:** write the same result with `pandas.transform` and with a window function, side by side

---

## 🔬 Understanding Check

1. **Reasoning.** What does a 95% CI mean? State it correctly, then state the common wrong version and say why it is wrong.
2. **Application.** Exercise 2: how many of your 1,000 intervals contained the truth? Did that make the definition concrete?
3. **Comparison.** When does `t.interval` differ meaningfully from `norm.interval`?
4. **Judgement.** Exercise 5: do the intervals overlap? What can and cannot you claim?
5. **Reasoning.** Why can you not have a narrow interval and high confidence on a small sample?
6. **SQL.** What is the difference between a window function and `GROUP BY`?
7. **Connection.** Window functions and `pandas.transform` — same idea. State it in one sentence.
8. **Project.** Did adding a CI change any Project 1 claim? Should you update the README?

---

## 🎯 Expected Outcome

- [ ] Compute CIs and choose between z and t correctly
- [ ] State the interpretation precisely
- [ ] Use the overlap check before claiming a difference
- [ ] Write window functions from memory

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 92–95 | 22 min |
| Interpretation | 13 min |
| Exercises 1–7 | 25 min |
| **SQL: window functions** | 25 min |
| Daily review | 5 min |
| **Total** | **~90 min** |

---

## 🧪 Mini Assessment

Six minutes, closed book. Two shops: A averages PKR 2,400 over 40 customers (SD 900); B averages 2,650 over 35 customers (SD 1,100).

1. A 95% CI for each
2. Do they overlap?
3. **Can you say B's customers spend more? Write the exact sentence you would put in a report.**

---

## 🔁 Daily Review

1. Exercise 2: how many intervals contained the truth?
2. Can I state the interpretation correctly without hedging?
3. Did a CI change anything in Project 1?
4. `LAG` versus the Day 44 self-join — how many lines each?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 92–95 read, code typed
- [ ] The 1,000-interval coverage simulation run, count recorded
- [ ] z vs t compared at two sample sizes
- [ ] The overlap check applied to real groups
- [ ] Both interpretation sentences written, right and wrong
- [ ] Six SQL window-function exercises working
- [ ] Committed to git

---

**[← Day 51](../Day_51/Day_51.md)** · **[Day 53 →](../Day_53/Day_53.md)** · [README](../../../README.md)
