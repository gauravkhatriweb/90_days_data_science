# Day 73 — R², Significance, and What a Coefficient Is Worth

|  |  |
|:--|:--|
| **Date** | Friday, 27 November 2026 |
| **Position** | Week 11 · Month 3 · Phase 6 |
| **Budget** | **~75 min** |
| **Code file** | `Day_73.py` |
| **Reading** | 📐 **Essential Math Ch. 5, pp. 171–185** |

> **Today is where Month 2's statistics and Month 3's modelling meet.** A regression coefficient is an estimate computed from a sample — so it has a standard error, a confidence interval and a p-value, and every misuse from Day 53 applies to it.
>
> **The practical outcome:** you will stop saying "R² is 0.87, so the model is good", and start asking what the number is actually measuring.

---

## 🎯 Objective

Interpret R², coefficient significance and prediction intervals correctly — and know what each one hides.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 5, pp. 171–185** | **PRIMARY** · reading + code | 40 min | Correlation · statistical significance · R² · standard error · prediction intervals |
| [StatQuest — R-squared](https://www.youtube.com/watch?v=bMccdk8EdGo) | **REINFORCEMENT** | 11 min | Where the number comes from |

---

## 🧠 Core Concepts

### R² — what it is, and the four things it is not

```
R² = 1 − (unexplained variation / total variation)
```

**"The proportion of variance in y explained by the model."** An R² of 0.87 means the model accounts for 87% of the spread in the outcome.

| R² is NOT | Why |
|:----------|:----|
| A measure of whether the model is correct | **Day 71's curved data had a good R² and the wrong shape.** Always plot residuals. |
| Comparable across datasets | Predicting human height and predicting stock returns have completely different achievable ceilings |
| Evidence of causation | It is a correlation, squared |
| Meaningful on its own for prediction quality | **It can only rise when you add features** — including pure noise |

**That last point is important enough to demonstrate.** Add twenty random columns to any model and R² improves, every time, because with enough parameters a model can fit the noise. That is why **adjusted R²** exists — it penalises added features — and why **R² on a held-out test set** is the only version worth quoting.

### RMSE, MAE, and which to report

| | Is | Use when |
|:--|:--|:--|
| **RMSE** | √(mean squared error) | Large errors matter disproportionately. In the units of y. |
| **MAE** | Mean absolute error | All errors matter equally. Robust to outliers. |
| **MAPE** | Mean absolute *percentage* error | Comparing across different scales — **breaks when y is near zero** |
| **R²** | Proportion of variance explained | Communicating fit, with caveats |

**Report RMSE or MAE in the units of the thing.** "The model is off by PKR 340 on average" is something a business can act on. "R² = 0.87" is not.

### Coefficient significance — Day 53, applied to a model

Each `βⱼ` has a standard error. The t-statistic is `βⱼ / SE(βⱼ)`, and the p-value asks: *if the true coefficient were zero, how likely is an estimate this large?*

**And every warning from Day 53 applies:**

- With many rows, trivially small coefficients become "significant"
- With many features, some will look significant by chance — twenty features at α = 0.05 gives you about one false positive
- **`p > 0.05` does not mean the feature has no effect** — it may mean you lack the data to detect it
- **Multicollinearity inflates standard errors**, so a genuinely important feature can appear insignificant purely because a correlated twin is in the model

**That last one is where Day 67's condition number earns its place.** Before interpreting any coefficient: check `cond(X)`. If it is above 1,000, the individual coefficients are unreliable even if the model predicts well. **A model can predict accurately and still have meaningless coefficients** — and confusing the two is one of the most common errors in applied work.

### Confidence interval versus prediction interval

Two different questions, routinely confused:

| | Answers | Width |
|:--|:--|:--|
| **Confidence interval** for the mean | "Where is the *average* y for this x?" | Narrow |
| **Prediction interval** for one observation | "Where will *this particular* y fall?" | **Much wider** |

The prediction interval must also carry the irreducible noise of individual outcomes, not just the uncertainty in the line.

**Almost every business question is a prediction interval question.** "What will *this house* sell for?" is not "what is the average price of houses like this?" — and quoting the narrow one makes a model look far more precise than it is.

### Correlation, once more

`r` measures *linear* association, from −1 to 1, and `r² = R²` for a single-predictor regression.

**Anscombe's quartet** — four datasets with identical means, variances, correlations and regression lines, and completely different shapes — is the standard demonstration that summary statistics cannot replace looking at the data. Exercise 8 makes you reproduce it.

---

## 💻 Code

`Day_73.py` — nine exercises.

**R² and its limits (1–4)**
1. Compute R² from scratch; match sklearn's `.score()`
2. **The noise demonstration:** add 20 columns of pure random noise. **Watch R² rise every time.** Then compute adjusted R² and watch it fall.
3. The same model's R² on train and on test. **How big is the gap?**
4. RMSE, MAE and MAPE on the same predictions. **Where does MAPE break?**

**Significance (5–7)**
5. Compute coefficient standard errors and t-statistics by hand; match `statsmodels`
6. **The multicollinearity effect:** fit with and without a correlated twin feature. **Watch the standard errors inflate and the p-values collapse.** Check `cond(X)` for both.
7. **The many-features effect:** fit on 20 pure-noise features. **How many came out "significant"?** *(Day 53's exercise 9, in a model.)*

**Intervals and looking (8–9)**
8. **Anscombe's quartet.** Compute the summary statistics for all four — identical. Then plot them. Write what each would have made you conclude.
9. Confidence interval versus prediction interval for the same x. **Plot both bands.** Which would you quote to a business, and why?

---

## 🔬 Understanding Check

1. **Reasoning.** Why can R² only rise when you add features? What does adjusted R² do about it?
2. **Application.** Exercise 3: how large was the train–test R² gap? What does a large gap mean?
3. **Judgement.** Exercise 6: what happened to the standard errors with a correlated twin? Can a model predict well and still have meaningless coefficients?
4. **Reasoning.** Exercise 7: how many noise features were "significant"? What does that mean for feature selection by p-value?
5. **Comparison.** Confidence interval vs prediction interval — which does a business question usually need?
6. **Communication.** Which metric do you report to a non-technical stakeholder, and why not R²?
7. **Understanding.** Exercise 8: what would you have concluded about each Anscombe dataset from the statistics alone?

---

## 🎯 Expected Outcome

- [ ] Interpret R² and state its four limitations
- [ ] Compute and interpret coefficient significance
- [ ] Recognise multicollinearity's effect on standard errors
- [ ] Choose the right interval and the right metric for the audience

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 171–185 | 40 min |
| StatQuest R-squared | 11 min |
| Nine exercises | 30 min |
| Daily review | 5 min |
| **Total** | **~86 min** |

---

## 🧪 Mini Assessment

Six minutes. A colleague reports: *"R² = 0.91, and all coefficients are significant at p < 0.05. The model is ready."*

Write four questions you would ask before agreeing, and say what answer would worry you for each.

---

## 🔁 Daily Review

1. Exercise 2: how much did R² rise from 20 noise columns?
2. Exercise 6: what did the correlated twin do to the standard errors?
3. Exercise 7: how many noise features were "significant"?
4. Which metric will I report in Project 3, and in what units?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 171–185 read
- [ ] R² computed from scratch and matched
- [ ] The noise demonstration run, adjusted R² compared
- [ ] Standard errors computed by hand and matched against statsmodels
- [ ] The multicollinearity effect demonstrated, `cond(X)` recorded
- [ ] Anscombe's quartet reproduced and plotted
- [ ] Both interval types plotted and compared
- [ ] Committed to git

---

**[← Day 72](../Day_72/Day_72.md)** · **[Day 74 →](../Day_74/Day_74.md)** · [README](../../../README.md)
