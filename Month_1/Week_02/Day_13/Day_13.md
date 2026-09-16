# Day 13 — Debugging: Reading What Python Tells You

|  |  |
|:--|:--|
| **Date** | Monday, 28 September 2026 |
| **Position** | Week 2 · Month 1 · Phase 1 — Python |
| **Budget** | **~45 min** — 🎓 **FALL SEMESTER BEGINS.** First day of classes. |
| **Code file** | `Day_13.py` |

> **Why today is 45 minutes.** Your own rule for the first weeks at NIT was *observe before optimising* — do not overload the schedule until you know what the schedule is. Today you find out when your classes are, how long the commute takes, and where you can actually study. That is the day's real work.
>
> Forty-five minutes of debugging practice fits around all of it, and debugging is the right topic: it is the skill that determines whether a 45-minute study slot produces progress or frustration.

---

## 🎯 Objective

Read a traceback correctly, use a real debugger instead of scattering print statements, and develop a method for finding a bug rather than guessing at it.

---

## 📚 Learn

### 🔴 MUST DO — no video, just method

**Read tracebacks from the bottom up.**

```
Traceback (most recent call last):
  File "Day_12.py", line 61, in main
    print(render(path, records, problems, top=top))
  File "shoptools/analysis.py", line 24, in render
    mean = total / count
ZeroDivisionError: division by zero
```

| Read this | To learn |
|:----------|:---------|
| **Last line** | *What* went wrong: `ZeroDivisionError` |
| **Second-to-last frame** | *Where*: `analysis.py`, line 24 |
| **Frames above it** | *How you got there* — the call chain |

Beginners read the top and panic. The bottom is the answer; the middle is the path.

And the real question this traceback asks is not "how do I stop the crash" — it is **"why is `count` zero?"** Wrapping it in a `try` hides the actual bug, which is that no rows parsed.

**Use `breakpoint()`.**

```python
def render(records):
    breakpoint()        # execution stops here, you get a prompt
    ...
```

| Command | Does |
|:--------|:-----|
| `n` | next line |
| `s` | step into the function |
| `c` | continue to the end or next breakpoint |
| `p name` | print a variable |
| `pp data` | pretty-print a structure |
| `l` | show surrounding code |
| `q` | quit |

Thirty seconds in `pdb` beats ten minutes of adding and deleting print statements — and unlike prints, you cannot accidentally commit it.

**When printing is the right answer:** loops over thousands of rows, where you want a pattern rather than one moment. Then print, but print *usefully*: `print(f"{i=} {row=}")`. The `=` suffix in an f-string prints both the name and the value.

### The method — four steps, in order

1. **Reproduce it reliably.** A bug you cannot trigger on demand cannot be fixed, only disturbed.
2. **Narrow it.** Halve the input. Still broken? Halve again. Five halvings take 50,000 rows down to one.
3. **Read the state at the failure point.** Not what you think is there — what *is* there. This is what `breakpoint()` is for.
4. **Fix the cause, not the symptom.** `try/except` around a `ZeroDivisionError` when the real problem is an empty list is not a fix; it is a disguise.

### 🟢 IF TIME

- Nothing. First day of university. Go and observe it.

---

## 💻 Code

`Day_13.py` — five bugs. Each is planted deliberately and each represents a real mistake from Days 1–12.

| # | Symptom | The lesson |
|:-:|:--------|:-----------|
| 1 | `ZeroDivisionError` | The cause is upstream, not where it crashed |
| 2 | Wrong answer, no error | The worst kind — mutation during iteration |
| 3 | `KeyError` on a column you can see | Encoding / whitespace in the key |
| 4 | `TypeError: unsupported operand` | A `None` from a failed conversion, propagating |
| 5 | Works on the sample, wrong on the full data | Off-by-one in a slice |

For each: write down your hypothesis **before** running the debugger, then check whether you were right. Tracking how often your first guess is correct is how debugging gets faster.

---

## 🔬 Understanding Check

1. **Debugging.** Why read a traceback from the bottom?
2. **Reasoning.** `try/except ZeroDivisionError` around bug 1 stops the crash. Why is that the wrong fix?
3. **Comparison.** When is `breakpoint()` better than `print()`, and when is it the other way round?
4. **Application.** A function is wrong on 3 rows out of 50,000. Describe your approach step by step.
5. **Understanding.** Bug 2 produces no error at all. Why are silent wrong answers more dangerous than crashes — especially in data work?
6. **Interview.** "Tell me about a bug that took you a long time to find." You now have five. Pick one and tell it in 60 seconds: symptom, hypothesis, method, cause.

---

## 🎯 Expected Outcome

- [ ] Locate a failure from a traceback in under 30 seconds
- [ ] Use `breakpoint()` and inspect state without leaving the terminal
- [ ] Distinguish the crash site from the cause
- [ ] Narrow a bug by halving the input

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Traceback reading + the method | 12 min |
| Five bugs, with hypotheses first | 28 min |
| Daily review | 5 min |
| **Total** | **~45 min** |

---

## 🧪 Mini Assessment

Take yesterday's `shopsummary`. Deliberately break one thing — delete `__init__.py`, or change a dict key, or flip a slice bound. Hand yourself the traceback tomorrow morning and find it in under two minutes.

---

## 🔁 Daily Review

1. How many of my five hypotheses were right before I opened the debugger?
2. Which bug type would have cost me the most time in a real project?
3. **Semester day 1.** What are my actual class hours, and where does the 60–90 minute study slot go — morning before class, or evening? Write the time down; the next 78 days depend on it.

---

## 📦 Completion Criteria

- [ ] All five bugs found and fixed
- [ ] A hypothesis written for each *before* debugging
- [ ] `breakpoint()` used at least twice
- [ ] Study slot decided and written down
- [ ] Committed to git

---

**[← Day 12](../Day_12/Day_12.md)** · **[Day 14 →](../Day_14/Day_14.md)** · [README](../../../README.md)
