    
WITH next_time_table AS (
    SELECT
      *,
      LEAD(firsttimecolumn, 1) OVER () secondtimecolumn
    FROM
      (
        SELECT
          dim_date_times.year AS year,
          dim_date_times.month AS month,
          dim_date_times.day AS day,
          dim_date_times.timestamp,
          TO_TIMESTAMP(year || '-' || month || '-' || day || ' ' || dim_date_times.timestamp, 'YYYY-MM-DD HH24:MI:SS') AS firsttimecolumn
        FROM
          orders_table
        LEFT JOIN
          dim_date_times
        ON
          orders_table.date_uuid = dim_date_times.date_uuid
        ORDER BY
          dim_date_times.year, dim_date_times.month, dim_date_times.day, dim_date_times.timestamp
      )
    )

SELECT
  year,
  AVG(AGE(secondtimecolumn, firsttimecolumn)) AS actual_time_taken
FROM
  next_time_table
GROUP BY
  year
ORDER BY
  2 DESC;
