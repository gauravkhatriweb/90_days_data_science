-- =============================================================================
-- Day 33 — SQL, day 1 of the track
-- =============================================================================
-- Engine: SQLite (built into Python -- `import sqlite3`. No install, no server.)
--
-- Build the database first, from Python:
--     import sqlite3, pandas as pd
--     con = sqlite3.connect("project_1/prices.db")
--     df.to_sql("prices", con, if_exists="replace", index=False)
--
-- Then run these with:
--     pd.read_sql_query(open("Day_33.sql").read(), con)
-- or in the sqlite3 CLI.
--
-- CLAUSE ORDER (how you write it):
--     SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY -> LIMIT
-- EXECUTION ORDER (how it runs):
--     FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
--
-- SELECT runs almost LAST. That is why a SELECT alias cannot be used in WHERE.
-- =============================================================================


-- Q1 -- everything. Useful once, to see the shape. Never in production.
SELECT * FROM prices LIMIT 10;


-- Q2 -- specific columns only.
-- WHY IS SELECT * A BAD HABIT ON A REAL TABLE?  ANSWER:



-- Q3 -- WHERE with a single condition: items over 1000.



-- Q4 -- AND / OR. Mind the precedence -- AND binds tighter than OR,
--       exactly like & vs | in NumPy on Day 31.



-- Q5 -- BETWEEN. Note: BETWEEN is INCLUSIVE at both ends.
--       (Compare with Python slices, which are not.)



-- Q6 -- IN, with a list of item names.



-- Q7 -- LIKE. '%' is any sequence, '_' is one character.
--       Find every item containing 'tea'.
--       IS LIKE CASE-SENSITIVE IN SQLITE?  TEST IT.  ANSWER:



-- Q8 -- ORDER BY with LIMIT: the five most expensive items.



-- =============================================================================
-- Q9 -- THE COMPARISON
-- Answer the same question in SQL and in Pandas. Write both.
--
--   Question: the ten most expensive items in the most recent week
--
--   SQL:
--
--   PANDAS:
--
--   WHICH READS BETTER?
--   WHICH WAS FASTER TO WRITE?
--   WOULD YOUR ANSWER CHANGE FOR A 50-MILLION-ROW TABLE? WHY?
-- =============================================================================


-- =============================================================================
-- Q10 -- THE INTERVIEW QUESTION
-- Why does this fail?
--
--     SELECT price * 1.17 AS price_with_tax
--     FROM prices
--     WHERE price_with_tax > 1000;
--
-- ANSWER (use execution order):
-- =============================================================================
