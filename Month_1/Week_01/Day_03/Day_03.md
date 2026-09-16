# Day 3 — Control Flow and Loops, the Python Way

|  |  |
|:--|:--|
| **Date** | Friday, 18 September 2026 |
| **Position** | Week 1 · Month 1 · Phase 1 — Python |
| **Budget** | **~120 min** — last full weekday before the weekend block |
| **Code file** | `Day_03.py` |

> **Why today looks like this.** Every language has loops. Python's difference is that **you almost never write an index.** The `for i = 0; i < n; i++` habit is the clearest sign of someone writing another language in Python, and it will make your Pandas code worse later — because Pandas punishes loop-thinking hard. Today replaces that habit.

---

## 🎯 Objective

Write loops that iterate over *things* rather than over *positions*, and know the four tools (`enumerate`, `zip`, `range`, `in`) that make indices unnecessary.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Python](https://www.youtube.com/watch?v=_aWbUudZ5Yo) · **`1:39:27 → 2:16:14`** | PRIMARY · @1.75× | 21 min | If / elif / else, logic building |
| [Sheryians Python](https://www.youtube.com/watch?v=_aWbUudZ5Yo) · **`2:16:14 → 3:00:00`** | PRIMARY · @1.75× | 25 min | For and while loops |
| The four tools below | REFERENCE | 8 min | What replaces the index |

### 🟢 IF TIME

- [Apna College `05:01:26 → 06:04:25`](https://www.youtube.com/watch?v=ERCMXc8x7mc) — loops explained differently, with a heavier practice-question emphasis. Only if the primary left gaps.

---

## 🧠 Core Concepts

### The four tools that kill the index

```python
items = ["tea", "sugar", "flour"]
prices = [1250, 180, 2600]

for item in items:                        # 1. iterate the thing
    print(item)

for i, item in enumerate(items, start=1): # 2. when you genuinely need position
    print(i, item)

for item, price in zip(items, prices):    # 3. two lists in step
    print(item, price)

for n in range(5):                        # 4. when you need a count, not a collection
    print(n)
```

**The rule:** reach for `range(len(x))` only when you are modifying `x` in place by index. Almost never.

### `else` on a loop — Python's strangest feature

```python
for row in rows:
    if row.is_valid():
        break
else:
    print("no valid row found")     # runs only if the loop never broke
```

Worth knowing because you will meet it in real code, not because you should write it often.

### Guard clauses beat nesting

```python
# nested -- the shape of code that gets hard to read
def process(row):
    if row is not None:
        if row.qty > 0:
            if row.price > 0:
                return row.qty * row.price

# guarded -- flat, and each failure reason is explicit
def process(row):
    if row is None:      return None
    if row.qty <= 0:     return None
    if row.price <= 0:   return None
    return row.qty * row.price
```

You will use this constantly in data cleaning, where most of the code is "reasons to reject a row."

### `while` — and why data work rarely needs it

`while` is for "until a condition changes": retry loops, user input, convergence. **Gradient descent on Day 72 is a `while` loop.** For iterating over data, `for` is nearly always correct.

### `break`, `continue`, and the cost of both

`continue` is fine and often clearer than nesting. `break` inside nested loops is where bugs live — if you need it, that block probably wants to be a function with a `return`.

---

## 💻 Code

### 🔴 MUST DO

`Day_03.py` — ten exercises, drawn from the Week 1 bank in `Tem.txt` (lines 1906–1937) but rewritten so each one has a reason:

1. FizzBuzz — but return a list, do not print (this distinction matters later)
2. Rewrite three index-based loops without indices
3. Two lists, one loop — use `zip` to build a price lookup
4. Numbered output with `enumerate(start=1)`
5. Find the second-largest number **without sorting**
6. Guard-clause refactor of a four-level nested function
7. A `while` loop that converges — halve a number until it is under a threshold, count the steps
8. Count vowels, consonants and digits in one pass
9. Print a triangle pattern (loop-nesting practice)
10. Validate a batch of transaction rows and return `(valid, rejected_with_reasons)`

Exercise 10 is the one that matters — it is a data-cleaning function in miniature and you will write its bigger version in Week 2.

### 🟢 IF TIME

- Questions Q12, Q15, Q22 and Q26 from the `Tem.txt` Week 1 bank (number guessing game, Fibonacci, Armstrong numbers, decimal→binary). Pure logic-building reps.

---

## 🔬 Understanding Check

1. **Comparison.** When is `for i in range(len(items))` actually correct rather than lazy?
2. **Reasoning.** Why does iterating with `enumerate` communicate intent better than manually incrementing a counter?
3. **Debugging.** This code silently does nothing. Why?
   ```python
   rows = [1, 2, 3]
   for row in rows:
       rows.remove(row)
   ```
4. **Application.** You have 50,000 shop transactions and need the ones above PKR 10,000. Describe the loop — then say why in Week 5 you will stop writing this loop at all.
5. **Understanding.** What does a `for/else` do, and why do most Python programmers avoid it?
6. **Teaching.** Explain `break` versus `continue` using a real-world queue.

---

## 🎯 Expected Outcome

- [ ] Write loops without indices by default
- [ ] Use `enumerate` and `zip` without looking up the syntax
- [ ] Refactor nested conditionals into guard clauses
- [ ] Explain why mutating a list while iterating it is a bug

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians `1:39:27 → 3:00:00` @1.75× | 46 min |
| Four tools + guard clauses | 8 min |
| Ten exercises | 55 min |
| Daily review | 10 min |
| **Total** | **~119 min** |

---

## 🧪 Mini Assessment

Closed book, 12 minutes. Given a list of `(item, qty, price)` tuples, return a dict mapping each item to its total revenue — but skip any row where `qty` or `price` is non-positive, and count how many you skipped. One function, no imports.

---

## 🔁 Daily Review

1. How many of my ten solutions used an index? (Target: at most one.)
2. Which exercise took longest, and was it the logic or the syntax?
3. Can I write `enumerate` and `zip` from memory right now, without scrolling up?
4. What is still unclear enough that I should revisit it tomorrow morning?

---

## 📦 Completion Criteria

- [ ] Ten exercises run correctly
- [ ] Exercise 10 returns both valid rows *and* rejection reasons
- [ ] Mini assessment done closed-book
- [ ] Understanding Check answered in writing
- [ ] Committed to git

---

**[← Day 2](../Day_02/Day_02.md)** · **[Day 4 →](../Day_04/Day_04.md)** · [README](../../../README.md)
