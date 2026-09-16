# Day 75 — Logistic Regression: Predicting a Yes or No

|  |  |
|:--|:--|
| **Date** | Sunday, 29 November 2026 |
| **Position** | Week 11 · Month 3 · Phase 6 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_75.py` |
| **Reading** | 📐 **Essential Math Ch. 6, pp. 193–211** |

> **The model most used in practice, and the one most often misread.** Logistic regression is the default for classification in banking, medicine, insurance and risk — not because it is the most accurate, but because **its coefficients can be explained to a regulator.** That combination of good-enough and defensible is what real deployments need.
>
> **And it is where three earlier days converge.** Day 18's logarithms, Day 18's Euler's number, and Day 72's gradient descent — because logistic regression has *no closed-form solution*, so it must be fitted iteratively. That is why gradient descent came first.

---

## 🎯 Objective

Understand how a linear model is turned into a probability, fit one, and interpret its coefficients as odds rather than as slopes.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 6, pp. 193–211** | **PRIMARY** · reading + code | 50 min | The logistic function · fitting · multivariable · log-odds |
| [StatQuest — Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8) | **REINFORCEMENT** | 9 min | The shape and the intuition |
| The log-odds section below | REFERENCE | 20 min | The interpretation — the part people get wrong |

### 🟢 IF TIME

- [Sheryians ML Part 3 `0:08:32 → 0:56:24`](https://www.youtube.com/playlist?list=PLaldQ9PzZd9qT0KsKJ7yCq70iFFP3MFJ5) — logistic regression with a scikit-learn walkthrough.

---

## 🧠 Core Concepts

### Why linear regression cannot do this

Predict "will this customer churn?" — the answer is 0 or 1. Fit a line and you get:

- Predictions above 1 and below 0, which are not probabilities
- An assumption that the effect is constant, when going from 10% to 20% likely is not the same as going from 80% to 90%
- Residuals that are never normal, so every interval and p-value is wrong

### The logistic function

```
p = 1 / (1 + e^(−z))     where   z = β₀ + β₁x₁ + ... + βₙxₙ
```

**The inside is a linear model.** `z` is exactly `X @ beta` from Day 66. The logistic function then squashes any real number into `(0, 1)`.

| z | p |
|:--|:--|
| −5 | 0.007 |
| −1 | 0.27 |
| 0 | **0.50** |
| 1 | 0.73 |
| 5 | 0.993 |

**That `e` is Day 18's Euler's number.** It is not decoration — it is what makes the derivative clean, which is what makes gradient descent work on this model.

### No closed form — which is why Day 72 mattered

Linear regression has `β = solve(XᵀX, Xᵀy)`. **Logistic regression has nothing equivalent.**

The error measure is not squared error but **log loss**:

```
log_loss = −(1/n) Σ [ y·log(p) + (1−y)·log(1−p) ]
```

Read what it does: when `y = 1`, only `log(p)` survives, and it punishes a confident wrong answer brutally — predicting 0.01 for something that happened costs `−log(0.01) ≈ 4.6`, while predicting 0.4 costs only 0.9. **Log loss punishes confident mistakes far more than uncertain ones**, which is exactly what you want from a probability model.

*(Squared error is not used here because it makes the surface non-convex, so gradient descent can get stuck. Log loss keeps it convex.)*

### Log-odds — the interpretation people get wrong

```
odds = p / (1 − p)              a probability of 0.75 is odds of 3, or "3 to 1"
log-odds = log(odds) = z        THE LINEAR PART
```

**This is the key sentence:** *logistic regression is a linear model **in the log-odds**.* The relationship is linear in `z`, not in `p`.

So a coefficient means:

> **βⱼ is the change in log-odds for a one-unit increase in xⱼ.**

And because nobody thinks in log-odds, exponentiate:

> **e^βⱼ is the odds ratio — the multiplicative change in the odds.**

| βⱼ | e^βⱼ | Means |
|:--|:--|:--|
| 0 | 1.00 | No effect |
| 0.5 | 1.65 | Odds increase 65% |
| 1.0 | 2.72 | Odds nearly triple |
| −0.7 | 0.50 | Odds halve |

**The mistake:** "e^β = 2 means the probability doubles." **It does not.** Odds double, and what that does to the probability depends entirely on where you started — from 0.10 the probability goes to 0.18, from 0.50 it goes to 0.67, and from 0.90 it barely moves. Saying "probability doubles" in a meeting is the single most common error in reading a logistic model, and it is often wrong by a large margin.

### The threshold is a business decision, not a default

The model outputs a probability. Turning it into a decision needs a cutoff, and **0.5 is a convention, not an answer.**

| Situation | Threshold |
|:----------|:----------|
| Screening for a treatable disease | **Low** — missing a case is far worse than a false alarm |
| Blocking a transaction as fraud | **High** — blocking a genuine customer has a real cost |
| Sending a retention offer | Wherever the offer stops being worth the cost |

**The right threshold comes from the relative cost of the two errors**, which is a business question. You will choose one properly tomorrow.

---

## 💻 Code

`Day_75.py` — eleven exercises.

**The function (1–3)**
1. Plot the logistic function; verify the table above; show what changes `z`
2. Plot the effect of a coefficient's size on steepness, and of the intercept on position
3. **Why not linear:** fit a line to binary data; plot it; mark where it predicts above 1 and below 0

**Fitting (4–6)**
4. **Implement log loss from scratch.** Show what it costs to be confidently wrong.
5. **Fit by gradient descent yourself** — reuse Day 72's loop with the logistic gradient. Watch log loss fall.
6. Compare with `sklearn.LogisticRegression`. **Do the coefficients match?**

**Interpretation (7–9)**
7. Fit a multivariable model; produce a table of coefficients, odds ratios, and a plain-English sentence for each
8. **The doubling mistake:** take a coefficient with `e^β = 2`. Compute the probability change starting from 0.1, 0.5 and 0.9. **Three different answers.** Write what you would say instead.
9. Plot the predicted-probability distribution. Are predictions clustered near 0.5, or confident? What does each pattern suggest?

**Applying it (10–11)**
10. Fit on your Project 3 data if it is a classification problem; otherwise on the Olist "was it delivered late?" question
11. **The threshold experiment:** accuracy, and the two error counts, at thresholds from 0.1 to 0.9. **Which would you choose, and what business reasoning decided it?**

---

## 🔬 Understanding Check

1. **Reasoning.** Name three specific reasons linear regression fails on a binary outcome.
2. **Understanding.** What does the logistic function do to `z`? Where does Euler's number come from?
3. **Connection.** Logistic regression has no closed form. What follows from that, and which earlier day makes it possible?
4. **Reasoning.** Why log loss rather than squared error? Two reasons.
5. **Interpretation.** Write a full plain-English sentence for a coefficient of 0.69.
6. **Debugging.** Exercise 8: what were the three probability changes for the same odds ratio? What should you say instead of "the probability doubles"?
7. **Judgement.** Exercise 11: which threshold did you choose? What would have to change for you to move it?

---

## 🎯 Expected Outcome

- [ ] Explain how a linear model becomes a probability
- [ ] Fit logistic regression by gradient descent and match sklearn
- [ ] Interpret coefficients as odds ratios, correctly
- [ ] Choose a threshold from business reasoning

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 193–211 | 50 min |
| StatQuest logistic regression | 9 min |
| Log-odds | 20 min |
| Exercises 1–9 | 70 min |
| Exercises 10–11 | 25 min |
| Daily review | 6 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

Eight minutes. A churn model gives `age` a coefficient of −0.04 and `support_tickets` a coefficient of 0.31.

1. The odds ratio for each
2. A plain-English sentence for each, avoiding the doubling mistake
3. Which matters more? **What do you need to know before answering that?**

---

## 🔁 Daily Review

1. Did my gradient-descent version match sklearn's coefficients?
2. Exercise 8: how different were the three probability changes?
3. Which threshold did I choose, and on what reasoning?
4. Can I explain log-odds to someone in 60 seconds without the formula?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 193–211 read, StatQuest watched
- [ ] Log loss implemented from scratch
- [ ] Logistic regression fitted by your own gradient descent, matched against sklearn
- [ ] A coefficient table with odds ratios and plain-English sentences
- [ ] The doubling mistake demonstrated with three starting probabilities
- [ ] Thresholds swept, one chosen with a business reason
- [ ] Committed to git

---

**[← Day 74](../Day_74/Day_74.md)** · **[Day 76 →](../Day_76/Day_76.md)** · [README](../../../README.md)
