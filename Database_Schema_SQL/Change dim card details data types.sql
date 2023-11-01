ALTER TABLE dim_card_details
  ALTER COLUMN card_number SET DATA TYPE VARCHAR(19),
  ALTER COLUMN expiry_date SET DATA TYPE VARCHAR(5),
  ALTER COLUMN date_payment_confirmed SET DATA TYPE DATE;
  