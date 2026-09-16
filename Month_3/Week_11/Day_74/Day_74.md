# Day 74 — Validation: The Day That Separates Real From Tutorial

|  |  |
|:--|:--|
| **Date** | Saturday, 28 November 2026 |
| **Position** | Week 11 · Month 3 · Phase 6 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_74.py` |
| **Reading** | 📐 **Essential Math Ch. 5, pp. 185–192 + exercises** |

> **If you keep one day from the machine learning block, keep this one.**
>
> Almost anyone can fit a model. The thing that distinguishes someone employable is knowing whether the number it produces means anything — and the honest answer is usually "less than it looks". Overfitting, leakage and improper validation are why student portfolios report 0.97 and why experienced reviewers do not believe them.
>
> **Today you will deliberately build a leaking model, get a beautiful score, and then find the leak.** That experience is worth more than any amount of reading about it, because after it you will recognise the feeling of a score that is too good.

---

## 🎯 Objective

Validate a model honestly, recognise overfitting and leakage from their symptoms, and understand the bias–variance trade-off.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 5, pp. 185–192** | **PRIMARY** · reading + code | 25 min | Train/test splits · multiple linear regression |
| [StatQuest — Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA) | **REINFORCEMENT** | 7 min | The trade-off, clearly |
| [StatQuest — Cross Validation](https://www.youtube.com/watch?v=fSytzGwwBVw) | **REINFORCEMENT** | 6 min | Why one split is not enough |
| The leakage section below | REFERENCE | 25 min | **The core of the day** |
| **Chapter 5 exercises, p. 192** | **PRACTICE** | 25 min | Answers in Appendix B |

---

## 🧠 Core Concepts

### Why a train–test split is not optional

A model can memorise. Evaluating it on data it memorised measures memory, not learning.

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
```

**The test set is touched once, at the very end.** Every time you look at it and change something, it becomes a little more like training data — and after ten such rounds it is no longer a measure of anything. This is Day 54's Texas sharpshooter, applied to model selection.

**That is why a third split exists:** train to fit, **validation** to choose, test to report. With little data, cross-validation replaces the validation set.

### Cross-validation

Split into k folds. Train on k−1, evaluate on the one left out, rotate, average.

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring="neg_root_mean_squared_error")
```

**What it buys you:** every row is used for both training and evaluation, and — more usefully — **you get a spread, not a point.** `[0.81, 0.79, 0.85, 0.62, 0.83]` tells you something `0.78` does not: one fold went badly, and that is worth investigating.

**The variants that matter:**

| Variant | When |
|:--------|:-----|
| `KFold` | The default |
| `StratifiedKFold` | **Classification** — keeps the class balance in every fold |
| `TimeSeriesSplit` | **Time-ordered data** — always train on the past, test on the future |
| `GroupKFold` | Repeated entities — keeps one customer entirely in one fold |

**Using plain `KFold` on time-series data trains on the future.** The score will be excellent and the model will fail in production.

### Overfitting and underfitting

| | Train | Test | Means |
|:--|:--|:--|:--|
| **Underfitting** | Poor | Poor | The model is too simple — high bias |
| **Good fit** | Good | Good, slightly worse | What you want |
| **Overfitting** | **Excellent** | **Poor** | Memorised the noise — high variance |

**The diagnostic is the gap.** Train R² 0.98 and test R² 0.62 is overfitting, regardless of how good 0.98 looks.

### Bias and variance

| | Is | Caused by |
|:--|:--|:--|
| **Bias** | Systematic error — wrong in the same direction every time | A model too simple for the truth |
| **Variance** | Sensitivity — a different training sample gives a very different model | A model complex enough to fit the noise |

**The trade-off:** more complexity lowers bias and raises variance. Total error falls, reaches a minimum, then rises. **Finding that minimum is what tuning is.** Exercise 5 makes you plot the curve on real data, and once you have seen it the trade-off stops being an abstraction.

### Leakage — the seven forms

**Leakage is any information in training that would not exist at prediction time.**

| # | Form | Example | Symptom |
|:-:|:-----|:--------|:--------|
| 1 | **Target leakage** | `days_late` used to predict "was it late?" | Near-perfect score |
| 2 | **Preprocessing before splitting** | `StandardScaler` or imputation fitted on all the data | Optimistic, subtly |
| 3 | **Temporal leakage** | Random split on ordered data | Excellent score, production failure |
| 4 | **Group leakage** | The same customer in train and test | Memorisation scored as learning |
| 5 | **Duplicate rows** | Exact duplicates split across both sets | Same |
| 6 | **Target encoding without folds** | Category means computed on all the data | Strong on test, weak in reality |
| 7 | **Feature selection on the full dataset** | Picking the top 20 correlated features before splitting | The test set chose its own features |

**Form 2 is the one you are most likely to commit**, because it feels harmless — and it is why `Pipeline` exists, which is tomorrow's tool and Day 79's proper treatment.

**The three defences:**
1. **The availability test** — Day 69. For each feature: would I know this at prediction time?
2. **Split first.** Before EDA, before scaling, before anything.
3. **Suspicion.** Treat any unexpectedly good score as a bug report. Go looking for the leak *before* celebrating.

---

## 💻 Code

`Day_74.py` — twelve exercises.

**Splitting (1–3)**
1. Split properly; fit; compare train and test scores; measure the gap
2. **Vary `random_state` over 20 splits.** Plot the test scores. **How much does the "test score" move purely by luck?**
3. Cross-validation, 5-fold. Compare the mean with a single split. Look at the spread.

**Overfitting (4–5)**
4. **Polynomial degrees 1 to 15** on the same data. Plot train and test error against degree. **Find where they diverge.**
5. **Learning curves:** performance against training-set size, for a simple and a complex model. **Which one would more data help?** *(This decides whether to collect more data or change the model — a real, expensive decision.)*

**Leakage — build each one (6–9)**
6. **Target leakage.** Add a feature derived from the target. **Get R² above 0.99.** Then find and remove it.
7. **Preprocessing leakage.** Scale before splitting versus inside a pipeline. **Measure the difference in reported score.**
8. **Temporal leakage.** Random split on time-ordered data versus `TimeSeriesSplit`. **How much better does the wrong one look?**
9. **Group leakage.** Duplicate some entities across the split. Watch the score inflate.

**Doing it right (10–12)**
10. Build the correct pipeline: split → `Pipeline(scaler, model)` → cross-validate → evaluate on test once
11. `TimeSeriesSplit` on your Project 2 data
12. **Audit Project 3.** Run the availability test on every planned feature, write the split strategy, and say which of the seven forms you are most at risk of.

**Chapter 5 exercises (p. 192)** — check against Appendix B. **Chapter 5 complete after today.**

---

## 🔬 Understanding Check

1. **Reasoning.** Why touch the test set only once? Connect it to the Texas sharpshooter.
2. **Application.** Exercise 2: how much did the test score move across random states? What does that mean for reporting a single number?
3. **Diagnosis.** Exercise 4: at what degree did train and test diverge? What is happening there?
4. **Judgement.** Exercise 5: which model would benefit from more data? How can you tell from the curves?
5. **Leakage.** Exercise 6: what R² did the leak produce? Would you have noticed without looking?
6. **Reasoning.** Exercise 7: why does scaling before splitting leak? It seems harmless — explain exactly what crosses the boundary.
7. **Application.** Exercise 8: how much better did the wrong split look? What would have happened in production?
8. **Project.** Exercise 12: which leakage form is Project 3 most at risk of, and what is your defence?

---

## 🎯 Expected Outcome

- [ ] Split, cross-validate and evaluate correctly by default
- [ ] Diagnose overfitting from the train–test gap
- [ ] Read a learning curve to decide between more data and a different model
- [ ] Recognise all seven leakage forms, having built four of them
- [ ] **Essential Math Chapter 5 complete**

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 185–192 | 25 min |
| StatQuest ×2 | 13 min |
| The leakage section | 25 min |
| Exercises 1–5 | 40 min |
| **Exercises 6–12 — build the leaks** | 50 min |
| **Chapter 5 exercises + checking** | 25 min |
| **Total** | **~178 min** |

---

## 🧪 Mini Assessment

Ten minutes. Someone hands you a model with **test R² of 0.96** predicting next-month customer spend.

Write the seven checks you would run, in order, and what each would catch.

---

## 🔁 Daily Review

1. Exercise 2: how far apart were the best and worst random splits?
2. Exercise 6: what score did my deliberate leak produce?
3. Exercise 7: how much did preprocessing leakage inflate the number?
4. **Which leakage form is Project 3 most at risk of?** Write the defence now, not on Day 81.

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 185–192 read, both StatQuest videos watched
- [ ] Twenty random splits compared, spread recorded
- [ ] The degree-vs-error curve plotted, divergence point found
- [ ] Learning curves plotted for two model complexities
- [ ] **Four leakage forms built deliberately and then fixed**
- [ ] A correct pipeline built end to end
- [ ] Project 3 leakage audit written
- [ ] **Chapter 5 exercises complete and checked**
- [ ] Committed to git

---

**[← Day 73](../Day_73/Day_73.md)** · **[Day 75 →](../Day_75/Day_75.md)** · [README](../../../README.md)
