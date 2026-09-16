# Day 29 — NumPy: Why Arrays Are Not Lists

|  |  |
|:--|:--|
| **Date** | Wednesday, 14 October 2026 |
| **Position** | Week 5 · Month 2 · **Phase 2 — Data manipulation** |
| **Budget** | **~75 min** |
| **Code file** | `Day_29.py` |

> **Month 2 starts here.** Python stops being the subject and becomes the tool.
>
> **Why NumPy gets only three days.** NumPy is a substrate, not a destination — you will use it constantly and rarely think about it. What matters is understanding *why* it exists, because that understanding is what makes Pandas make sense. Pandas is built on NumPy, and every "why is Pandas doing that?" question from Day 32 onward has a NumPy answer.

---

## 🎯 Objective

Understand what an array is, why it is faster than a list, and how indexing and slicing differ from Python's — including the copy-versus-view distinction that causes silent bugs.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians NumPy](https://www.youtube.com/watch?v=Utgwk0r9Zq4) · **`19:28 → 1:04:12`** · @1.75× | PRIMARY | 25 min | Why arrays, then indexing, slicing, iteration |
| The memory model below | REFERENCE | 12 min | The part the video does not explain |

**Skip `0:00 → 19:28`** — it is Anaconda and Jupyter setup, and you already have a working environment from Day 1. Starting at 19:28 saves you twenty minutes on installation you do not need.

### 🟢 IF TIME

- [3Blue1Brown — Vectors, Chapter 1](https://www.youtube.com/watch?v=fNk_zzaMoSs) · 10 min. You get the full linear algebra block on Days 65–68; this is a useful preview of what an array *represents*.

---

## 🧠 Core Concepts

### Why a list is slow

```python
prices = [1250, 180, 2600]
```

A Python list is an array of **pointers**. Each element is a full `PyObject` somewhere else in memory, carrying a type tag, a reference count and the value. Adding two lists element-wise means: follow a pointer, check the type, unbox the value, add, allocate a new object, store a pointer. Per element.

```python
prices = np.array([1250, 180, 2600])
```

A NumPy array is **one contiguous block of raw numbers**, all the same type. The type is checked once, for the whole array. Adding two arrays runs a tight loop in C over adjacent memory — no pointers, no type checks, no allocation per element.

**Two consequences:**

| | Effect |
|:--|:--|
| **Speed** | 10–100× on numeric work — measure it in exercise 1 |
| **Memory** | A million integers: ~8 MB as an array, ~40 MB as a list |

**And the cost:** an array has **one dtype**. Mixed types force it to `object`, which throws away every advantage. `np.array([1, "two", 3.0])` produces an object array that is slower than a list.

### `dtype`, `shape`, `ndim`, `size`

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape     # (2, 3)  -- 2 rows, 3 columns
a.ndim      # 2
a.size      # 6
a.dtype     # dtype('int64')
```

**`shape` is the one to internalise.** Most NumPy errors are shape errors, and most shape errors are solved by printing `.shape` before the line that failed.

### The integer-overflow trap

```python
np.array([2_000_000_000, 2_000_000_000], dtype=np.int32).sum()
# -294967296   -- wrapped around, silently
```

Python integers are arbitrary precision. NumPy integers are fixed width. This produces a **wrong number with no error**, and it is one of the few places NumPy will genuinely lie to you.

### Indexing: where it stops being like a list

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

a[0]            # [1 2 3]       -- a row
a[0, 2]         # 3             -- row 0, column 2  (a[0][2] also works, slower)
a[:, 1]         # [2 5]         -- a whole COLUMN. Lists cannot do this.
a[a > 3]        # [4 5 6]       -- boolean mask
a[[0, 1], [1, 2]]  # [2 6]      -- fancy indexing: (0,1) and (1,2)
```

`a[:, 1]` is the one that changes how you think. Selecting a column from a list of lists needs a comprehension; here it is a slice, and it is instant.

### The copy-versus-view trap — the important one

```python
a = np.array([1, 2, 3, 4, 5])
b = a[1:4]        # a VIEW -- no data copied
b[0] = 999
a                 # [1, 999, 3, 4, 5]   <- a changed
```

**NumPy slices are views; Python list slices are copies.** A slice is a window onto the same memory. Writing through the window changes the original.

```python
b = a[1:4].copy()     # explicit copy when you need independence
```

This is by far the most common source of "my data changed and I do not know why" — and it appears again in Pandas as the `SettingWithCopyWarning` on Day 33. Understanding it here means understanding it there.

**Fancy indexing and boolean masks always copy.** Basic slicing always views. That asymmetry is worth remembering.

---

## 💻 Code

`Day_29.py` — eleven exercises:

**Why arrays (1–3)**
1. **Measure it.** Sum a million values as a list and as an array. Time both. Record the ratio.
2. Measure memory for both with `sys.getsizeof` and `.nbytes`.
3. Build an array of mixed types, inspect the dtype, and explain what was lost.

**Anatomy (4–6)**
4. Create arrays with `array`, `zeros`, `ones`, `arange`, `linspace`, `random.rand`; print shape, ndim, size, dtype for each
5. Reshape 1–12 into `(3,4)`, then `(4,3)`, then `(2,2,3)`. Explain what `-1` does in `reshape`.
6. **Reproduce the int32 overflow.** Then fix it two ways.

**Indexing (7–9)**
7. From a 2D array: one element, one row, one column, a sub-block
8. Boolean masking — all values above the mean, and the count
9. Fancy indexing to pull out a specific set of coordinates

**The trap (10–11)**
10. **Reproduce the view bug.** Slice, modify, watch the original change. Then use `.copy()`.
11. Determine experimentally which of these are views and which are copies: basic slice, boolean mask, fancy index, `reshape`, `transpose`, `ravel`. *(Use `np.shares_memory`.)*

---

## 🔬 Understanding Check

1. **Reasoning.** Why is a NumPy array faster than a list for numeric work? Answer in terms of memory layout.
2. **Understanding.** Exercise 3: what did the array lose when you mixed types?
3. **Debugging.** Exercise 6 gave a wrong sum with no error. Why does NumPy allow this, and how would you catch it in real data?
4. **Comparison.** Python list slices vs NumPy array slices — state the difference and why NumPy chose its behaviour.
5. **Application.** You slice a column from a big array and modify it. What happens to the original, and when do you want that?
6. **Reasoning.** Exercise 11: why do boolean masks copy while basic slices view?
7. **Connection.** Pandas is built on NumPy. Predict one Pandas behaviour that will surprise you because of what you learned today. *(Check yourself on Day 33.)*

---

## 🎯 Expected Outcome

- [ ] Explain why arrays are faster, in terms of memory
- [ ] Read and write `.shape` fluently
- [ ] Index rows, columns, blocks, masks and fancy coordinates
- [ ] Predict whether an operation gives a view or a copy

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians NumPy `19:28 → 1:04:12` @1.75× | 25 min |
| Memory model | 12 min |
| Eleven exercises | 32 min |
| Daily review | 6 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Five minutes, closed book. Given a `(100, 5)` array of exam scores — 100 students, 5 subjects:

1. The mean score per subject
2. Every student whose average is above 80
3. The highest score in subject 3, and which student got it
4. A copy of the first ten students that can be modified without touching the original

---

## 🔁 Daily Review

1. Exercise 1: what was the actual speed ratio? Did it surprise me?
2. Did I predict the view bug before running exercise 10?
3. Exercise 11: which results surprised me?
4. What is the one NumPy idea I would struggle to explain right now?

---

## 📦 Completion Criteria

- [ ] Speed and memory measured, with real numbers recorded
- [ ] The int32 overflow reproduced and fixed
- [ ] The view bug reproduced and fixed
- [ ] Exercise 11's view/copy table completed experimentally
- [ ] Mini assessment done closed-book
- [ ] Committed to git

---

**[← Month 1 Review](../../../Month_1/Month_1_Review.md)** · **[Day 30 →](../Day_30/Day_30.md)** · [README](../../../README.md)
