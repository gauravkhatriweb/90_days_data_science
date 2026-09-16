# Day 66 — Matrices as Transformations

|  |  |
|:--|:--|
| **Date** | Friday, 20 November 2026 |
| **Position** | Week 10 · Month 3 · Phase 5 |
| **Budget** | **~75 min** |
| **Code file** | `Day_66.py` |
| **Reading** | 📐 **Essential Math Ch. 4, pp. 121–129** |

> **The idea that makes linear algebra click.** A matrix is usually taught as a grid of numbers with rules for multiplying it. That view explains nothing.
>
> The useful view: **a matrix is a function that moves space.** Multiplying by a matrix takes every point in the plane and moves it somewhere else — rotating, stretching, shearing or flattening. Once you see that, matrix multiplication becomes composition of transformations, determinants become an area scale factor, and eigenvectors become "the directions that do not turn". All of it follows.

---

## 🎯 Objective

See a matrix as a transformation of space, and understand matrix-vector multiplication as "where do the basis vectors land?"

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| **Essential Math Ch. 4, pp. 121–129** | **PRIMARY** · reading + code | 30 min | Linear transformations · basis vectors · matrix-vector multiplication |
| [3Blue1Brown — Ch. 3: Linear transformations and matrices](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | **REINFORCEMENT** | 11 min | **Watch this one properly.** It is the clearest ten minutes in the series. |
| The sections below | REFERENCE | 10 min | The ML connection |

---

## 🧠 Core Concepts

### Basis vectors, and what a matrix really records

In 2D, the basis vectors are `î = [1,0]` and `ĵ = [0,1]`. Every vector is a combination of them: `[3,2] = 3î + 2ĵ`.

**A matrix records where the basis vectors land after the transformation.**

```
A = [[2, 1],
     [0, 3]]
```

Read the **columns**: `î` goes to `[2,0]`, and `ĵ` goes to `[1,3]`. That is the entire content of the matrix.

**And that is why matrix-vector multiplication works the way it does.** A transformation keeps linear combinations intact, so if `v = 3î + 2ĵ`, then after the transformation `v` is `3×(new î) + 2×(new ĵ)`:

```
A @ [3,2] = 3*[2,0] + 2*[1,3] = [8,6]
```

The multiplication rule is not an arbitrary convention — it is the only rule consistent with "the transformation preserves linear combinations". Seeing that once is worth more than memorising the rule ten times.

### The transformations worth recognising

| Matrix | Does |
|:-------|:-----|
| `[[1,0],[0,1]]` | Nothing — the identity |
| `[[2,0],[0,2]]` | Scales everything by 2 |
| `[[2,0],[0,1]]` | Stretches x only |
| `[[0,-1],[1,0]]` | Rotates 90° |
| `[[1,1],[0,1]]` | Shear |
| `[[1,2],[2,4]]` | **Collapses the plane to a line** — the columns are dependent |

**The last one is Day 65's linear dependence, seen as a transformation.** A matrix whose columns are dependent squashes space into a lower dimension — and squashing loses information, which is why it cannot be undone, which is why the matrix has no inverse, which is why a regression with collinear features fails. **Five facts, one cause.**

### Where this lives in machine learning

```python
predictions = X @ weights
```

`X` is `(n_samples, n_features)`. `weights` is `(n_features, 1)`. The result is `(n_samples, 1)`.

**Every linear model is one matrix multiplication.** Linear regression, logistic regression (before the sigmoid), and one layer of a neural network are all `X @ W + b`. The differences are what happens afterwards and how the weights are found — not the arithmetic.

**Shapes, and the error you will meet constantly:**

```
(m, n) @ (n, p) -> (m, p)
     inner dimensions must match, and both disappear
```

`ValueError: matmul: Input operand 1 has a mismatch...` means the inner dimensions disagree. **Print both shapes** — the fix is almost always a `reshape(-1, 1)` or a transpose.

---

## 💻 Code

`Day_66.py` — eight exercises. **Visualise every transformation** by applying it to a grid of points.

1. Apply five named matrices to a unit grid; plot before and after. Name what each does.
2. **Read the columns:** for each matrix, predict where `î` and `ĵ` land *before* computing
3. Verify by hand that `A @ v` equals `v₁ × (column 1) + v₂ × (column 2)`
4. **The collapse:** apply `[[1,2],[2,4]]`. Watch the plane become a line. Check the rank.
5. Build a rotation matrix for an arbitrary angle; apply it to your Project 2 data in 2D
6. **Shapes:** trigger the matmul dimension error on purpose. Read it. Fix it two ways.
7. `X @ weights` on a real feature matrix. **State every shape before running.**
8. Compose two transformations: apply A then B, versus applying `B @ A` at once. **Same result — why?** And check whether `A @ B` equals `B @ A`.

Exercise 8 previews tomorrow: matrix multiplication *is* composition, and it is not commutative because doing a rotation then a stretch is not the same as a stretch then a rotation.

---

## 🔬 Understanding Check

1. **Understanding.** What do the columns of a matrix tell you?
2. **Reasoning.** Why is the matrix-vector multiplication rule the only one that could work? Answer with linear combinations.
3. **Application.** Exercise 4: the plane collapsed to a line. What is the rank, and what does that mean for information?
4. **Connection.** Connect "collapses space" to "has no inverse" to "regression fails with collinear features".
5. **Debugging.** You get a matmul dimension error. What are the two shapes, and what is the fix?
6. **Application.** Exercise 7: `X` is `(1000,5)`. What shape must `weights` be? What shape are the predictions?
7. **Reasoning.** Exercise 8: does `A @ B` equal `B @ A`? Give a geometric reason.

---

## 🎯 Expected Outcome

- [ ] Read a matrix as "where do the basis vectors land"
- [ ] Predict what a transformation does before computing it
- [ ] Connect rank deficiency to non-invertibility and to failed regressions
- [ ] Reason about matmul shapes without trial and error

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Essential Math pp. 121–129 | 30 min |
| 3Blue1Brown Ch. 3 | 11 min |
| The ML connection | 10 min |
| Eight exercises | 20 min |
| Daily review | 5 min |
| **Total** | **~76 min** |

---

## 🧪 Mini Assessment

Five minutes, no computation. Given `A = [[3,0],[0,0.5]]`:

1. Where do `î` and `ĵ` land?
2. Describe what it does to the plane, in words
3. Does it have an inverse? How do you know?
4. What happens to the area of a unit square? *(Tomorrow names this.)*

---

## 🔁 Daily Review

1. Did the "columns are where the basis vectors land" framing change anything?
2. Exercise 4: what was the rank after the collapse?
3. Can I explain why collinear features break a regression, geometrically?
4. Does `A @ B` equal `B @ A`? Why not, in one sentence?

---

## 📦 Completion Criteria

- [ ] Essential Math pp. 121–129 read, 3Blue1Brown Ch. 3 watched
- [ ] Five transformations visualised, each named
- [ ] Basis-vector landings predicted before computing
- [ ] The collapse demonstrated, rank checked
- [ ] The matmul error triggered and fixed twice
- [ ] `X @ weights` computed with shapes stated first
- [ ] Committed to git

---

**[← Day 65](../Day_65/Day_65.md)** · **[Day 67 →](../Day_67/Day_67.md)** · [README](../../../README.md)
