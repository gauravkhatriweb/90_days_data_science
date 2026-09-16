# Day 87 — One Dashboard

|  |  |
|:--|:--|
| **Date** | Friday, 11 December 2026 |
| **Position** | Week 13 · Month 3 · Phase 7 |
| **Budget** | **~75 min** |
| **Code file** | `dashboard/app.py` *(Streamlit)* or a Power BI file |

> **Why one day and not a course.** `Tem.txt` contains 21 hours of Power BI, DAX and Excel video. That is 13% of the entire budget spent on tool operation, for a skill that is the fastest on the whole list to pick up when a specific job asks for a specific tool.
>
> **What a portfolio actually needs is one dashboard that exists** — evidence you can build an interface someone else uses, rather than a notebook only you can run. That is today. If a role later demands Power BI specifically, the full course is still there and it will take a weekend.

---

## 🎯 Objective

Build one interactive dashboard from Project 2's data that a non-technical person could use without you present.

---

## 📚 Learn — dashboards versus notebooks (15 min)

### The difference that matters

| Notebook | Dashboard |
|:---------|:----------|
| For you | **For someone else** |
| Linear — runs top to bottom | **Non-linear — they click wherever they like** |
| You are there to explain | **You are not there** |
| Exploration | **Answering a recurring question** |

**A dashboard answers a question someone asks repeatedly.** If they would ask it once, write a report. Building a dashboard for a one-off question is the most common waste in analytics.

### Which tool

| | Use when |
|:--|:--|
| **Streamlit** | Python already, fast to build, deployable free, **and it is code — so it lives in git** |
| **Power BI** | The organisation already uses it; a role names it explicitly |
| **Tableau** | Same reasoning |
| **Metabase / Looker** | The company already has it |

**Streamlit is the right choice here.** It is Python, it is a file in your repository that a reviewer can read, it deploys free on Streamlit Community Cloud, and a live URL in a CV is worth more than a screenshot.

```python
import streamlit as st
import pandas as pd

st.title("Retail performance")

df = load_data()                                    # cache this
region = st.selectbox("Region", sorted(df.region.unique()))
dates = st.date_input("Period", [df.date.min(), df.date.max()])

filtered = df[(df.region == region) & df.date.between(*dates)]

col1, col2, col3 = st.columns(3)
col1.metric("Revenue", f"PKR {filtered.revenue.sum():,.0f}")
col2.metric("Orders", f"{len(filtered):,}")
col3.metric("Average order", f"PKR {filtered.revenue.mean():,.0f}")

st.plotly_chart(build_trend_chart(filtered))
```

### Six rules for a dashboard someone will use

1. **One question per dashboard.** "Retail performance" is a theme, not a question. "Which regions and categories are under-performing this month?" is a question.
2. **The headline number at the top**, with a comparison. A number with no comparison is trivia.
3. **Three to five charts. Not twelve.** A dashboard that shows everything communicates nothing.
4. **Filters that matter** — the two or three a user actually varies.
5. **It must load in under three seconds.** Cache the data; pre-aggregate; do not compute a groupby over a million rows on every click.
6. **Say what it does not show.** One line at the bottom. The same honesty as a README.

### The mistake to avoid

**Do not build a dashboard of everything you know.** The instinct after a good analysis is to put all of it on screen. Every extra chart makes the important one harder to find, and a reviewer reads twelve charts as "did not know what mattered".

---

## 💻 The Work

### 🔴 MUST DO (60 min)

1. **Write the question** the dashboard answers, in one sentence. **And who asks it.**
2. `pip install streamlit`; create `dashboard/app.py`
3. Load Project 2's processed data; **cache it** with `@st.cache_data`
4. The headline metric row — three or four `st.metric` tiles, each with a comparison
5. Two or three filters that matter
6. Three to five charts, each answering part of the question
7. **The load-time check.** Under three seconds. If not, pre-aggregate.
8. **A one-line note on what it does not show**
9. `streamlit run dashboard/app.py` — click through it as a user would
10. **The stranger test:** hand it to someone and watch. **Do not explain anything.** Note every place they hesitate.
11. Fix the top two hesitations

### 🟢 IF TIME

- Deploy to Streamlit Community Cloud. **A live URL is worth more than a screenshot** — it is the difference between "I built a dashboard" and "here it is."
- Add it to the Project 2 README with a screenshot and the link.

---

## 🔬 Understanding Check

1. **Framing.** What question does it answer, and who asks it?
2. **Judgement.** Which charts did you leave out? *(If none, you probably included too many.)*
3. **Observation.** Exercise 10: where did your tester hesitate? What did that reveal?
4. **Performance.** What did you have to do to get under three seconds?
5. **Honesty.** What does it not show? Is that written on it?
6. **Comparison.** When is a dashboard the wrong answer and a one-off report the right one?

---

## 🎯 Expected Outcome

- [ ] A working dashboard answering one named question
- [ ] Headline metrics with comparisons
- [ ] Three to five charts, filters that matter
- [ ] Loads in under three seconds
- [ ] Tested on a real person

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Dashboards vs notebooks | 15 min |
| Build it (1–9) | 45 min |
| Stranger test and fixes (10–11) | 10 min |
| Daily review | 5 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

**The stranger test.** Hand it over, say nothing, and watch. If they find the answer to your stated question without help, it works.

---

## 🔁 Daily Review

1. The question, and who asks it.
2. Where did my tester hesitate?
3. What did I leave out, and was that hard?
4. Is it deployed, or only local?

---

## 📦 Completion Criteria

- [ ] The question and its audience written down
- [ ] Dashboard runs, with cached data
- [ ] Metric tiles with comparisons
- [ ] Three to five charts, two or three filters
- [ ] Loads in under three seconds
- [ ] "What this does not show" present
- [ ] Stranger test done, top two hesitations fixed
- [ ] Committed to git

---

**[← Day 86](../Day_86/Day_86.md)** · **[Day 88 →](../Day_88/Day_88.md)** · [README](../../../README.md)
