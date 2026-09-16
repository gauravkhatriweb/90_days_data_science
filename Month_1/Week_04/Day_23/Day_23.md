# Day 23 — P0: The Analysis Layer

|  |  |
|:--|:--|
| **Date** | Thursday, 8 October 2026 |
| **Position** | Week 4 · Month 1 · **OOP block, day 9 of 9** · **P0 build 2 of 3** |
| **Budget** | **~75 min** |
| **Code file** | `Day_23.py` + `lifelog/analysis.py`, `lifelog/formatters.py` |

> **The last day of the OOP block.** Yesterday built the parsing layer; today builds the part that answers questions and the part that prints them — and those two must not know about each other. When you are done, `LogCollection` will compute streaks without knowing whether the output is text or JSON, and the formatters will render without knowing where the logs came from. That separation is what the last nine days were for.

---

## 🎯 Objective

Complete the analysis and output layers with a clean separation between computing an answer and presenting it.

---

## 📚 Learn

**Nothing new.** Build.

### 🟢 IF TIME

- Skim `itertools.groupby` in the docs. Streak detection is a classic use, and you will meet the same idea in Pandas' `groupby` on Day 34.

---

## 💻 Code

### 🔴 MUST DO — `LogCollection` (40 min)

The object that holds many logs and answers questions about them.

```python
class LogCollection:
    def __init__(self, logs): ...

    @classmethod
    def from_source(cls, source): ...       # takes any LogSource

    # dunders -- it should behave like a collection
    __len__ · __getitem__ · __iter__ · __contains__(date) · __repr__

    # properties
    date_range · total_words · missing_dates

    # queries
    longest_streak() · section_frequency() · by_weekday()
    longest(n=5) · shortest(n=5) · filter(start, end)
```

Three that need real thought:

**`missing_dates`** — every date between the first and last log with no file. Do not assume the logs are sorted or unique.

**`longest_streak()`** — the longest run of consecutive dates. Return `(start, end, length)`. **Test it against a hand-checked answer** — off-by-one is almost guaranteed here, and it is exactly the Day 13 bug 5 shape.

**`filter(start, end)`** — returns a **new `LogCollection`**, not a list. That is what makes it chainable, and it is why the class exists rather than a pile of functions.

### 🔴 MUST DO — formatters (25 min)

```python
class Formatter(ABC):
    @abstractmethod
    def render(self, collection: LogCollection) -> str: ...
```

- `TextFormatter` — the human report
- `JsonFormatter` — the same facts, machine-readable

**The rule that matters:** `LogCollection` must contain **zero formatting code**, and the formatters must contain **zero analysis**. If a formatter is computing a streak, the boundary is in the wrong place.

**Test the boundary:** swap the formatter and confirm both produce the same *facts* in different shapes. If the JSON version is missing something the text version has, the analysis is leaking into the presentation.

### 🔴 MUST DO — run it on everything (10 min)

Point it at all 116 logs across every month directory. Read the output. **Does it match what you remember about your own year?** If the longest streak looks wrong, it probably is — and you are the only person who could catch it.

### 🟢 IF TIME

- Add `section_frequency()` output as a sorted table. Which section do you log most, and does that match what you think your priorities have been?

---

## 🔬 Understanding Check

1. **Design.** Why does `filter()` return a `LogCollection` rather than a list?
2. **Reasoning.** What breaks, concretely, if `TextFormatter` computes the streak itself?
3. **Debugging.** Your streak is one day too long. Where is the off-by-one likely to be, and how would you test for it without printing?
4. **Application.** You want "logs mentioning `data science`". Is that a method on `LogCollection`, a new class, or a function? Justify it.
5. **Understanding.** `LogCollection` has `__iter__` and `__getitem__`. Do you need both? What does each give you?
6. **Reflection.** Nine days of OOP end today. What would this project have looked like on Day 14 — and would it have been worse?
7. **Data.** What did the output tell you about your own logging that you did not know?

---

## 🎯 Expected Outcome

- [ ] `LogCollection` answering six questions about 116 real files
- [ ] Two formatters producing the same facts in different shapes
- [ ] No formatting in the analysis, no analysis in the formatters
- [ ] A verified-correct streak calculation

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| `LogCollection` | 40 min |
| Formatters | 20 min |
| Run on all 116 logs | 10 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Hand-write the expected longest streak for one month by looking at the filenames. Then run the code. **They must match.** If they do not, the bug is yours to find — and finding it is worth more than the feature.

---

## 🔁 Daily Review

1. Did my hand-checked streak match the code's answer? If not, where was the bug?
2. Which section do I log most often? Does that match what I believe my priorities are?
3. How many days did I actually log in September, and what is the real streak?
4. **The OOP block is over.** Compare today's comfort with Day 15's. What specifically changed?

---

## 📦 Completion Criteria

- [ ] `LogCollection` with all dunders, properties and queries
- [ ] `filter()` returns a `LogCollection`
- [ ] Streak verified against a hand-checked month
- [ ] Both formatters produce identical facts
- [ ] Runs on all 116 real logs
- [ ] Committed to git

---

**[← Day 22](../Day_22/Day_22.md)** · **[Day 24 →](../Day_24/Day_24.md)** · [README](../../../README.md)
