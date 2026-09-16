# Day 69 — What Machine Learning Actually Is

|  |  |
|:--|:--|
| **Date** | Monday, 23 November 2026 |
| **Position** | Week 10 · Month 3 · **Phase 6 — Machine Learning begins** |
| **Budget** | **~75 min** |
| **Code file** | `Day_69.py` |

> **Why the first ML day has almost no modelling in it.** Sixty-eight days of foundation exist so that today can be honest. Most people meet machine learning as a library — `fit`, `predict`, an accuracy number — and never find out what the number means or when the whole approach is wrong.
>
> Today is the framing: what ML is, what it is not, when it is the wrong tool, and the one mistake that invalidates more student projects than any other. **Eleven days of ML follow. They are deliberately narrow** — regression, classification, and an unusual amount of time on evaluation — because a person who deeply understands three models and validation is employable, and a person who has run nine models and cannot tell a good one from a lucky one is not.

---

## 🎯 Objective

Be able to say what machine learning is in terms of the mathematics you already know, and recognise when it is the wrong tool.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians ML Part 1](https://www.youtube.com/playlist?list=PLaldQ9PzZd9qT0KsKJ7yCq70iFFP3MFJ5) · **`0:00 → 0:28`** · @1.75× | PRIMARY | 16 min | Definitions, the three types, where ML sits |
| The sections below | REFERENCE | 30 min | **The framing. This is the day's real content.** |

**Watch only the first 28 minutes.** The rest of Part 1 is EDA and preprocessing, which you did properly across Days 32–41. Re-watching it would be exactly the content consumption this plan is designed against.

### 🟢 IF TIME

- [Sheryians ML Part 1 `0:28 → 1:01`](https://www.youtube.com/playlist?list=PLaldQ9PzZd9qT0KsKJ7yCq70iFFP3MFJ5) — the ML-specific framing of EDA and feature selection. Watch at 2× and skip anything you already know.

---

## 🧠 Core Concepts

### What it is, in terms you already have

> **Machine learning is finding a function that maps inputs to outputs, by searching for the parameters that minimise error on examples.**

Break that against what you know:

| The phrase | What it is | Day |
|:-----------|:-----------|:---:|
| "a function that maps inputs to outputs" | `f(x) = y` — Chapter 1's definition of a function | 10 |
| "inputs" | A feature matrix `X`, a cloud of points | 65 |
| "parameters" | A weight vector `β` | 65 |
| "maps" | `X @ β` — a matrix multiplication | 66 |
| "minimise error" | An optimisation — follow the derivative downhill | 25, 72 |
| "on examples" | A **sample**, so the result is a sample statistic | 48 |

**That last row is the one everyone skips, and it is why statistics came first in this plan.** Your model's accuracy is a number computed on one sample. It has a standard error. It has a confidence interval. A model scoring 94% on 100 test cases and one scoring 94% on 10,000 are not the same claim — which is Day 47's beta distribution, applied to a model.

### The three types

| Type | You have | You want | Example |
|:-----|:---------|:---------|:--------|
| **Supervised** | Inputs **and** known answers | Predict the answer for new inputs | Price prediction, churn, spam |
| **Unsupervised** | Inputs only | Structure | Customer segments (Day 86) |
| **Reinforcement** | An environment and a reward | A policy | Out of scope, and mostly not what companies do |

**Supervised is nearly all of commercial machine learning**, and it splits in two:

- **Regression** — the answer is a number *(Days 71–74)*
- **Classification** — the answer is a category *(Days 75–78)*

### The workflow, and where the time actually goes

```
    business question          ← the step that decides whether any of it matters
          ↓
    get and clean data         ← 60-80% of the real time
          ↓
    SPLIT: train / test        ← before looking at anything
          ↓
    explore TRAIN only         ← the discipline that makes the rest valid
          ↓
    features → model → tune
          ↓
    evaluate on TEST, once
          ↓
    interpret, and state limits
```

**The split comes third, not seventh.** Every roadmap in `Tem.txt` shows EDA before splitting. That ordering is how leakage happens — and leakage is the single most common reason a student project reports 0.97 and is worthless.

### Leakage — the mistake that invalidates projects

**Leakage is when information that would not be available at prediction time gets into training.**

| Form | Example | Result |
|:-----|:--------|:-------|
| **Target leakage** | A `discount_applied` column that only exists for completed orders | Near-perfect score, useless model |
| **Train–test contamination** | Scaling or imputing before splitting | Test set is no longer independent |
| **Temporal leakage** | Random split on time-series data | You trained on the future |
| **Duplicate leakage** | The same customer in both sets | The model memorised rather than learned |

**The test that catches most of it:** *for every feature, ask — would I actually know this value at the moment I need the prediction?* If not, it leaks.

**The symptom:** a score that seems too good. Treat 0.99 as a bug report until proven otherwise. You will build a leaking model deliberately on Day 74 so you recognise the feeling.

### When machine learning is the wrong answer

| Situation | Better |
|:----------|:-------|
| You need to know *why* | A statistical model, or a simple rule |
| Little data | Domain rules |
| A rule already works | Keep the rule. It is explainable and free. |
| The question is descriptive | SQL and a chart — Projects 1 and 2 |
| The cost of being wrong is very high | A human, possibly assisted |
| Nobody agrees what "correct" means | Define that first |

**A good analyst's most valuable ML skill is often saying "this does not need a model."** A `CASE WHEN` that a shopkeeper can read and override beats a random forest nobody trusts.

### The baseline rule

**Before any model, establish what "no model" achieves.**

| Problem | Baseline |
|:--------|:---------|
| Regression | Always predict the mean |
| Classification | Always predict the majority class |
| Time series | Predict the last value |
| Any | The existing business rule |

**If your model does not clearly beat the baseline, you do not have a model.** And a baseline of 94% — because 94% of transactions are not fraud — is why "94% accurate" can mean "learned nothing". That is Day 76.

---

## 💻 Code

`Day_69.py` — seven exercises. Mostly reasoning; deliberately little modelling.

1. **Rewrite the definition** of machine learning using the mathematics of Days 65–68. No jargon borrowed from elsewhere.
2. **Classify ten problems** as supervised regression, supervised classification, unsupervised, or *not a machine learning problem at all*. At least three should be the last category.
3. **Build the baselines.** On a real dataset, compute mean-prediction RMSE and majority-class accuracy. **These are the numbers any model must beat.**
4. **Find the leakage.** Given a list of twelve candidate features for predicting whether an order is delivered late, mark each as safe or leaking, and say why.
5. **The availability test:** for each feature in your Project 2 data, write down whether it would be known at prediction time.
6. **Three problems where ML is the wrong tool** — from your own experience, LifeOS, or SwiftBase. Say what you would do instead.
7. **The project brief.** Write a one-paragraph problem statement for Project 3 *(which starts on Day 80)*: the question, the target, the features you would have, and the baseline you must beat.

Exercise 7 matters. Deciding the problem now means Days 71–79 can be studied with a specific use in mind — and that is the difference between learning a method and learning it *for something*.

---

## 🔬 Understanding Check

1. **Definition.** Define machine learning using only concepts from Days 65–68.
2. **Reasoning.** Why must the train–test split happen before exploration rather than after?
3. **Application.** Exercise 4: which feature was the subtlest leak? How would you have caught it in real work?
4. **Judgement.** Exercise 3: what is the baseline for your intended Project 3 problem? What would beating it by 2% be worth?
5. **Reasoning.** Give a concrete situation where a `CASE WHEN` rule beats a trained model, and say why.
6. **Connection.** Your model's accuracy is a sample statistic. What follows from that? *(Two things.)*
7. **Scoping.** What is your Project 3 question? Is the data available, and do you know the answer for past cases?

---

## 🎯 Expected Outcome

- [ ] Define machine learning without mystique
- [ ] Classify a problem, including recognising non-problems
- [ ] Compute a baseline before modelling
- [ ] Spot leakage using the availability test
- [ ] Have a Project 3 problem chosen

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians ML Part 1 `0:00 → 0:28` @1.75× | 16 min |
| The framing | 30 min |
| Seven exercises | 24 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Five minutes. A manager says: *"Can we use AI to predict which customers will leave?"*

Answer in four parts: what you would need, what the baseline is, what could leak, and **one reason this might not be worth building.**

---

## 🔁 Daily Review

1. Which of my ten classifications in exercise 2 was hardest, and why?
2. Exercise 4: the subtlest leak, and how I would have caught it.
3. What is my Project 3 question, and what is its baseline?
4. Does "fitting a model" still feel like magic after Days 65–68?

---

## 📦 Completion Criteria

- [ ] The definition rewritten in terms of vectors and matrices
- [ ] Ten problems classified, including three non-ML ones
- [ ] Baselines computed on real data
- [ ] Twelve features assessed for leakage
- [ ] The availability test applied to Project 2's features
- [ ] **The Project 3 brief written**
- [ ] Committed to git

---

**[← Day 68](../Day_68/Day_68.md)** · **[Day 70 →](../Day_70/Day_70.md)** · [README](../../../README.md)
