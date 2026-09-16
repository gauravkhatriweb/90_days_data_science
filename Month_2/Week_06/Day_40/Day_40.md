# Day 40 — How to Actually Explore Data

|  |  |
|:--|:--|
| **Date** | Sunday, 25 October 2026 |
| **Position** | Week 6 · Month 2 · Phase 2 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_40.py` + `project_1/notebooks/02_exploration.ipynb` |
| **Project** | 📊 **P1 — the real exploration** |

> **Why EDA gets a method and not just tools.** Yesterday you looked at every variable, which is the mechanical part. Today is the part that separates an analyst from someone who makes charts: **exploration driven by questions, with a loop that has a stopping condition.**
>
> Without a method, EDA becomes an endless production of plots that each look interesting and together say nothing. With one, it converges.

---

## 🎯 Objective

Run a question-driven exploration loop, handle outliers with a decision rather than a default, and reach a defensible answer to at least one Project 1 question.

---

## 📚 Learn — the method (40 min)

### 🔴 MUST DO

No video. This is the day's material.

### The loop

```
        ┌─────────────────────────────────────┐
        │  1. Ask a specific question         │
        │  2. Predict the answer              │  ← the step everyone skips
        │  3. Compute the minimum to check it │
        │  4. Compare with your prediction    │
        │  5. Surprised?  → new question      │
        │     Confirmed?  → next question     │
        └─────────────────────────────────────┘
                   stop when the questions
                   stop changing your mind
```

**Step 2 is what makes this work.** If you predict "tea rose about 20%" and it rose 34%, you have learned something and you have a new question. If you compute first and then decide 34% is what you expected, you have learned nothing — hindsight makes everything look obvious.

Write the prediction down. In the notebook. Before you run the cell.

### Bad questions and good ones

| Bad | Why | Good |
|:----|:----|:-----|
| "Let me explore the data" | No stopping condition | "Which three items rose fastest between Jan and Sep?" |
| "Is there a correlation?" | Between what, and so what? | "Do cooking-oil and wheat prices move together, and with what lag?" |
| "What are the trends?" | Unfalsifiable | "Did any item fall in price while overall inflation rose?" |
| "Is this significant?" | Significance is not a question | "Is the rural–urban gap larger than the month-to-month variation?" |

A good question is one where **a specific answer would change what you say.**

### Outliers — a decision, not a default

An outlier is only an error if you can say *why*. The usual detectors:

```python
q1, q3 = df.price.quantile([0.25, 0.75]); iqr = q3 - q1
outliers = df[(df.price < q1 - 1.5*iqr) | (df.price > q3 + 1.5*iqr)]

z = (df.price - df.price.mean()) / df.price.std()     # assumes roughly normal
outliers = df[z.abs() > 3]
```

**IQR is the safer default** — it uses quantiles, so extreme values do not distort the threshold the way they distort the mean and standard deviation that z-scores depend on.

Then decide, per outlier, which of these it is:

| Kind | Example | What to do |
|:-----|:--------|:-----------|
| **Data error** | Price of 0, or 10,000× the neighbours | Remove — and record how many |
| **Real and important** | A genuine 40% spike during a shortage | **Keep.** This may be the finding. |
| **Real but out of scope** | One wholesale price among retail | Exclude with a stated rule |

**Removing outliers because they are inconvenient is the most common way an honest analysis becomes dishonest.** Whatever you do, the count goes in the README.

### Correlation is not causation — and the specific ways it fails

`corr()` gives you a number. Before it means anything:

1. **Pearson only measures *linear* association.** A perfect U-shaped relationship has a correlation near zero. Always plot it.
2. **Outliers dominate.** One extreme point can move a correlation from 0.1 to 0.8. Check with and without.
3. **Confounders.** Every price in Pakistan rose in 2026. Any two prices will correlate strongly — because both correlate with time, not with each other. **Detrend first, or correlate the changes rather than the levels.**
4. **Spurious correlation.** Test enough pairs and some will correlate by chance. Twenty items give 190 pairs; at p < 0.05 you expect about 9 false positives. *(This is the Texas sharpshooter fallacy — Nield covers it on Day 54.)*

**Point 3 is the one that will affect your project directly.** Correlating raw price levels across a year of inflation will produce a heatmap of 0.9s that means nothing at all.

```python
df_wide.pct_change().corr()      # correlate the CHANGES, not the levels
```

### Time-series specifics

| Component | Question |
|:----------|:---------|
| **Trend** | Where is it going over the whole period? |
| **Seasonality** | Does it repeat — Ramadan, harvests, winter? |
| **Cycle** | Longer irregular swings |
| **Noise** | What is left |

```python
df.set_index("date")["price"].rolling(4).mean()      # smooth to see trend
df.set_index("date")["price"].pct_change()           # period-on-period change
df.set_index("date")["price"].resample("M").mean()   # change granularity
```

**Percentage change, not absolute change**, when comparing items at different price levels. A PKR 50 rise on tea at 1,250 and on salt at 60 are completely different events.

---

## 📊 Project 1 — the real exploration (110 min)

In `02_exploration.ipynb`. **Write the prediction before every cell that answers something.**

**1. Question one (35 min)** — take your most interesting question. Predict. Compute. Compare. Follow the surprise.

**2. Question two (30 min)** — same loop.

**3. Outlier decisions (20 min)** — find them with IQR, classify each, decide, record counts in `NOTES.md`.

**4. Relationships done properly (25 min)** — correlate percentage changes, not levels. Compare against the naive level correlation and note how different they are. Plot every pair you intend to claim anything about.

### The stopping condition

Stop when a new question stops changing your mind. If the last four cells confirmed what you already believed, you are finished exploring and ready to communicate — which is Day 43.

---

## 💻 Code

### 🔴 MUST DO

`Day_40.py` — six exercises, then the notebook.

1. Write five questions about your data. Mark each good or bad against the table above, and rewrite the bad ones.
2. IQR and z-score detection on the same column. Do they agree? Where do they differ, and why?
3. Classify ten real outliers from your data into the three kinds
4. **The confounding demonstration:** correlate raw price levels across items, then correlate the percentage changes. **Compare the two heatmaps.** Write what the difference means.
5. Decompose one item's series: rolling mean for trend, then the residual. Is there visible seasonality?
6. **The spurious-correlation demonstration:** generate 20 random series, correlate all 190 pairs, and count how many exceed 0.5 by chance. What does that number teach you?

---

## 🔬 Understanding Check

1. **Reasoning.** Why predict before computing? What goes wrong without it?
2. **Application.** Exercise 4: how different were the two correlation matrices? What would you have concluded from the naive one?
3. **Comparison.** IQR vs z-score — when does each fail?
4. **Judgement.** You found an item whose price tripled in one week. How do you decide whether it is an error or a finding?
5. **Reasoning.** Exercise 6: how many spurious correlations appeared? What does that mean for someone who tests many hypotheses?
6. **Understanding.** Why percentage change rather than absolute change when comparing items?
7. **Project.** What is your answer to question one? What evidence supports it, and what would falsify it?
8. **Stopping.** Have the last few questions changed your mind? If not, you are done exploring.

---

## 🎯 Expected Outcome

- [ ] Run the question-predict-check loop deliberately
- [ ] Classify outliers instead of deleting them
- [ ] Avoid the confounded-correlation trap
- [ ] Have a defensible answer to at least one project question

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| The EDA method | 40 min |
| Six exercises | 25 min |
| **Project 1 — real exploration** | 105 min |
| Daily review | 10 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

Write your answer to question one as **three sentences**: what you found, what evidence supports it, and what would have to be true for you to be wrong.

The third sentence is the one that matters, and it is the one most people cannot write.

---

## 🔁 Daily Review

1. How many predictions were wrong? *(Being wrong often is a good sign — it means you are learning from the data rather than confirming yourself.)*
2. Exercise 4: what would I have wrongly concluded from the level correlations?
3. How many outliers did I remove, and can I justify every one?
4. Am I done exploring, or is there a question still changing my mind?

---

## 📦 Completion Criteria

- [ ] Five questions written and graded
- [ ] Both outlier methods compared on real data
- [ ] The confounding demonstration done, with both heatmaps saved
- [ ] The spurious-correlation count recorded
- [ ] At least one project question answered with evidence
- [ ] Outlier decisions and counts recorded in `NOTES.md`
- [ ] Committed to git

---

**[← Day 39](../Day_39/Day_39.md)** · **[Day 41 →](../Day_41/Day_41.md)** · [README](../../../README.md)
