ALTER TABLE dim_date_times
  ALTER COLUMN month SET DATA TYPE VARCHAR(2),
  ALTER COLUMN year SET DATA TYPE VARCHAR(4),
  ALTER COLUMN day SET DATA TYPE VARCHAR(2),
  ALTER COLUMN time_period SET DATA TYPE VARCHAR(10),
  ALTER COLUMN date_uuid SET DATA TYPE UUID USING (date_uuid::UUID);