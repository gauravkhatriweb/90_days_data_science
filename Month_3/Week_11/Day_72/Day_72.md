# Day 72 — Gradient Descent: Where the Calculus Pays Off

|  |  |
|:--|:--|
| **Date** | Thursday, 26 November 2026 |
| **Position** | Week 11 · Month 3 · Phase 6 |
| **Budget** | **~75 min** |
| **Code file** | `Day_72.py` |
| **Reading** | 📐 **Essential Math Ch. 5, pp. 161–171** |

> **This is the day the plan was built towards.** On Day 19 you read that a derivative is the slope of a function at a point. On Day 25 you learned the chain rule. Those days were forty minutes each, on weekends, alongside your calculus course, and they probably felt like a detour.
>
> **Today they become the thing that trains every model.** Gradient descent is: *compute the slope, step downhill, repeat.* That is the whole algorithm, and the slope is a derivative. Every model from here — logistic regression, trees' splitting criteria, neural networks — is optimising something, and this is how.
>
> **Write it yourself today.** Once you have implemented gradient descent in fifteen lines, no optimiser is ever mysterious again.

---

## 🎯 Objective

Implement gradient descent from scratch, understand what the learning rate does, and know why anything beyond a closed-form model needs it.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 5, pp. 161–171** | **PRIMARY** · reading + code | 30 min | Gradient descent · overfitting and variance · stochastic gradient descent |
| [StatQuest — Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8) | **REINFORCEMENT** | 23 min | The clearest explanation there is. Worth all 23 minutes. |

---

## 🧠 Core Concepts

### The algorithm

```
1. Start anywhere
2. Compute the slope of the error, with respect to each parameter
3. Step in the opposite direction, by (learning rate × slope)
4. Repeat until the steps stop helping
```

```python
for _ in range(iterations):
    predictions = X @ beta
    error = predictions - y
    gradient = (2 / n) * X.T @ error       # the derivative of MSE wrt beta
    beta -= learning_rate * gradient
```

**Five lines.** That is every optimiser you have ever heard of, in its simplest form.

### Why the derivative is exactly the right tool

The error surface is a function of the parameters: pick a slope and an intercept, get a total error. You want its lowest point.

**The derivative tells you which way is uphill.** Go the other way. That is all "gradient" means — the collection of partial derivatives, one per parameter, each answering *"if I nudge only this one, how does the error change?"*

**Which is precisely Day 19's partial derivatives**, and the reason that page said they would return.

For mean squared error the derivative is clean:

```
MSE  = (1/n) Σ (Xβ − y)²
dMSE/dβ = (2/n) Xᵀ(Xβ − y)
```

That is a matrix multiplication — Day 66 — of the transposed feature matrix by the error vector. **Every idea in this plan converges on that one line.**

### The learning rate — the only knob, and it matters

| Rate | Behaviour |
|:-----|:----------|
| **Too small** | Converges, but takes forever |
| **About right** | Smooth, fast descent |
| **Too large** | Oscillates around the minimum |
| **Much too large** | **Diverges** — the error explodes to infinity |

You will produce all four in exercise 3, and seeing divergence once is worth more than reading about it.

**It also depends on feature scale.** If one feature is in thousands and another in tens, the error surface is a long narrow valley, and a rate that works for one parameter is far too large for the other. **That is why gradient-based models need scaled features** — Day 79's `StandardScaler`, and now you know the actual reason rather than the rule.

### Batch, stochastic, mini-batch

| | Uses per step | Trade-off |
|:--|:--|:--|
| **Batch** | All rows | Smooth, accurate, slow on large data |
| **Stochastic (SGD)** | One row | Noisy, fast, and the noise can escape local minima |
| **Mini-batch** | 32–256 rows | The practical compromise; what everything real uses |

The noise in SGD is a feature, not a defect — it is why stochastic methods work on surfaces where batch descent would settle into the first dip it finds.

### Why bother, when linear regression has a closed form?

**Because almost nothing else does.**

| Model | Closed form? |
|:------|:-------------|
| Linear regression | ✅ — and it fails on collinear or very wide data |
| Ridge regression | ✅ |
| **Logistic regression** | ❌ — **Day 75** |
| Neural networks | ❌ |
| Most modern models | ❌ |

Gradient descent also scales where the closed form does not: `(XᵀX)⁻¹` is `O(features³)`, which is impossible at 100,000 features, while gradient descent is linear in both rows and features per step.

### Convergence, local minima, and honesty

**Convex** surfaces — like MSE for a linear model — have one minimum, and gradient descent always finds it. **Non-convex** surfaces have many, and it finds *a* minimum, not *the* minimum.

Neural networks are non-convex. So "trained" means "found somewhere good enough", not "found the best". That is worth knowing before anyone tells you a model is optimal.

---

## 💻 Code

`Day_72.py` — eight exercises. **Write the algorithm yourself before importing anything.**

**Building it (1–3)**
1. **Gradient descent from scratch**, five lines, on the Day 71 data. Print the cost every 100 iterations and watch it fall.
2. **Compare with the closed form.** Same answer? To how many decimal places? How many iterations did it take?
3. **The learning-rate experiment.** Run at 0.0001, 0.001, 0.01, 0.1, 1.0. **Plot the cost curves on one chart.** Find the one that diverges.

**Seeing it (4–5)**
4. **Plot the path.** For a two-parameter model, draw the error surface as a contour plot and trace the descent across it.
5. **Feature scaling.** Run gradient descent with unscaled features, then scaled. **Compare the iteration counts.** This is the practical reason for `StandardScaler`.

**Variants (6–7)**
6. Implement stochastic gradient descent. Compare its cost curve with batch — note the noise.
7. Mini-batch at sizes 1, 32, 256, and all. Compare time and smoothness.

**The payoff (8)**
8. **Write the chain rule connection.** In a comment, trace: the error depends on the prediction, the prediction depends on β, so the derivative of error with respect to β is the product of two derivatives. **This is backpropagation in miniature** — and it is why Chapter 1 mattered.

---

## 🔬 Understanding Check

1. **Understanding.** Explain gradient descent in three sentences to someone who knows what a slope is.
2. **Connection.** Why is the derivative exactly the right tool? What question does it answer at each step?
3. **Application.** Exercise 3: which learning rate diverged? What did the cost curve look like?
4. **Reasoning.** Exercise 5: how many more iterations did unscaled features need? Explain it with the shape of the error surface.
5. **Comparison.** Batch, stochastic, mini-batch — when is each right?
6. **Reasoning.** Linear regression has a closed form. Give two reasons to use gradient descent anyway.
7. **Judgement.** Non-convex surfaces have many minima. What does "trained" mean then?
8. **Integration.** Exercise 8: trace the chain rule from error back to β. Why does this matter beyond linear regression?

---

## 🎯 Expected Outcome

- [ ] Write gradient descent from scratch without reference
- [ ] Diagnose a learning rate from its cost curve
- [ ] Explain why gradient methods need scaled features
- [ ] Connect the chain rule to how models are trained

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 161–171 | 30 min |
| StatQuest gradient descent | 23 min |
| Eight exercises | 35 min |
| Daily review | 5 min |
| **Total** | **~93 min** — if over, do exercises 6–7 tomorrow |

---

## 🧪 Mini Assessment

Eight minutes, closed book. Write gradient descent for `y = mx + c` from scratch — no NumPy matrix shortcuts, just two parameters and a loop. Run it. **Does it converge to the same answer as `np.polyfit`?**

---

## 🔁 Daily Review

1. How many iterations to match the closed form?
2. Which learning rate diverged, and what did the curve do?
3. Unscaled vs scaled: how many more iterations?
4. **Days 19 and 25 were forty minutes each on weekends.** Did they pay off today? Write the honest answer — it decides whether you keep protecting the maths track in December.

---

## 📦 Completion Criteria

- [ ] Gradient descent written from scratch and converging
- [ ] Matched against the closed form
- [ ] Five learning rates plotted, including one that diverges
- [ ] The descent path traced on a contour plot
- [ ] The scaling experiment run, iteration counts recorded
- [ ] SGD implemented and compared
- [ ] The chain-rule trace written
- [ ] Committed to git

---

**[← Day 71](../Day_71/Day_71.md)** · **[Day 73 →](../Day_73/Day_73.md)** · [README](../../../README.md)
