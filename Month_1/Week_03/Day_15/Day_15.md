# Day 15 — Why Objects Exist

|  |  |
|:--|:--|
| **Date** | Wednesday, 30 September 2026 |
| **Position** | Week 3 · Month 1 · Phase 1 — **OOP block, day 1 of 9** |
| **Budget** | **~75 min** — semester week 1 |
| **Code file** | `Day_15.py` |

> **Why this block exists, and why it is nine days.** You have said OOP is your weakest and least favourite area. That is why it gets more time than anything else in Month 1, and why four different teachers explain it.
>
> **And here is the diagnosis.** Most OOP tutorials start with `class Dog:` and `def bark():`. Nobody has ever needed a Dog class. So the syntax goes in, the *reason* does not, and you end up able to write a class without knowing when to. That is not a failure of ability — it is a failure of teaching order.
>
> So this block starts backwards. Today you do not write a class. Today you take code you already wrote — `shopsummary` — and find the specific place where functions stop being enough. **Only then does the syntax mean anything.**
>
> One more thing worth knowing: next semester you take **CSE 205 — Object-Oriented Programming and Data Structures**, four credits, in Java. These nine days are also that course's head start.

---

## 🎯 Objective

Be able to state, from your own code, the problem that objects solve — before learning any class syntax.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| The diagnosis below — **do this first, with your own code open** | PRACTICE | 25 min | Find the problem yourself |
| [Corey Schafer — OOP 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM) | **PRIMARY** · 15 min | 15 min | Now the syntax has something to attach to |

### 🟢 IF TIME

- [Sheryians Python `7:24:17 → 7:50:00`](https://www.youtube.com/watch?v=_aWbUudZ5Yo) — the same ground at a gentler pace. Use it only if Corey Schafer moved too fast.

---

## 🧠 Core Concepts

### The diagnosis — do this before any video

Open your Day 12 `shopsummary`. Look for these four symptoms. **You wrote this code; the problem is genuinely in there.**

**Symptom 1 — the same arguments, everywhere.**

```python
total_revenue(records, min_qty=1)
top_n(records, key="revenue", n=3)
group_totals(records, by="region", value="revenue")
validate_rows(records)
```

`records` is passed to every function. It is not really an *argument* — it is the thing the whole module is *about*.

**Symptom 2 — data and the operations on it live apart.** `records` is in one place; the six functions that only make sense for `records` are in another. Nothing connects them. Nothing stops you passing the wrong list.

**Symptom 3 — derived values get recomputed or passed around.** `total` is computed in one function and needed in three. So you either recompute it, or thread it through every signature.

**Symptom 4 — two sources, two sets of functions.** Add CSV *and* JSON input and you get `read_records_csv()` and `read_records_json()`, and then every caller needs an `if`.

**Now write, in your own words:** *"Functions became awkward in `shopsummary` when ______."*

That sentence is the point of today. An object is **data and the operations that belong to it, kept together, with the shared state held once.**

### The syntax, now that it has a job

```python
class SalesData:
    def __init__(self, records):     # runs when you create one
        self.records = records       # state lives on the instance
        self._total = None           # derived, computed once

    def total(self):                 # an operation that belongs to the data
        if self._total is None:
            self._total = sum(r["qty"] * r["price"] for r in self.records)
        return self._total
```

```python
data = SalesData(records)     # create an INSTANCE of the CLASS
data.total()                  # the data is no longer an argument
```

| Term | Meaning |
|:-----|:--------|
| **Class** | The blueprint. `SalesData`. |
| **Instance** | One actual thing built from it. `data`. |
| **Attribute** | Data on an instance. `data.records`. |
| **Method** | A function that belongs to the class. `data.total()`. |
| **`__init__`** | Runs at creation. **Not** a constructor in the Java sense — the object already exists; this initialises it. |
| **`self`** | The instance the method was called on. |

### `self` — the thing everyone finds strange

`data.total()` is Python quietly calling `SalesData.total(data)`. The instance is passed as the first argument, and by convention that parameter is named `self`. It is not a keyword. It is a parameter name you could change — and should not.

This is the one-sentence version: **`self` is how a method knows which instance it was called on.**

---

## 💻 Code

### 🔴 MUST DO

`Day_15.py`:

1. Write the diagnosis — the four symptoms as they appear in *your* `shopsummary`, with line references
2. Complete the sentence: *"Functions became awkward when ______"*
3. Write `SalesData` with `__init__` storing records, and a `count()` method
4. Create two instances from different record lists; show they do not interfere
5. Add `total()` and `mean()`, both using `self.records`
6. Demonstrate `SalesData.count(data)` and `data.count()` producing the same result — then explain `self` in a comment
7. **The counter-example:** write a class that should have been a function, and say why

Exercise 7 matters as much as the rest. OOP has an opposite failure mode — wrapping one function in a class for no reason — and knowing both edges is what "understanding OOP" means.

### 🟢 IF TIME

- Convert one more `shopsummary` function into a method and note what got simpler.

---

## 🔬 Understanding Check

1. **Reasoning.** In your own words, from your own code: what problem do objects solve that functions do not?
2. **Understanding.** What is the difference between a class and an instance? Give a non-programming analogy that is not "blueprint and house".
3. **Debugging.** `TypeError: count() takes 0 positional arguments but 1 was given`. What did the author forget?
4. **Comparison.** When is a class the wrong choice? Give a concrete example — exercise 7 is your answer.
5. **Application.** Look at your LifeOS Apps Script or SwiftBase code. Name one place where an object would genuinely have helped, and one where it would have been overkill.
6. **Teaching.** Explain `self` to someone who has written functions but never a class. Under 60 seconds.

---

## 🎯 Expected Outcome

- [ ] State the problem objects solve, using my own code as the example
- [ ] Write a class with `__init__` and a method without copying syntax
- [ ] Explain `self` without saying "it just means the object"
- [ ] Recognise when a class is the *wrong* answer

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| The diagnosis, in your own code | 25 min |
| Corey Schafer OOP 1 | 15 min |
| Seven exercises | 30 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Five minutes, closed book. Write a class `Inventory` that holds a dict of item → quantity, with `add(item, qty)` and `low_stock(threshold)`. Then answer in one sentence: **why is this better as a class than as two functions plus a dict?** If you cannot answer that, the class is not justified.

---

## 🔁 Daily Review

1. What was my sentence — "functions became awkward when ___"?
2. Did the syntax make more sense *after* the diagnosis than it has in previous attempts at OOP?
3. What is still unclear about `self`?
4. Exercise 7: what made that class unjustified?

---

## 📦 Completion Criteria

- [ ] Four symptoms identified in your own `shopsummary`, with line references
- [ ] The sentence written
- [ ] `SalesData` works with two independent instances
- [ ] `self` explained in your own words, in a comment
- [ ] The counter-example written and justified
- [ ] Committed to git

---

**[← Week 2 Review](../../Week_02/Week_02_Review.md)** · **[Day 16 →](../Day_16/Day_16.md)** · [README](../../../README.md)
