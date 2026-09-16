# Day 65 — Vectors: What the Data Actually Is

|  |  |
|:--|:--|
| **Date** | Thursday, 19 November 2026 |
| **Position** | Week 10 · Month 3 · **Phase 5 — Linear algebra** |
| **Budget** | **~75 min** |
| **Code file** | `Day_65.py` |
| **Reading** | 📐 **Essential Math Ch. 4, pp. 109–121** |

> **Why four days of linear algebra immediately before machine learning.** Not as a separate "maths month" — that is how people learn eigenvectors in October and forget them by December. These four days exist **so that Days 71–86 make sense.**
>
> Specifically: a dataset **is** a matrix. A row **is** a vector. A model's coefficients **are** a vector. Prediction **is** a matrix multiplication. PCA **is** an eigenvector problem. If those sentences currently sound like metaphors, these four days turn them into facts — and machine learning stops being a library you call and becomes something you can reason about.

---

## 🎯 Objective

See a data row as a vector, and understand span and linear dependence — which is where multicollinearity comes from.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 4, pp. 109–121** | **PRIMARY** · reading + code | 35 min | Vectors · adding · scaling · span · linear dependence |
| [3Blue1Brown — Ch. 1: Vectors](https://www.youtube.com/watch?v=fNk_zzaMoSs) | **REINFORCEMENT** | 10 min | The geometric picture |
| [3Blue1Brown — Ch. 2: Linear combinations, span, basis](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | **REINFORCEMENT** | 10 min | Span, visually |

**Why both, and in this order:** Nield gives you the computation and the NumPy. 3Blue1Brown gives you the picture, and the picture is what you remember in three weeks. Read first, watch second.

**This also directly supports MAT 265** — and linear algebra will appear formally later in your degree.

---

## 🧠 Core Concepts

### Three ways to see a vector

| View | A vector is | Useful for |
|:-----|:------------|:-----------|
| **Physics** | An arrow with direction and length | Geometric intuition |
| **Computer science** | An ordered list of numbers | Code |
| **Data science** | **One observation, with one number per feature** | **This one** |

```python
customer = np.array([34, 12, 4500, 2])     # age, orders, spend, returns
```

That customer *is* a point in four-dimensional space. Every customer is another point. **Your entire dataset is a cloud of points in feature-space**, and every model you will build is a statement about the shape of that cloud.

**This reframing is the point of today.** "Similar customers are close together" stops being a metaphor once you can compute the distance.

### Adding and scaling

```python
a + b          # combine -- tip to tail
3 * a          # scale -- same direction, three times as long
-1 * a         # reverse
```

A **linear combination** is any `c₁v₁ + c₂v₂ + ...`.

**Why that phrase matters:** a linear model's prediction *is* a linear combination of the features. `price = 3.2×area + 1.8×rooms − 0.5×age` is a weighted sum of vectors. When you fit a model on Day 71, you are finding the weights.

### Span and linear dependence — where multicollinearity comes from

**Span** = everywhere you can reach with linear combinations of a set of vectors.

- Two vectors pointing in different directions in 2D: their span is the **whole plane**
- Two vectors on the same line: their span is **just that line** — the second adds nothing

That second case is **linear dependence**: one vector is already a combination of the others, so it carries no new information.

**This is exactly multicollinearity.** If your dataset has `price_in_pkr` and `price_in_usd`, they are linearly dependent — one is the other times a constant. The second column adds no information, and it makes the model's coefficients unstable and uninterpretable, because there are infinitely many weight combinations that produce the same prediction.

**Practical consequences you will meet:**
- Highly correlated features → unstable, un-interpretable coefficients
- Perfectly dependent features → the matrix cannot be inverted, and the fit fails or silently produces nonsense
- **The one-hot trap:** encoding a category into k columns creates a dependency, because the k-th is `1 − sum of the others`. This is why `drop_first=True` exists — Day 79.

Everything on this list is one idea: **columns that are linear combinations of other columns carry no extra information and break the mathematics.**

### Distance and similarity

```python
np.linalg.norm(a)          # length
np.linalg.norm(a - b)      # Euclidean distance between two observations
a @ b                      # dot product -- how much they point the same way
```

Cosine similarity — the dot product divided by both lengths — measures direction while ignoring magnitude. It is what recommender systems use, and what k-means uses a cousin of on Day 86.

**Distance is why scaling matters.** If spend is in thousands and age in tens, spend dominates every distance calculation, and any distance-based model is really just measuring spend. That is Day 79's `StandardScaler`, and the reason for it is this paragraph.

---

## 💻 Code

`Day_65.py` — nine exercises. **Plot everything in 2D** — the geometry is the point.

1. Create vectors; add, scale, negate; plot each step
2. Show that `a + b` and `b + a` land in the same place, geometrically
3. Linear combinations: reach a target point with two given vectors. **Find the coefficients.**
4. **Span:** two independent vectors — sample many combinations and see the plane fill. Then two dependent ones — watch it collapse to a line.
5. **Build multicollinearity on purpose.** Add `price_usd = price_pkr / 280` to a dataset. Check the correlation, then the rank of the matrix. **What does `np.linalg.matrix_rank` say?**
6. **The one-hot trap:** encode a three-category column into three columns. Show the dependency. Then drop one and show it is gone.
7. Distance between customers, with and without scaling. **Which feature dominates unscaled?**
8. Cosine similarity — find the two most similar customers by direction, and compare with the nearest by distance. Are they the same pair?
9. Take one real row from your Project 2 data and treat it as a vector. What are its dimensions? What does its length mean, if anything?

---

## 🔬 Understanding Check

1. **Reframing.** What is a row of your dataset, in linear-algebra terms? What is the whole dataset?
2. **Understanding.** What is span? What does it mean for a set of vectors to be linearly dependent?
3. **Application.** Exercise 5: what happened to the matrix rank? Why does that break a regression?
4. **Reasoning.** Exercise 6: why does one-hot encoding create a dependency? Why does dropping one column fix it?
5. **Application.** Exercise 7: which feature dominated the unscaled distance? What does that predict about Day 79?
6. **Comparison.** Euclidean distance vs cosine similarity — when is each right?
7. **Connection.** A linear model is a linear combination of features. What, then, is "fitting" the model?

---

## 🎯 Expected Outcome

- [ ] See a data row as a vector and a dataset as a cloud of points
- [ ] Explain span and linear dependence geometrically
- [ ] Connect linear dependence to multicollinearity and the one-hot trap
- [ ] Explain why distance-based methods need scaling

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 109–121 | 35 min |
| 3Blue1Brown Ch. 1–2 | 20 min |
| Nine exercises | 15 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Five minutes. Given three feature columns where the third is the sum of the first two:

1. What is the rank of the matrix?
2. What happens if you fit a linear regression on all three?
3. Which column would you drop, and how would you decide?

---

## 🔁 Daily Review

1. Did seeing a customer as a point in feature-space change how I think about the data?
2. Exercise 5: what was the rank, and why does that break things?
3. Which feature dominated the unscaled distance?
4. Can I explain multicollinearity in terms of span, without using the word "correlated"?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 109–121 read, 3Blue1Brown Ch. 1–2 watched
- [ ] The span demonstration plotted, both independent and dependent
- [ ] Multicollinearity built on purpose, rank checked
- [ ] The one-hot dependency shown and fixed
- [ ] Distance computed with and without scaling
- [ ] Committed to git

---

**[← Day 64](../Day_64/Day_64.md)** · **[Day 66 →](../Day_66/Day_66.md)** · [README](../../../README.md)
