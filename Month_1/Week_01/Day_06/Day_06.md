# Day 6 — Comprehensions

|  |  |
|:--|:--|
| **Date** | Monday, 21 September 2026 |
| **Position** | Week 1 · Month 1 · Phase 1 — Python |
| **Budget** | **~45 min** — 🎓 **NIT Orientation begins today.** Short day on purpose. |
| **Code file** | `Day_06.py` |

> **Why today is short.** Orientation runs all week, Monday to Saturday, and it is mandatory. Trying to hold a two-hour study day on top of it is how plans die in week one. So today is 45 minutes on one high-value topic that needs no video, and it is designed to be done on your phone or laptop in a gap.
>
> **Today's real priority is orientation.** Meet people. Find the buildings. Ask about societies. That is genuinely more valuable to your 2027 than 90 extra minutes of Python.

---

## 🎯 Objective

Replace three-line loops with one-line comprehensions where — and only where — it makes the code clearer.

---

## 📚 Learn

### 🔴 MUST DO

No video today. Read this section, then write code. 10 minutes of reading, 30 of doing.

**The shape:**

```python
[ expression  for item in iterable  if condition ]
```

Read it in the order it executes: `for` → `if` → `expression`.

```python
prices = [1250, 180, 2600, 540]

[p * 1.17 for p in prices]                    # list
{p for p in prices if p > 500}                # set -- deduplicates
{name: p for name, p in zip(items, prices)}   # dict
(p * 1.17 for p in prices)                    # generator -- computes lazily
```

**The one rule that matters:** a comprehension should fit on one line and read like a sentence. Two conditions, a nested loop and a ternary inside is not clever — it is a loop that is now harder to debug. When in doubt, write the loop.

```python
# fine
clean = [clean_text(r) for r in rows if r]

# write the loop instead
out = [f(x) if x > 0 else g(x) for row in data for x in row if x is not None]
```

**Why this matters beyond style:** comprehensions are the mental bridge to vectorised thinking. `[p * 1.17 for p in prices]` is one step from `prices * 1.17` in NumPy on Day 29 — *describe the transformation, do not manage the iteration*. Getting comfortable here makes Week 5 easier.

### 🟢 IF TIME

- Skip it. Go to orientation. Talk to someone in your cohort.

---

## 💻 Code

### 🔴 MUST DO

`Day_06.py` — eight conversions. Each gives you a loop; you write the comprehension.

1. Squares of even numbers in a range
2. Clean a list of messy strings
3. Filter rows above a threshold
4. Build `{item: price}` from two lists
5. Extract one field from a list of dicts
6. Nested — flatten a list of lists
7. A dict comprehension with a condition on the **value**
8. **The trap:** one comprehension that should have stayed a loop — write it both ways and say which you would ship

---

## 🔬 Understanding Check

1. **Reasoning.** When is a comprehension *worse* than the loop it replaces?
2. **Comparison.** What do you get from a generator expression `(...)` that you do not get from a list `[...]`? When does the difference matter?
3. **Application.** You have 2 million rows and need one field from each. List comprehension or generator? Why?
4. **Understanding.** In `[f(x) for x in data if g(x)]`, what runs first — `f` or `g`?

---

## 🎯 Expected Outcome

- [ ] Write list, dict and set comprehensions without looking up the syntax
- [ ] Know when to refuse to write one
- [ ] Explain what a generator expression buys you

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Read the section above | 10 min |
| Eight conversions | 28 min |
| Daily review | 7 min |
| **Total** | **~45 min** |

---

## 🧪 Mini Assessment

Two minutes. Convert this, from memory:

```python
result = {}
for row in rows:
    if row["qty"] > 0:
        result[row["item"]] = row["qty"] * row["price"]
```

---

## 🔁 Daily Review

1. Which comprehension did I have to write as a loop first?
2. Did exercise 8 change my opinion about when to use them?
3. **Orientation check:** one useful thing I learned about NIT today, and one person's name I now know.

---

## 📦 Completion Criteria

- [ ] Eight conversions written and running
- [ ] Exercise 8 answered — both versions, plus a judgement
- [ ] Mini assessment done from memory
- [ ] Daily review filled in, including the orientation line

---

**[← Day 5](../Day_05/Day_05.md)** · **[Day 7 →](../Day_07/Day_07.md)** · [README](../../../README.md)
