import pandas as pd
import dateparser
import database_utils
import data_extraction
import datetime

class DataCleaning:

  def __init__ (self):
    pass

  def clean_user_data(self, data):
    #drop null rows
    data = data.dropna()
    #set index
    data = data.set_index('index')
    #format phone numbers
    data['phone_number'] = data['phone_number'].str.replace("(", "")
    data['phone_number'] = data['phone_number'].str.replace(")", "")
    data['phone_number'] = data['phone_number'].str.replace(" ", "")
    data['phone_number'] = data['phone_number'].str.replace(".", "")
    data['phone_number'] = data['phone_number'].str.replace("x", "")
    data['phone_number'] = data['phone_number'].str.replace("-", "")

    for date in data['date_of_birth']:
      date = dateparser.parse(str(date))

    return data
  
  def clean_card_data(self, data):
    pass





engine = database_utils.DatabaseConnector().init_db_engine("db_creds.yaml")
db = data_extraction.DataExtractor(engine)
table = db.read_rds_table('legacy_users')
table_to_clean = DataCleaning()
clean_table = table_to_clean.clean_user_data(table)

print(clean_table.head())

#database_utils.DatabaseConnector().upload_to_db(clean_table, "dim_users")
