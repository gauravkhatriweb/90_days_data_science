# Day 88 — The Portfolio Pass

|  |  |
|:--|:--|
| **Date** | Saturday, 12 December 2026 |
| **Position** | Week 13 · Month 3 · Phase 7 |
| **Budget** | **~180 min** — weekend deep-work day |
| **Code file** | **None.** Today is editing, not building. |

> **This is the highest-value day of the last two weeks, and the one most likely to be skipped** because nothing new gets built.
>
> **The arithmetic:** you have spent roughly 150 hours over 90 days. A reviewer will spend about **ninety seconds** on each repository before deciding whether to read further. Three hours spent making those four and a half minutes work is the best return available to you — and skipping it means three genuinely good projects that nobody gets far enough into to see.

---

## 🎯 Objective

Make three repositories that a stranger can understand, run and believe — and a portfolio page that frames them.

---

## 📚 Learn — the ninety seconds (20 min)

### What a reviewer actually does

| Seconds | They look at |
|:--------|:-------------|
| 0–10 | The repository name and description. Is this worth opening? |
| 10–30 | The top of the README. What is this, and what did they find? |
| 30–45 | An image, if there is one. **Most repositories have none.** |
| 45–70 | The file structure. Does this person organise code? |
| 70–90 | One source file, skimmed. Is it readable? |

**They do not run it. They do not open the notebooks.** They decide from the README and the structure.

### The seven things that decide it

| | Signal |
|:--|:--|
| **A finding-titled README** | This person communicates results, not activity |
| **An image above the fold** | Effort, and something to react to |
| **A stated limitation** | Judgement, and honesty |
| **`src/` rather than only notebooks** | Writes software, not just scripts |
| **A `tests/` directory** | Rare in junior portfolios, and noticed |
| **`requirements.txt`** | Thinks about reproducibility |
| **Recent, regular commits** | Sustained work rather than a weekend |

### The seven that lose it

| | Reads as |
|:--|:--|
| A default GitHub README, or none | Abandoned |
| A README that describes the topic, not the finding | Cannot summarise |
| Notebook outputs committed with errors visible | Careless |
| Absolute paths like `/Users/gauravkhatri/...` | Never ran it anywhere else |
| Data files committed | Does not know what belongs in git |
| No limitations anywhere | Naive, or hiding something |
| "Titanic", "Iris" | Followed a tutorial |

---

## 💻 The Work

### 🔴 MUST DO — repository hygiene, all three (60 min)

For **each** of Projects 1, 2 and 3:

1. **The ninety-second test.** Open it in a browser as a stranger. Set a timer. **Write down what you understood.**
2. README titled with the finding
3. An image in the first screen
4. Limitations present and prominent
5. Reproduction instructions — **tested**
6. `requirements.txt`, pinned
7. `.gitignore` correct; **no data files, no `.venv`, no `__pycache__`**
8. Notebook outputs cleared
9. `grep -r "/Users/"` — nothing
10. A repository **description and topics** set on GitHub *(most people forget this, and it is what shows in search)*

### 🔴 MUST DO — the portfolio README (50 min)

11. Create or update your GitHub profile README
12. **One line on who you are.** *"First-year Data Science & Business Analytics student at NIT Lahore (ASU curriculum). I build things with data and write down what they cannot tell you."*
13. **The three projects, in a table** — each with: the question, the finding, the tools, and a link
14. **Order them by what you want to be hired for**, not chronologically
15. A short "what I am learning now" line — honest and current
16. Contact details

### 🔴 MUST DO — the cross-project pass (40 min)

17. **Consistency:** the same README structure, the same tone, the same chart styling across all three. **A consistent portfolio reads as deliberate; an inconsistent one reads as a collection of assignments.**
18. **Kill the weakest thing.** Something in one of them is clearly worse than the rest. Fix it or remove it.
19. **The one-line summary of each**, written to be read together. Do they cover different skills, or do two overlap?
20. **Your best single artefact** — pick it, and make it better. **One excellent thing beats three good ones.**

### 🔴 MUST DO — external presence (20 min)

21. **LinkedIn:** headline, about section, projects. Link the repositories.
22. **One post.** Your best finding, in five sentences: the question, the data, the finding, the surprise, the link. **You do not have to publish it today** — but write it while it is fresh.

---

## 🔬 Understanding Check

1. **The test.** What did you understand from each repository in ninety seconds? Was it the finding?
2. **Signals.** Which of the seven positive signals are present in all three? Which are missing?
3. **Judgement.** What did you remove in exercise 18? Why was it weak?
4. **Coverage.** Do your three projects cover different skills, or do two overlap?
5. **Positioning.** Which project do you lead with, and what role does that imply you want?
6. **Honesty.** Is there anything in these repositories you would not want an interviewer to open?

---

## 🎯 Expected Outcome

- [ ] Three repositories that pass the ninety-second test
- [ ] A portfolio README framing them
- [ ] Consistency across all three
- [ ] One artefact deliberately made excellent
- [ ] An external presence that links to it

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| The ninety seconds | 20 min |
| Repository hygiene ×3 | 60 min |
| Portfolio README | 50 min |
| Cross-project pass | 40 min |
| External presence | 20 min |
| **Total** | **~190 min** — if over, drop exercise 22 |

---

## 🧪 Mini Assessment

**The real test:** send one repository link to someone who does not work in data. Ask them, after ninety seconds, what it is about and what you found.

**If they can answer, it works.** If they cannot, the README is for you rather than for them.

---

## 🔁 Daily Review

1. What did a real person take away in ninety seconds?
2. Which positive signals are still missing?
3. What did I cut, and what did I make excellent?
4. **Would I be comfortable if an interviewer opened any of these right now?**

---

## 📦 Completion Criteria

- [ ] Ninety-second test run on all three, results written
- [ ] All ten hygiene items done for each
- [ ] Portfolio README published
- [ ] Projects ordered by intent, not by date
- [ ] Consistency pass done
- [ ] Weakest element removed or fixed
- [ ] One artefact made deliberately excellent
- [ ] LinkedIn updated and linked
- [ ] Committed and pushed

---

**[← Day 87](../Day_87/Day_87.md)** · **[Day 89 →](../Day_89/Day_89.md)** · [README](../../../README.md)
