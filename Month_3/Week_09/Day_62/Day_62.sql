-- =============================================================================
-- Day 62 — RFM segmentation and the funnel
-- =============================================================================
-- RFM sorts PEOPLE. The funnel sorts STEPS.
-- Both are one good query. Both end in something a business can act on.
-- =============================================================================


-- =============================================================================
-- RFM
-- =============================================================================

-- 1-3 -- R, F, M per customer, then NTILE(5) each.
--        WATCH THE RECENCY REVERSAL: for R, LOWER IS BETTER.
WITH customer_stats AS (
    SELECT
        c.customer_unique_id,
        JULIANDAY((SELECT MAX(order_purchase_timestamp) FROM orders))
          - JULIANDAY(MAX(o.order_purchase_timestamp))  AS recency_days,
        COUNT(DISTINCT o.order_id)                      AS frequency,
        SUM(i.price + i.freight_value)                  AS monetary
    FROM customers c
    JOIN orders o      ON o.customer_id = c.customer_id
    JOIN order_items i ON i.order_id = o.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY c.customer_unique_id
),
scored AS (
    SELECT *,
        NTILE(5) OVER (ORDER BY recency_days ASC)  AS r_score,   -- ASC: recent = 5
        NTILE(5) OVER (ORDER BY frequency DESC)    AS f_score,   -- DESC: more = ... check!
        NTILE(5) OVER (ORDER BY monetary DESC)     AS m_score
    FROM customer_stats
)
SELECT * FROM scored LIMIT 20;
--        CAREFUL: NTILE assigns 1 to the FIRST group in the ordering.
--        VERIFY: does your best customer actually score 5,5,5?
--        IF NOT, WHICH ORDERING IS REVERSED?


-- 4 -- map to named segments with CASE
--       champions / loyal / at risk / new / hibernating / big-spender-once



-- 5 -- customers AND total revenue per segment



-- 6 -- SANITY CHECK.
--      Do champions hold a DISPROPORTIONATE share of revenue? They should.
--      IF NOT, SOMETHING IS REVERSED.
--      champions: ____% of customers, ____% of revenue



-- 7 -- THE BUSINESS CASE.
--      At-risk customers: high F and M, low R.
--      HOW MANY: ____     HOW MUCH HISTORICAL REVENUE: ____
--      DAYS SINCE LAST ORDER (median): ____
--      This number is why the analysis was worth doing.



-- =============================================================================
-- THE FUNNEL
-- =============================================================================

-- 8 -- counts at each stage
SELECT
    COUNT(*)                                                                  AS placed,
    SUM(CASE WHEN order_approved_at IS NOT NULL THEN 1 ELSE 0 END)            AS approved,
    SUM(CASE WHEN order_delivered_carrier_date IS NOT NULL THEN 1 ELSE 0 END) AS shipped,
    SUM(CASE WHEN order_delivered_customer_date IS NOT NULL THEN 1 ELSE 0 END) AS delivered
FROM orders;


-- 9 -- STEP-TO-STEP rates, not just totals.
--      Losing 40% at approve->ship is a DIFFERENT PROBLEM from 40% at place->approve,
--      and it belongs to a different team.



-- 10 -- EXCLUDE orders too recent to have completed the journey.
--       WHAT CUTOFF DID I USE, AND WHY?
--       WHAT WOULD INCLUDING THEM HAVE DONE TO MY CONCLUSION?



-- 11 -- SEGMENT the funnel by one dimension (state / category / seller size)



-- 12 -- THE FINDING: the worst segment, at the worst step.
--       SEGMENT: ____   STEP: ____   RATE: ____ vs overall ____
--       WHAT WOULD I RECOMMEND?



-- =============================================================================
-- MINI ASSESSMENT -- one sentence with numbers:
--
--   "There are ____ at-risk customers representing ____ of historical revenue,
--    and they have not ordered in ____ days."
--
--   That sentence is a business case.
-- =============================================================================
