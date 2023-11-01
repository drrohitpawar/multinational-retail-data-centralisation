UPDATE dim_products
SET product_price = LTRIM(product_price, '£')