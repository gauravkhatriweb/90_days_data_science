# Day 38 — Charts That Answer a Question

|  |  |
|:--|:--|
| **Date** | Friday, 23 October 2026 |
| **Position** | Week 6 · Month 2 · Phase 2 |
| **Budget** | **~75 min** |
| **Code file** | `Day_38.py` |

> **Why visualisation is not a 2.5-hour video here.** Nobody learns Matplotlib by watching Matplotlib. You learn it by needing a specific chart, making it, and being annoyed by the default. So today is forty minutes of *principles* — the object model and how to choose a chart — and then you use it every day for the rest of the challenge.
>
> **The principle that matters most:** a chart is an argument, not a decoration. If you cannot say in one sentence what a chart is supposed to make the reader realise, do not draw it.

---

## 🎯 Objective

Choose the right chart for a question, build it with the object-oriented Matplotlib API, and make it readable without explanation.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Visualization](https://www.youtube.com/watch?v=-jTD74eEy2I) · **`05:29 → 41:21`** · @1.75× | PRIMARY | 20 min | Matplotlib fundamentals |
| The object model + chart-choice sections below | REFERENCE | 20 min | The part that makes the rest unnecessary |

**Skip `0:00 → 05:29`** (library history) and **`01:45:09 → end`** (Plotly, Cufflinks, and the IPL project) — Plotly is a nice-to-have you can pick up in an hour when a job needs it, and the project time is better spent on your own.

### 🟢 IF TIME

- [Sheryians `41:21 → 1:05:57`](https://www.youtube.com/watch?v=-jTD74eEy2I) — Seaborn distribution plots. You do Seaborn properly tomorrow.

---

## 🧠 Core Concepts

### Use the object API, not the state machine

```python
# pyplot state machine -- fine for one throwaway chart
plt.plot(x, y)
plt.title("Prices")
plt.show()

# object API -- USE THIS
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y)
ax.set_title("Prices")
```

`plt.plot` draws on "whatever the current axes are", which becomes ambiguous the moment you have two charts. `fig, ax = plt.subplots()` gives you named objects you can pass to functions, test, and reuse.

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(...)
axes[0, 1].hist(...)
fig.suptitle("Price overview")
fig.tight_layout()
```

**The anatomy:** a `Figure` is the canvas. An `Axes` is one plot on it — with an x-axis, a y-axis, a title and the data. `ax.plot`, `ax.set_xlabel`, `ax.legend`, `ax.annotate` all belong to one `Axes`.

### Choosing the chart — by question, not by preference

| The question | Chart | Watch out for |
|:-------------|:------|:--------------|
| How has X changed over time? | **Line** | x must be ordered; gaps should show as gaps, not straight lines |
| How do categories compare? | **Bar** | **Start the y-axis at zero.** Sort by value unless the order means something. |
| How is one variable distributed? | **Histogram** | Bin count changes the story — try several |
| How does the distribution compare across groups? | **Box or violin** | Box hides multimodality; violin shows it |
| Do two variables relate? | **Scatter** | Overplotting — use alpha or a hexbin above ~2,000 points |
| What is it made of? | **Stacked bar** | Only the bottom segment is easy to compare. Three or four segments maximum. |
| How do many variables relate? | **Heatmap** | Needs a diverging colour scale centred sensibly |

**Two charts to avoid almost always:**

- **Pie charts** with more than about five slices. Humans compare angles badly. A sorted bar chart says the same thing and is readable.
- **Dual y-axes.** Two different scales on one chart let you manufacture any correlation you like by choosing the ranges. Use two stacked panels instead.

### Making a chart readable — the checklist

1. **A title that states the finding**, not the contents. Not "Price over time" — "Tea prices rose 34% while sugar stayed flat".
2. **Axis labels with units.** "Price (PKR/kg)", not "price".
3. **Sort categorical bars by value** unless the order is meaningful (months, sizes).
4. **Direct labels beat legends** when there are few series — put the name at the end of the line.
5. **Annotate the point you are making** with `ax.annotate`. The reader should not have to hunt.
6. **Remove what carries no information** — chart junk, heavy gridlines, 3D effects, decorative colour.
7. **Colour must mean something.** If it encodes nothing, use one colour.

### Accessibility, briefly

Around 8% of men have some form of colour-vision deficiency. Red-green pairs are the common failure. Use `viridis` or `cividis` for continuous scales, `tab10` for categories, and **never encode a distinction by colour alone** — vary the marker or the line style too. This is one line of work and it makes your charts better for everyone.

---

## 💻 Code

`Day_38.py` — ten charts on your real PBS data. **For each, write the one-sentence finding in a comment before drawing it.** If you cannot, that is the wrong chart.

1. Line — one item's price over time, with a stated finding
2. Line — four items on one chart, **direct-labelled**, no legend
3. Bar — average price by item, **sorted, zero-based**
4. Histogram — the price distribution, at 10, 30 and 100 bins. **How does the story change?**
5. Box plot — price distribution per item
6. Scatter — two items against each other, with alpha for overplotting
7. `subplots(2,2)` — four related views in one figure with a shared title
8. **Annotate** the largest single price jump with `ax.annotate`
9. **The rewrite:** take chart 3 and give it a finding-title, unit labels, sorting and one annotation. Save before and after; compare them.
10. **The bad chart:** deliberately make a misleading one — truncate the y-axis, or use a dual axis. Then write what it implies and why it is dishonest.

Exercise 10 matters. Knowing how charts lie is the only reliable defence against doing it accidentally, and you will be reading other people's charts for the rest of your career.

---

## 🔬 Understanding Check

1. **Reasoning.** Why does the object API beat `plt.plot` once you have more than one chart?
2. **Application.** Exercise 4: how did the histogram's story change with bin count? What does that say about "letting the data speak"?
3. **Comparison.** When is a box plot better than a histogram, and when is it worse?
4. **Reasoning.** Why do dual y-axes make it easy to mislead?
5. **Understanding.** Exercise 9: what specifically made the rewritten chart better?
6. **Judgement.** Exercise 10: what did your misleading chart imply, and how would you catch it in someone else's work?
7. **Application.** Which single chart best answers one of your Project 1 questions? Have you drawn it yet?

---

## 🎯 Expected Outcome

- [ ] Build any chart with `fig, ax = plt.subplots()`
- [ ] Choose a chart from the question, not from habit
- [ ] Title a chart with its finding
- [ ] Recognise a misleading chart on sight

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians Matplotlib @1.75× | 20 min |
| Object model + chart choice | 20 min |
| Ten charts | 30 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Eight minutes. One chart that answers a Project 1 question, meeting all seven readability rules. **Show it to someone who has not seen the data and ask what it says.** If they get it in ten seconds, it works.

---

## 🔁 Daily Review

1. Which chart did I draw before I knew what it was supposed to show? *(Be honest — it happens.)*
2. How much did the bin count change the histogram's story?
3. What did my deliberately-misleading chart imply?
4. Which chart from today is going into Project 1?

---

## 📦 Completion Criteria

- [ ] Ten charts, each with a written finding **before** drawing
- [ ] Every chart uses `fig, ax`
- [ ] The rewrite in exercise 9 saved before and after
- [ ] The misleading chart made and explained
- [ ] One chart shown to a person and understood in ten seconds
- [ ] Committed to git

---

**[← Day 37](../Day_37/Day_37.md)** · **[Day 39 →](../Day_39/Day_39.md)** · [README](../../../README.md)
