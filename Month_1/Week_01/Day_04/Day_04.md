# Day 4 — Functions That Do One Thing

|  |  |
|:--|:--|
| **Date** | Saturday, 19 September 2026 |
| **Position** | Week 1 · Month 1 · Phase 1 — Python |
| **Budget** | **~180 min** — first deep-work day. Still free. |
| **Code file** | `Day_04.py` |

> **Why today looks like this.** Functions are the unit you will spend the next 87 days inside. Every cleaning step, every feature, every metric is a function. Getting them right now — clear inputs, one job, an honest return value — is worth more than any library you will learn later. This is also the day that makes Day 15's OOP block possible: **you cannot understand why objects exist until functions start feeling insufficient.**

---

## 🎯 Objective

Write functions with explicit contracts: you know what goes in, what comes out, and what happens when the input is wrong — without reading the body.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Python](https://www.youtube.com/watch?v=_aWbUudZ5Yo) · **`4:06:22 → 4:33:38`** | PRIMARY · @1.5× | 18 min | Functions, parameters, returns |
| [CodeWithHarry `4:50:53 → 5:17:16`](https://www.youtube.com/watch?v=UrsmFxEIp5k) | REINFORCEMENT · @1.5× | 18 min | Functions and recursion — a second angle, worth it here |
| Docstrings, type hints, the mutable-default trap — below | REFERENCE | 15 min | Professional habits, learned once |

### 🟢 IF TIME

- [Apna College `06:04:25 → 07:05:27`](https://www.youtube.com/watch?v=ERCMXc8x7mc) — functions and recursion with a practice-question focus.
- Read the `math` and `statistics` standard-library docs for 10 minutes. Knowing what already exists stops you writing it.

---

## 🧠 Core Concepts

### Arguments — the full picture

```python
def analyse(data, *, method="mean", drop_na=True, **options):
    ...
```

| Form | Meaning | When to use |
|:-----|:--------|:------------|
| `data` | positional | The thing the function is about |
| `*args` | any number of positional | Rare in data code — usually a sign a list belongs there |
| `*` alone | everything after must be keyword | **Use this.** It stops `analyse(df, "median", False)` from being written |
| `method="mean"` | keyword with default | Options with a sensible default |
| `**options` | arbitrary keywords | Pass-through to another function |

**The keyword-only marker `*` is the single most useful habit on this page.** A call like `clean(df, True, False, True)` is unreadable six weeks later. `clean(df, drop_na=True, lowercase=False, strip=True)` is not.

### The mutable default trap

```python
def add_row(row, rows=[]):      # BUG -- the list is created ONCE
    rows.append(row)
    return rows

add_row("a")     # ['a']
add_row("b")     # ['a', 'b']   <- the previous call leaked in
```

The default is evaluated once, at definition time. The fix:

```python
def add_row(row, rows=None):
    if rows is None:
        rows = []
    rows.append(row)
    return rows
```

This appears in real interviews and in real bugs.

### Scope, and why globals hurt in data work

Python looks up names Local → Enclosing → Global → Built-in. Reading a global works; assigning to one needs `global`, which is almost always the wrong answer. A function that reads a global dataframe is a function you cannot test, cannot reuse, and cannot reason about. **Pass it in.**

### Return contracts

Decide what a function returns when things go wrong — and be consistent:

| Strategy | Good for |
|:---------|:---------|
| Return `None` | "Not found" is a normal outcome |
| Return a tuple `(result, errors)` | Batch processing — you want both |
| Raise an exception | The caller *cannot* sensibly continue |

The worst option is returning `-1` sometimes, `None` other times, and an empty string on Sundays. Pick one per function and document it.

### Docstrings and type hints

```python
def total_revenue(rows: list[dict], *, min_qty: int = 1) -> float:
    """Sum qty * price over rows, skipping rows below min_qty.

    Args:
        rows: transaction dicts with 'qty' and 'price' keys.
        min_qty: rows with qty below this are ignored.

    Returns:
        Total revenue. 0.0 if no row qualifies.
    """
```

Type hints do not enforce anything at runtime. They are documentation your editor can read — and in three weeks, `rows: list[dict]` will save you from opening the function to remember what it wants.

### Pure vs impure

A **pure** function's output depends only on its inputs, and it changes nothing outside itself. Pure functions are testable, reusable and composable. Keep the impure parts — reading files, printing, writing to disk — at the edges of your program, not in the middle.

---

## 💻 Code

### 🔴 MUST DO

`Day_04.py` — build a small reusable module, not scattered exercises. By the end you have **nine functions you will actually import later this week**:

1. `clean_text(raw)` — strip, lowercase, collapse internal whitespace
2. `to_number(value, default=None)` — safe numeric conversion
3. `parse_row(line, *, sep=",")` — one CSV line → typed dict
4. `total_revenue(rows, *, min_qty=1)` — with a real docstring and type hints
5. `top_n(rows, key, n=3)` — generic, works on any key
6. `summarise(numbers)` — returns `(count, total, mean, min, max)` in one pass
7. `validate_rows(rows)` — Day 3's exercise 10, now with a documented contract
8. `demonstrate_mutable_default()` — reproduce the bug, then fix it
9. `safe_divide(a, b)` — pick and document a return strategy for `b == 0`

### 🟢 IF TIME

- Add `*` to every function above so all options are keyword-only. Notice how the call sites read afterwards.
- Write `factorial` both recursively and iteratively. Then answer: which would you ship, and why?

---

## 🔬 Understanding Check

1. **Debugging.** Explain precisely why the mutable-default bug happens. At what moment is the list created?
2. **Comparison.** Return `None`, return `(result, errors)`, or raise? Give a data-work example where each is the right answer.
3. **Reasoning.** Why are type hints useful if Python ignores them at runtime?
4. **Application.** You are writing a function that removes outliers. What are its inputs, its return value, and its behaviour on an empty list? Decide before writing a line.
5. **Understanding.** What makes a function pure, and why does purity matter more in data pipelines than in a web app?
6. **Interview.** "What does `*` do in a function signature?" Answer in under 30 seconds.
7. **Teaching.** Explain scope to someone who thinks a variable is a variable.

---

## 🎯 Expected Outcome

- [ ] Write a function with a docstring, type hints and keyword-only options without looking it up
- [ ] Spot and fix the mutable-default bug on sight
- [ ] Choose a return strategy deliberately rather than by accident
- [ ] Have nine working helpers saved for reuse this week

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians functions @1.5× | 18 min |
| CodeWithHarry functions @1.5× | 18 min |
| Concepts + traps | 15 min |
| Build the nine helpers | 100 min |
| Daily review | 15 min |
| **Total** | **~166 min** |

---

## 🧪 Mini Assessment

Closed book, 20 minutes. Write `group_totals(rows, *, by, value)` that groups a list of dicts by any key and sums any numeric key, returning `{group: total}`. It must:

- work on any keys, not hardcoded ones
- skip rows missing either key, and report how many it skipped
- have a docstring stating what it returns when `rows` is empty

*(You are writing `pandas.groupby().sum()` by hand. On Day 34 you get the one-liner — and you will understand what it is doing.)*

---

## 🔁 Daily Review

1. Which of my nine functions would I not be able to rewrite from memory tomorrow?
2. Did I choose return strategies deliberately, or default to returning `None` everywhere?
3. Where did I have to look something up? That is the thing to drill.
4. Did today take more than 180 minutes? If yes, which block overran, and what gets cut next weekend?

---

## 📦 Completion Criteria

- [ ] All nine helpers work and are saved in `Day_04.py`
- [ ] At least three have full docstrings and type hints
- [ ] The mutable-default bug reproduced *and* fixed
- [ ] `group_totals` written closed-book
- [ ] Understanding Check answered in writing
- [ ] Committed to git

---

**[← Day 3](../Day_03/Day_03.md)** · **[Day 5 →](../Day_05/Day_05.md)** · [README](../../../README.md)
