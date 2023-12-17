from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector

d_cleaning = DataCleaning()
d_extractor = DataExtractor()
db_connector = DatabaseConnector()

engine = db_connector.init_db_engine("db_creds.yaml")
db = d_extractor.read_rds_table(engine, 'legacy_users')
clean_table = d_cleaning.clean_user_data(db)

db_connector.upload_to_db(clean_table, "dim_users")