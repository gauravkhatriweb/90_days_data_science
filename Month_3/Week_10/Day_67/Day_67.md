# Day 67 — Determinants, Inverses, and Solving Systems

|  |  |
|:--|:--|
| **Date** | Saturday, 21 November 2026 |
| **Position** | Week 10 · Month 3 · Phase 5 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_67.py` |
| **Reading** | 📐 **Essential Math Ch. 4, pp. 129–142** |

> **Today everything from Days 65 and 66 connects.** Determinant, rank, invertibility and linear dependence turn out to be four descriptions of one property, and that property is exactly what makes a linear regression solvable or not.
>
> By the end of today you should be able to look at a feature matrix and say whether a model can be fitted on it — and why — without running anything.

---

## 🎯 Objective

Understand the determinant as an area scale factor, see why a zero determinant means no inverse, and solve a linear system — which is what fitting a regression actually is.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 4, pp. 129–142** | **PRIMARY** · reading + code | 55 min | Matrix multiplication · determinants · special matrices · systems and inverses |
| [3Blue1Brown — Ch. 4: Matrix multiplication as composition](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | **REINFORCEMENT** | 10 min | Why the rule is composition |
| [3Blue1Brown — Ch. 6: The determinant](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | **REINFORCEMENT** | 10 min | The area picture |
| [3Blue1Brown — Ch. 7: Inverse matrices, column space, null space](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | **REINFORCEMENT** | 12 min | Why inverses fail |

---

## 🧠 Core Concepts

### Matrix multiplication is composition

`B @ A` means "apply A, then apply B". Read **right to left**, like function composition `f(g(x))`.

That is why `A @ B ≠ B @ A` in general — rotating then stretching is not the same as stretching then rotating. **It is not an algebraic quirk; it is a fact about the world**, and once you have seen the two results as pictures you will not forget it.

### The determinant — how much area changes

Apply a matrix to a unit square. The determinant is **the area of the resulting shape**.

| det | Means |
|:---:|:------|
| 2 | Areas double |
| 1 | Areas preserved — a rotation |
| 0.5 | Areas halve |
| **0** | **Everything collapses to a line or a point** |
| negative | Space was flipped over |

**`det = 0` is the important case.** It means the transformation squashed space into fewer dimensions. Information was destroyed, and destroyed information cannot be recovered — **so there is no inverse.**

### The four statements that are one statement

For a square matrix, these are all equivalent:

| Statement | |
|:----------|:|
| `det(A) = 0` | |
| `A` has no inverse | |
| `A`'s columns are linearly dependent | ← Day 65 |
| `A` collapses space to a lower dimension | ← Day 66 |
| `Ax = b` has no unique solution | |

**Memorising five facts is hard. Understanding one is not.** They are five views of "the columns do not carry independent information."

### Solving `Ax = b` — and why regression is this

A system of equations is a matrix equation:

```
2x + 3y = 12          [[2, 3],  @ [x,  =  [12,
4x + 1y = 14           [4, 1]]    y]       14]
```

```python
np.linalg.solve(A, b)         # use this
np.linalg.inv(A) @ b          # do NOT -- slower and numerically worse
```

**Never compute an inverse to solve a system.** `solve` uses a factorisation that is faster and far more numerically stable. Computing `inv` and multiplying is one of the most common signs of code written by someone following the textbook notation rather than the numerical practice.

**The regression connection:** fitting a linear regression by the closed-form solution means solving

```
(XᵀX) β = Xᵀy
```

for `β`. That is a linear system. And if the columns of `X` are dependent — multicollinearity — then `XᵀX` has determinant zero, has no inverse, and **there is no unique solution.** Infinitely many coefficient vectors fit equally well, which is exactly why collinear features produce unstable, meaningless coefficients.

**Every idea in this challenge so far arrives at that paragraph.** Day 65's span, Day 66's collapse, today's determinant, and Day 73's coefficient interpretation are one chain.

### Condition number — the practical version

Perfect dependence is rare in real data. **Near-dependence is common**, and it is worse in a way, because nothing errors.

```python
np.linalg.cond(X)
```

| Condition number | Means |
|:-----------------|:------|
| ~1 | Well-conditioned |
| < 30 | Fine |
| 30–100 | Some multicollinearity |
| **> 1000** | **Coefficients are unreliable** |

A high condition number means small changes in the data produce large changes in the coefficients — so your interpretation of "this feature has coefficient 3.2" is noise. **Check `cond(X)` before you interpret any regression coefficient.** It takes one line and it is a habit most people never build.

---

## 💻 Code

`Day_67.py` — eleven exercises.

**Composition (1–3)**
1. Apply A then B by hand, then `B @ A` at once. Confirm identical.
2. Show `A @ B ≠ B @ A` visually — rotate-then-stretch versus stretch-then-rotate
3. Compose three transformations; predict the combined effect before computing

**Determinants (4–6)**
4. Compute determinants for the six Day 66 matrices; **connect each to what you saw**
5. **The area proof:** transform a unit square, measure the output area, compare with the determinant
6. Negative determinant — visualise the flip

**Inverses (7–9)**
7. Invert an invertible matrix; confirm `A @ A⁻¹ = I`
8. **Try to invert the collapsed matrix.** Read the error. Connect it to the four statements.
9. `solve` vs `inv @ b` — time both, and compare accuracy on a badly-conditioned system

**The regression connection (10–11)**
10. **Solve a regression by hand** with the normal equations: `β = solve(XᵀX, Xᵀy)`. Compare with `sklearn`'s answer. **They should match.**
11. **Add a collinear column and try again.** What happens to the determinant, the condition number, and the coefficients? **Then check `cond(X)` on your Project 2 feature matrix.**

Exercise 10 is the one that makes Day 71 easy: you will have already fitted a linear regression from first principles.

---

## 🔬 Understanding Check

1. **Understanding.** What does the determinant measure geometrically?
2. **Reasoning.** Why does `det = 0` mean no inverse? Answer with information, not algebra.
3. **Integration.** State the four equivalent statements. Explain why they are one idea.
4. **Application.** Exercise 11: what happened to the coefficients with a collinear column? Why is that dangerous even without an error?
5. **Practice.** Why use `solve` rather than `inv @ b`? Two reasons.
6. **Judgement.** Your feature matrix has `cond(X) = 4000`. What does that mean for interpreting coefficients?
7. **Connection.** Exercise 10 fitted a regression with linear algebra. What is the "learning" in machine learning, then?

---

## 🎯 Expected Outcome

- [ ] Explain the determinant as area scaling
- [ ] State the four equivalent statements and why they are one
- [ ] Solve a linear system properly
- [ ] Fit a linear regression from first principles
- [ ] Check conditioning before interpreting coefficients

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 129–142 | 55 min |
| 3Blue1Brown Ch. 4, 6, 7 | 32 min |
| Exercises 1–9 | 55 min |
| **Exercises 10–11 — the regression connection** | 30 min |
| Daily review | 8 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

Eight minutes. Given a feature matrix `X` with four columns, one of which is the mean of two others:

1. What is `det(XᵀX)`?
2. Can you fit a linear regression? What happens if you try?
3. What is `cond(X)` roughly?
4. Which column would you drop, and how would you decide which?

---

## 🔁 Daily Review

1. Which of the four equivalent statements did I understand least well before today?
2. Exercise 10: did my hand-fitted regression match sklearn?
3. Exercise 11: what is `cond(X)` on my real data? Should I trust its coefficients?
4. **ML starts in two days.** Does "fitting a model" feel like magic still, or like arithmetic?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 129–142 read, three 3Blue1Brown chapters watched
- [ ] `A @ B ≠ B @ A` demonstrated visually
- [ ] The determinant-as-area verified empirically
- [ ] Inverting a singular matrix attempted, the error connected to the four statements
- [ ] **A linear regression fitted with `solve`, matching sklearn**
- [ ] A collinear column added and its effect on coefficients recorded
- [ ] `cond(X)` computed on real Project 2 data
- [ ] Committed to git

---

**[← Day 66](../Day_66/Day_66.md)** · **[Day 68 →](../Day_68/Day_68.md)** · [README](../../../README.md)
