# Day 20 — Abstraction: Designing the Interface First

|  |  |
|:--|:--|
| **Date** | Monday, 5 October 2026 |
| **Position** | Week 3 · Month 1 · **OOP block, day 6 of 9** |
| **Budget** | **~75 min** |
| **Code file** | `Day_20.py` |

> **Why abstraction comes last, not first.** Most courses teach the four pillars in the order *encapsulation, inheritance, polymorphism, abstraction* — and abstraction is the one that gets three vague sentences about "hiding complexity." It comes last here because it is the only one that is genuinely a **design skill** rather than a syntax feature, and design skills need something to design.
>
> You now have that: three sources, three ledger types, a working tool. Today you decide what their shared contract should be.

---

## 🎯 Objective

Design an interface before writing the classes that satisfy it, and know when to enforce that interface with an abstract base class rather than trusting duck typing.

---

## 📚 Learn

### 🔴 MUST DO — read, then design

Abstraction is **deciding what a caller needs to know, and refusing to expose anything else.**

You have already done it four times:
- `read_records(path)` — the caller does not know how quoting is handled
- `source.load()` — the caller does not know if it is CSV, JSON or a fake
- `ledger.total` — the caller does not know it is cached
- `len(ledger)` — the caller does not know the records are a list

In each case there is a **contract** (what it promises) and an **implementation** (how it keeps the promise), and the caller depends only on the contract.

### Abstract base classes — enforcing the contract

Day 19's duck typing worked with no shared base class. So when is declaring one worth it?

```python
from abc import ABC, abstractmethod

class DataSource(ABC):
    """Any source of ledger records."""

    @abstractmethod
    def load(self) -> list[dict]:
        """Return records as a list of dicts. Raise DataSourceError on failure."""

    @abstractmethod
    def describe(self) -> str:
        """One line naming where the data came from — for the report header."""

    def is_empty(self) -> bool:            # CONCRETE -- shared by all subclasses
        return len(self.load()) == 0
```

```python
class CsvSource(DataSource):
    def load(self): ...
    # forgot describe()

CsvSource()
# TypeError: Can't instantiate abstract class CsvSource
#            with abstract method describe
```

**The error arrives at instantiation, not at the call site three hours later.** That is the entire value: with duck typing, a missing `describe()` surfaces when someone happens to call it, possibly in production. With an ABC, it surfaces the moment anyone tries to create the object.

### When an ABC earns its place

| Use an ABC | Stay with duck typing |
|:-----------|:----------------------|
| Several implementations that must stay in step | One or two implementations |
| Other people (or future you) will add more | The whole thing is in one file |
| The contract needs documenting somewhere real | The contract is obvious |
| You want the failure early and loud | A small script |

**Honest assessment:** in day-to-day Python, most code does not need ABCs and duck typing is fine. Learn them because the *thinking* — "what is the contract here?" — is the valuable part, and because scikit-learn's estimator interface (Day 79) is exactly this pattern.

### The four pillars, now that you have used all of them

| Pillar | What you actually did |
|:-------|:----------------------|
| **Encapsulation** | `_cache` internal, `@property` for computed values, validation in setters — Day 19 |
| **Inheritance** | `OnlineLedger(Ledger)` with `super()`, and the "is a" test — Day 18 |
| **Polymorphism** | One `print_report()` over three types; `load_all()` with no base class — Days 18–19 |
| **Abstraction** | The contract each class promises, independent of how it keeps it — today |

**If someone asks you to explain OOP, do not recite these four words.** Explain the problem from Day 15 — data and behaviour drifting apart, arguments threaded everywhere — and then show how these four answer it.

### 🟢 IF TIME

- Read scikit-learn's ["Developing estimators"](https://scikit-learn.org/stable/developers/develop.html) page for 10 minutes. `fit`/`predict`/`transform` is an interface contract, and knowing that now makes Day 79 read differently.

---

## 💻 Code

### 🔴 MUST DO — design first, then implement

`Day_20.py`:

1. **Design before coding.** In a comment, write the contract for `DataSource`: what methods, what each returns, what each raises. **Do not write a class yet.**
2. Implement `DataSource(ABC)` with `@abstractmethod` for `load()` and `describe()`
3. Add a concrete `is_empty()` — shared behaviour, defined once
4. Implement `CsvSource` and `DictSource` against it
5. **Break it on purpose:** write a source missing `describe()`. Note *when* the error appears.
6. Compare: write the same missing-method case with duck typing. Note when *that* error appears. Write the difference in a comment.
7. Write `ReportFormatter(ABC)` with `format(ledger) -> str`, plus `TextFormatter` and `JsonFormatter`
8. Wire it together: `Ledger(source, formatter)` — the final composition
9. Swap both source and formatter at runtime; count the classes needed for 3 sources × 2 formats

### 🟢 IF TIME

- Add `ApiSource` that raises on failure. Where should the retry logic live — in the source, in `Ledger`, or in the caller? Argue it in a comment.

---

## 🔬 Understanding Check

1. **Reasoning.** What does abstraction mean beyond "hiding complexity"? Answer with `source.load()` as the example.
2. **Comparison.** Exercises 5 and 6: when does each approach surface a missing method? Why does that difference matter in a team?
3. **Application.** SwiftBase needs to send receipts by SMS, WhatsApp and print. Design the interface. What must every sender promise?
4. **Understanding.** Why can an ABC contain concrete methods as well as abstract ones? What does that give you?
5. **Reasoning.** Exercise 9: how many classes for 3 sources × 2 formats with composition? With inheritance? Show the arithmetic.
6. **Interview.** "Explain the four pillars of OOP." Answer with the Day 15 problem first, then the four as solutions. 90 seconds.
7. **Degree link.** CSE 205 teaches this in Java, where `interface` and `abstract class` are separate keywords. From what you know of Python's version, what do you think the difference is?

---

## 🎯 Expected Outcome

- [ ] Write a contract before writing a class
- [ ] Use `ABC` and `@abstractmethod` correctly
- [ ] Explain when an ABC beats duck typing, and when it is overhead
- [ ] Explain OOP through the problem it solves, not the four words

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Read abstraction + ABCs | 18 min |
| Design the contract (exercise 1) | 10 min |
| Exercises 2–9 | 40 min |
| Daily review | 7 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Eight minutes, closed book. Design a `Notifier` interface for SwiftBase — SMS, WhatsApp, printed receipt. Write the ABC with abstract methods and one concrete shared method, plus one implementation. Then answer: **what should happen when a notifier fails, and whose job is it to decide?**

---

## 🔁 Daily Review

1. Did designing the contract first change what I built compared to Days 18–19?
2. Exercise 6: how much later did the duck-typing failure appear?
3. Can I explain OOP through a problem rather than four vocabulary words?
4. Two days of the OOP block left, then the project. Which pillar is still weakest?

---

## 📦 Completion Criteria

- [ ] Contract written **before** any class
- [ ] `DataSource(ABC)` with two abstract and one concrete method
- [ ] Missing-method failure demonstrated both ways, timing noted
- [ ] `Ledger(source, formatter)` runs with both swapped
- [ ] Class-count arithmetic written down
- [ ] `Notifier` designed closed-book
- [ ] Committed to git

---

**[← Day 19](../Day_19/Day_19.md)** · **[Day 21 →](../Day_21/Day_21.md)** · [README](../../../README.md)
