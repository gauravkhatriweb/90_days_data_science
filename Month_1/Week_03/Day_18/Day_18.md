# Day 18 — Inheritance, and Knowing When Not To Use It

|  |  |
|:--|:--|
| **Date** | Saturday, 3 October 2026 |
| **Position** | Week 3 · Month 1 · **OOP block, day 4 of 9** |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | `Day_18.py` |
| **Second track** | 📐 **Essential Math Ch. 1, pp. 1–21** (40 min) — supports MAT 265 |

> **Why today is the pivot of the whole block.** Inheritance is the topic that makes people say they dislike OOP — not because it is hard to write, but because tutorials teach it with `Animal → Dog → Puppy` and never mention that **most real inheritance hierarchies are mistakes.** Professional Python code uses composition far more than inheritance.
>
> Today you will build the same feature both ways and compare them. By the end you should have an opinion, not a rule.
>
> Today also starts the second track: **Essential Math Chapter 1**, 40 minutes at the end. Your MAT 265 course is covering this material now, so this is the one place in the plan where a single study block counts twice.

---

## 🎯 Objective

Implement inheritance correctly, implement composition correctly, and be able to argue which one a given problem needs.

---

## 📚 Learn — Track 1: OOP (≈ 55 min)

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Corey Schafer — OOP 4: Inheritance](https://www.youtube.com/watch?v=RSl87lqOXDE) | **PRIMARY** | 20 min | Subclasses, `super()`, method resolution |
| [Apna College `8:51:23 → 9:59:06`](https://www.youtube.com/watch?v=ERCMXc8x7mc) · @1.5× | **REINFORCEMENT** | 25 min | OOPS Part 2 — inheritance from a second teacher |
| The composition section below | REFERENCE | 10 min | The part neither video covers well |

### 🟢 IF TIME

- [CodeWithHarry `7:23:17 → 7:48:07`](https://www.youtube.com/watch?v=UrsmFxEIp5k) — a third angle on inheritance. Take it only if the first two left you unsure.

---

## 🧠 Core Concepts — Inheritance

### The mechanics

```python
class Ledger:
    def __init__(self, name, records=None):
        self.name = name
        self.records = records or []

    def total(self):
        return sum(r["qty"] * r["price"] for r in self.records)


class OnlineLedger(Ledger):
    def __init__(self, name, records=None, delivery_fee=0.0):
        super().__init__(name, records)      # run the parent's setup FIRST
        self.delivery_fee = delivery_fee     # then add your own

    def total(self):                          # OVERRIDE
        return super().total() + self.delivery_fee * len(self.records)
```

**`super()` is the part to get right.** It calls the parent's version. Forgetting `super().__init__()` means the parent's attributes are never created, and you get an `AttributeError` somewhere far away from the actual mistake.

### The test that decides it

**Inheritance means "is a".** Composition means "has a".

| Statement | True? | Therefore |
|:----------|:-----:|:----------|
| An online ledger **is a** ledger | ✅ | Inheritance is defensible |
| A ledger **is a** CSV parser | ❌ | It **has a** parser → composition |
| A ledger **is a** report formatter | ❌ | It **has a** formatter → composition |
| A `Manager` **is an** `Employee` | ✅ | Defensible |
| A `Car` **is an** `Engine` | ❌ | It **has an** engine |

If you have to argue for the "is a", it is not one.

### The stricter test — substitutability

Anywhere the parent works, the child must work too, without the caller knowing. If `OnlineLedger.total()` returned a string while `Ledger.total()` returned a float, every function taking a `Ledger` breaks when handed an `OnlineLedger`. **The subclass must keep the parent's promises.**

*(This is the Liskov Substitution Principle. You do not need the name. You do need the idea, and CSE 205 will name it for you next semester.)*

### Why deep hierarchies go wrong

```
Ledger → RetailLedger → OnlineRetailLedger → InternationalOnlineRetailLedger
```

Now change something in `Ledger`. Which of the four breaks? You cannot tell without reading all four. Every level adds a place where behaviour can be overridden, and behaviour scattered across four files is behaviour nobody can trace.

**Practical rule: one or two levels. If you want a third, you probably want composition.**

---

## 🧠 Core Concepts — Composition

### What it looks like

```python
class CsvSource:
    def __init__(self, path): self.path = path
    def load(self): return parse_csv(self.path)

class JsonSource:
    def __init__(self, path): self.path = path
    def load(self): return json.loads(self.path.read_text())


class Ledger:
    def __init__(self, name, source):
        self.name = name
        self.source = source              # HAS A source
        self.records = source.load()
```

```python
Ledger("shop", CsvSource(path))
Ledger("shop", JsonSource(path))
Ledger("shop", ApiSource(url))          # new source, Ledger untouched
```

**Compare that to the inheritance version:** `CsvLedger`, `JsonLedger`, `ApiLedger`, `CachedCsvLedger`, `CachedJsonLedger`… Every combination needs its own class. Composition combines; inheritance multiplies.

### The four reasons composition usually wins

1. **Flexible at runtime** — swap the source after the object exists
2. **Testable** — pass a fake source, no files needed *(this is how you test on Day 25)*
3. **No combinatorial explosion** — three sources × two formatters is 5 classes, not 6
4. **Shallow and readable** — everything a `Ledger` does is in `Ledger`

### When inheritance is genuinely right

- A real "is a", with substitutability
- Sharing a substantial implementation, not just a name
- One or two levels
- Framework-imposed (`class MyModel(BaseEstimator)` in scikit-learn — Day 79)

---

## 📐 Learn — Track 2: Essential Math Ch. 1 (40 min)

**Read pages 1–21:** *Number Theory · Order of Operations · Variables · Functions · Summations · Exponents · Logarithms · Euler's Number and Natural Logarithms.*

Work the code as you read — Nield writes everything in Python, so this is 40 minutes of reading-and-typing, not reading alone.

### The three that matter later

| Concept | Where it comes back |
|:--------|:--------------------|
| **Summations (Σ)** | Every statistical formula from Day 48 onward. `Σ` is a `for` loop with a total — once you see that, formulas stop being intimidating. |
| **Logarithms** | Day 75. Logistic regression is built on log-odds, and "log" there means exactly what it means here. |
| **Euler's number *e*** | Day 75 again. The logistic function is `1/(1+e^-x)`. |

### The MAT 265 link

Ask yourself as you read: **has my calculus course covered this yet?** If yes, this is revision from a second angle. If not, you have just pre-read the lecture. Either way the same 40 minutes counts twice. Note the overlap in today's review.

---

## 💻 Code

### 🔴 MUST DO

`Day_18.py` — two parts.

**Part A — inheritance (40 min)**
1. `Ledger` base class with `__init__` and `total()`
2. `OnlineLedger(Ledger)` — override `total()`, use `super()` in both places
3. **The `super()` bug:** remove `super().__init__()` and watch where the `AttributeError` appears — note that it is nowhere near the real mistake
4. Add `RetailLedger`; write one function that accepts any ledger and works on all three — that is substitutability in action
5. **Break substitutability on purpose:** make one subclass return a string from `total()`. Watch exercise 4's function break. Restore it.

**Part B — composition (45 min)**
6. Write `CsvSource` and `DictSource`, both with `load()`
7. Rewrite `Ledger` to take a source instead of records
8. Swap the source at runtime and reload
9. Add `JsonSource` — and count how many existing lines you had to change *(the answer should be zero)*
10. **The comparison:** implement "a ledger that reads CSV and formats as JSON" both ways. Count the classes each needs. Write which you would ship and why.

Exercise 10 is the assessment. Everything before it is preparation for having an opinion.

### 🟢 IF TIME

- Refactor Day 12's `shopsummary` to use a source object. Run it on both CSV and a dict.

---

## 🔬 Understanding Check

1. **Reasoning.** Give one example of a genuine "is a" from SwiftBase's domain, and one "has a" that a beginner might wrongly model as inheritance.
2. **Debugging.** You forgot `super().__init__()`. Where does the error surface, and why is that far from the cause?
3. **Comparison.** Three sources and two output formats. How many classes with inheritance? With composition? Show the arithmetic.
4. **Application.** Exercise 5 broke a caller by changing a return type. State the rule it violated in your own words.
5. **Reasoning.** Why is a four-level hierarchy harder to change than a four-part composition?
6. **Understanding.** In exercise 9, how many existing lines changed when you added a third source? What does that number tell you?
7. **Interview.** "When would you choose composition over inheritance?" 45 seconds, with an example.
8. **Maths.** Write the summation Σ(i=1 to 5) of i² as a Python loop, then as a comprehension. Which reads more like the notation?

---

## 🎯 Expected Outcome

- [ ] Write a subclass with correct `super()` usage in both `__init__` and an override
- [ ] Apply the "is a / has a" test to a new problem
- [ ] Explain substitutability with the example you broke yourself
- [ ] Argue for composition with a concrete class count
- [ ] Read Σ notation as a loop

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Corey Schafer inheritance | 20 min |
| Apna College OOPS Part 2 @1.5× | 25 min |
| Composition section | 10 min |
| Part A — inheritance | 40 min |
| Part B — composition | 45 min |
| **Essential Math Ch. 1, pp. 1–21** | 40 min |
| Daily review | 10 min |
| **Total** | **~190 min** — if you are over, drop the Apna College video |

---

## 🧪 Mini Assessment

Ten minutes, closed book. A payment system handles cash, card and mobile wallet, each with a different fee calculation, and must log every transaction.

Design it **twice** — once with inheritance, once with composition. Do not write full implementations; write the class names, what each holds and what each does. Then write three sentences on which you would ship.

---

## 🔁 Daily Review

1. Which felt more natural to write — inheritance or composition? Which felt more natural to *change*?
2. Exercise 3: how far from the actual mistake did the `AttributeError` appear?
3. Exercise 9: how many lines changed when you added a source?
4. **Maths:** has MAT 265 covered any of pages 1–21 yet? Which parts were revision and which were new?
5. Has OOP started to feel less unpleasant? Rate 1–5, and say what changed.

---

## 📦 Completion Criteria

- [ ] Three-class inheritance hierarchy working with `super()`
- [ ] The `super()` bug reproduced and located
- [ ] Substitutability broken on purpose and restored
- [ ] Composition version working with three interchangeable sources
- [ ] Exercise 10 comparison written, with a stated preference and reason
- [ ] Essential Math pp. 1–21 read, with code typed
- [ ] MAT 265 overlap noted
- [ ] Committed to git

---

**[← Day 17](../Day_17/Day_17.md)** · **[Day 19 →](../Day_19/Day_19.md)** · [README](../../../README.md)
