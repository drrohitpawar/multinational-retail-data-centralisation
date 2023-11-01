import data_extraction
import data_cleaning
import database_utils
import json
import pandas as pd

header = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
num_of_store_ep = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'

num_of_store = data_extraction.DataExtractor().list_number_of_stores(num_of_store_ep, header)
#451 stores

store_data_raw = data_extraction.DataExtractor().retrieve_stores_data('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/0', header)
store_data_dict = json.loads(store_data_raw)
store_data = pd.DataFrame.from_dict([store_data_dict])

for n in range(1,451):
  sdr = data_extraction.DataExtractor().retrieve_stores_data(f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{str(n)}', header)
  sdd = json.loads(sdr)
  sd = pd.DataFrame.from_dict([sdd])
  store_data = pd.concat([store_data, sd])

clean_store_data = data_cleaning.DataCleaning().clean_store_data(store_data)
database_utils.DatabaseConnector().upload_to_db(clean_store_data, "dim_store_details")

