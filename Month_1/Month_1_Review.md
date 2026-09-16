# Month 1 Review — Python

|  |  |
|:--|:--|
| **Covers** | Days 1–28 · 16 September – 13 October 2026 |
| **Phase** | Python foundations, OOP, project P0 |
| **Budget** | ~90 min |
| **This month's reality** | 5 free days · orientation week · SAT results · semester started · add/drop |

> This is a **capability audit**, not a reflection. Every finding needs evidence you can point at. The month ends with a decision about Month 2, and that decision should follow from what is written here.

---

## 📍 Part 1 — The Baseline Comparison (20 min)

**Retake the Day 1 diagnostic.** Same twelve tasks, closed book, 50 minutes maximum. `Month_1/Week_01/Day_01/Day_01.py`.

| | Day 1 | Day 28 | Change |
|:--|:-----:|:------:|:------:|
| Diagnostic score / 12 | ___ | ___ | ___ |
| Tasks 1–4 (basic Python) | ___ | ___ | |
| Tasks 5–8 (idiom) | ___ | ___ | |
| Tasks 9–12 (OOP) | ___ | ___ | |

**The OOP block was the largest investment of the month. Did tasks 9–12 move?** If they did not, that is the single most important finding on this page, and Month 2 must respond to it.

---

## 🧠 Part 2 — Knowledge Audit

For each, mark honestly: ✅ can explain and use · 🟡 can use, cannot explain · ❌ neither.

| Topic | Day | Status | Evidence |
|:------|:---:|:------:|:---------|
| Python idiom vs JavaScript habits | 2 | | |
| Loops without indices | 3 | | |
| Functions: keyword-only, docstrings, contracts | 4 | | |
| Choosing list / set / dict / tuple | 5 | | |
| Big-O of membership testing | 5 | | |
| Comprehensions, and when not to | 6 | | |
| Text cleaning sequence | 7 | | |
| Multi-level sorting | 8 | | |
| Exception strategy | 9 | | |
| File handling, CSV parsing by hand | 11 | | |
| Modules, packages, venv | 12 | | |
| Debugging method | 13 | | |
| **Why objects exist** | 15 | | |
| `self`, instances, state | 16 | | |
| Class vs instance variables | 17 | | |
| `classmethod` / `staticmethod` | 17 | | |
| **Inheritance vs composition** | 18 | | |
| Substitutability | 18 | | |
| `@property`, encapsulation | 19 | | |
| Dunder methods | 19 | | |
| Polymorphism, duck typing | 19 | | |
| ABCs, designing a contract | 20 | | |
| Testing with pytest | 25 | | |
| Generators, lazy evaluation | 26 | | |
| `pathlib`, `datetime`, `collections`, `json` | 27 | | |

**🟡 count: ___** — these are the dangerous ones. Something you can use but cannot explain will fail you in an interview and in any situation slightly different from the one you learned it in.

---

## 💻 Part 3 — Practical Audit

**What can you build?** Answer with things you have actually built.

| | Evidence |
|:--|:--|
| A CLI tool from scratch, no libraries | `shopsummary` — works? ☐ |
| An OOP system over real data | `lifelog` — works on 116 logs? ☐ |
| Swappable implementations behind an interface | How many sources? ___ |
| A test suite | How many tests? ___ · all green? ☐ |
| A repository a stranger could run | README present and accurate? ☐ |

**The real question:** if you were handed a new messy dataset tomorrow and told "summarise this in Python, no Pandas" — could you? **Yes / No / Slowly.** Be honest; the answer determines the Month 2 pace.

---

## 📐 Part 4 — Mathematics Audit

Essential Math **Chapter 1** — complete? ☐

| Concept | Can explain it? | Where it returns |
|:--------|:---------------:|:-----------------|
| Summation notation Σ | | Every statistics formula, Day 48+ |
| Logarithms | | Log-odds, Day 75 |
| Euler's number *e* | | The logistic function, Day 75 |
| Limits | | The definition of a derivative |
| **Derivatives** | | **Gradient descent, Day 72** |
| Partial derivatives | | Multi-feature models, Day 72 |
| **Chain rule** | | Backpropagation, and Day 72 |
| Integrals | | Probability density, Day 50 |

**MAT 265 overlap:** what fraction of your calculus course so far has Chapter 1 pre-taught? ___%

> If that fraction is high, the maths track is earning its time twice over and should be protected during exam weeks rather than dropped. If it is low, the timing needs adjusting — say so below.

---

## 🎓 Part 5 — University Audit

| | Answer |
|:--|:--|
| **CSE 110** — ahead of, level with, or behind this plan? | |
| **MAT 265** — has it reached derivatives? | |
| **CSE 205 next semester** — how much have you pre-learned? | |
| Contact hours per week | |
| Realistic daily study slot, and when | |
| **Did the 60–90 min weekday budget hold?** | |
| Mid-semester exam dates, if known | |

> If the weekday budget did **not** hold, do not resolve to try harder. Reduce Month 2's scope now — the reduction protocol is in Part 8.

---

## 🛠️ Part 6 — Portfolio Audit

| Project | Status | Portfolio-worthy? |
|:--------|:-------|:------------------|
| `shopsummary` (Day 12) | | No — a learning exercise, and that is fine |
| `lifelog` / P0 (Days 22–26) | | Probably not — but it proves you can design |
| **Real portfolio projects** | **0** | **Correct. P1 starts Day 32.** |

**This is on plan.** Month 1 was never meant to produce portfolio pieces; it was meant to produce the ability to build them. The first real one ships on Day 45.

---

## 💼 Part 7 — Career Audit

What is honestly true now that was not on 16 September? Be specific enough that you could say it in an interview and answer a follow-up.

> 1. ______________________________________________
> 2. ______________________________________________
> 3. ______________________________________________

**The interview test:** if someone asked "tell me about a Python project you've built," could you talk for two minutes about `lifelog` — the design decisions, the trade-offs, the bugs you found? **Yes / No.**

---

## 🔮 Part 8 — Month 2 Decisions

Month 2 is Days 29–56: NumPy, Pandas, cleaning, EDA, visualisation, **Project 1**, probability, statistics, and the SQL track starting Day 33.

### A. The pace decision

| If Month 1 was… | Then Month 2… |
|:----------------|:--------------|
| **Comfortable, diagnostic improved 3+, Day 26 ≥ 8** | Runs as written. Consider compressing NumPy from 3 days to 2 and giving the day to statistics. |
| **Manageable, some days missed, Day 26 = 6–7.5** | Runs as written. Use IF TIME blocks on the 🟡 topics from Part 2. |
| **Hard, several days missed, Day 26 < 6** | **Reduce.** Cut every IF TIME block. Hold the MUST DO line only. Accept that Project 1 may ship on Day 47 instead of 45. |
| **Not sustainable at all** | Drop the weekday budget to 45 minutes and extend Project 1 by a week. **A slower plan you finish beats a faster one you abandon.** |

**My pace decision:** ______________________________________________

### B. Specific fixes

The three weakest items from Part 2, and where each gets remediated:

| Weakness | Fix | Which day's IF TIME |
|:---------|:----|:--------------------|
| | | |
| | | |
| | | |

### C. Structural changes

- [ ] Study slot time confirmed / changed to: ___________
- [ ] Maths track staying on weekends / moving to: ___________
- [ ] SQL track starting Day 33 as planned / moved to: ___________
- [ ] Anything from Month 1 being repeated: ___________

### D. The one thing

If only one thing improves in Month 2, what should it be?

> ______________________________________________

---

## 📊 Month 1 Scorecard

| Measure | Result |
|:--------|:-------|
| Days completed | ___ / 28 |
| Day 1 diagnostic → Day 28 | ___ → ___ / 12 |
| Day 21 OOP explanation | ___ / 10 |
| Day 26 assessment | ___ / 9 |
| Topics marked ✅ | ___ / 25 |
| Topics marked 🟡 (the risk) | ___ |
| Essential Math Ch. 1 | ☐ complete |
| Projects shipped | `shopsummary` ☐ · `lifelog` ☐ |
| Tests written | ___ |
| Total honest hours | ___ h |
| **OOP comfort, 1–5** (Day 15: ___ → now: ___) | |
| **Biggest win** | |
| **Biggest gap** | |
| **Would I have predicted this on Day 1?** | |

---

<div align="center">

**Month 1 is the only month where the subject is the language itself.**
From Day 29, Python is the tool and data is the subject.

**[← Day 28](./Week_04/Day_28/Day_28.md)** · **[Day 29 — NumPy →](../Month_2/Week_05/Day_29/Day_29.md)** · **[README](../README.md)**

</div>
