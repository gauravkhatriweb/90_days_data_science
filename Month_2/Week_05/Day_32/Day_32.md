# Day 32 — Pandas, and Getting Real Data

|  |  |
|:--|:--|
| **Date** | Saturday, 17 October 2026 |
| **Position** | Week 5 · Month 2 · Phase 2 — Data manipulation |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_32.py` + the `project_1/` folder |
| **Starts today** | 📊 **Project 1 — "What Actually Got Expensive"** |

> **Two things start today.** Pandas, which is the single most-used tool in the job you are aiming at. And **Project 1**, your first portfolio piece — built on Pakistan Bureau of Statistics price data, because it is real, it is messy in instructive ways, it matters to people you know, and **nobody else's GitHub has it.**
>
> The project runs from today to Day 45. Data acquisition takes the last 45 minutes of today, and it is deliberately early: the most common reason a data project dies is discovering on day six that the data does not support the question.

---

## 🎯 Objective

Load, inspect and select from a DataFrame with confidence — and get real, messy Pakistani price data onto your machine.

---

## 📚 Learn — Track 1: Pandas (≈ 45 min)

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Pandas](https://www.youtube.com/watch?v=QUaSmqBeR9w) · **`0:25 → 35:20`** · @1.75× | PRIMARY | 20 min | Series, DataFrames, the index |
| [Sheryians Pandas](https://www.youtube.com/watch?v=QUaSmqBeR9w) · **`1:24:47 → 1:27:58`** · @1.5× | PRIMARY | 3 min | Filtering, sorting, selecting |
| The sections below | REFERENCE | 20 min | The index, and `loc` vs `iloc` |

### 🟢 IF TIME

- The Pandas "10 minutes to pandas" official guide — 15 minutes, and it is the best-organised summary of the API that exists.

---

## 🧠 Core Concepts

### A DataFrame is NumPy with labels

| NumPy | Pandas | What was added |
|:------|:-------|:---------------|
| `ndarray` | `DataFrame` | Column names, a row index, mixed dtypes per column |
| One dtype for everything | One dtype **per column** | Strings and numbers in one table |
| `a[0, 2]` | `df.loc["tea", "price"]` | Selection by **label**, not just position |
| `a.sum(axis=0)` | `df.sum(axis=0)` | Same axis rule as Day 30 |

Everything from Days 29–31 still applies underneath: vectorisation, broadcasting, the axis rule, views versus copies. **Pandas adds labels and heterogeneity; it does not replace the model.**

### The index — the concept people skip and then fight

Every DataFrame has a row index. Default is `0, 1, 2, …`, but it can be dates, item names, anything.

```python
df.set_index("item")        # a column becomes the index
df.reset_index()            # the index becomes a column
df.index                    # inspect it
```

**Why it matters:** the index is what Pandas aligns on. When you add two Series, it matches by index, not by position.

```python
a = pd.Series([1, 2, 3], index=["x", "y", "z"])
b = pd.Series([10, 20, 30], index=["z", "y", "x"])
a + b       # x:31, y:22, z:13  -- aligned by LABEL, not position
```

This is a feature — it prevents a whole class of silent misalignment bugs that NumPy would let through. It is also surprising the first time, and it explains most "why are there NaNs in my result?" moments.

### `loc` versus `iloc`

```python
df.loc["tea", "price"]        # by LABEL
df.loc["tea":"sugar"]         # label slice -- END IS INCLUSIVE
df.loc[df.price > 1000]       # boolean mask by label

df.iloc[0, 2]                 # by POSITION
df.iloc[0:3]                  # positional slice -- END IS EXCLUSIVE
```

**The inclusive/exclusive difference is real and catches everyone.** `df.loc["a":"c"]` gives you a, b and c. `df.iloc[0:3]` gives you rows 0, 1 and 2. The reasoning: with labels you usually mean "from here to there, inclusive"; with positions, Python's convention applies.

### Selection, ranked by how often you will use it

```python
df["price"]                   # one column -> a Series
df[["item", "price"]]         # several columns -> a DataFrame
df[df.price > 1000]           # boolean filter -- the workhorse
df.query("price > 1000 and region == 'sindh'")   # readable for long conditions
df.nlargest(5, "price")
df.sample(5)
```

**`df["price"]` gives a Series; `df[["price"]]` gives a DataFrame.** One bracket versus two. Worth internalising now, because a surprising number of errors are "expected DataFrame, got Series".

### Inspecting — the first five lines of every analysis

```python
df.shape · df.info() · df.describe() · df.head() · df.dtypes
df.isna().sum()          # missing values per column
df["region"].value_counts()
df.nunique()
```

**Make this a habit:** `shape`, `info()`, `head()`, `isna().sum()`, `describe()` — in that order, every single time you load a dataset. It takes thirty seconds and it catches wrong dtypes, unexpected nulls and silently truncated files before they become five hours of confusion.

---

## 📊 Track 2: Project 1 — Data Acquisition (45 min)

### The project

**"What Actually Got Expensive"** — an analysis of Pakistani price data that answers questions a normal person would ask, with evidence.

Candidate questions *(you will narrow to three on Day 43)*:

- Which essential goods rose fastest over the period, and by how much?
- Does the official inflation figure match what happened to the things people buy weekly?
- How do urban and rural price movements differ?
- Which items are most volatile — and what does volatility mean for a household budget?
- Is there seasonality, and can it be separated from the trend?

### Where the data is

| Source | What | Format |
|:-------|:-----|:-------|
| [PBS — Price Statistics](https://www.pbs.gov.pk/price-statistics/) | **SPI** weekly (a basket of essentials, by income group) · **CPI** monthly, urban/rural | Excel |
| [PBS — Monthly inflation reports](https://www.pbs.gov.pk/) | Item-level CPI tables | Excel / PDF |
| [Open Data Pakistan](https://opendata.com.pk/dataset) | Trade, demographic, provincial | CSV |
| [Pakistan Data Hub](https://pakdatahub.com/) | ~23,000 economic series, REST API, free tier | JSON / CSV |

**Start with SPI weekly.** It is item-level, it is weekly so there are plenty of observations, and it covers things you personally buy.

### Today's job: acquire and survey — nothing else

1. Create `project_1/` with `data/raw/`, `data/processed/`, `notebooks/`, `src/`
2. Download at least 12 months of SPI or CPI data. **Save the raw files untouched.**
3. Add a `data/raw/SOURCES.md` recording, for each file: the URL, the date you downloaded it, what it covers, and any notes on the format
4. Load one file with `pd.read_excel`. **It will not work cleanly.** Expect merged header cells, multi-row headers, footnotes in the data area, and a base-year change.
5. Run the five-line inspection ritual on it
6. Write, in `project_1/NOTES.md`: what is in this data, what shape it is in, and **three questions it could honestly answer.** Also write one question it *cannot* answer, and why.

**Do not clean anything today.** Today is acquisition and honest survey. Cleaning is Day 41.

> [!IMPORTANT]
> **Recording your sources is not bureaucracy.** On Day 45 the README has to let a stranger reproduce this. On Day 88, a reviewer will check whether you documented where the data came from. Undocumented data is not evidence.

---

## 💻 Code

### 🔴 MUST DO

`Day_32.py` — Pandas mechanics (12 exercises), then `project_1/` acquisition.

1. Build a Series three ways; inspect `.index` and `.values`
2. **Index alignment:** add two Series with differently-ordered indexes, predict the result first
3. Build a DataFrame from a dict, a list of dicts, and a NumPy array
4. Read a CSV — set the index, parse dates, select columns, control dtypes
5. The five-line inspection ritual on a real file
6. `loc` versus `iloc`: same selection both ways, then demonstrate the inclusive/exclusive difference
7. `df["col"]` vs `df[["col"]]` — print both types
8. Boolean filtering — single, compound with `&`, and the same thing via `.query()`
9. `set_index`, `reset_index`, `sort_index`, `sort_values`
10. `nlargest`, `value_counts`, `nunique`, `sample`
11. Add a computed column three ways; time each
12. **`read_excel` on a real PBS file.** Handle `header=`, `skiprows=`, `usecols=`. Record what you had to do.

### 🟢 IF TIME

- Load a second PBS file and check whether the column names match the first. *(They often will not. Note it — it is Day 41's problem.)*

---

## 🔬 Understanding Check

1. **Understanding.** What does a DataFrame add to a NumPy array? Name three things.
2. **Reasoning.** Exercise 2: why does Pandas align on index rather than position? What bug does that prevent?
3. **Comparison.** `loc` vs `iloc` — state the two differences, including the slice-end behaviour.
4. **Debugging.** A function expects a DataFrame and got a Series. What did the caller most likely write?
5. **Application.** Exercise 12: what did `read_excel` need to handle that `read_csv` did not?
6. **Project.** What are your three answerable questions? What is one question the data cannot answer, and how do you know?
7. **Judgement.** You have surveyed the raw data. Is it good enough for a portfolio project? If not, what else do you need — and is that a today problem or a Day 41 problem?

---

## 🎯 Expected Outcome

- [ ] Load, inspect and select from a DataFrame without looking things up
- [ ] Explain index alignment and predict its results
- [ ] Use `loc` and `iloc` correctly, including slice ends
- [ ] Have real PBS data on disk, with sources documented
- [ ] Have three honest, answerable project questions written down

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians Pandas (two segments) | 23 min |
| Index, `loc`/`iloc`, selection | 20 min |
| Twelve exercises | 70 min |
| **Project 1 — acquisition and survey** | 45 min |
| Daily review | 12 min |
| **Total** | **~170 min** |

---

## 🧪 Mini Assessment

The project is the assessment. It passes when:

- Raw data is on disk and unmodified
- `SOURCES.md` records URL, download date and coverage for every file
- One file loads into a DataFrame, however ugly
- `NOTES.md` has three answerable questions and one honest limitation

---

## 🔁 Daily Review

1. Exercise 2: did I predict the index-alignment result?
2. What did `read_excel` actually need to make the PBS file load?
3. What is genuinely messy about this data? List the top three problems.
4. Which of my three questions am I most interested in? *(That one becomes the project's headline on Day 43.)*

---

## 📦 Completion Criteria

- [ ] Twelve Pandas exercises working
- [ ] `project_1/` structure created
- [ ] 12+ months of PBS data downloaded, raw files untouched
- [ ] `data/raw/SOURCES.md` complete
- [ ] One file loaded and the inspection ritual run
- [ ] `NOTES.md` with three questions and one limitation
- [ ] Committed to git

---

**[← Day 31](../Day_31/Day_31.md)** · **[Day 33 →](../Day_33/Day_33.md)** · [README](../../../README.md)
