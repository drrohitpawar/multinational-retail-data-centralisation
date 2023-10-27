import data_cleaning
import data_extraction
import database_utils

df = data_extraction.DataExtractor().retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
df = data_cleaning.DataCleaning().clean_card_data(df)
database_utils.DatabaseConnector().upload_to_db(df, "dim_card_details")

