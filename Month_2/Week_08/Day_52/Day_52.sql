-- =============================================================================
-- Day 52 — Window functions
-- =============================================================================
-- GROUP BY   COLLAPSES rows -> one row per group
-- WINDOW     KEEPS rows     -> every row, plus its group's statistic
--
-- That is exactly what pandas .transform() does. Same idea, two syntaxes.
-- =============================================================================


-- Q8 -- each row beside its item's average
SELECT
    item, week, price,
    AVG(price) OVER (PARTITION BY item)            AS item_avg,
    price - AVG(price) OVER (PARTITION BY item)    AS diff_from_avg
FROM prices
ORDER BY item, week;
--       COMPARE: df["diff"] = df["price"] - df.groupby("item")["price"].transform("mean")


-- Q9 -- LAG: week-on-week change IN ONE LINE.
SELECT
    item, week, price,
    LAG(price) OVER (PARTITION BY item ORDER BY week)   AS prev_week,
    ROUND((price - LAG(price) OVER (PARTITION BY item ORDER BY week))
          * 100.0 / LAG(price) OVER (PARTITION BY item ORDER BY week), 2) AS pct_change
FROM prices
ORDER BY item, week;
--       COMPARE WITH DAY 44's SELF-JOIN.
--       SELF-JOIN LINES: ____    WINDOW LINES: ____
--       WHICH IS CLEARER? WHICH IS FASTER, AND WHY?


-- Q10 -- ROW_NUMBER vs RANK vs DENSE_RANK on TIED data. All three differ.
SELECT
    item, price,
    ROW_NUMBER()  OVER (ORDER BY price DESC) AS row_num,
    RANK()        OVER (ORDER BY price DESC) AS rnk,
    DENSE_RANK()  OVER (ORDER BY price DESC) AS dense_rnk
FROM prices
LIMIT 20;
--       WITH TIES, HOW DOES EACH BEHAVE?
--         ROW_NUMBER :
--         RANK       :
--         DENSE_RANK :
--       WHICH WOULD I USE FOR "TOP 3 PER CATEGORY, NO TIES"?


-- Q11 -- rolling 4-week average with an explicit frame
SELECT
    item, week, price,
    AVG(price) OVER (
        PARTITION BY item
        ORDER BY week
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
    ) AS rolling_4wk
FROM prices;
--       WHAT HAPPENS IN THE FIRST THREE WEEKS OF EACH ITEM?
--       IS THAT THE BEHAVIOUR I WANT?


-- Q12 -- top 3 per item, using a CTE
WITH ranked AS (
    SELECT item, week, price,
           ROW_NUMBER() OVER (PARTITION BY item ORDER BY price DESC) AS rn
    FROM prices
)
SELECT item, week, price
FROM ranked
WHERE rn <= 3
ORDER BY item, rn;
--       WHY DOES THE RANKING NEED A CTE (OR SUBQUERY)?
--       (hint: Day 33's execution order -- WHERE runs before SELECT)


-- =============================================================================
-- Q13 -- THE CONNECTION
--   Same result, two tools:
--
--   PANDAS:  df["item_avg"] = df.groupby("item")["price"].transform("mean")
--   SQL:     AVG(price) OVER (PARTITION BY item)
--
--   STATE THE SHARED IDEA IN ONE SENTENCE:
-- =============================================================================
