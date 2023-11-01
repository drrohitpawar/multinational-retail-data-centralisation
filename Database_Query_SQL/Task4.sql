--How many sales are coming from online?

SELECT
  COUNT(*) AS number_of_sales,
  SUM(orders_table.product_quantity) AS product_quantity_count,
  CASE
    WHEN dim_store_details.store_type = 'Web Portal' THEN 'Web'
    ELSE 'Offline'
  END AS location_web_offline
FROM
  orders_table
LEFT JOIN
  dim_store_details
ON
  orders_table.store_code = dim_store_details.store_code
GROUP BY
  location_web_offline;

