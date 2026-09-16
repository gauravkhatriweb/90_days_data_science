# Week 3 Review — The OOP Block

|  |  |
|:--|:--|
| **Covers** | Days 15–21 · 30 September – 6 October 2026 |
| **Topics** | Why objects · instances · class variables · inheritance · composition · encapsulation · dunder methods · polymorphism · abstraction |
| **Budget** | 45–60 min |
| **Also this week** | 📐 Essential Math Ch. 1, pp. 1–31 |

> This is the most important review in Month 1. OOP was your stated weakness, it got the most days of any topic, and **Month 2 and CSE 205 both depend on it.** Grade it honestly — a generous score here costs you in November.

---

## ⏸️ Catch-Up Rights

| Day | Done? | If not — MUST DO only |
|:---:|:-----:|:----------------------|
| 15 · Why objects | ☐ | **The diagnosis + the sentence.** Non-negotiable — everything else assumes it. |
| 16 · Instances, state | ☐ | `ShopLedger` + the cache bug |
| 17 · Class variables | ☐ | The mutable-class-variable bug + one `classmethod` |
| 18 · Inheritance vs composition | ☐ | Exercise 10 — the comparison |
| 19 · Properties, dunders | ☐ | `@property`, `__repr__`, `__len__`, `__getitem__` |
| 20 · Abstraction | ☐ | The contract (ex 1) + the ABC |
| 21 · Explanation test | ☐ | Part A, all ten |

---

## 📝 Part 1 — Knowledge (closed book, 15 min)

If you completed Day 21 Part A, **use that score here** rather than repeating it. Otherwise answer these:

1. State the problem objects solve, using your own `shopsummary` as the example.
2. Why does `self.records.append(x)` on a class variable affect every instance?
3. What does `cls` give you inside a `classmethod` that hardcoding the class name does not?
4. State the "is a / has a" test and give one example of each.
5. What does substitutability require of a subclass?
6. What can `@property` let you change later without breaking callers?
7. Why is `__repr__` worth writing in every class?
8. When is an ABC worth the overhead over duck typing?

**Score: ___ / 8** *(or Day 21 Part A: ___ / 10)*

---

## 💻 Part 2 — Coding (closed book, 20 min)

If you completed Day 21 Part C, that is Task A. Otherwise:

**Task A — 10 min.** `Inventory` with `__init__`, a mutator, a cached `@property`, a `classmethod` constructor, and four dunder methods.

**Task B — 5 min.** Given `EmailSender`, `SmsSender` and `WhatsAppSender` with different internals, write one function that sends through all three. No inheritance.

**Task C — 5 min.** A `Report` class must support CSV, JSON and XML output, and read from a file or a database. Sketch the design. State how many classes and why.

**Score: ___ / 3**

---

## 🧩 Part 3 — Problem Solving (open book, 10 min)

> SwiftBase needs a receipt system. Receipts can be printed, sent by SMS, or sent on WhatsApp. Each has a different format and a different failure mode — the printer jams, SMS costs money and can fail silently, WhatsApp needs internet.
>
> Design it. Write class names, what each holds, what each promises, and which relationships are "is a" and which are "has a". Then answer: **where does retry logic live, and why there?**

This is the design question, and it is the one that separates people who can write classes from people who can design systems.

---

## 🔁 Part 4 — Retention Check

- [ ] I can write a class with `__init__`, a property and two dunder methods from memory
- [ ] I can explain `self` without saying "it just means the object"
- [ ] I recognise the mutable-class-variable bug on sight
- [ ] I use `super()` correctly in both `__init__` and an override
- [ ] I apply the "is a" test before reaching for inheritance
- [ ] I write `__repr__` in every class by habit now
- [ ] I can explain duck typing with my own example
- [ ] I write the contract before the class

> Weak this week: ______________________________________________

---

## 📐 Part 5 — Mathematics Track

- Chapter 1, pages 1–31 read? ☐
- **Summations:** can you write Σ(i=1 to n) of xᵢ as a Python loop without hesitating?
- **Logarithms:** what is `log(x)` asking? *(Day 75 needs this.)*
- **Derivatives:** what is a derivative, in one sentence, in your own words?
- **MAT 265 overlap:** which pages has your calculus course already covered? Which are ahead of it?
- Is the 40-minutes-on-weekends pace working, or does it need to move?

---

## 🎓 Part 6 — University Link

- **CSE 205 (next semester, Java):** you have now covered classes, inheritance, polymorphism, encapsulation and abstraction. What fraction of that course do you think you have pre-learned? What will be genuinely new? *(Answer: data structures and Big O — which is why Day 5's cost table exists.)*
- **CSE 110:** is your course ahead of or behind this plan?
- **Time reality:** two full weeks of semester are done. Is the daily budget holding?

---

## 🛠️ Part 7 — What Could I Build Now?

Days 22–26 turn all of this into a project on your own LifeOS data. Before reading that brief — what would *you* build with objects now?

> ______________________________________________

---

## 💼 Part 8 — Career

"Object-oriented programming" on a CV means nothing. What can you now demonstrate? Aim for something like *"refactored a CLI tool into a composed design with swappable data sources and output formatters."*

> ______________________________________________

---

## 🔮 Part 9 — The Decision

**This is the most consequential decision point in Month 1.**

| If… | Then… |
|:----|:------|
| Day 21 Part A ≥ 8 and Part C was clean | ✅ **Continue.** Days 22–26 as a project. |
| Part A 5–7 | 🔧 **Reinforce while building.** Rewatch Corey Schafer 4 and 6 in Day 22's IF TIME. The project will close the gap. |
| Part A ≤ 4 | 🛑 **Stop and repeat.** Redo Days 15 and 18 on Days 22–23. Shift the project to 24–27, and compress Day 27 into Day 26. **This is the correct decision, not a failure.** |
| Everything clean, OOP now feels easy | ⏩ Make the Day 22–26 project harder: add a second data source and a proper test suite from the start. |

**My decision:**

> ______________________________________________

---

## 📊 Week 3 Scorecard

| Measure | Result |
|:--------|:-------|
| Days completed | ___ / 7 |
| Day 21 Part A — explanation | ___ / 10 |
| Part 2 — coding | ___ / 3 |
| Retention boxes | ___ / 8 |
| Essential Math pp. 1–31 | ☐ |
| Honest hours this week | ___ h |
| **OOP comfort, 1–5 (was 1 on Day 15)** | ___ |
| **Biggest weakness** | |
| **Biggest win** | |

---

**[← Day 21](./Day_21/Day_21.md)** · **[Day 22 →](../Week_04/Day_22/Day_22.md)** · [README](../../README.md)
