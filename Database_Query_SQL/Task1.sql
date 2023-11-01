--How many stores does the business have and in which countries?

SELECT
  country_code AS country,
  COUNT(*) AS total_no_stores
FROM
  dim_store_details
GROUP BY
  country_code;
