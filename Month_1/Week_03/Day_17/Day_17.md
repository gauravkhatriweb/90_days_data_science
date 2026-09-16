# Day 17 — Class Variables, and Methods That Do Not Need an Instance

|  |  |
|:--|:--|
| **Date** | Friday, 2 October 2026 |
| **Position** | Week 3 · Month 1 · **OOP block, day 3 of 9** |
| **Budget** | **~75 min** |
| **Code file** | `Day_17.py` |

> **Why today matters more than it looks.** Class variables are the source of one of the nastiest bugs in Python — a mutable class variable shared silently across every instance. And `classmethod` is what makes alternative constructors possible, which is the pattern that finally solves Symptom 4 from Day 15 (CSV *and* JSON input without duplicating everything).

---

## 🎯 Objective

Know exactly where a piece of data lives — on the class or on the instance — and use `classmethod` to build objects from more than one kind of source.

---

## 📚 Learn

### 🔴 MUST DO

| Resource | Type | Time | Purpose |
|:---------|:-----|-----:|:--------|
| [Corey Schafer — OOP 2: Class Variables](https://www.youtube.com/watch?v=BJ-VvGyQxho) | **PRIMARY** | 12 min | Class vs instance, and the lookup order |
| [Corey Schafer — OOP 3: classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M) | **PRIMARY** | 15 min | Alternative constructors — the useful part |

### 🟢 IF TIME

- Only if Day 16's review said the reinforcement layer is still needed: [CodeWithHarry `7:07:11 → 7:23:17`](https://www.youtube.com/watch?v=UrsmFxEIp5k) practice set.

---

## 🧠 Core Concepts

### Where does the value live?

```python
class ShopLedger:
    currency = "PKR"          # CLASS variable -- one copy, shared

    def __init__(self, name):
        self.name = name      # INSTANCE variable -- one per object
```

Python's lookup order on `obj.attr`: **instance first, then class.** So:

```python
a = ShopLedger("A")
a.currency            # "PKR"  -- not found on instance, found on class
a.currency = "USD"    # creates an INSTANCE variable that SHADOWS the class one
ShopLedger.currency   # still "PKR"
```

Assigning through the instance never changes the class variable. It creates a new instance variable that hides it. **This surprises almost everyone once.**

### The bug that actually costs you hours

```python
class ShopLedger:
    records = []                    # MUTABLE class variable -- shared

    def add(self, r):
        self.records.append(r)      # mutates the SHARED list

a, b = ShopLedger(), ShopLedger()
a.add({"item": "tea"})
b.records                           # [{'item': 'tea'}]  <- b has a's data
```

`self.records.append(...)` never assigns, so it never creates an instance variable. It reaches through to the class list and mutates it — for every instance, forever.

This is the **same shape** as the Day 4 mutable-default-argument bug: a mutable object created once at definition time and shared thereafter. Recognising that the two are one idea is worth more than memorising both.

**The rule:** class variables should be immutable — strings, numbers, tuples, frozensets. Anything mutable belongs in `__init__`.

### Legitimate uses of class variables

```python
class ShopLedger:
    currency = "PKR"                      # a constant for all instances
    VALID_REGIONS = ("sindh", "punjab")   # a tuple, so it cannot be mutated
    instances_created = 0                 # a genuine shared counter
```

### `classmethod` — alternative constructors

Receives the **class** rather than the instance:

```python
class ShopLedger:
    def __init__(self, name, records=None):
        self.name = name
        self.records = records or []

    @classmethod
    def from_csv(cls, path):
        records = parse_csv(path)
        return cls(path.stem, records)     # cls, not ShopLedger

    @classmethod
    def from_json(cls, path):
        return cls(path.stem, json.loads(path.read_text()))
```

```python
ledger = ShopLedger.from_csv(Path("sales.csv"))
```

**This is the answer to Day 15's Symptom 4.** One class, one `__init__`, several ways in — and no `if source_type == "csv"` anywhere.

Why `cls` and not the class name directly? Because if someone subclasses `ShopLedger`, `cls` will be the subclass and `from_csv` will return the right type. Hardcoding the name breaks that silently.

### `staticmethod` — and why it is usually not the answer

```python
@staticmethod
def is_valid_region(region):
    return region in ShopLedger.VALID_REGIONS
```

Receives neither `self` nor `cls`. It is a plain function that happens to live inside a class for organisation.

**Use it sparingly.** If it needs no instance and no class, ask whether it should just be a module-level function. Usually it should. `staticmethod` earns its place when the function is conceptually bound to the class and nowhere else.

### The three, side by side

| | Receives | Use when |
|:--|:--|:--|
| **instance method** | `self` | It needs this object's data — the default |
| **`@classmethod`** | `cls` | Alternative constructor, or it needs class-level data |
| **`@staticmethod`** | nothing | Rare. A helper that belongs here by meaning only. |

---

## 💻 Code

### 🔴 MUST DO

`Day_17.py`:

1. Add `currency = "PKR"` to `ShopLedger`; demonstrate the lookup order
2. Assign `a.currency = "USD"`; show `ShopLedger.currency` is unchanged, and explain
3. **Reproduce the mutable-class-variable bug** — make `records` a class variable and watch two ledgers share data
4. Fix it, and write the connection to the Day 4 mutable-default bug in a comment
5. Add `instances_created` as a genuine shared counter
6. Write `from_csv(cls, path)` — an alternative constructor
7. Write `from_records(cls, records, name)` — a second one
8. Use `cls` rather than the class name; then subclass `ShopLedger` and show why that mattered
9. Add one `staticmethod`, then argue in a comment for or against it being a module function

### 🟢 IF TIME

- Add `from_json`. Notice you touched neither `__init__` nor any existing method. That is the payoff.

---

## 🔬 Understanding Check

1. **Understanding.** What is Python's attribute lookup order on `obj.attr`?
2. **Debugging.** Two instances share a list. Explain exactly why `self.records.append(x)` did not create an instance variable.
3. **Comparison.** What do the mutable-class-variable bug and the mutable-default-argument bug have in common? State the shared principle in one sentence.
4. **Reasoning.** Why `cls` instead of the class name inside a `classmethod`? What breaks if you hardcode it?
5. **Application.** Your ledger must load from CSV, JSON and a database. Sketch the class. How many `__init__` methods?
6. **Reasoning.** When is `staticmethod` justified rather than a module-level function?
7. **Interview.** "Explain `classmethod` versus `staticmethod`." Under 45 seconds, with an example.

---

## 🎯 Expected Outcome

- [ ] Predict whether an attribute lives on the class or the instance
- [ ] Recognise the mutable-class-variable bug on sight
- [ ] Write alternative constructors with `classmethod`
- [ ] Explain why `cls` matters for subclasses

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Corey Schafer 2 + 3 | 27 min |
| Nine exercises | 40 min |
| Daily review | 8 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Six minutes, closed book. Write `Transaction` with a class-level `count` that tracks how many have been created, an instance `amount`, and a `from_string("tea:4:1250")` alternative constructor.

---

## 🔁 Daily Review

1. Did I predict the class-variable bug before running exercise 3?
2. Can I state the shared principle behind that bug and the Day 4 one, in one sentence?
3. Which of the three method types would I use most in real code, and why?
4. Tomorrow is inheritance — three hours, three teachers. Is there anything from Days 15–17 I should re-read first?

---

## 📦 Completion Criteria

- [ ] Lookup order demonstrated with real output
- [ ] Mutable-class-variable bug reproduced *and* fixed
- [ ] Connection to the Day 4 bug written down
- [ ] Two alternative constructors working, using `cls`
- [ ] The subclass demonstration shows why `cls` mattered
- [ ] `Transaction` written closed-book
- [ ] Committed to git

---

**[← Day 16](../Day_16/Day_16.md)** · **[Day 18 →](../Day_18/Day_18.md)** · [README](../../../README.md)
