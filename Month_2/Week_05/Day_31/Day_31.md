# Day 31 — NumPy Finished: Aggregation, Masking, and Matrices

|  |  |
|:--|:--|
| **Date** | Friday, 16 October 2026 |
| **Position** | Week 5 · Month 2 · Phase 2 — Data manipulation |
| **Budget** | **~75 min** |
| **Code file** | `Day_31.py` |

> **Last NumPy day.** Three days, and that is deliberate — you now understand the substrate well enough that Pandas will make sense tomorrow. Today closes out the operations you will actually reach for, plus a first look at matrix multiplication, which returns on Day 67 as linear algebra and again on Day 71 as the mathematics under linear regression.

---

## 🎯 Objective

Aggregate, filter and reshape arrays fluently, and understand `@` well enough to recognise it when it reappears inside a model.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians NumPy](https://www.youtube.com/watch?v=Utgwk0r9Zq4) · **`1:30:01 → 1:59:34`** · @1.75× | PRIMARY | 17 min | The practical exercises — Sudoku validity, score analysis |
| The sections below | REFERENCE | 12 min | Aggregation, masking, `@` |

### 🟢 IF TIME

- Do the Sudoku-validity exercise from the video yourself before watching the solution. It is a genuinely good axis and reshaping problem.

---

## 🧠 Core Concepts

### Aggregation, and the NaN problem

```python
a.sum() · a.mean() · a.std() · a.var() · a.min() · a.max()
a.argmin() · a.argmax()        # the INDEX, not the value
np.median(a) · np.percentile(a, [25, 50, 75])
a.cumsum() · a.cumprod()
```

**`argmax` is the one worth noticing.** `a.max()` gives you the highest value; `a.argmax()` gives you *where it is*, which is usually the more useful question — "which product sold most" rather than "how much did it sell".

**The NaN rule:** any aggregation over an array containing `np.nan` returns `nan`.

```python
a = np.array([1, 2, np.nan, 4])
a.mean()            # nan   -- one missing value poisons the whole result
np.nanmean(a)       # 2.333 -- the nan-aware version
```

Every aggregation has a `nan`-prefixed twin: `nanmean`, `nansum`, `nanstd`, `nanmax`. **Real data has missing values**, so you will use these constantly from Day 33 onward. And note that `nan != nan` — which is why you test with `np.isnan()`, never with `== np.nan`.

### Boolean masking is filtering

```python
mask = prices > 1000        # an array of True/False, same shape
prices[mask]                # the values where True
mask.sum()                  # how many -- True counts as 1
mask.any() · mask.all()
np.where(mask)              # the INDICES where True

mask = (prices > 1000) & (qty < 5)      # & and |, NOT `and`/`or`
mask = ~(prices > 1000)                  # ~ for not
```

**The parentheses are mandatory.** `prices > 1000 & qty < 5` parses as `prices > (1000 & qty) < 5` because `&` binds tighter than `>`. This produces either an error or a wrong answer, and it is one of the most common NumPy mistakes.

`and`/`or` do not work on arrays at all — they ask for a single truth value and an array has many, so you get "The truth value of an array with more than one element is ambiguous." That error message means "you used `and` instead of `&`."

### Stacking and splitting

```python
np.vstack([a, b])      # stack rows      (2,3) + (2,3) -> (4,3)
np.hstack([a, b])      # stack columns   (2,3) + (2,3) -> (2,6)
np.concatenate([a, b], axis=0)
np.split(a, 3, axis=0)
```

These are `pd.concat` on Day 36, with the same axis meaning.

### `@` — matrix multiplication

```python
a * b       # ELEMENT-WISE -- shapes must match or broadcast
a @ b       # MATRIX MULTIPLICATION -- inner dimensions must agree
```

```
(m, n) @ (n, p)  ->  (m, p)
     ^inner dims match, and both disappear
```

Why this matters beyond NumPy: **a linear model is a matrix multiplication.** Predicting with `n` features across `m` rows is `X @ weights` — an `(m, n)` matrix of data times an `(n, 1)` vector of coefficients gives `(m, 1)` predictions. When you write `model.predict(X)` on Day 74, this is what runs.

You get the full geometric meaning on Days 65–68. Today, just recognise the operator and the shape rule.

---

## 💻 Code

`Day_31.py` — nine exercises:

**Aggregation (1–3)**
1. Ten aggregations on a `(100, 5)` array, with and without `axis`
2. **The NaN poison:** insert one `nan`, watch `mean()` return `nan`, fix with `nanmean`. Then count the NaNs.
3. `argmax` across an axis to answer "which product sold most in each region"

**Masking (4–6)**
4. Compound conditions with `&` and `|`
5. **The precedence bug:** write it without parentheses, see what happens, fix it
6. `np.where` to get indices, then use them to look up matching names from a second array

**Structure (7–8)**
7. `vstack`, `hstack`, `concatenate`, `split` — with shapes printed at each step
8. Build a `(1000, 3)` dataset from three separate 1D arrays

**Matrices (9)**
9. `*` versus `@` on the same pair of arrays. Predict both result shapes, then verify. Then compute a prediction as `X @ weights` — **this is exactly the arithmetic inside a linear model.**

---

## 🔬 Understanding Check

1. **Debugging.** Your mean came back as `nan`. What happened, and what are two fixes?
2. **Reasoning.** Why does `np.nan != np.nan`? How do you actually test for it?
3. **Debugging.** "The truth value of an array with more than one element is ambiguous" — what did you write, and what did you mean?
4. **Understanding.** Why do the parentheses in `(a > 1) & (b < 5)` matter?
5. **Comparison.** `a * b` vs `a @ b` — what must be true of the shapes in each case?
6. **Application.** Exercise 9's `X @ weights` is what a linear model computes. If `X` is `(1000, 5)`, what shape must `weights` be, and what shape are the predictions?
7. **Connection.** You are done with NumPy. Name three things you now expect Pandas to inherit from it.

---

## 🎯 Expected Outcome

- [ ] Aggregate along any axis, and handle NaN correctly
- [ ] Build compound boolean masks with correct precedence
- [ ] Stack and split arrays with confidence about shapes
- [ ] Explain `@` and predict its output shape

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians NumPy `1:30:01 → 1:59:34` @1.75× | 17 min |
| Aggregation, masking, `@` | 12 min |
| Nine exercises | 38 min |
| Daily review | 8 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Seven minutes, closed book. A `(200, 6)` array of student marks with some `nan` values:

1. Each subject's average, ignoring missing marks
2. How many marks are missing, per subject
3. Students with any mark below 40
4. The best subject for each student *(by index, and then by name)*
5. `marks @ weights` where `weights` is six subject credit-weights — and state the output shape before running it

---

## 🔁 Daily Review

1. Did I predict the NaN poisoning, or did it surprise me?
2. What did the precedence bug in exercise 5 actually produce?
3. Can I state the `@` shape rule without looking?
4. **NumPy is done in three days.** Was that enough, or is something still shaky? Pandas starts tomorrow and is built on this.

---

## 📦 Completion Criteria

- [ ] All nine exercises run
- [ ] NaN poisoning reproduced and fixed
- [ ] The precedence bug reproduced and fixed
- [ ] `X @ weights` computed, with the shape predicted first
- [ ] Mini assessment done closed-book
- [ ] Committed to git

---

**[← Day 30](../Day_30/Day_30.md)** · **[Day 32 →](../Day_32/Day_32.md)** · [README](../../../README.md)
