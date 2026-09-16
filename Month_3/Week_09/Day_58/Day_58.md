# Day 58 — Project 2: Questions Before Queries

|  |  |
|:--|:--|
| **Date** | Thursday, 12 November 2026 |
| **Position** | Week 9 · Month 3 · Phase 4 |
| **Budget** | **~75 min** |
| **Code file** | `Day_58.sql` + the `project_2/` folder |
| **Starts today** | 🛒 **Project 2 — Retail Analytics in SQL** |

> **Why a SQL-first project.** Project 1 was Python and Pandas. Project 2 is deliberately SQL, because that is what an entry-level analyst does most days and what an interview will test. It is also a different *kind* of thinking — declarative, set-based, and closer to how a real data warehouse is queried.
>
> **Two days shorter than planned**, because Days 60–61 are the NASA Space Apps hackathon. That is scheduled, not lost — and it is the reason today starts with scoping rather than querying.

---

## 🎯 Objective

Set up a real multi-table retail database and decide what questions the project will answer — before writing a single analytical query.

---

## 📋 The Brief

### The data

**[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)** — about 100,000 real orders from 2016–2018 across nine related tables: orders, order items, customers, sellers, products, payments, reviews, geolocation, and a category-name translation.

| Why this dataset | |
|:--|:--|
| **Real commercial data**, anonymised | Not a teaching toy |
| **Nine tables** | You cannot answer anything without joins — which is the point |
| **Genuinely messy** | Missing review scores, orders with no items, multiple payment rows per order, duplicate geolocation entries |
| **Real business questions** | Delivery delay, seller performance, review scores, repeat purchase |
| **Not overused in SQL** | Most published Olist work is Pandas EDA. A SQL cohort-and-retention analysis is a different, less common piece. |

*Alternative if Kaggle is awkward:* the [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) dataset, though it is a single table and so exercises joins far less.

### The framing

Analyse it as **a marketplace operator would** — the same questions SwiftBase would eventually have to answer for its own customers:

- Who are our best customers, and what makes them different?
- Do customers come back? How many, and how fast do we lose them?
- Which sellers or categories are actually worth having?
- Where does the order journey break down?
- What does a late delivery cost us?

**Every one of these ends in a decision.** That is the difference between this and an EDA notebook.

### The deliverable, by Day 64

- A SQLite database built from the raw CSVs, with a documented schema
- A `queries/` folder — one well-commented, readable file per question
- A written analysis: findings, with numbers, with limitations
- **A recommendation memo** — one page, five-part structure from Day 57
- A README a stranger can follow

---

## 💻 Code

### 🔴 MUST DO — setup and scoping (75 min)

**1. Get the data and build the database (25 min)**
- Download the nine CSVs into `project_2/data/raw/`
- Load each into SQLite with `pandas.to_sql`
- **Record the row count of every table** — you need these to sanity-check every join later
- Write `SOURCES.md`

**2. Map the schema (20 min)**
- For each table: columns, types, what a row *is*
- **Draw the relationships.** Which key joins to which? One-to-one, one-to-many, many-to-many?
- **Find the grain of each table.** "One row per order" and "one row per order item" are different, and confusing them is how revenue gets double-counted.
- Check every intended join key for duplicates *(Day 36's discipline)*

**3. Data-quality survey (15 min)**
- Nulls per column in the tables you will use
- Orders with no items? Items with no product? Payments with no order?
- Date ranges — and whether the first and last months are complete
- **Write it all in `NOTES.md`**

**4. Choose the questions (15 min)**
Pick **three**, and write for each:
- The precise question
- The metric, defined the Day 57 way
- The tables needed
- The decision it would inform
- What could make the answer misleading

> [!IMPORTANT]
> **Three questions, not eight.** You have Days 59, 62 and 64 — roughly four hours. Three answered properly is a portfolio piece. Eight answered shallowly is a notebook.

**Suggested — pick three:**

| Question | Technique | Why it is worth doing |
|:---------|:----------|:----------------------|
| Cohort retention by first-purchase month | Window functions, self-join | The single most common analytics question in a product company |
| RFM segmentation | `NTILE`, CTEs | The most practical customer segmentation there is |
| Does delivery delay predict review score? | Joins, date arithmetic, aggregation | Connects operations to customer sentiment — and to money |
| Seller concentration — what share comes from the top 10%? | Window functions, running totals | Concentration risk is a real board-level question |
| The order funnel — where do orders die? | `CASE`, conditional aggregation | Directly actionable |
| Category profitability including freight | Joins, arithmetic | Reveals categories that look good and are not |

---

## 🔬 Understanding Check

1. **Schema.** What is the grain of `order_items` versus `orders`? What breaks if you confuse them?
2. **Joins.** Which of your intended joins is one-to-many? What does that do to your row count, and how will you verify it?
3. **Data quality.** What is the worst quality problem you found? How will you handle it?
4. **Scoping.** Why three questions rather than eight?
5. **Metrics.** For your first question, write the metric precisely enough that another analyst would reproduce your number.
6. **Judgement.** Which of your three questions is most likely to produce a *boring* answer? Is it still worth asking?

---

## 🎯 Expected Outcome

- [ ] A queryable database with all nine tables and recorded row counts
- [ ] A documented schema with relationships and grains
- [ ] A data-quality survey in writing
- [ ] Three questions, each with a defined metric and a decision it informs

---

## ⏱️ Time Budget

| Block | Time |
|:------|-----:|
| Download and load | 25 min |
| Schema mapping | 20 min |
| Quality survey | 15 min |
| Question selection | 15 min |
| **Total** | **~75 min** |

---

## 🧪 Mini Assessment

Without running an analytical query, answer from the schema alone: **how would you compute total revenue?** Which table, which column, and what do you do about freight, multiple payment rows, and cancelled orders?

If you cannot answer that from the schema, the schema mapping is not finished.

---

## 🔁 Daily Review

1. What is the grain of each table I will use?
2. What is the worst data-quality problem, and what is my plan?
3. My three questions, and the decision each informs.
4. **The hackathon is in two days.** Is Day 59's work scoped so that stopping there is a clean stopping point?

---

## 📦 Completion Criteria

- [ ] Nine tables loaded, row counts recorded
- [ ] Schema documented with relationships and grains
- [ ] Join keys checked for duplicates
- [ ] Data-quality survey written in `NOTES.md`
- [ ] Three questions chosen, with metrics and decisions
- [ ] `SOURCES.md` written
- [ ] Committed to git

---

**[← Day 57](../Day_57/Day_57.md)** · **[Day 59 →](../Day_59/Day_59.md)** · [README](../../../README.md)
