from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector

d_cleaning = DataCleaning()
d_extractor = DataExtractor()
db_connector = DatabaseConnector()

engine = db_connector.init_db_engine("db_creds.yaml")
orders_data = d_extractor.read_rds_table(engine, 'orders_table')

#reset index and delete level_0
orders_data = orders_data.iloc[: , 1:]
orders_data = orders_data.set_index('index')

clean_data = d_cleaning.clean_orders_data(orders_data)

db_connector.upload_to_db(clean_data, "orders_table")