# Day 19 — Encapsulation, Properties, and Making Objects Behave Like Python

|  |  |
|:--|:--|
| **Date** | Sunday, 4 October 2026 |
| **Position** | Week 3 · Month 1 · **OOP block, day 5 of 9** |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_19.py` |
| **Second track** | 📐 **Essential Math Ch. 1, pp. 22–31** (40 min) — limits and derivatives |

> **Why today is the one that changes how your code feels.** Dunder methods are what make an object work with `len()`, `for`, `in`, `[]`, `==` and `print()`. Until you have written them, your classes are containers you poke at with method calls. After today, they behave like the built-in types — and Pandas, which you meet in two weeks, is almost entirely dunder methods. `df[df.price > 100]` works because someone implemented `__getitem__` and `__gt__`.

---

## 🎯 Objective

Control what a class exposes, turn computed values into attributes with `@property`, and make objects work with Python's built-in syntax.

---

## 📚 Learn — Track 1: OOP (≈ 50 min)

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Corey Schafer — OOP 5: Special (Magic/Dunder) Methods](https://www.youtube.com/watch?v=3ohzBxoFHAY) | **PRIMARY** | 13 min | `__repr__`, `__str__`, `__len__`, operator overloading |
| [Corey Schafer — OOP 6: Property Decorators](https://www.youtube.com/watch?v=jCzT9XFZ5bw) | **PRIMARY** | 10 min | Getters and setters, the Python way |
| Encapsulation + polymorphism below | REFERENCE | 15 min | Neither video covers these properly |

### 🟢 IF TIME

- [Sheryians Python `9:18:32 → 9:45:00`](https://www.youtube.com/watch?v=_aWbUudZ5Yo) — decorators, which is the machinery under `@property`.

---

## 🧠 Core Concepts

### Encapsulation — Python's version is a convention, not a wall

| Name | Means | Enforced? |
|:-----|:------|:----------|
| `self.total` | Public. Use freely. | — |
| `self._cache` | **Internal.** Not part of the API. | **No.** A promise between adults. |
| `self.__secret` | Name-mangled to `_ClassName__secret` | Partly — it discourages, it does not prevent |

Python has no `private`. The single underscore is a signal: *"this is mine, I may change it, do not depend on it."* Coming from a language with real access control, this feels wrong. It works because the convention is universal.

**Use `_` liberally for internals. Use `__` almost never** — it exists to avoid name collisions in subclasses, not to hide things.

### `@property` — computed values that look like attributes

```python
class Ledger:
    def __init__(self, records):
        self.records = records

    @property
    def total(self):
        return sum(r["qty"] * r["price"] for r in self.records)

    @property
    def mean(self):
        return self.total / len(self.records) if self.records else 0.0
```

```python
ledger.total        # no parentheses -- reads like data, computes like a method
```

**Why this matters beyond style:** you can start with a plain attribute `self.total = ...` and later turn it into a computed `@property` **without changing a single caller.** That is the whole point — the public interface stays stable while the implementation changes.

With a setter, it becomes validation at the boundary:

```python
    @property
    def delivery_fee(self):
        return self._delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, value):
        if value < 0:
            raise ValueError(f"delivery fee cannot be negative: {value}")
        self._delivery_fee = value
```

Now `ledger.delivery_fee = -50` raises immediately, at the place the mistake was made — instead of producing a wrong total three functions later.

### Dunder methods — the ones actually worth knowing

| Method | Enables | Notes |
|:-------|:--------|:------|
| `__repr__` | `repr(obj)`, the REPL, debugger output | **Write this one always.** Aim for unambiguous. |
| `__str__` | `str(obj)`, `print(obj)` | Optional — falls back to `__repr__` |
| `__len__` | `len(obj)` | Must return a non-negative `int` |
| `__getitem__` | `obj[key]`, **and iteration for free** | This is the Pandas one |
| `__eq__` | `==` | Define `__hash__` too if you want it in a set |
| `__lt__` | `<`, and `sorted()` | `functools.total_ordering` generates the rest |
| `__contains__` | `in` | Otherwise Python falls back to iterating |
| `__iter__` | `for x in obj` | Explicit iteration |
| `__add__` | `+` | Only when addition genuinely means something |

**`__repr__` is the highest-value method on this list.** Without it, debugging shows `<Ledger object at 0x10f3a2b50>`, which tells you nothing. With it, you see `Ledger('Khatri Traders', 47 records, PKR 128,400.00)` in every traceback and debugger frame for the rest of the project.

The convention: `__repr__` should ideally be something you could paste back into Python to recreate the object.

### Polymorphism — you have already used it

Day 18, exercise 4: one `print_report()` function that worked on three ledger types. That is polymorphism — **the same call doing the right thing for different types.**

Python does it through **duck typing**: it never checks the class, only whether the method exists.

```python
def load_all(sources):
    return [s.load() for s in sources]      # works for ANY object with .load()
```

`CsvSource`, `JsonSource` and a test fake share no base class. They share a *method name*. That is enough, and it is why composition is so cheap in Python.

**The practical consequence:** you do not need an interface to write polymorphic code. Tomorrow you will learn when declaring one anyway is worth it.

---

## 📐 Learn — Track 2: Essential Math Ch. 1 (40 min)

**Read pages 22–31:** *Limits · Derivatives · Partial Derivatives.*

Type the SymPy examples as you go — Nield's whole approach is that you compute derivatives with `sympy` rather than by hand, which is why this fits in 40 minutes.

### The one sentence to hold on to

> **A derivative is the slope of a function at a single point — how fast the output changes when you nudge the input.**

That is all it is. And it is the entire foundation of Day 72, where gradient descent works by asking "which way is downhill from here?" — a question whose answer *is* a derivative.

**Partial derivatives** are the same idea with more than one input: nudge one variable, hold the others still. A model with twelve features needs twelve partial derivatives to know which way is downhill. That is the whole of training.

### The MAT 265 link

Limits, continuity and derivatives are the core of your calculus course. Same content, forty pages, with Python. Note in the review which parts your course has reached.

---

## 💻 Code

### 🔴 MUST DO

`Day_19.py` — one class, built up properly:

1. Add `_` prefixes to every internal attribute in `ShopLedger`; access one from outside and observe nothing stops you
2. Demonstrate `__` name mangling, then explain why it is not "private"
3. Convert `total()` and `mean()` to `@property` — and confirm **no caller had to change**
4. Add a `delivery_fee` setter that rejects negatives; show the error appears at assignment, not later
5. Write `__repr__`. Make it genuinely useful in a traceback.
6. Write `__str__` for a human-readable one-liner; show where each is used
7. `__len__` so `len(ledger)` works
8. `__getitem__` so `ledger[0]` works — then discover that `for r in ledger` now works too, and explain why
9. `__eq__` comparing ledgers by content; then add `__hash__` and put them in a set
10. `__lt__` so `sorted(ledgers)` orders by total
11. `__contains__` so `"tea" in ledger` works
12. **Polymorphism:** one function over three unrelated classes that only share a method name — no inheritance anywhere

### 🟢 IF TIME

- `__add__` to merge two ledgers. Then argue in a comment whether `+` is honest here or clever-but-confusing.

---

## 🔬 Understanding Check

1. **Understanding.** Python has no `private`. Why does the underscore convention work anyway?
2. **Reasoning.** What does `@property` let you change later without breaking callers? Why is that valuable in a library?
3. **Comparison.** `__repr__` vs `__str__` — who is each for, and which would you write if you wrote only one?
4. **Application.** Exercise 4 rejects a negative fee at assignment. Why is failing there better than failing in `total()`?
5. **Understanding.** Exercise 8: why did implementing `__getitem__` also give you iteration?
6. **Reasoning.** Exercise 12 works with no shared base class. What is Python actually checking?
7. **Interview.** "What is duck typing?" 30 seconds, with an example from today.
8. **Maths.** In one sentence, what is a derivative? In one more, why will gradient descent need it?

---

## 🎯 Expected Outcome

- [ ] Use `_` and `@property` deliberately
- [ ] Validate at assignment rather than at use
- [ ] Write `__repr__`, `__len__`, `__getitem__`, `__eq__` from memory
- [ ] Explain duck typing with your own example
- [ ] Say what a derivative is without hedging

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Corey Schafer 5 + 6 | 23 min |
| Encapsulation + polymorphism | 15 min |
| Twelve exercises | 90 min |
| **Essential Math Ch. 1, pp. 22–31** | 40 min |
| Daily review | 12 min |
| **Total** | **~180 min** |

---

## 🧪 Mini Assessment

Twelve minutes, closed book. Write `PriceList`:

- holds `{item: price}`
- `len()` gives the item count
- `pl["tea"]` returns a price, raising `KeyError` with a useful message if absent
- `"tea" in pl` works
- `for item in pl` iterates item names
- `__repr__` shows the class name and item count
- `pl.average` is a **property**, not a method

---

## 🔁 Daily Review

1. Which dunder method changed how my code *feels* the most?
2. Exercise 3: did any caller need to change when `total()` became a property?
3. Can I now explain why `df[df.price > 100]` works in Pandas, in terms of dunder methods?
4. **Maths:** what is a derivative, in my own words? Has MAT 265 reached limits yet?
5. Two-thirds through the OOP block. Rate my comfort 1–5 and say what is still weakest.

---

## 📦 Completion Criteria

- [ ] All twelve exercises working
- [ ] `@property` conversion required zero caller changes
- [ ] `__repr__` genuinely useful in a traceback
- [ ] Exercise 8's free iteration explained
- [ ] `PriceList` written closed-book
- [ ] Essential Math pp. 22–31 read with SymPy examples typed
- [ ] Derivative definition written in my own words
- [ ] Committed to git

---

**[← Day 18](../Day_18/Day_18.md)** · **[Day 20 →](../Day_20/Day_20.md)** · [README](../../../README.md)
