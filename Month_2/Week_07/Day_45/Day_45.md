# Day 45 — Ship It

|  |  |
|:--|:--|
| **Date** | Friday, 30 October 2026 |
| **Position** | Week 7 · Month 2 · Phase 2 |
| **Budget** | **~75 min** |
| **Code file** | `project_1/README.md` |
| **Project** | 📊 **P1 ships today** — your first portfolio piece |

> **Why the README is the project.** A reviewer will spend ninety seconds on your repository and most of it on the README. Your cleaning code can be excellent and your analysis correct, and none of it registers if the front page does not say what you found and how to reproduce it.
>
> This is also the halfway point of the ninety days. **Today you go from someone learning data science to someone with evidence of it.**

---

## 🎯 Objective

Ship a repository a stranger can read, run and trust.

---

## 📚 Learn — what a data-project README needs (20 min)

### The structure

```markdown
# Title — the finding, not the topic

One paragraph: what question, what data, what you found.

![headline chart](figures/headline.png)

## The finding
Claim · evidence · comparison · limitation.

## The data
Source, period, granularity, how to get it, licence.

## What I did
Clean → explore → analyse. Named decisions, with counts.

## Reproducing this
    git clone ...
    pip install -r requirements.txt
    python -m src.clean
    python -m src.charts

## Limitations
What this does not show. Be specific.

## Repository layout
Where things are.
```

### Six rules

**1. Title the finding, not the topic.** "Pakistan Inflation Analysis" says nothing. "Cooking oil rose 4× faster than the official inflation figure, Jan–Sep 2026" is a reason to keep reading.

**2. The headline chart goes above the fold.** A reviewer should see the finding before scrolling.

**3. Reproduction instructions must actually work.** Test them in a fresh clone. This is the most common failure in student portfolios — instructions written from memory that skip an undocumented step.

**4. State limitations prominently.** Counter-intuitive but true: a project that says what it cannot show reads as more trustworthy, not less. Anyone experienced will find the limitations anyway; finding them already written is the difference between "careful" and "naive".

**5. Numbers, not adjectives.** Not "cleaned the data" — "dropped 412 of 5,200 rows (7.9%): 380 with no price, 32 with dates outside the study period".

**6. No apologies.** Do not write "this is just a beginner project". Let the work be judged on what it is. Stating a limitation is confidence; apologising for the whole thing is not.

### The repository checklist

- [ ] `README.md` — finding first, chart above the fold
- [ ] `requirements.txt` — pinned, and actually complete
- [ ] `.gitignore` — `.venv`, `__pycache__`, `.ipynb_checkpoints`
- [ ] `data/raw/` with `SOURCES.md` *(large files ignored, sources documented)*
- [ ] `src/` — `clean.py`, `charts.py`
- [ ] `tests/` — they exist and they pass
- [ ] `notebooks/` — named in order, **outputs cleared**
- [ ] `figures/` — regenerable
- [ ] No hardcoded absolute paths *(`/Users/gauravkhatri/...` in a public repo is an immediate tell)*

---

## 💻 Code

### 🔴 MUST DO — ship (50 min)

1. Write the README against the structure above (25 min)
2. Title it with the finding
3. Put the headline chart above the fold
4. Every claim gets a number
5. Write the limitations section — **aim for at least four**
6. **Test reproduction in a fresh clone.** Actually clone it to a new directory and follow your own instructions. Fix whatever breaks — something will.
7. `requirements.txt` with pinned versions
8. Clear all notebook outputs
9. `grep -r "/Users/" .` — remove every absolute path
10. Final commit and push
11. Update `PILLARS/career.md`'s portfolio tracker with the project

### 🟢 IF TIME

- Write a five-sentence LinkedIn post: the question, the finding, the surprise, the method, the repository link. You do not have to publish it today, but write it while the work is fresh.

---

## 🔬 Understanding Check

1. **Communication.** Why title the README with the finding rather than the topic?
2. **Judgement.** Why do prominent limitations make a project more credible?
3. **Reproduction.** What broke when you tested the fresh clone? *(Something did.)*
4. **Self-assessment.** Would you be comfortable if an interviewer opened this repository right now? What would you not want them to look at?
5. **Reflection.** What would you do differently on the next project? Name three things.
6. **Career.** Describe this project in 30 seconds, as you would to an interviewer: question, method, finding, limitation.

---

## 🎯 Expected Outcome

- [ ] A shipped repository a stranger can read and run
- [ ] A README leading with the finding
- [ ] Reproduction tested from a fresh clone
- [ ] Your first genuine portfolio piece

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| README structure and rules | 20 min |
| Write it (1–5) | 25 min |
| Repository hygiene (6–11) | 25 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

**The fresh-clone test.** Clone into a new directory, follow your own README exactly, and see whether the analysis regenerates. If it does not, fix it — that is the difference between a project and a folder.

---

## 🔁 Daily Review

1. What broke in the fresh-clone test?
2. How many limitations did I list? Is that honest or performative?
3. Three things I would do differently next time.
4. **Halfway.** I have a portfolio project. What does that change about what I can say?

---

## 📦 Completion Criteria

- [ ] README complete, finding-titled, chart above the fold
- [ ] At least four limitations stated specifically
- [ ] Every claim carries a number
- [ ] Fresh-clone reproduction test passed
- [ ] `requirements.txt` pinned; notebooks cleared; no absolute paths
- [ ] Committed, pushed, and added to the career-pillar portfolio tracker
- [ ] **Project 1 shipped** 🎉

---

**[← Day 44](../Day_44/Day_44.md)** · **[Day 46 →](../Day_46/Day_46.md)** · [README](../../../README.md)
