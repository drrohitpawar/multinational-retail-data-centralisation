ALTER TABLE dim_products
ADD COLUMN still_available VARCHAR;

UPDATE dim_products
SET still_available =   CASE
                          WHEN removed = 'Removed' THEN FALSE
                          ELSE TRUE
                        END;

ALTER TABLE dim_products
DROP COLUMN removed;

ALTER TABLE dim_products
ALTER COLUMN product_price SET DATA TYPE FLOAT USING (product_price::FLOAT),
ALTER COLUMN weight SET DATA TYPE FLOAT USING (weight::FLOAT),
ALTER COLUMN product_code SET DATA TYPE VARCHAR(11),
ALTER COLUMN date_added SET DATA TYPE DATE,
ALTER COLUMN uuid SET DATA TYPE UUID USING (uuid::UUID),
ALTER COLUMN weight_class SET DATA TYPE VARCHAR;
