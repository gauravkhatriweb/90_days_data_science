# Day 39 — Seaborn, and the First Look at Your Data

|  |  |
|:--|:--|
| **Date** | Saturday, 24 October 2026 |
| **Position** | Week 6 · Month 2 · Phase 2 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_39.py` + `project_1/notebooks/01_first_look.ipynb` |
| **Project** | 📊 **P1 — first exploratory pass** |

> **Why Seaborn after Matplotlib and not instead of it.** Seaborn is a layer on top of Matplotlib that knows about statistics and about DataFrames. It draws a distribution, a regression line or a grouped comparison in one call — but when you need to adjust something, you adjust the underlying `Axes`, which is why yesterday came first.
>
> **The second half of today is the project**, and it is the first time you look at your own data properly. Expect it to be worse than you hoped. That is normal and it is information.

---

## 🎯 Objective

Produce statistical plots in one line, and complete a first honest exploratory pass over the PBS data.

---

## 📚 Learn — Track 1: Seaborn (≈ 50 min)

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Visualization](https://www.youtube.com/watch?v=-jTD74eEy2I) · **`41:21 → 1:45:09`** · @1.75× | PRIMARY | 35 min | Distribution, categorical, matrix and regression plots |
| The sections below | REFERENCE | 15 min | The long-data requirement and figure-vs-axes plots |

**Skip `1:45:09 → end`** — Plotly and Cufflinks. Interactive charts are a nice-to-have; you can pick them up in an hour when a role asks for them.

---

## 🧠 Core Concepts

### Seaborn wants long data

```python
sns.lineplot(data=df_long, x="date", y="price", hue="item")
```

`hue`, `col` and `row` all expect a **column whose values are the groups** — which is exactly the long format from Day 37. This is why reshaping came first. If a Seaborn call is fighting you, the usual cause is that the data is wide.

### The four families

```python
# distribution
sns.histplot(data=df, x="price", hue="item", kde=True)
sns.kdeplot(data=df, x="price", hue="item", fill=True)
sns.ecdfplot(data=df, x="price")          # underrated -- no binning choice at all

# categorical
sns.boxplot(data=df, x="item", y="price")
sns.violinplot(data=df, x="item", y="price")     # shows multimodality a box hides
sns.barplot(data=df, x="item", y="price")        # NOTE: shows the MEAN + a CI
sns.countplot(data=df, x="region")               # shows COUNTS

# relational
sns.scatterplot(data=df, x="qty", y="price", hue="region", size="revenue")
sns.lineplot(data=df, x="date", y="price", hue="item")

# matrix and multi-panel
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", center=0)
sns.pairplot(df, hue="region")                   # expensive above ~8 columns
```

**Three things worth knowing now:**

`sns.barplot` plots the **mean with a confidence interval**, not a sum. People expect a total and get an average. Use `estimator="sum"` if you want totals, and know which one you asked for.

`ecdfplot` has no bin-size choice, so it cannot mislead the way a histogram can. It is harder to read at first and worth the effort.

`center=0` on a diverging heatmap matters. Without it, a correlation of 0 can be coloured as if it were strong.

### Figure-level versus axes-level — the thing that confuses everyone

| Axes-level | Figure-level |
|:-----------|:-------------|
| `histplot`, `boxplot`, `scatterplot`, `lineplot` | `displot`, `catplot`, `relplot`, `pairplot`, `lmplot` |
| Draws onto an `ax` you give it | Creates its own figure |
| `ax=axes[0,1]` works | `ax=` **raises an error** |
| Returns an `Axes` | Returns a `FacetGrid` |

**The rule:** use axes-level plots inside your own `subplots` layout. Use figure-level plots when you want faceting (`col="region"` producing one panel per region) and are happy for Seaborn to own the figure.

"`ax` is an invalid keyword argument" means you used a figure-level function inside a subplot grid. Drop the `dis`/`cat`/`rel` prefix and you get the axes-level twin.

### Styling once, at the top

```python
sns.set_theme(style="whitegrid", palette="colorblind", context="notebook")
```

`palette="colorblind"` costs nothing and fixes the red-green problem from yesterday for every chart in the notebook.

---

## 📊 Track 2: Project 1 — first exploratory pass (110 min)

### The rule for today: describe, do not conclude

The purpose of a first pass is **to find out what you have**, not to answer the question. Analysts who start hunting for their conclusion on day one find it, whether or not it is there.

### Work through this in `01_first_look.ipynb`

**1. Load and inspect (15 min)**
- The five-line ritual
- Time range, granularity, item count, observations per item
- `df.isna().mean() * 100` per column

**2. Every variable on its own (30 min)**
- Each numeric column: histogram, box plot, `describe()`
- Each categorical column: `value_counts()`, then a bar chart
- The date column: are there gaps? Plot observations per period.
- **Write one sentence per variable** in `NOTES.md`

**3. Data-quality inventory (25 min)**
- Duplicate rows? Duplicate `(item, date)` pairs?
- Impossible values — negative prices, zeros, absurd outliers
- Inconsistent item naming: how many spellings of the same thing?
- Does the base year change anywhere? *(PBS restates the SPI base — check.)*
- **Write the full list in `NOTES.md`. Do not fix anything yet.**

**4. Relationships (25 min)**
- Correlation heatmap across items in wide form
- Every item's price over time on one chart
- Do items move together? Which are volatile and which are stable?

**5. Write down what you found (15 min)**
In `NOTES.md`:
- Five things you did not know before today
- Three data-quality problems that will need fixing on Day 41
- **One thing that surprised you**
- Whether your three questions from Day 32 still look answerable

> [!IMPORTANT]
> **If one of your three questions no longer looks answerable, say so now.** Changing the question on Day 39 is good analysis. Discovering it on Day 45 while writing the README is a failed project.

---

## 💻 Code

### 🔴 MUST DO

`Day_39.py` — Seaborn mechanics (8 exercises), then the notebook.

1. `set_theme` with a colourblind palette
2. `histplot` with `hue` and `kde`; then the same as an `ecdfplot`. Compare.
3. `boxplot` and `violinplot` of the same data side by side — find a case where the violin shows something the box hides
4. `barplot` with the default estimator and with `estimator="sum"` — note how differently they read
5. `heatmap` of correlations, `annot=True`, `center=0`
6. `pairplot` on five columns — then say why you would not do this on fifty
7. **The figure-vs-axes error:** call a figure-level function with `ax=`, read the error, then fix it with the axes-level twin
8. `relplot` with `col="item"` — faceting, one panel per item

### 🟢 IF TIME

- `sns.lmplot` with a regression line. You get the mathematics on Day 71 — seeing the line now is a useful preview.

---

## 🔬 Understanding Check

1. **Reasoning.** Why does Seaborn want long data? Connect it to Day 37.
2. **Debugging.** "`ax` is an invalid keyword argument" — what did you call, and what is the fix?
3. **Comparison.** Exercise 3: what did the violin show that the box hid? Why does that matter?
4. **Application.** `barplot` defaults to the mean. Name a business question where reading it as a total would be badly wrong.
5. **Understanding.** Why does an ECDF plot not mislead the way a histogram can?
6. **Project.** What are the five things you did not know about your data this morning?
7. **Project.** Do all three questions still look answerable? If not, what is the new one?
8. **Judgement.** What surprised you? Surprise usually means either a data problem or a real finding — which is it?

---

## 🎯 Expected Outcome

- [ ] Produce any standard statistical plot in one line
- [ ] Know when to use figure-level versus axes-level
- [ ] Have a complete data-quality inventory written down
- [ ] Have five specific findings and three specific problems

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians Seaborn @1.75× | 35 min |
| Long data + figure/axes | 15 min |
| Eight Seaborn exercises | 20 min |
| **Project 1 — first exploratory pass** | 110 min |
| Daily review | 10 min |
| **Total** | **~190 min** — if over, cut exercises 6–8 |

---

## 🧪 Mini Assessment

The `NOTES.md` entry is the assessment. It passes when someone who has never seen this data could read it and know: what is in it, what is wrong with it, and what it can honestly answer.

---

## 🔁 Daily Review

1. Five things I did not know this morning.
2. Three data-quality problems for Day 41.
3. What surprised me — and is it a data problem or a finding?
4. Are my three questions still answerable? If not, what changed?

---

## 📦 Completion Criteria

- [ ] Eight Seaborn exercises done
- [ ] The figure-vs-axes error triggered and fixed
- [ ] `01_first_look.ipynb` complete: every variable examined
- [ ] Data-quality inventory written in `NOTES.md`
- [ ] Five findings, three problems, one surprise written down
- [ ] Question viability confirmed or revised
- [ ] Committed to git

---

**[← Day 38](../Day_38/Day_38.md)** · **[Day 40 →](../Day_40/Day_40.md)** · [README](../../../README.md)
