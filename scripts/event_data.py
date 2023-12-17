from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector

d_cleaning = DataCleaning()
d_extractor = DataExtractor()
db_connector = DatabaseConnector()

address = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'

d_extractor.extract_json_from_s3(address)
event_data = d_extractor.read_json('date_details.json')
clean_event_data = d_cleaning.clean_events_data(event_data)

db_connector.upload_to_db(clean_event_data, "dim_date_times")
