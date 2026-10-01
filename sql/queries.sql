-- SQL practice file for data science interviews and analysis

-- 1. Basic select
SELECT *
FROM customers
LIMIT 10;

-- 2. Aggregation
SELECT country,
       COUNT(*) AS customer_count,
       AVG(age) AS avg_age
FROM customers
GROUP BY country
ORDER BY customer_count DESC;

-- 3. Filter and aggregate
SELECT product_category,
       SUM(revenue) AS total_revenue
FROM sales
WHERE sale_date >= '2024-01-01'
GROUP BY product_category;

-- 4. Join example
SELECT c.customer_id,
       c.country,
       s.total_revenue
FROM customers c
LEFT JOIN (
    SELECT customer_id, SUM(amount) AS total_revenue
    FROM orders
    GROUP BY customer_id
) s
ON c.customer_id = s.customer_id;

-- 5. Window function example
SELECT customer_id,
       order_date,
       amount,
       SUM(amount) OVER (
           PARTITION BY customer_id
           ORDER BY order_date
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM orders;

-- 6. CTE example
WITH daily_sales AS (
    SELECT DATE(order_date) AS order_day,
           SUM(amount) AS daily_revenue
    FROM orders
    GROUP BY DATE(order_date)
)
SELECT order_day,
       daily_revenue,
       AVG(daily_revenue) OVER () AS avg_daily_revenue
FROM daily_sales;

-- 7. Median-like percentile practice (dialect-specific)
-- In PostgreSQL: SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY amount) FROM orders;

-- 8. Null-safe conditional example
SELECT customer_id,
       COALESCE(last_purchase_date, 'never') AS last_purchase_date
FROM customers;
