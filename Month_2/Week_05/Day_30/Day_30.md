# Day 30 — Vectorisation and Broadcasting

|  |  |
|:--|:--|
| **Date** | Thursday, 15 October 2026 |
| **Position** | Week 5 · Month 2 · Phase 2 — Data manipulation |
| **Budget** | **~75 min** |
| **Code file** | `Day_30.py` |

> **Why today is the most important NumPy day.** Vectorisation is a change in how you think, not a feature you use. Twenty-nine days of Python have trained you to write loops. NumPy asks you to **describe a transformation of a whole array** and let it handle the iteration. Once that switch happens, Pandas reads naturally. Until it does, you will write slow Pandas code that looks like Python.
>
> Broadcasting is the rule that makes it work on arrays of different shapes — and it is the source of most NumPy confusion, so it gets explained properly here rather than demonstrated.

---

## 🎯 Objective

Replace loops with array expressions, and predict broadcasting behaviour before running the code.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians NumPy](https://www.youtube.com/watch?v=Utgwk0r9Zq4) · **`1:04:12 → 1:30:01`** · @1.75× | PRIMARY | 15 min | Maths operations, broadcasting, matrix multiplication, stacking |
| The broadcasting rules below | REFERENCE | 15 min | The video shows it; this explains it |

### 🟢 IF TIME

- The NumPy docs page on broadcasting — the diagrams are the clearest explanation that exists.

---

## 🧠 Core Concepts

### Vectorisation: describe, do not iterate

```python
# Python thinking
result = []
for p in prices:
    result.append(p * 1.17)

# NumPy thinking
result = prices * 1.17
```

The second is shorter, and 50× faster because the loop runs in C. But the real change is **conceptual**: you stopped managing iteration and started describing a transformation.

```python
revenue      = qty * price                          # element-wise
discounted   = np.where(qty > 10, price * 0.9, price)   # vectorised if/else
above_mean   = prices[prices > prices.mean()]       # vectorised filter
total_by_row = matrix.sum(axis=1)                   # vectorised aggregation
```

**`np.where` is the vectorised `if`.** Any time you catch yourself writing a loop with an `if` inside to build an array, that is `np.where`.

### The `axis` argument — the thing everyone gets wrong

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])

a.sum()           # 21  -- everything
a.sum(axis=0)     # [5, 7, 9]   -- collapse ROWS, one result per column
a.sum(axis=1)     # [6, 15]     -- collapse COLUMNS, one result per row
```

**The reliable mental model: `axis=n` is the axis that disappears.**

`a.shape` is `(2, 3)`. `axis=0` removes the first dimension → result shape `(3,)`. `axis=1` removes the second → result shape `(2,)`.

"axis=0 means columns" is the common phrasing and it causes constant confusion. "axis=0 is the axis that vanishes" never does. This same argument appears in Pandas on Day 34, meaning the same thing.

### Broadcasting — the actual rules

Broadcasting lets arrays of different shapes work together. Compare shapes **from the right**:

1. If dimensions are equal → compatible
2. If one of them is 1 → stretch it
3. If one array has fewer dimensions → pad its shape with 1s on the left
4. Otherwise → error

```
(3, 4)  +  (4,)      ->  (4,) becomes (1,4), stretches to (3,4)   ✅
(3, 4)  +  (3,)      ->  (3,) becomes (1,3), and 3 ≠ 4            ❌
(3, 4)  +  (3, 1)    ->  stretches to (3,4)                        ✅
(3, 1)  +  (1, 4)    ->  both stretch, result is (3,4)             ✅
```

The second one is the trap: adding a per-row value to a `(3,4)` array needs shape `(3,1)`, not `(3,)`. The fix is `values.reshape(-1, 1)` or `values[:, np.newaxis]`.

**Nothing is copied.** Broadcasting is a view trick — a `(3,1)` array used against `(3,4)` does not become twelve values in memory. That is why it is fast and memory-cheap.

### Where vectorisation stops helping

It is not always the answer:

- **Genuinely sequential logic** — where each step depends on the last
- **Very small arrays** — under ~100 elements the overhead can dominate
- **Readability** — a chain of eight broadcast operations nobody can read is worse than a clear loop

Measure before assuming. Exercise 9 makes you do exactly that.

---

## 💻 Code

`Day_30.py` — ten exercises:

**Vectorisation (1–4)**
1. Rewrite three loops from Day 3 as array expressions. Time both versions.
2. `np.where` — apply a tiered discount without any loop
3. Chain five operations into one expression; compare against the loop version for both speed and readability
4. A normalisation function — `(x - mean) / std` — vectorised

**Axis (5–6)**
5. For a `(4, 6)` array, compute six different aggregations with `axis=0` and `axis=1`. **Predict each result's shape before running.**
6. Write the "axis that disappears" rule in your own words, then verify it on a 3D array

**Broadcasting (7–8)**
7. Predict the result shape for eight shape pairs, then check. Score yourself.
8. **The `(3,)` vs `(3,1)` trap.** Add a per-row value to a `(3,4)` array — get the error, understand it, fix it two ways.

**Judgement (9–10)**
9. **Find where vectorisation loses.** Time a loop against a vectorised version at n = 10, 100, 1,000, 100,000. Find the crossover.
10. Write a running-total calculation both ways. Then argue in a comment whether `np.cumsum` or a loop is better here, and why.

---

## 🔬 Understanding Check

1. **Reasoning.** What does vectorisation actually change — the speed, or how you think? Argue for both.
2. **Understanding.** State the axis rule in your own words. Why is "axis=0 means columns" misleading?
3. **Debugging.** `(3,4) + (3,)` raises an error but `(3,4) + (4,)` works. Explain, using the rules.
4. **Application.** Exercise 8 needed `(3,1)`. Why does NumPy not just guess what you meant?
5. **Reasoning.** Broadcasting does not copy data. Why does that matter for a 10 GB array?
6. **Comparison.** Exercise 9: where was the crossover? What does that tell you about optimising small data?
7. **Connection.** Pandas uses broadcasting constantly. Predict what `df["price"] * 1.17` does, and what `df["price"] * other_column` requires.

---

## 🎯 Expected Outcome

- [ ] Write array expressions instead of loops by default
- [ ] Predict the output shape of any aggregation
- [ ] Predict whether two shapes broadcast, and to what
- [ ] Know when vectorisation is not worth it

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians NumPy `1:04:12 → 1:30:01` @1.75× | 15 min |
| Broadcasting rules | 15 min |
| Ten exercises | 38 min |
| Daily review | 7 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Six minutes, closed book. A `(50, 4)` array of daily sales — 50 days, 4 products. Without any loop:

1. Total revenue per product
2. Each day's sales as a percentage of that day's total *(broadcasting)*
3. Days where any product sold more than twice its own average
4. The array normalised per product: subtract each product's mean, divide by its standard deviation

Item 4 is the one that needs the `(1,4)` versus `(4,)` distinction to be right.

---

## 🔁 Daily Review

1. Exercise 7: how many of the eight shape predictions were right?
2. Exercise 9: where was the crossover? Did that change my instinct about optimising?
3. Can I state the axis rule without looking?
4. Am I still reaching for loops first? Honestly?

---

## 📦 Completion Criteria

- [ ] Loop and vectorised timings recorded with real numbers
- [ ] Shape predictions written before running, scored
- [ ] The `(3,)` vs `(3,1)` error hit and fixed twice
- [ ] The crossover point found and recorded
- [ ] Mini assessment done with zero loops
- [ ] Committed to git

---

**[← Day 29](../Day_29/Day_29.md)** · **[Day 31 →](../Day_31/Day_31.md)** · [README](../../../README.md)
