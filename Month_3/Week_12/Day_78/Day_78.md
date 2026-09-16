# Day 78 — Trees and Forests

|  |  |
|:--|:--|
| **Date** | Wednesday, 2 December 2026 |
| **Position** | Week 12 · Month 3 · Phase 6 |
| **Budget** | **~75 min** |
| **Code file** | `Day_78.py` |

> **Why trees get one day and not three.** They are the other half of practical machine learning — everything so far has been linear, and trees are the main non-linear family you will actually meet. A gradient-boosted tree is what usually wins on tabular business data.
>
> **But one day is enough**, because the ideas are simpler than regression's and because the thing that makes a tree project good is still validation, not the model. This is also the first day on the **cut list** if you are behind — see the Month 2 Review.

---

## 🎯 Objective

Understand how a tree splits, why a single tree overfits, how a forest fixes it, and why feature importance is less trustworthy than it looks.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [StatQuest — Decision and Classification Trees](https://www.youtube.com/watch?v=_L39rN6gz7Y) | **PRIMARY** | 18 min | How a split is chosen |
| [StatQuest — Random Forests Part 1](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ) | **PRIMARY** | 10 min | Bagging, and why it works |
| The sections below | REFERENCE | 15 min | Importance, and the limits |

### 🟢 IF TIME

- [StatQuest — Regularization: Ridge](https://www.youtube.com/watch?v=Q81RR3yKn30) and [Lasso](https://www.youtube.com/watch?v=NGf0voTMlcs) — 40 minutes for both, and they are the other main answer to overfitting. Worth it if you have the time.

---

## 🧠 Core Concepts

### How a tree decides

At each node, try every feature and every threshold, and pick the split that most reduces impurity.

| Measure | Used for |
|:--------|:---------|
| **Gini** | Classification — the default, slightly faster |
| **Entropy** | Classification — nearly identical results |
| **MSE** | Regression |

**A tree is a sequence of if-statements**, learned rather than written. That is its great advantage: a shallow tree can be printed and handed to a shopkeeper.

**What trees do well:**
- Non-linear relationships, without you specifying the form
- Interactions, automatically
- Mixed feature types
- **No scaling needed** — splits are order-based, so units do not matter *(unlike everything in Days 71–76)*

**What they do badly:**
- **A single tree overfits badly.** Grown fully, it memorises.
- Unstable — small data changes give a different tree
- Cannot extrapolate beyond the range it was trained on
- Biased towards high-cardinality features

### Why a forest fixes it

**Bagging:** train many trees, each on a bootstrap sample of the rows, each considering a random subset of features at every split. Average their predictions.

The randomness **decorrelates** the trees. Individually each is mediocre and overfit; averaged, their errors cancel and the variance falls dramatically. **This is the bias–variance trade-off from Day 74, exploited deliberately.**

| Parameter | Does |
|:----------|:-----|
| `n_estimators` | More trees — monotonically better, then flat. 100–500 is usually enough. |
| `max_depth` | The main overfitting control |
| `min_samples_leaf` | Prevents leaves fitted to one row |
| `max_features` | How much decorrelation |

**Random forests are hard to overfit with more trees** — adding trees does not hurt, unlike adding depth. That makes them forgiving, which is part of why they are so widely used.

### Feature importance — and why to distrust it

`.feature_importances_` looks like an answer to "what drives this?" **It is not, quite.**

| Problem | |
|:--------|:|
| **Biased towards high-cardinality features** | A continuous feature offers more split points, so it accumulates importance |
| **Splits importance across correlated features** | Two correlated features each get half, so both look unimportant |
| **Measures usefulness for splitting, not causation** | A leaky feature is the most "important" of all |
| **Computed on training data** by default | It can reflect memorisation |

**Use permutation importance instead** — shuffle one column, measure how much test performance drops. It measures what the model actually relies on, on held-out data, and it is one extra line.

**And in every case, importance is not causation.** "Support tickets is the most important feature for churn" does not mean reducing tickets reduces churn. Day 43's rule, again.

### Boosting, briefly

Gradient boosting builds trees **sequentially**, each correcting the previous one's errors. XGBoost and LightGBM are the standard implementations, and they are what usually win on tabular data.

**They are also easier to overfit** and need more careful tuning than a random forest. **Out of scope for these ninety days** — noted here so you know the name, and so that "should I use XGBoost?" has an answer: not until a random forest with honest validation is not enough.

---

## 💻 Code

`Day_78.py` — nine exercises.

**A single tree (1–4)**
1. Fit a depth-2 tree; **print it as text and read the rules aloud.** This is the interpretability advantage.
2. **Watch it overfit:** depths 1 to 20, plot train and test accuracy. **Find where they diverge.** *(Day 74's curve, on a different model.)*
3. Fit an unlimited-depth tree: train accuracy 1.0, test much lower
4. Control it with `max_depth`, `min_samples_leaf` and `min_samples_split`; note which helps most

**Forests (5–6)**
5. Random forest against the single tree; compare the train–test gap
6. `n_estimators` from 1 to 500; plot test performance. **Where does it flatten?**

**Importance (7–9)**
7. `.feature_importances_` — plot them
8. **Permutation importance.** Compare with the built-in. **Where do they disagree, and which do you believe?**
9. **The cardinality bias:** add a pure-noise column with many unique values. **Watch it rank as important.** Then check permutation importance on it.

---

## 🔬 Understanding Check

1. **Understanding.** How does a tree choose a split?
2. **Reasoning.** Why does a single tree overfit so badly, and why does averaging many fix it?
3. **Application.** Exercise 2: at what depth did train and test diverge?
4. **Reasoning.** Why do trees need no feature scaling when Days 71–76's models do?
5. **Judgement.** Exercise 9: what importance did the noise feature get? What does that teach you?
6. **Comparison.** Built-in versus permutation importance — where did they disagree, and why?
7. **Interpretation.** Your forest says `support_tickets` is most important for churn. What can and cannot you conclude?
8. **Judgement.** For Project 3 — linear model or forest? Argue both sides, then decide on interpretability and on performance separately.

---

## 🎯 Expected Outcome

- [ ] Explain a split and read a printed tree
- [ ] Diagnose tree overfitting from depth curves
- [ ] Explain why bagging reduces variance
- [ ] Distrust feature importance appropriately, and use permutation importance

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| StatQuest trees + forests | 28 min |
| Importance and limits | 15 min |
| Nine exercises | 27 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Five minutes. A random forest gets 0.89 test accuracy; a logistic regression gets 0.86. The business needs to explain every decision to customers.

**Which do you ship, and what do you say about the 3%?**

---

## 🔁 Daily Review

1. Exercise 2: where did the depth curves diverge?
2. Exercise 9: how important did the pure-noise feature look?
3. Where did the two importance measures disagree?
4. Linear or forest for Project 3? What decided it?

---

## 📦 Completion Criteria

- [ ] A depth-2 tree printed and its rules read aloud
- [ ] Depth-vs-accuracy curves plotted, divergence found
- [ ] Forest compared against a single tree on the train–test gap
- [ ] `n_estimators` curve plotted, flattening point noted
- [ ] Permutation importance compared against built-in
- [ ] The cardinality-bias demonstration run
- [ ] A Project 3 model-family decision written with reasons
- [ ] Committed to git

---

**[← Week 11 Review](../../Week_11/Week_11_Review.md)** · **[Day 79 →](../Day_79/Day_79.md)** · [README](../../../README.md)
