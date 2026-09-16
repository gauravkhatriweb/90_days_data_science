# Day 9 — Errors Are Information

|  |  |
|:--|:--|
| **Date** | Thursday, 24 September 2026 |
| **Position** | Week 2 · Month 1 · Phase 1 — Python |
| **Budget** | **~45 min** — 🎓 Orientation day 4 |
| **Code file** | `Day_09.py` |

> **Why today looks like this.** Real data breaks code constantly — a missing field, a number stored as `"N/A"`, a file that moved. The difference between a beginner and someone employable is not that their code never fails; it is that **when it fails, it says why**. A pipeline that crashes with `KeyError: 'qty'` on row 38,412 and stops is nearly useless. One that processes 39,988 rows and hands you a list of twelve rejections with reasons is a day's work saved.

---

## 🎯 Objective

Handle failure deliberately: catch what you can recover from, let the rest crash loudly, and never hide a bug behind a bare `except`.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Sheryians Python](https://www.youtube.com/watch?v=_aWbUudZ5Yo) · **`6:23:24 → 6:43:23`** | PRIMARY · @1.75× | 12 min | Exception handling |
| The rules below | REFERENCE | 8 min | The part that matters |

### 🟢 IF TIME

- Nothing. Orientation.

---

## 🧠 Core Concepts

### The full shape

```python
try:
    value = float(raw)
except ValueError:
    value = None                # a failure you EXPECTED and can recover from
except (TypeError, KeyError) as e:
    log(f"unexpected: {e}")     # catch several, keep the object
    raise                       # re-raise -- you logged it, you did not fix it
else:
    clean.append(value)         # runs only if NOTHING was raised
finally:
    handle.close()              # runs either way -- cleanup
```

`else` and `finally` are the parts people skip. `else` keeps the `try` block down to *only the line that can fail*, which makes the `except` honest.

### The exceptions you will actually meet

| Exception | Cause in data work |
|:----------|:-------------------|
| `ValueError` | `float("N/A")`, `int("12.7")` |
| `KeyError` | A dict is missing a column |
| `IndexError` | A row is shorter than expected |
| `TypeError` | `None + 5`, `"5" * "2"` |
| `FileNotFoundError` | The path is wrong. It is nearly always the path. |
| `ZeroDivisionError` | A denominator that is empty in real data |

### Three rules

**1. Never write a bare `except:`.**

```python
try:
    process(row)
except:              # catches EVERYTHING, including your typos and Ctrl-C
    pass             # and then silently discards them
```
This is the single most destructive pattern in beginner data code. It turns a five-minute bug into a three-hour one. Catch the specific exception you expect.

**2. Keep the `try` block as small as possible.** Wrapping forty lines in one `try` means you cannot tell which line failed.

**3. Fail loudly at the edges, quietly in the middle.** A per-row failure should be recorded and skipped. A missing input file should stop the program immediately.

### Raising your own

```python
if not rows:
    raise ValueError("no rows to analyse -- check the input path")
```

A good message names **what was wrong** and **what to check**. `raise ValueError("bad input")` helps nobody.

### Custom exceptions — one line, real value

```python
class DataQualityError(Exception):
    """Raised when input data fails validation."""
```

Now a caller can catch *your* failures separately from Python's. You will use this in Project 1.

---

## 💻 Code

`Day_09.py` — eight exercises:

1. `safe_float(value)` — return `None` rather than raising, and say why in a comment
2. Handle `FileNotFoundError` with a message naming the path it tried
3. Catch two exception types in one `except`, keeping the exception object
4. Use `else` to keep the `try` block to one line
5. Use `finally` to guarantee cleanup, and prove it runs even when an exception escapes
6. Define `DataQualityError` and raise it with a message a human can act on
7. **The anti-pattern:** write the bare-`except` version, watch it swallow a typo, then fix it
8. **The real one:** a batch processor over 6 deliberately broken rows that returns `(processed, failures)` where each failure is `(index, exception_type, message)`

---

## 🔬 Understanding Check

1. **Reasoning.** What is wrong with `except: pass`? Describe a concrete bug it would hide for hours.
2. **Comparison.** When should a function return `None` on failure, and when should it raise?
3. **Understanding.** What does `else` add to a `try` block that putting the code inside `try` does not?
4. **Application.** Loading 50,000 rows, 12 are malformed. Describe your error strategy — what stops, what continues, what gets recorded?
5. **Debugging.** `ValueError: could not convert string to float: ''` — what is the data problem, and what are two possible fixes?
6. **Interview.** "What is the difference between an error and an exception in Python?"

---

## 🎯 Expected Outcome

- [ ] Write specific `except` clauses by default
- [ ] Use `else` and `finally` correctly
- [ ] Raise exceptions with messages that name the fix
- [ ] Build a batch processor that survives bad rows and reports them

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Sheryians exceptions @1.75× | 12 min |
| Three rules | 8 min |
| Eight exercises | 20 min |
| Daily review | 5 min |
| **Total** | **~45 min** |

---

## 🧪 Mini Assessment

Three minutes. Write `parse_price(raw)` that turns `"1,250.00"`, `"540"`, `"N/A"`, `""` and `None` into a float or `None` — with exactly one `try` and one specific `except`.

---

## 🔁 Daily Review

1. In exercise 7, what did the bare `except` swallow? How long would that have cost me in a real project?
2. Do I have a default error strategy now, or am I still deciding case by case?
3. **Tomorrow is SAT results day.** Day 10 is deliberately a 30-minute reading day. Respect that — do not add to it.

---

## 📦 Completion Criteria

- [ ] Eight exercises run
- [ ] Exercise 7 demonstrates the anti-pattern *and* the fix
- [ ] Exercise 8 returns both processed rows and structured failures
- [ ] `parse_price` written closed-book
- [ ] Committed to git

---

**[← Day 8](../Day_08/Day_08.md)** · **[Day 10 →](../Day_10/Day_10.md)** · [README](../../../README.md)
