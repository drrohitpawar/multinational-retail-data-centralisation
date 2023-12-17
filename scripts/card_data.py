from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector

d_cleaning = DataCleaning()
d_extractor = DataExtractor()
db_connector = DatabaseConnector()

df = d_extractor.retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
df = d_cleaning.clean_card_data(df)
db_connector.upload_to_db(df, "dim_card_details")

