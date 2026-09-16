-- =============================================================================
-- Project 2 — setup and schema mapping
-- =============================================================================
-- Build from Python first:
--     import sqlite3, pandas as pd
--     con = sqlite3.connect("project_2/olist.db")
--     for name in ["orders","order_items","customers","sellers","products",
--                  "payments","reviews","geolocation","category_translation"]:
--         pd.read_csv(f"data/raw/{name}.csv").to_sql(name, con,
--                     if_exists="replace", index=False)
-- =============================================================================


-- 1 -- ROW COUNTS. Record these. Every join gets checked against them.
SELECT 'orders' AS t, COUNT(*) AS n FROM orders
UNION ALL SELECT 'order_items',  COUNT(*) FROM order_items
UNION ALL SELECT 'customers',    COUNT(*) FROM customers
UNION ALL SELECT 'sellers',      COUNT(*) FROM sellers
UNION ALL SELECT 'products',     COUNT(*) FROM products
UNION ALL SELECT 'payments',     COUNT(*) FROM payments
UNION ALL SELECT 'reviews',      COUNT(*) FROM reviews;


-- 2 -- THE GRAIN OF EACH TABLE.
--      "One row per ____" for each. Getting this wrong double-counts revenue.
--
--      orders      : one row per ____
--      order_items : one row per ____
--      payments    : one row per ____       <- check: can an order have several?
--      reviews     : one row per ____
--
SELECT order_id, COUNT(*) AS n FROM order_items GROUP BY order_id
ORDER BY n DESC LIMIT 5;

SELECT order_id, COUNT(*) AS n FROM payments GROUP BY order_id
ORDER BY n DESC LIMIT 5;
--      SO: JOINING orders TO payments MULTIPLIES ROWS WHEN ____


-- 3 -- CHECK EVERY JOIN KEY FOR DUPLICATES  (Day 36's discipline)
SELECT 'customers.customer_id' AS key_name, COUNT(*) - COUNT(DISTINCT customer_id) AS dupes FROM customers
UNION ALL
SELECT 'products.product_id',  COUNT(*) - COUNT(DISTINCT product_id)  FROM products
UNION ALL
SELECT 'sellers.seller_id',    COUNT(*) - COUNT(DISTINCT seller_id)   FROM sellers;


-- 4 -- ORPHANS. Rows on one side with no match on the other.
SELECT COUNT(*) AS orders_with_no_items
FROM orders o LEFT JOIN order_items i ON o.order_id = i.order_id
WHERE i.order_id IS NULL;
--      HOW MANY? IS THAT EXPECTED? WHAT KIND OF ORDER HAS NO ITEMS?


-- 5 -- DATE RANGE. Are the first and last months COMPLETE?
SELECT
    MIN(order_purchase_timestamp) AS first_order,
    MAX(order_purchase_timestamp) AS last_order,
    COUNT(DISTINCT substr(order_purchase_timestamp, 1, 7)) AS n_months
FROM orders;
--      A PARTIAL FIRST OR LAST MONTH WILL DISTORT EVERY MONTHLY TREND.
--      WHICH MONTHS WILL I EXCLUDE, AND WHY?


-- 6 -- NULLS in the columns you actually need
SELECT
    SUM(CASE WHEN order_delivered_customer_date IS NULL THEN 1 ELSE 0 END) AS no_delivery_date,
    SUM(CASE WHEN order_approved_at IS NULL THEN 1 ELSE 0 END)             AS no_approval,
    COUNT(*)                                                                AS total
FROM orders;


-- 7 -- ORDER STATUS distribution. Which statuses count as "a sale"?
SELECT order_status, COUNT(*) AS n
FROM orders GROUP BY order_status ORDER BY n DESC;
--      WHICH STATUSES WILL I INCLUDE IN REVENUE, AND WHY?
--      (this decision goes in the README -- it changes every number)


-- =============================================================================
-- MINI ASSESSMENT -- answer from the SCHEMA, before any analytical query
--
--   HOW DO I COMPUTE TOTAL REVENUE?
--     table:
--     column:
--     what about freight:
--     what about multiple payment rows per order:
--     what about cancelled / unavailable orders:
--
--   If I cannot answer this from the schema, the schema mapping is not done.
-- =============================================================================
