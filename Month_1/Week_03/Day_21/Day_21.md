# Day 21 — Can You Teach It?

|  |  |
|:--|:--|
| **Date** | Tuesday, 6 October 2026 |
| **Position** | Week 3 · Month 1 · **OOP block, day 7 of 9** |
| **Budget** | **~60 min** |
| **Code file** | `Day_21.py` |
| **Also today** | ✍️ **[Week 3 Review](../Week_03_Review.md)** |

> **Why the test is "explain it" rather than "write it."** You can already copy class syntax — you could probably do that before Day 15. The question this block has to answer is whether you *understand* it, and the reliable test for understanding is explanation without notes. If you can write a class but cannot say why composition usually beats inheritance, the block has not worked yet and Days 22–26 need to be adjusted.
>
> This is also interview preparation. Every one of these questions is asked in real technical interviews, and CSE 205 will examine you on the same ground next semester.

---

## 🎯 Objective

Prove — out loud and in writing, without notes — that the six days of OOP produced understanding rather than familiarity.

---

## 📚 Learn

**Nothing new.** Retrieval only.

---

## 💻 Code

### 🔴 MUST DO — Part A: the explanation test (25 min)

Answer each in **writing, closed book, 2–3 minutes each**. Full sentences. If you catch yourself writing "it's basically like a blueprint", stop and try again with something concrete from your own code.

1. **The problem.** What was wrong with `shopsummary` on Day 15 that objects fixed? Answer from your code, not in general terms.
2. **`self`.** What is it? Why does `data.count()` work when `count` is defined as `count(self)`?
3. **Class vs instance variable.** State the difference and describe the bug that comes from getting it wrong.
4. **`classmethod` vs `staticmethod`.** When each, and what does `cls` give you that the class name does not?
5. **Inheritance vs composition.** State the test you use to choose. Give one example of each from a real system.
6. **Substitutability.** What did you break on Day 18, and what rule did it violate?
7. **`@property`.** What can you change later without breaking callers?
8. **`__repr__`.** Why is it the highest-value dunder method?
9. **Duck typing.** What does Python check when you call `source.load()`?
10. **ABC vs duck typing.** When is declaring an interface worth the overhead?

**Score 1 point each. 8+ means the block worked.**

### 🔴 MUST DO — Part B: the teaching test (15 min)

Two explanations, out loud, timed, no notes. Record yourself if that helps — hearing yourself hesitate is diagnostic.

**B1 — 90 seconds.** Explain to a JavaScript developer who has never written a class why objects exist and when to use them. No jargon: no "encapsulation", no "abstraction", no "pillars".

**B2 — 60 seconds.** Explain to an interviewer when you would choose composition over inheritance. Use a concrete example.

If you cannot do B1 without the four vocabulary words, you have learned the vocabulary rather than the idea. That is worth knowing today.

### 🔴 MUST DO — Part C: build from memory (20 min)

`Day_21.py`, closed book. One class that uses everything:

```
class Inventory
    __init__(shop_name, items=None)     every attribute declared
    add(item, qty, price)               mutator, invalidates cache
    remove(item)                        mutator
    total_value                         @property, cached
    low_stock(threshold)                query
    from_csv(path)                      @classmethod
    __repr__  __len__  __getitem__  __contains__  __eq__
    _cache                              underscore-internal
```

Then a `TrackedInventory(Inventory)` subclass that records every change — and in a comment, argue whether that should have been inheritance or composition.

---

## 🔬 Understanding Check

The transfer questions — the ones that show whether this generalises.

1. **Application.** Pick one file from your LifeOS Apps Script or SwiftBase work. Which parts would genuinely improve as objects? Which would not? Be specific about files.
2. **Reasoning.** You are about to meet Pandas. A `DataFrame` is an object with dunder methods. Predict three of them and say what syntax each enables.
3. **Degree link.** CSE 205 covers this in Java, where every method lives inside a class and access modifiers are enforced. Name two things that will feel different, and one that will feel identical.
4. **Self-assessment.** Is OOP still your least favourite topic? If yes, what specifically still bothers you — the concept, the syntax, or knowing when to use it? The answer changes what Days 22–26 emphasise.

---

## 🎯 Expected Outcome

- [ ] Explain all ten concepts without notes
- [ ] Teach OOP to a non-OOP programmer in 90 seconds without jargon
- [ ] Build a complete class from memory
- [ ] Know precisely what is still weak

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Part A — ten written explanations | 25 min |
| Part B — two spoken explanations | 15 min |
| Part C — build from memory | 20 min |
| **Total** | **~60 min** · then the Week 3 Review |

---

## 🧪 Mini Assessment

Parts A, B and C are the assessment. The number that matters is **Part A out of 10** — it decides what happens next:

| Score | Meaning | Action |
|:-----:|:--------|:-------|
| **8–10** | It worked | Days 22–26 proceed as a project. Build with confidence. |
| **5–7** | Partial | Rewatch Corey Schafer 4 and 6 during Day 22's IF TIME. Build anyway — the project will finish the job. |
| **≤ 4** | Not yet | **Do not move on.** Repeat Days 15 and 18 on Days 22–23 and shift the project to 24–27. Losing two days here is far cheaper than carrying a hole into Month 2. |

---

## 🔁 Daily Review

1. Part A score: ___ / 10. Which questions failed?
2. Could I do B1 without jargon? What did I fall back on?
3. Part C — which method did I have to look up?
4. **Honest answer:** is OOP still my least favourite topic? What changed, and what did not?

---

## 📦 Completion Criteria

- [ ] Ten written explanations, closed book
- [ ] Both spoken explanations attempted and timed
- [ ] `Inventory` built from memory
- [ ] Score recorded and the action from the table above taken
- [ ] **[Week 3 Review](../Week_03_Review.md) completed**
- [ ] Committed to git

---

**[← Day 20](../Day_20/Day_20.md)** · **[Week 3 Review →](../Week_03_Review.md)** · [README](../../../README.md)
