# Day 71 — Linear Regression: Fitting a Line, Properly

|  |  |
|:--|:--|
| **Date** | Wednesday, 25 November 2026 |
| **Position** | Week 11 · Month 3 · Phase 6 — Machine Learning |
| **Budget** | **~75 min** |
| **Code file** | `Day_71.py` |
| **Reading** | 📐 **Essential Math Ch. 5, pp. 147–161** |

> **You have already done this.** On Day 67 you solved `β = solve(XᵀX, Xᵀy)` and matched sklearn. Today gives that line its name, its justification, and its assumptions.
>
> **Why linear regression is worth four days** when it is the simplest model there is: it is interpretable, it is the foundation of logistic regression and of a neural network layer, its assumptions are the ones every model inherits, and **it is the model most often used in real business analysis** — because a coefficient someone can read beats a forest nobody trusts.

---

## 🎯 Objective

Understand what "best fit" means, why squared error was chosen, and the two ways to find the coefficients.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 5, pp. 147–161** | **PRIMARY** · reading + code | 35 min | Basic regression · residuals · squared error · closed form · inverse matrix |
| [StatQuest — Linear Regression](https://www.youtube.com/watch?v=nk2CQITm_eo) | **REINFORCEMENT** | 27 min | The picture, and where R² comes from |

**Read first, watch second** — the video will then confirm rather than introduce.

### 🟢 IF TIME

- [Sheryians ML Part 2 `0:06:29 → 0:46:30`](https://www.youtube.com/playlist?list=PLaldQ9PzZd9qT0KsKJ7yCq70iFFP3MFJ5) — regression fundamentals and the cost function, with a scikit-learn walkthrough.

---

## 🧠 Core Concepts

### The model

```
ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
```

or, as you saw it on Day 66:

```python
predictions = X @ beta
```

**A linear combination of the features** — Day 65's phrase. "Linear" means linear *in the coefficients*, not in the data: `y = β₀ + β₁x + β₂x²` is still a linear model, because you can create `x²` as a column and the coefficients still enter linearly. That distinction is worth holding, because it means linear models can fit curves.

### Residuals, and why squared

A **residual** is `yᵢ − ŷᵢ` — what the model missed on that row.

Why not just sum them? **Positive and negative residuals cancel**, so a terrible model can sum to zero. So you need a measure that treats both directions as error:

| Option | Behaviour |
|:-------|:----------|
| Sum of absolute errors | Robust to outliers, **no closed-form solution**, not differentiable at zero |
| **Sum of squared errors** | Differentiable everywhere, has a closed form, **and punishes large errors disproportionately** |

**Squared error is a choice with consequences.** Doubling an error quadruples its cost, so the fit is pulled hard towards outliers. That is sometimes right — a forecast that is wildly wrong once may be worse than one slightly wrong often — and sometimes badly wrong. Knowing it is a choice rather than a law is the point.

*(There is a deeper justification — squared error is the maximum-likelihood estimate under normally distributed errors — which is worth knowing exists. Nield mentions it; you do not need it today.)*

### Two ways to find β

**1. The closed form — the normal equations**

```
β = (XᵀX)⁻¹ Xᵀy
```

```python
beta = np.linalg.solve(X.T @ X, X.T @ y)     # never inv() -- Day 67
```

Exact, one step, no tuning. **And it fails when `XᵀX` has no inverse** — Day 67's four statements — which is what multicollinearity does.

It is also `O(n³)` in the number of features, so it becomes impractical above a few thousand columns.

**2. Gradient descent** — tomorrow. Iterative, works at any scale, and it is how every model beyond linear regression is actually fitted.

**scikit-learn's `LinearRegression` uses neither exactly** — it uses a least-squares solver (SVD-based) that is numerically stable even when `XᵀX` is close to singular. Worth knowing when your hand-written version disagrees with it slightly.

### The assumptions — and what breaking each does

| Assumption | If broken |
|:-----------|:----------|
| **Linearity** — the relationship really is a line | The model is wrong, no matter how much data you add |
| **Independence** — observations do not influence each other | Standard errors too small → false significance |
| **Homoscedasticity** — error spread is constant across x | Coefficients still unbiased, but intervals wrong |
| **Normal residuals** — approximately | Matters for intervals and p-values on small samples |
| **No perfect multicollinearity** | No unique solution at all |

**Check by plotting residuals against fitted values.** A random cloud means fine. A curve means non-linearity. A widening fan means heteroscedasticity. **That single plot catches more problems than any test statistic**, and it takes ten seconds.

### The interpretation — and the sentence to avoid

> **βⱼ is the expected change in y for a one-unit increase in xⱼ, holding all other features constant.**

"Holding all others constant" is doing enormous work. If two features move together in reality, holding one constant describes a situation that never occurs — and the coefficient describes an imaginary world.

**And never:** "a one-unit increase in x *causes* a βⱼ change in y." You have a correlation with a line through it. Day 43's rule, and it remains the fastest way to lose credibility with anyone experienced.

---

## 💻 Code

`Day_71.py` — nine exercises.

**Seeing it (1–3)**
1. Generate data with a known relationship; plot it; **draw a line by eye and record your guess for the slope**
2. Compute the residuals for your eyeballed line and for the fitted line; compare the sums of squares
3. **Why squared:** compute the sum of raw residuals for a deliberately terrible model. **It is near zero.** Then do the same with squares.

**Fitting (4–6)**
4. Fit by the closed form with `solve`. Compare with your eyeball guess.
5. Compare against `sklearn.LinearRegression`. **Do they agree to how many decimal places?**
6. **Break it:** add a perfectly collinear column. Watch `solve` fail, and watch sklearn *not* fail. **What did sklearn silently do?**

**Diagnostics (7–9)**
7. **The residual plot.** Fit a line to genuinely curved data. Look at the residuals. **The curve is obvious there and invisible in R².**
8. Build heteroscedastic data; see the fan in the residual plot
9. Fit on your Project 3 data. Interpret one coefficient in a full sentence — including the "holding constant" clause and what it assumes.

---

## 🔬 Understanding Check

1. **Reasoning.** Why square the residuals rather than take absolute values? Name a cost of that choice.
2. **Application.** Exercise 3: what was the sum of raw residuals for the bad model? What does that show?
3. **Connection.** `β = solve(XᵀX, Xᵀy)` fails when `XᵀX` is singular. Connect that to Day 67's four statements.
4. **Debugging.** Exercise 6: sklearn did not fail where your solver did. What did it do, and is that good or dangerous?
5. **Diagnostics.** Exercise 7: what did the residual plot show that the fit statistics did not?
6. **Interpretation.** Write a full interpretation of one coefficient, including the assumption that makes it questionable.
7. **Judgement.** Which of the five assumptions is most likely violated in your Project 3 data? How would you check?

---

## 🎯 Expected Outcome

- [ ] Explain "best fit" in terms of squared residuals, and why squared
- [ ] Fit by the closed form and match sklearn
- [ ] Read a residual plot
- [ ] Interpret a coefficient precisely, without implying causation

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 147–161 | 35 min |
| StatQuest linear regression | 27 min |
| Nine exercises | 30 min |
| Daily review | 5 min |
| **Total** | **~95 min** — if over, drop the StatQuest video to tomorrow |

---

## 🧪 Mini Assessment

Six minutes. Given a fitted model `price = 12000 + 3200×area − 850×age`:

1. Interpret each coefficient in a full sentence
2. What does the intercept mean here? Is it meaningful?
3. Name one thing this model cannot tell you that someone will ask it to

---

## 🔁 Daily Review

1. How close was my eyeballed slope to the fitted one?
2. Exercise 6: what did sklearn do that my solver would not?
3. What did the residual plot in exercise 7 reveal?
4. Which assumption is most at risk in my Project 3 data?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 147–161 read
- [ ] A line fitted by eye, then by closed form, and compared
- [ ] The cancelling-residuals demonstration run
- [ ] sklearn agreement checked to decimal places
- [ ] The collinear break demonstrated on both solvers
- [ ] Residual plots produced for curved and heteroscedastic data
- [ ] One coefficient interpreted in full, with its assumption
- [ ] Committed to git

---

**[← Week 10 Review](../../Week_10/Week_10_Review.md)** · **[Day 72 →](../Day_72/Day_72.md)** · [README](../../../README.md)
