--What percentage of sales come through each type of store?

SELECT
  store_type,
  total_sales,
  ((total_sales / SUM(total_sales) OVER ()) * 100) AS percentage_total
FROM
( 
  SELECT
    dim_store_details.store_type AS store_type,
    ROUND(SUM(orders_table.product_quantity * dim_products.product_price)) AS total_sales
  FROM
    orders_table
  LEFT JOIN
    dim_store_details
  ON
    orders_table.store_code = dim_store_details.store_code
  LEFT JOIN
    dim_products
  ON
    orders_table.product_code = dim_products.product_code
  GROUP BY
    dim_store_details.store_type
)
ORDER BY
  percentage_total DESC;