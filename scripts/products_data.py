from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector

d_cleaning = DataCleaning()
d_extractor = DataExtractor()
db_connector = DatabaseConnector()

address = 's3://data-handling-public/products.csv'

d_extractor.extract_from_s3(address)
df = d_extractor.read_csv('products.csv')

converted_product_weights = d_cleaning.convert_product_weights(df)
clean_data = d_cleaning.clean_products_data(converted_product_weights)

db_connector.upload_to_db(clean_data, "dim_products")