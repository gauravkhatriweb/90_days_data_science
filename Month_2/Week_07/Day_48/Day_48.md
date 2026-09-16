# Day 48 — Descriptive Statistics, and Why n−1

|  |  |
|:--|:--|
| **Date** | Monday, 2 November 2026 |
| **Position** | Week 7 · Month 2 · Phase 3 — Statistics |
| **Budget** | **~75 min** (50 stats + 25 SQL) |
| **Code files** | `Day_48.py` · `Day_48.sql` |
| **Reading** | 📐 **Essential Math Ch. 3, pp. 63–78** |

> **Why "descriptive statistics" is not the easy bit.** You already know how to call `.mean()`. What you do not yet have is the thing that matters: **the difference between a population and a sample, and what that difference does to every formula.** It is the reason for `n−1`, the reason a sample mean is uncertain, and the foundation of everything from Day 50 to Day 90.
>
> Pandas' `.std()` and NumPy's `.std()` give different answers by default, for exactly this reason. Most people never notice.

---

## 🎯 Objective

Understand population versus sample deeply enough that `n−1` is obvious rather than memorised, and know when each measure of centre and spread is the honest one.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 3, pp. 63–78** | **PRIMARY** · reading + code | 35 min | Data · populations, samples, bias · mean, median, mode · variance and SD |
| The sections below | REFERENCE | 15 min | `n−1` and the bias catalogue |

---

## 🧠 Core Concepts

### Population versus sample — the distinction everything rests on

| | Population | Sample |
|:--|:--|:--|
| What | Every member | A subset you actually measured |
| Mean | μ (mu) | x̄ (x-bar) |
| Variance | σ² | s² |
| Divide by | **n** | **n − 1** |
| You usually have | Almost never | Always |

**You essentially never have a population.** Your PBS data is a sample of prices — specific shops, specific weeks, specific grades. Every number you compute is a *sample statistic*, and it is an estimate of something you cannot observe.

That single realisation is what makes statistics necessary. If you had the population, you would just look.

### Why n−1 — the intuition, not the algebra

Variance measures spread around the **true mean**. But you do not know the true mean, so you use the sample mean instead.

Here is the problem: **the sample mean is, by construction, the point that minimises the squared distances within your sample.** No other value gives a smaller sum of squared deviations for that data. So measuring spread around it gives you the smallest possible answer — smaller, on average, than the spread around the true mean would be.

Your variance is systematically too small. Dividing by `n − 1` instead of `n` makes the number slightly larger, and it turns out to correct the bias exactly.

**The clue is in how much it matters.** At n = 5, `n−1` changes the answer by 25%. At n = 1,000, by 0.1%. **The correction matters exactly when your sample is small** — which is exactly when you should be least confident. That is not a coincidence; it is the point.

```python
np.std(data)              # ddof=0 -- POPULATION -- the default
np.std(data, ddof=1)      # ddof=1 -- SAMPLE     -- what you almost always want
df["price"].std()         # pandas defaults to ddof=1 -- SAMPLE
```

**NumPy and Pandas have opposite defaults.** Read that line again. It is a real source of quietly inconsistent numbers, and it is worth checking in any code that computes a standard deviation.

### Mean, median, mode — a choice, not a habit

| | Best when | Fails when |
|:--|:--|:--|
| **Mean** | Roughly symmetric, no extreme values | **One outlier moves it arbitrarily far** |
| **Median** | Skewed data, outliers present | Ignores magnitude entirely |
| **Mode** | Categorical data, finding the typical case | Meaningless on continuous data |

The classic case: income. A hundred people earning PKR 50,000 and one earning 500 million gives a *mean* of about 5 million — a figure nobody in the room earns. The median is 50,000.

**"Average" is ambiguous and the ambiguity is sometimes deliberate.** When someone reports an average, ask which one, and why that one.

### Weighted mean — when observations are not equal

```python
np.average(values, weights=weights)
```

You need it whenever units differ in importance: a CPI where food weighs more than transport, a GPA where credit hours differ, an average price across shops of different sizes. **Your PBS SPI data is already a weighted mean** — the basket weights come from household expenditure surveys. Computing an unweighted mean of the same items gives a different, and less meaningful, number.

### The biases that ruin samples

| Bias | Happens when | Real example |
|:-----|:-------------|:-------------|
| **Selection** | The sample is not representative | Online survey about internet access |
| **Self-selection** | People choose to participate | Reviews are written by the delighted and the furious |
| **Survivorship** | Failures are invisible | "Successful startups did X" — so did the failed ones |
| **Confirmation** | You look until you find it | Testing twenty hypotheses, reporting one |

**Survivorship bias is the one to watch in your own work.** PBS records prices in shops that were open and reporting. Shops that closed because they could not source stock are not in the data — and their absence is exactly the signal a shortage would produce.

---

## 💻 Code

### 🔴 MUST DO — statistics (`Day_48.py`, 35 min)

1. Compute mean, median and mode on your PBS prices. Where do they disagree, and what does that tell you about the distribution?
2. **The outlier demonstration:** add one extreme value; record how far the mean moves and how far the median moves
3. Implement variance from scratch, both `n` and `n−1`, and match SciPy
4. **The n−1 demonstration:** simulate 10,000 samples of size 5 from a known population. Compute the variance both ways. **Which one averages to the true value?** *(This is the empirical proof, and it is more convincing than the algebra.)*
5. Show `np.std` and `df.std()` disagreeing, and explain why
6. Weighted versus unweighted mean on your SPI items — how different?
7. Range, IQR and standard deviation on the same data. When would each mislead?
8. **Name the sampling bias in your own PBS data** and write one sentence on what it means for your Project 1 conclusion

### 🔴 MUST DO — SQL (`Day_48.sql`, 25 min)

9. `AVG`, `SUM`, `COUNT`, `MIN`, `MAX` with `GROUP BY`
10. **The median problem:** SQL has no `MEDIAN`. Compute it with `NTILE` or `ROW_NUMBER` — and note how much harder it is than `.median()`
11. Standard deviation in SQL — `STDEV`/`stdev_samp` availability varies by engine; compute it manually if needed
12. A weighted average in SQL: `SUM(value * weight) / SUM(weight)`
13. **The comparison:** which of these five statistics is awkward in SQL, and what does that tell you about where each tool belongs?

---

## 🔬 Understanding Check

1. **Reasoning.** Why does dividing by `n−1` correct the bias? Explain without algebra, using the sample mean's minimising property.
2. **Application.** Exercise 4: which divisor averaged to the true variance? Did the empirical result convince you more than the argument?
3. **Debugging.** Your NumPy and Pandas standard deviations differ. Why, and which do you want?
4. **Judgement.** Exercise 2: how far did the mean move versus the median? When is the mean's sensitivity a feature rather than a bug?
5. **Reasoning.** Why is SPI a weighted mean? What would an unweighted version measure instead?
6. **Application.** Name the sampling bias in your PBS data and what it does to your conclusion.
7. **SQL.** Why is the median awkward in SQL and trivial in Pandas? What does that suggest about tool choice?
8. **Connection.** You now know a sample statistic is an estimate. What is the obvious next question? *(Day 51 answers it.)*

---

## 🎯 Expected Outcome

- [ ] Explain `n−1` without memorising it
- [ ] Choose mean, median or mode deliberately
- [ ] Know which tool's default you are using
- [ ] Name the bias in a sample you are working with

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 63–78, with code | 35 min |
| `n−1` and biases | 15 min |
| Exercises 1–8 | 25 min |
| **SQL: exercises 9–13** | 25 min |
| Daily review | 5 min |
| **Total** | **~105 min** — if over, move the SQL block to Day 49 |

---

## 🧪 Mini Assessment

Six minutes, closed book. A dataset of 40 salaries, one of them ten times the others.

1. Which measure of centre do you report, and why?
2. Which measure of spread, and why?
3. Compute the sample standard deviation with the correct divisor
4. **One sentence you would put in the report about that one value**

---

## 🔁 Daily Review

1. Exercise 4: which divisor won? Did the simulation convince me more than the argument did?
2. How far apart were the weighted and unweighted SPI means?
3. What bias is in my PBS data, and did I mention it in the Project 1 README?
4. **The next question:** a sample statistic is an estimate — so how wrong can it be? *(Day 51.)*

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 63–78 read, code typed
- [ ] The `n−1` simulation run, with the winning divisor recorded
- [ ] The NumPy/Pandas default difference demonstrated
- [ ] Weighted vs unweighted comparison computed
- [ ] The bias in your own data named in writing
- [ ] Five SQL exercises done, including the median
- [ ] Committed to git

---

**[← Day 47](../Day_47/Day_47.md)** · **[Day 49 →](../Day_49/Day_49.md)** · [README](../../../README.md)
