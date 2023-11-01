ALTER TABLE orders_table
ADD CONSTRAINT dim_users_fkey
FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid),


ADD CONSTRAINT dim_products_fkey
FOREIGN KEY (product_code) REFERENCES dim_products(product_code),


ADD CONSTRAINT dim_store_details_fkey
FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code),


ADD CONSTRAINT dim_card_details_fkey
FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number)
NOT VALID,


ADD CONSTRAINT dim_date_times_fkey
FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid);