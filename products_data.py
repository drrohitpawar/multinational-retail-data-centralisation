import data_cleaning
import data_extraction
import database_utils
#from pandasgui import show
address = 's3://data-handling-public/products.csv'

data_extraction.DataExtractor().extract_from_s3(address)
df = data_extraction.DataExtractor().read_csv('products.csv')

converted_product_weights = data_cleaning.DataCleaning().convert_product_weights(df)
clean_data = data_cleaning.DataCleaning().clean_products_data(converted_product_weights)

database_utils.DatabaseConnector().upload_to_db(clean_data, "dim_products")