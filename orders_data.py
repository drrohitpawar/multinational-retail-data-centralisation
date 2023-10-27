import data_cleaning
import data_extraction
import database_utils
from pandasgui import show

engine = database_utils.DatabaseConnector().init_db_engine("db_creds.yaml")
orders_data = data_extraction.DataExtractor().read_rds_table(engine, 'orders_table')

#reset index and delete level_0
orders_data = orders_data.iloc[: , 1:]
orders_data = orders_data.set_index('index')

clean_data = data_cleaning.DataCleaning().clean_orders_data(orders_data)

database_utils.DatabaseConnector().upload_to_db(clean_data, "orders_table")