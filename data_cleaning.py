import pandas as pd
import datetime
import string
import numpy as np

class DataCleaning:

  def __init__ (self):
    pass

  def clean_user_data(self, data):
    #drop null rows
    data = data.dropna()
    #dropping rows with string 'NULL'
    data = data.drop(data[data.phone_number == 'NULL'].index)
    #remove all rows in email with no '@'
    data = data[data.email_address.str.contains("@")]
    #set index
    data = data.set_index('index')
    #format phone numbers
    data['phone_number'] = data['phone_number'].str.replace("(", "")
    data['phone_number'] = data['phone_number'].str.replace(")", "")
    data['phone_number'] = data['phone_number'].str.replace(" ", "")
    data['phone_number'] = data['phone_number'].str.replace(".", "")
    data['phone_number'] = data['phone_number'].str.replace("x", "")
    data['phone_number'] = data['phone_number'].str.replace("-", "")
    #standardise date_payment_confimed column to datetime format
    data['date_of_birth'] = pd.to_datetime(data['date_of_birth'], format='mixed', dayfirst=False)
    #standardise date_payment_confimed column to datetime format
    data['join_date'] = pd.to_datetime(data['join_date'], format='mixed', dayfirst=False)
    
    return data
  
  def clean_card_data(self, data):
    #drop nulls
    data = data.dropna()
    #drop repeated header rows
    data = data.drop(data[data['card_number'] == 'card_number'].index)
    #drop rows with non-numbers in card_number
    data = data[pd.to_numeric(data['card_number'], errors='coerce').notnull()]
    #standardise date_payment_confimed column to datetime format
    data['date_payment_confirmed'] = pd.to_datetime(data['date_payment_confirmed'], format='mixed', dayfirst=False)

    return data
  
  def clean_store_data(self, data):
    #removing rows with values with lat column as they are all null
    data = data[data['lat'].isnull()]
    #dropping blank/unneccessary columns
    data = data.drop(columns=['lat'])
    #standardise date_payment_confimed column to datetime format
    data['opening_date'] = pd.to_datetime(data['opening_date'], format='mixed', dayfirst=False)
    #Changing continent names starting with 'ee'
    data.loc[data["continent"] == "eeEurope", "continent"] = 'Europe'
    data.loc[data["continent"] == "eeAmerica", "continent"] = 'America'

    return data
  
  def convert_product_weights(self, data):
    #drop null values
    data = data.dropna()
    #convert column to string for easier maniupulation
    data['weight'] = data['weight'].astype(str)
    #convert oz to kg
    data['weight'] = data['weight'].apply(lambda x: (float(x[:-2]) * 0.028) if 'oz' in x else x)
    #convert kg to value without 'kg
    data['weight'] = data['weight'].apply(lambda x: float(x.strip('kg')) if 'kg' in str(x) else x)

    #convert 'value x value' values to kg
    def process_weight(x):
      if isinstance(x, str):
          if ' x ' in x and 'g' in x:
              parts = x.split(" ")
              if len(parts) == 3:
                  value = float(parts[0])
                  value_2= parts[2]
                  remove_g = value_2[:-1]
                  float_value_2 = float(remove_g)
                  return value * float_value_2 / 1000
      return x 
    data['weight'] = data['weight'].apply(process_weight)

    #convert g and ml to kg
    data['weight'] = data['weight'].apply(lambda x: float(x.strip('g .')) if 'g .' in str(x) else x)
    data['weight'] = data['weight'].apply(lambda x: float(x.strip('g')) / 1000 if 'g' in str(x) else x)
    data['weight'] = data['weight'].apply(lambda x: float(x.strip('ml')) /1000 if 'ml' in str(x) else x)

    return data
  
  def clean_products_data(self, data):
    #drop null values
    data = data.dropna()
    #drop any values from product price with no £ prefix
    data = data[data.product_price.str.contains("£")]
    #convert weight column to float
    data['weight'] = data['weight'].astype(float)
    #standardise date_payment_confimed column to datetime format
    data['date_added'] = pd.to_datetime(data['date_added'], format='mixed', dayfirst=False)
    return data
  
  def clean_orders_data(self, data):
     data = data.drop(columns=['first_name', 'last_name', '1'])
     return data
  
  def clean_events_data(self, data):
    #drop null values
    data = data.dropna()
    #drop rows with non numbers in month column
    data = data[pd.to_numeric(data['month'], errors='coerce').notnull()]

    return data