import data_cleaning
import data_extraction
import database_utils
from pandasgui import show

address = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'

data_extraction.DataExtractor().extract_json_from_s3(address)
event_data = data_extraction.DataExtractor().read_json('date_details.json')
clean_event_data = data_cleaning.DataCleaning().clean_events_data(event_data)

database_utils.DatabaseConnector().upload_to_db(clean_event_data, "dim_date_times")
