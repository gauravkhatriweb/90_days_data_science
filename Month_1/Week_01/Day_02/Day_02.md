# Day 2 — Python Idiom: The Translation Layer

|  |  |
|:--|:--|
| **Date** | Thursday, 17 September 2026 |
| **Position** | Week 1 · Month 1 · Phase 1 — Python |
| **Budget** | **~120 min** — still free, still high capacity |
| **Code file** | `Day_02.py` |

> **Why today looks like this.** You already know what a variable, a loop and a function *are* — three years at Aptech and a MERN stack settled that. What you do not yet have is Python's **idiom**: the way Python people actually write. So today is not "learn variables." It is a translation layer from what you already know, plus the places where Python genuinely behaves differently from JavaScript and will bite you.
>
> Watch at **1.5–2×**. If the instructor is explaining what a string is, skip forward.

---

## 🎯 Objective

Stop writing JavaScript in Python. Leave today able to read idiomatic Python without translating it in your head first.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Python](https://www.youtube.com/watch?v=_aWbUudZ5Yo) · **`25:19 → 59:11`** | PRIMARY · video @1.75× | 20 min | Variables, data types, strings, type conversion |
| [Sheryians Python](https://www.youtube.com/watch?v=_aWbUudZ5Yo) · **`59:11 → 1:39:27`** | PRIMARY · video @1.75× | 23 min | Operators — arithmetic, comparison, logical, identity |
| The translation table below | REFERENCE | 10 min | The traps specifically |

### 🟢 IF TIME

- [CodeWithHarry `34:55 → 1:40:20`](https://www.youtube.com/watch?v=UrsmFxEIp5k) — variables, datatypes and strings in Hindi, if any of the above did not land. **Only if it did not land.** Do not watch this by default.

---

## 🧠 Core Concepts

### The translation table — JavaScript → Python

| What you do in JS | What you do in Python | The trap |
|:------------------|:----------------------|:---------|
| `let x = 5; const y = 6;` | `x = 5` · `Y = 6` (convention only) | Python has **no real constants**. `Y` uppercase is a promise, not a rule. |
| `camelCase` | `snake_case` | Enforced socially, not by the interpreter. Use it anyway. |
| `` `Hello ${name}` `` | `f"Hello {name}"` | The `f` prefix is mandatory. Forgetting it prints the braces literally. |
| `===` vs `==` | `==` vs `is` | **`is` is not a strict `===`.** `is` compares *identity* (same object in memory). Use `==` for values, `is` only for `None`, `True`, `False`. |
| `null` and `undefined` | `None` | One concept, not two. |
| `x ? a : b` | `a if x else b` | Condition goes in the middle. Reads strangely at first. |
| `arr.length` | `len(arr)` | A function, not a property. Same for `str`, `dict`, `set`. |
| `"5" + 5 → "55"` | `"5" + 5 → TypeError` | **Python refuses to guess.** This is a feature. Convert explicitly: `int("5") + 5`. |
| `&&` `\|\|` `!` | `and` `or` `not` | Words, not symbols. |
| `//` comment | `#` comment | `//` in Python is *integer division*. Writing `// note` will not error — it will do something. |
| `typeof x` | `type(x)` | Returns the class, not a string. |
| Blocks with `{ }` | Blocks with **indentation** | Four spaces. Mixing tabs and spaces is a runtime error. |

### Truthiness — where Python and JS actually disagree

Python treats these as false: `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`.

The important one: **an empty list is falsy in Python; an empty array is truthy in JavaScript.** This single difference will cause you a real bug in the next 90 days if you do not internalise it now:

```python
rows = []
if rows:                 # False -- this is the Pythonic empty check
    process(rows)

if len(rows) > 0:        # works, but nobody writes this
    process(rows)
```

### Mutable vs immutable — the concept that matters most today

| Immutable | Mutable |
|:----------|:--------|
| `int` `float` `str` `tuple` `bool` `frozenset` | `list` `dict` `set` |

A string operation never changes the string — it returns a new one. `"abc".upper()` does not modify `"abc"`. This is why:

```python
name = "gaurav"
name.upper()          # computes "GAURAV", throws it away
print(name)           # 'gaurav' -- unchanged

name = name.upper()   # you have to reassign
```

Lists are the opposite — `sort()` changes the list and returns `None`. Assigning `x = my_list.sort()` gives you `None`, and this catches almost everyone once.

### Strings — the ones you will actually use

`.strip()` `.lower()` `.upper()` `.split(sep)` `sep.join(list)` `.replace(a, b)` `.startswith()` `.endswith()` `.find()` `in`

`.strip()` and `.split()` alone will do most of your data cleaning in Week 2.

---

## 💻 Code

### 🔴 MUST DO

`Day_02.py` — nine exercises. The first five are direct translations of JavaScript you have written a hundred times; the last four are the traps.

1. Write a greeting with an f-string, including a computed value inside the braces
2. Fix four `TypeError`s caused by implicit-conversion habits
3. Predict the output of six truthiness checks **before** running them, then run them
4. Demonstrate the `is` vs `==` difference with two identical lists
5. Show that `.sort()` returns `None` and explain in a comment why
6. Chain five string methods to clean a messy product name
7. Split a CSV line by hand and convert the numeric fields
8. Write the ternary three ways and say which reads best
9. Build a small price-formatting helper used later in the week

### 🟢 IF TIME

- Take any 20-line JavaScript function from your SwiftBase or LifeOS work and rewrite it in Python. This is the highest-value exercise on this page — it forces the translation on code you actually understand.

---

## 🔬 Understanding Check

1. **Debugging.** `total = "5" + 5` raises `TypeError` in Python but returns `"55"` in JavaScript. Which language's behaviour would you rather have in a data-cleaning script, and why?
2. **Understanding.** Why does `"abc".upper()` not change `"abc"`? What would break if strings were mutable?
3. **Comparison.** When is `is` the correct operator and `==` wrong? Give a concrete case.
4. **Application.** You read a CSV row as `['  ACME ', '42', '199.50']`. Write the sequence of operations that turns it into a usable record. Name each method.
5. **Reasoning.** Python refuses to add a string and an integer. Name one situation where this strictness saves you and one where it is annoying.
6. **Teaching.** Explain mutable vs immutable to someone who has only used Excel.

---

## 🎯 Expected Outcome

By the end of today I can:

- [ ] Write Python that does not look like translated JavaScript
- [ ] Predict truthiness correctly for lists, dicts, strings and zero
- [ ] Explain why `my_list.sort()` returns `None` and `sorted(my_list)` does not
- [ ] Clean a messy string with chained methods without looking up the names

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians `25:19 → 1:39:27` @1.75× | 43 min |
| Translation table + traps | 10 min |
| Nine exercises | 50 min |
| Daily review | 10 min |
| **Total** | **~113 min** |

---

## 🧪 Mini Assessment

Closed book, 10 minutes. Given:

```python
raw = "  Ariel Detergent 1kg ,  2 , 545.00  "
```

Produce `{'item': 'ariel detergent 1kg', 'qty': 2, 'price': 545.0}` in one function. No imports.

---

## 🔁 Daily Review

1. Which trap in the translation table did I get wrong when I predicted the output?
2. What can I now write from memory that I could not yesterday?
3. Is there anything from the video I watched but could not reproduce? (If yes, that goes in tomorrow's warm-up.)
4. Was 1.75× too fast, right, or too slow? Adjust tomorrow accordingly.

---

## 📦 Completion Criteria

- [ ] All nine exercises in `Day_02.py` run without error
- [ ] Truthiness predictions written down **before** running, and scored
- [ ] Mini assessment completed closed-book in under 12 minutes
- [ ] Understanding Check answered in writing
- [ ] Committed to git

---

**[← Day 1](../Day_01/Day_01.md)** · **[Day 3 →](../Day_03/Day_03.md)** · [README](../../../README.md)
