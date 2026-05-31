-- analysis_queries.sql

-- 1. Top 10 customers by total sales and profitability
SELECT
    f.customer_id,
    f.customer_name,
    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit,
    AVG(f.discount) AS avg_discount
FROM public.fact f
GROUP BY
    f.customer_id,
    f.customer_name
ORDER BY total_sales DESC
LIMIT 10;


-- 2. Regional performance analysis
SELECT
    f.country_region,
    COUNT(DISTINCT f.order_id) AS total_orders,
    COUNT(DISTINCT f.customer_id) AS total_customers,
    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit,
    AVG(f.price) AS avg_unit_price
FROM public.fact f
GROUP BY
    f.country_region
ORDER BY total_sales DESC;


-- 3. Product performance with profitability ranking
SELECT
    f.product_name,
    SUM(f.quantity) AS total_quantity_sold,
    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit,
    AVG(f.discount) AS avg_discount,
    RANK() OVER (ORDER BY SUM(f.profit) DESC) AS profit_rank
FROM public.fact f
GROUP BY
    f.product_name
ORDER BY total_profit DESC
LIMIT 15;