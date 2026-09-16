# Day 24 — Code Quality: Making It Readable by Someone Else

|  |  |
|:--|:--|
| **Date** | Friday, 9 October 2026 |
| **Position** | Week 4 · Month 1 · **P0 build 3 of 3** |
| **Budget** | **~60 min** — 🎓 **Add/drop deadline today.** Handle university first. |
| **Code file** | `Day_24.py` — a refactor pass over `lifelog/` |

> **Why today is short.** The add/drop deadline is today. If you are still deciding on a course change — including the pending `SSC101 → PHI105` swap — **that takes priority over everything on this page.** It is a decision with a semester-long consequence; this is an hour of refactoring.
>
> **Why refactoring is the topic.** `lifelog` works. Working is not the same as finishable. The gap between "runs on my machine" and "another person can read it" is where portfolio projects are won, and it is a much smaller amount of work than people expect — about an hour, done deliberately.

---

## 🎯 Objective

Take working code to readable code, and learn the specific standards a reviewer looks for.

---

## 📚 Learn

### 🔴 MUST DO — the checklist

**Naming**

| Bad | Good | Why |
|:----|:-----|:----|
| `d`, `lst`, `tmp` | `log_date`, `logs`, `parsed` | Single letters only for loop counters and coordinates |
| `process()` | `extract_sections()` | Say what it does, not that it does something |
| `data` | `daily_logs` | "Data" is every variable in this project |
| `getTotal()` | `total()` | Python is `snake_case`, and `get` is usually noise |
| `flag`, `check` | `is_empty`, `has_sections` | Booleans read as questions: `is_`, `has_`, `can_` |

**Functions**
- One job. If the docstring needs "and", split it.
- Under 20 lines as a default, not a law.
- Under four parameters — more means an object is hiding in there.
- Return one type, or document every alternative.

**Modules** — each file should have one sentence describing it. If you cannot write that sentence, the file is doing two things.

**Comments** — explain *why*, never *what*.

```python
# bad -- restates the code
i += 1   # increment i

# good -- explains a decision the code cannot
# PBS restated the SPI base year in 2022, so pre-2022 values are
# rescaled before comparison. See the note in README.
```

**The single-underscore audit.** Every attribute and method: is it part of the interface, or internal? Mark internals with `_`. This is the clearest signal to a reader of what they are allowed to depend on.

**Dead code.** Delete it. It is in git history; leaving it commented out makes every reader wonder if it matters.

### 🟢 IF TIME

- Run `pip install ruff && ruff check lifelog/`. Read every warning before fixing any — the categories tell you what habits to change, which is worth more than the fixes.

---

## 💻 Code

### 🔴 MUST DO — the refactor pass

Go through `lifelog/` against the checklist:

1. **Names.** Every variable, function and class. Rename anything that needs a comment to explain it.
2. **Long functions.** Find the longest; split it if it does two things.
3. **Parameters.** Any function with four or more — is there an object hiding there?
4. **Docstrings.** Every public class and method. One line minimum, stating the return and the empty case.
5. **Comments.** Delete every one that restates the code. Add ones that explain a decision.
6. **Underscores.** Mark every internal.
7. **Module docstrings.** One sentence per file. If you cannot write it, split the file.
8. **Dead code.** Delete it.
9. **A `README.md` for `lifelog/`** — what it does, how to run it, what the output means. **Ten lines is enough.** This is the habit the portfolio projects need.
10. **The stranger test.** Reread `analysis.py` as if someone else wrote it. Note every point where you had to pause. Those pauses are the remaining work.

### 🟢 IF TIME

- Add type hints to every public method. You have used them since Day 4; this makes them consistent.

---

## 🔬 Understanding Check

1. **Reasoning.** Why is a comment explaining *what* code does usually a sign of a problem?
2. **Application.** Which function was hardest to name? What does that difficulty tell you about what it does?
3. **Comparison.** `_parse_sections` vs `parse_sections` — what does the underscore promise a reader?
4. **Reasoning.** A function with six parameters. What is the refactor, and why is it better than a longer signature?
5. **Self-assessment.** In the stranger test, how many times did you pause? What were the top three causes?
6. **Career.** A reviewer opens a GitHub repository and spends 90 seconds. What do they look at? Does `lifelog/` survive it?

---

## 🎯 Expected Outcome

- [ ] Every name says what it is
- [ ] Every public method documented
- [ ] Internals marked with `_`
- [ ] A README a stranger could follow
- [ ] No dead code

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Read the checklist | 10 min |
| Refactor pass (1–8) | 30 min |
| README + stranger test | 15 min |
| Daily review | 5 min |
| **Total** | **~60 min** |

---

## 🧪 Mini Assessment

The stranger test. Read `analysis.py` top to bottom without running it. **Count the pauses.** Under three is good. More than five means the naming is still doing work the reader has to do.

---

## 🔁 Daily Review

1. How many pauses in the stranger test? Top three causes?
2. Which rename improved readability the most?
3. Did I find a function doing two jobs? Which?
4. **Add/drop:** is the course change settled? If not, that is tomorrow's first task — before any study.

---

## 📦 Completion Criteria

- [ ] All ten refactor steps done
- [ ] Every public method has a docstring
- [ ] `lifelog/README.md` exists
- [ ] Stranger test done, pauses counted
- [ ] Committed to git
- [ ] **Add/drop decision made** — this matters more than the code

---

**[← Day 23](../Day_23/Day_23.md)** · **[Day 25 →](../Day_25/Day_25.md)** · [README](../../../README.md)
