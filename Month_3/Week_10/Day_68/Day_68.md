# Day 68 — Eigenvectors, and Why PCA Works

|  |  |
|:--|:--|
| **Date** | Sunday, 22 November 2026 |
| **Position** | Week 10 · Month 3 · Phase 5 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_68.py` |
| **Reading** | 📐 **Essential Math Ch. 4, pp. 142–146 + exercises** |

> **Linear algebra finishes today**, with the idea that most people memorise and almost nobody understands. An eigenvector is not a formula — it is **a direction the transformation does not turn.** Once that is a picture rather than a definition, PCA stops being a black box and becomes obvious.

---

## 🎯 Objective

Understand eigenvectors geometrically, and be able to explain why PCA finds the directions of greatest variance.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 4, pp. 142–146** | **PRIMARY** · reading + code | 30 min | Eigenvectors and eigenvalues |
| [3Blue1Brown — Ch. 14: Eigenvectors and eigenvalues](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | **REINFORCEMENT** | 17 min | **The picture. Essential.** |
| **Chapter 4 exercises, p. 146** | **PRACTICE** | 30 min | Answers in Appendix B |
| The PCA section below | REFERENCE | 20 min | The payoff |

---

## 🧠 Core Concepts

### The idea

Apply a transformation. Most vectors get **knocked off their original line** — they rotate as well as stretch.

**Some do not.** They stay on their own line and only get longer or shorter. Those are the **eigenvectors**, and how much they stretch is the **eigenvalue**.

```
A v = λ v
```

"Transforming `v` has the same effect as just scaling it by λ."

```python
values, vectors = np.linalg.eig(A)
```

| Eigenvalue | Means |
|:-----------|:------|
| λ > 1 | Stretched in that direction |
| λ = 1 | Unchanged |
| 0 < λ < 1 | Squashed |
| λ = 0 | **Collapsed** — that direction is destroyed *(and so `det = 0`)* |
| λ < 0 | Flipped and scaled |

**The det = 0 connection:** the determinant is the product of the eigenvalues. One zero eigenvalue means one direction is destroyed, which means area becomes zero, which means no inverse. **Yesterday's four statements, from a different angle.**

### Why this matters: PCA

Take your data's **covariance matrix** — it records how features vary together.

Its **eigenvectors are the directions of greatest variance in your data**, and its **eigenvalues are how much variance lies along each.**

That is the whole of principal component analysis:

1. Centre the data
2. Compute the covariance matrix
3. Find its eigenvectors and eigenvalues
4. Sort by eigenvalue, descending — **the first eigenvector is the direction the data varies most along**
5. Project onto the top k

**Why it is useful:** if two features are highly correlated, the data really lives along one direction in that two-dimensional space. PCA finds that direction and lets you keep one number instead of two, losing almost nothing.

**Why it has a real cost:** the new axes are *combinations* of your original features. "Principal component 1" might be `0.6×income + 0.5×spend − 0.3×age`, which has no name and no meaning to a business. **You trade interpretability for compactness** — and that is a genuine trade, not a free win. Most of the time you should not do it.

### Where you meet it

| Use | Day |
|:----|:---:|
| PCA for dimensionality reduction | 86 |
| PCA to visualise high-dimensional data in 2D | 86 |
| Detecting near-collinearity via tiny eigenvalues | 67, and in practice |
| PageRank, spectral clustering, recommender systems | beyond this challenge |

### The honest caveats

- **PCA needs scaled data.** Without scaling, the feature with the largest units dominates every component — Day 65's distance problem again, and the single most common PCA mistake.
- **It only finds linear structure.** Data curved along a spiral is not helped.
- **Interpretability is gone.** Never present a principal component to a business audience as though it were a variable they can act on.

---

## 💻 Code

`Day_68.py` — ten exercises.

**Seeing eigenvectors (1–4)**
1. **The visual:** apply a matrix to many unit vectors; draw each before and after. **Find the ones that did not rotate.** Then compute `np.linalg.eig` and confirm you found them.
2. Verify `A @ v == λ * v` for each eigenvector
3. Matrices with interesting eigen-structure: a rotation *(no real eigenvectors — why?)*, a scale *(everything is an eigenvector)*, a shear *(only one)*
4. **The collapse:** eigenvalues of `[[1,2],[2,4]]`. One is zero. Connect it to `det = 0`.

**Building PCA (5–8)**
5. Generate correlated 2D data; plot it; **guess the direction of greatest variance by eye**
6. Compute the covariance matrix and its eigenvectors. **Plot them on the data.** Did your guess match?
7. Project onto the first component. How much variance is retained?
8. **Compare with `sklearn.decomposition.PCA`.** Same directions? *(Signs may flip — that is fine, and understanding why is the exercise.)*

**The cautions (9–10)**
9. **PCA without scaling**, on data with one feature in thousands and one in tens. **Watch component 1 become "the big feature".** Then scale and redo.
10. Apply PCA to your Project 2 feature matrix. Plot the explained-variance ratio. **How many components for 90%?** Then: **would you actually use it here? Argue both sides.**

**Chapter exercises (p. 146)** — do them, check against Appendix B. **Chapter 4 is complete after today.**

---

## 🔬 Understanding Check

1. **Understanding.** What is an eigenvector, geometrically? Do not use the word "eigenvalue" in your answer.
2. **Reasoning.** Why does a rotation matrix have no real eigenvectors? Answer with the picture.
3. **Connection.** Why does a zero eigenvalue mean `det = 0`? Connect it to yesterday's four statements.
4. **Application.** Why are the eigenvectors of the covariance matrix the directions of greatest variance?
5. **Judgement.** Exercise 9: what happened without scaling? Why is this the most common PCA mistake?
6. **Trade-off.** PCA costs interpretability. When is that worth paying, and when is it not?
7. **Application.** Exercise 10: would you use PCA on your data? Argue both sides, then decide.
8. **Integration.** Days 65–68 in one paragraph: what is a dataset, what is a model, and what is fitting?

---

## 🎯 Expected Outcome

- [ ] Explain an eigenvector as a direction that does not rotate
- [ ] Connect eigenvalues to determinants and rank
- [ ] Build PCA from the covariance matrix
- [ ] Know why scaling matters and what interpretability costs
- [ ] **Essential Math Chapter 4 complete**

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 142–146 | 30 min |
| 3Blue1Brown Ch. 14 | 17 min |
| The PCA section | 20 min |
| Exercises 1–10 | 75 min |
| **Chapter 4 exercises + checking** | 30 min |
| Daily review | 8 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

Eight minutes. Explain PCA to someone who knows what a scatter plot is and nothing else. No matrices, no eigenvectors — just the picture and the trade-off. Then say when you would not use it.

---

## 🔁 Daily Review

1. Exercise 1: did I find the eigenvectors by eye before computing them?
2. Exercise 9: what did unscaled PCA produce?
3. Would I use PCA on my own data? What decided it?
4. **Chapter 4 exercise score: ___ / ___.** Which did I get wrong?
5. **Linear algebra is done. ML starts tomorrow.** Does "fitting a model" still feel like magic?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 142–146 read, 3Blue1Brown Ch. 14 watched
- [ ] Eigenvectors found visually *before* computing them
- [ ] The zero-eigenvalue case connected to `det = 0`
- [ ] PCA built from the covariance matrix and matched against sklearn
- [ ] The unscaled-PCA failure demonstrated
- [ ] A decision made about PCA on your own data, with reasons
- [ ] **Chapter 4 exercises complete and checked**
- [ ] Committed to git

---

**[← Day 67](../Day_67/Day_67.md)** · **[Day 69 →](../Day_69/Day_69.md)** · [README](../../../README.md)
