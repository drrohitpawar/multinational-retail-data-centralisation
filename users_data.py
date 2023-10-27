import data_cleaning
import data_extraction
import database_utils

engine = database_utils.DatabaseConnector().init_db_engine("db_creds.yaml")
db = data_extraction.DataExtractor().read_rds_table(engine, 'legacy_users')
clean_table = data_cleaning.DataCleaning().clean_user_data(db)


database_utils.DatabaseConnector().upload_to_db(clean_table, "dim_users")