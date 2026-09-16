# Day 80 — Project 3: Set Up To Be Honest

|  |  |
|:--|:--|
| **Date** | Friday, 4 December 2026 |
| **Position** | Week 12 · Month 3 · Phase 6 |
| **Budget** | **~75 min** |
| **Code file** | `project_3/src/data.py` |
| **Starts today** | 🤖 **Project 3 — the end-to-end machine learning project** |

> **This is the project that matters most.** Project 1 showed you can analyse. Project 2 showed you can query and recommend. Project 3 has to show you can build a model **and be honest about it** — which is the rarer and more valuable thing, because almost every junior portfolio contains a model and almost none contain an honest evaluation of one.
>
> **Six days: 80 to 85.** The brief was written on Day 69, the leakage audit on Day 74, the pipeline on Day 79. Today is not "decide what to build" — today is **build the infrastructure that makes the next five days trustworthy.**

---

## 🎯 Objective

Get the data, split it correctly, compute the baseline, and establish the evaluation protocol — before any modelling.

---

## 📋 The Brief

### What it must contain

| | Required |
|:--|:--|
| A real question with a stated decision behind it | ✅ |
| A target defined precisely enough to reproduce | ✅ |
| Features that pass the availability test | ✅ |
| **A baseline, computed first** | ✅ |
| A split strategy chosen for the data's structure | ✅ |
| A metric chosen from the cost of each error | ✅ |
| **Honest evaluation, including where it fails** | ✅ |
| A written recommendation with limitations | ✅ |

### What it must not be

**No Titanic, no Iris, no Boston Housing.** A reviewer who sees those closes the tab.

**Candidate problems, if Day 69's brief needs replacing:**

| Problem | Data | Why it works |
|:--------|:-----|:-------------|
| **Will this Olist order be delivered late?** | Olist — already loaded from Project 2 | Real, imbalanced, rich features, a genuine business decision |
| **Will this customer order again within 90 days?** | Olist | Classic retention; needs careful temporal handling |
| **What review score will this order receive?** | Olist | Ordinal target, connects operations to sentiment |
| **Predict next month's SPI for an item** | PBS — Project 1 | Time series; needs `TimeSeriesSplit` and honest lag features |
| **Predict the price band of a product** | PBS or Olist | Multi-class, and the class balance is interesting |

**The late-delivery problem is the strongest default** — you already have the data, it is imbalanced enough to make Day 76's metrics matter, and "which orders should we warn the customer about?" is a decision someone would actually make.

---

## 💻 Code

### 🔴 MUST DO (75 min)

**1. Fix the problem statement (10 min)** — in `project_3/README.md`, write:
- The question, in one sentence
- The decision it informs, and who makes it
- The target, defined precisely
- **What a wrong prediction costs, in each direction**

**2. Build the dataset (25 min)** — `src/data.py`
- Load, join, and produce one row per prediction unit
- **Check the grain.** One row per order, per customer, per customer-month?
- Apply the Day 74 availability test to every column, and **drop the leaks in code, with a comment saying why**
- Save to `data/processed/`

**3. Split — before anything else (15 min)**
- Choose the strategy and **write the reason**: random, stratified, time-ordered or grouped
- **If there is any time dimension, use it.** Random splits on temporal data are Day 74's form 3.
- Split, and save the test set separately. **You will touch it once, on Day 82.**

**4. Compute the baseline (10 min)**
- Classification: the majority-class rate
- Regression: predicting the mean
- **And the business baseline** — what does the current rule or process achieve?
- **Write these numbers in the README now.** Every later number gets compared with them.

**5. Fix the evaluation protocol (15 min)** — write it down *before* seeing any model output:
- The primary metric, and why *(Day 76's cost reasoning)*
- The cross-validation scheme
- What improvement over baseline would make this worth deploying
- **What result would make you abandon the project**

That last point is the Day 54 discipline: deciding what would change your mind *before* you have results is the only reliable defence against finding what you hoped for.

---

## 🔬 Understanding Check

1. **Framing.** What decision does this inform, and who makes it? If you cannot name a person, the framing is too abstract.
2. **Definition.** Read your target definition aloud. Could someone else reproduce the exact same column from it?
3. **Leakage.** Which columns did you drop, and why? Which was the hardest call?
4. **Splitting.** Why that split strategy? What would the wrong one have done?
5. **Baseline.** What are the three baselines? Which is the honest comparison?
6. **Protocol.** What result would make you abandon this? Be specific.
7. **Costs.** What does a false positive cost, and a false negative? Put numbers on both.

---

## 🎯 Expected Outcome

- [ ] A precise problem statement with a named decision
- [ ] A dataset at the right grain, with leaks removed in code
- [ ] A split chosen for the data's structure, test set untouched
- [ ] Three baselines computed and written down
- [ ] An evaluation protocol fixed **before** any modelling

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Problem statement | 10 min |
| Dataset construction | 25 min |
| Split | 15 min |
| Baselines | 10 min |
| Evaluation protocol | 15 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

**No model today.** The day passes when someone could read your README and know exactly what you are predicting, what it is worth, what you are comparing against, and what would count as failure — **without seeing a single result.**

---

## 🔁 Daily Review

1. What are my three baselines?
2. Which leaking column was the hardest call?
3. What would make me abandon this project?
4. Did I resist fitting a model today? *(If you fitted one, note it — and note whether it changed how you set up the evaluation.)*

---

## 📦 Completion Criteria

- [ ] Problem statement written, with the decision and the costs
- [ ] `src/data.py` produces a dataset at a documented grain
- [ ] Leaking columns dropped in code, with reasons
- [ ] Split done, strategy justified, **test set set aside untouched**
- [ ] Three baselines computed and in the README
- [ ] Evaluation protocol written **before** any modelling
- [ ] Committed to git

---

**[← Day 79](../Day_79/Day_79.md)** · **[Day 81 →](../Day_81/Day_81.md)** · [README](../../../README.md)
