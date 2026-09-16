# Day 33 — Missing Data, Types, and the Start of SQL

|  |  |
|:--|:--|
| **Date** | Sunday, 18 October 2026 |
| **Position** | Week 5 · Month 2 · Phase 2 — Data manipulation |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code files** | `Day_33.py` · `Day_33.sql` |
| **Starts today** | 🗄️ **The SQL track** — 25–30 min, most weekdays, from now to Day 64 |

> **Why SQL starts on Day 33 and not week 12.** Every roadmap in `Tem.txt` puts SQL after machine learning. That is the wrong order for someone whose realistic first job title is Data Analyst: **entry-level postings list SQL more often than they list machine learning.** SQL also has no prerequisites — it needs nothing from Python or statistics — so delaying it buys nothing.
>
> It runs as a **thin parallel track** rather than a block: 25–30 minutes on selected days, all the way to Project 2. Spaced practice beats a three-week sprint for a query language, and a 25-minute SQL drill is the right kind of work for a tired Tuesday evening when a 90-minute Pandas session is not.
>
> **The other half of today is the part of Pandas that is actually the job.** Real data is missing, mistyped and inconsistent. This is where analysts spend most of their time, and it is the skill that separates people who can handle real data from people who can handle tutorials.

---

## 🎯 Objective

Handle missing values, wrong dtypes and messy text in Pandas — and write your first SQL queries.

---

## 📚 Learn — Track 1: Pandas (≈ 40 min)

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Pandas](https://www.youtube.com/watch?v=QUaSmqBeR9w) · **`35:20 → 45:33`** · @1.5× | PRIMARY | 7 min | Handling missing data |
| [Sheryians Pandas](https://www.youtube.com/watch?v=QUaSmqBeR9w) · **`1:17:20 → 1:24:47`** · @1.5× | PRIMARY | 5 min | Data operations |
| The sections below | REFERENCE | 25 min | The decisions the video does not cover |

---

## 🧠 Core Concepts — Missing Data

### The three kinds of "missing", and why the distinction matters

| Kind | Meaning | What you may do |
|:-----|:--------|:----------------|
| **MCAR** — missing completely at random | A sensor dropped a reading | Dropping is fairly safe |
| **MAR** — missing at random, given other data | Rural prices missing more often | Can be imputed from other columns |
| **MNAR** — missing *because of* the value | High earners skip the income question | **Dropping biases your result.** The missingness is itself information. |

Nobody labels these for you. You have to reason about **why** a value is absent, and the answer changes what you are allowed to do. Dropping MNAR data and reporting a mean is how an analysis becomes confidently wrong.

**So the first question is never "how do I fill this?" It is "why is this missing?"**

### The mechanics

```python
df.isna().sum()                       # per column
df.isna().mean() * 100                # percentage -- more useful
df.isna().sum(axis=1).value_counts()  # how many rows have 1, 2, 3 missing

df.dropna()                           # any NaN anywhere -- usually too aggressive
df.dropna(subset=["price"])           # only where it matters
df.dropna(thresh=5)                   # keep rows with >= 5 non-null values

df["price"].fillna(df["price"].median())    # median beats mean -- outlier-resistant
df["region"].fillna("unknown")               # do not invent a category silently
df["price"].ffill()                          # forward fill -- ONLY for ordered data
df["price"].interpolate()                    # ONLY for continuous ordered data
```

**`ffill` and `interpolate` are for time series.** Using them on unordered data invents numbers from whichever row happened to be above.

### The rule that keeps you honest

**Record every decision.** Not in your head — in `NOTES.md`:

> "34 of 1,240 SPI observations were missing. All were in weeks where PBS did not publish (public holidays). I forward-filled these because the underlying prices genuinely persisted. No imputation was applied to item-level gaps; those rows were dropped and the count is reported."

That is the difference between an analysis and a guess. And on Day 88, that paragraph is what a reviewer reads.

### `NaN` vs `None` vs `NaT` vs `pd.NA`

| | Appears in | Note |
|:--|:--|:--|
| `np.nan` | float columns | A float. Forces an int column to become float. |
| `None` | object columns | Python's null |
| `pd.NaT` | datetime columns | "Not a Time" |
| `pd.NA` | nullable dtypes (`Int64`, `boolean`, `string`) | The modern unified one |

**The int-becomes-float surprise:** a column of integers with one missing value becomes `float64`, and your ids turn into `1001.0`. The fix is the nullable `Int64` dtype (capital I), which holds integers and `pd.NA` together.

---

## 🧠 Core Concepts — Dtypes and Text

### Getting the types right is most of cleaning

```python
df["price"] = pd.to_numeric(df["price"], errors="coerce")   # bad values -> NaN
df["date"]  = pd.to_datetime(df["date"], errors="coerce")
df["region"] = df["region"].astype("category")               # memory + speed
df["qty"] = df["qty"].astype("Int64")                        # nullable integer
```

**`errors="coerce"` is the important argument.** Without it, one `"N/A"` in 40,000 rows raises and you get nothing. With it, bad values become `NaN` and you can count and inspect them — which is what you wanted anyway.

**`category` is worth knowing:** a column with 12 distinct region names repeated 100,000 times stores 100,000 strings by default. As a category it stores 12 strings and 100,000 small integers. On a large dataset that is a large memory difference and faster grouping.

### The `.str` accessor — Day 7, vectorised

```python
df["item"].str.strip().str.lower()
df["item"].str.replace(r"\s+", " ", regex=True)
df["item"].str.contains("tea", case=False, na=False)
df["item"].str.split(",", expand=True)          # -> multiple columns
```

Every method you drilled on Day 7 exists here, applied to a whole column at once. **`na=False` on `.contains` matters** — without it, missing values produce `NaN` in the mask, and `NaN` in a boolean mask raises.

### The `SettingWithCopyWarning`

```python
subset = df[df.price > 1000]
subset["discount"] = 0.1        # SettingWithCopyWarning
```

This is **Day 29's view-versus-copy problem**, in Pandas. `subset` might be a view or a copy, Pandas cannot always tell, so it warns that your write may or may not reach the original.

Two correct fixes:

```python
subset = df[df.price > 1000].copy()     # explicit copy -- usually what you meant
df.loc[df.price > 1000, "discount"] = 0.1   # modify the original directly
```

**Never suppress the warning.** It is telling you your data may not have changed.

---

## 🗄️ Learn — Track 2: SQL begins (30 min)

### Setup — five minutes, not fifty

We use **SQLite**, through Python's built-in `sqlite3`. No installation, no server, no configuration. It supports everything this challenge needs, including window functions and CTEs.

> **On the Sheryians SQL course:** it uses PostgreSQL and spends `0:12:58 → 0:25:09` on installation. **Skip that.** The SQL itself is nearly identical for everything we cover. The differences you will meet — `AUTOINCREMENT` vs `SERIAL`, and SQLite's looser type handling — are noted where they matter. If you later need PostgreSQL for a job, the transfer is a day's work.

### Today's SQL

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [SQLBolt lessons 1–4](https://sqlbolt.com/) | **PRACTICE** | 20 min | Interactive, in-browser, no setup. `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`. |
| `Day_33.sql` | PRACTICE | 10 min | The same, against a database you build from PBS data |

SQLBolt is the right starting resource because it is *doing*, immediately, with feedback — not watching.

### The one idea to take from today

**SQL is declarative.** You describe the result you want; the database decides how to get it.

```sql
SELECT item, price FROM prices WHERE price > 1000 ORDER BY price DESC LIMIT 5;
```

No loop. No iteration. **This is the same mental shift as Day 30's vectorisation** — describe the transformation, do not manage the mechanics. Two tools, one idea, and noticing that now means learning it once.

### Clause order versus execution order

You write:
```
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
```

It executes:
```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

**`SELECT` runs almost last.** That single fact explains why you cannot use a column alias defined in `SELECT` inside `WHERE` — the alias does not exist yet when `WHERE` runs. This is asked in interviews and it confuses people for months.

---

## 💻 Code

### 🔴 MUST DO — Pandas (`Day_33.py`, 85 min)

**Missing data (1–5)**
1. Missing counts, percentages and a per-row missing distribution on your PBS data
2. `dropna` four ways; report how many rows each removes
3. `fillna` with mean, median, a constant and `ffill`. **Compare the resulting means** — the choice changes your answer.
4. Classify your PBS missingness as MCAR, MAR or MNAR, and justify it in a comment
5. **The int-to-float surprise:** an int column with one NaN. Then fix it with `Int64`.

**Dtypes (6–8)**
6. `to_numeric(errors="coerce")` — count how many values it turned into NaN, and inspect them
7. Parse dates, including a column with two different formats
8. Convert a repeated string column to `category`; measure memory before and after

**Text (9–11)**
9. Chain `.str` methods to clean the PBS item names
10. `.str.contains` with and without `na=False` — see the failure
11. `.str.split(expand=True)` to break a combined field into columns

**The trap (12)**
12. **Reproduce `SettingWithCopyWarning`.** Then fix it both ways, and explain in a comment how it connects to Day 29.

### 🔴 MUST DO — SQL (`Day_33.sql`, 30 min)

13. SQLBolt lessons 1–4
14. Build a SQLite database from your PBS DataFrame with `df.to_sql`
15. Write eight queries: `SELECT`, column selection, `WHERE`, `AND`/`OR`, `BETWEEN`, `IN`, `LIKE`, `ORDER BY` with `LIMIT`
16. Run the same question in Pandas and in SQL. **Compare the two.** Which reads better? Which was faster to write?

### 🟢 IF TIME

- SQLBolt lessons 5–6 (joins). You get them properly on Day 36.

---

## 🔬 Understanding Check

1. **Reasoning.** What is the difference between MCAR and MNAR, and why does it change what you may do?
2. **Application.** Exercise 3: how much did the mean move between fill strategies? What does that tell you about reporting a mean from imputed data?
3. **Debugging.** An integer id column shows `1001.0`. What happened, and what is the fix?
4. **Understanding.** Why does `errors="coerce"` make cleaning easier rather than sloppier?
5. **Debugging.** You got `SettingWithCopyWarning` and your change did not appear. Explain it in terms of Day 29.
6. **SQL.** Why can you not use a `SELECT` alias inside `WHERE`? Answer with execution order.
7. **Comparison.** Exercise 16: which was clearer, Pandas or SQL? Would your answer change for a 50-million-row table?
8. **Project.** What is genuinely missing in your PBS data, and which kind of missingness is it?

---

## 🎯 Expected Outcome

- [ ] Diagnose missing data before deciding how to handle it
- [ ] Fix dtypes with `coerce` and count what it caught
- [ ] Clean a text column with `.str` methods
- [ ] Recognise and fix `SettingWithCopyWarning`
- [ ] Write basic SQL from memory, and explain execution order

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians Pandas (two segments) | 12 min |
| Missing data, dtypes, text | 25 min |
| Pandas exercises 1–12 | 85 min |
| **SQL: SQLBolt + exercises 13–16** | 30 min |
| Daily review | 12 min |
| **Total** | **~165 min** |

---

## 🧪 Mini Assessment

Ten minutes. Take the ugliest PBS file you have and write **one function** that loads it, coerces the numeric columns, parses dates, cleans item names and returns `(clean_df, report)` — where `report` states how many values were coerced to NaN, how many rows were dropped and why.

This function is the seed of Day 41's cleaning pipeline.

---

## 🔁 Daily Review

1. How far apart were the means under different fill strategies?
2. Which kind of missingness does my PBS data have? How confident am I?
3. Did I predict the `SettingWithCopyWarning`, given Day 29?
4. **SQL day 1.** Did the declarative style feel natural or strange? What did it remind me of?

---

## 📦 Completion Criteria

- [ ] All twelve Pandas exercises run on real PBS data
- [ ] Fill-strategy comparison recorded with actual numbers
- [ ] The int-to-float surprise reproduced and fixed
- [ ] `SettingWithCopyWarning` reproduced and fixed twice
- [ ] SQLBolt 1–4 complete
- [ ] SQLite database built, eight queries working
- [ ] Missingness classification written in `NOTES.md`
- [ ] Committed to git

---

**[← Day 32](../Day_32/Day_32.md)** · **[Day 34 →](../Day_34/Day_34.md)** · [README](../../../README.md)
