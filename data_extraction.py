from sqlalchemy import create_engine, URL, inspect
import database_utils
import pandas as pd
import tabula
import requests
import boto3

class DataExtractor:
  def __init__(self):
    pass
  
  def list_db_tables(self, engine):
    inspector = inspect(engine)
    return inspector.get_table_names()
  
  def read_rds_table(self, engine, table_name):
    table = pd.read_sql_table(table_name, engine)
    return table

  def retrieve_pdf_data(self, link):
    #I found it easier to convert pdf data to csv and then read to dataframe
    tab = pd.read_csv("output.csv")
    return tab
  
  def list_number_of_stores(self, endpoint, headers):
    response = requests.get(endpoint, headers=headers)
    return response.text
  
  def retrieve_stores_data (self, endpoint, headers):
    response = requests.get(endpoint, headers=headers)
    return response.text
  
  def extract_from_s3(self, address):
    s3 = boto3.client('s3')
    path_parts = address.replace('s3://', '').split('/')
    bucket = path_parts[-2]
    object = path_parts[-1]
    s3.download_file(bucket, object, 'products.csv')

  def read_csv(self, file):
    return pd.read_csv(file)
  
  def extract_json_from_s3(self, address):
    s3 = boto3.client('s3')
    path_parts = address.replace('https://', '').split('/')
    object = path_parts[-1]
    bucket = path_parts[0].split('.')[0]
    s3.download_file(bucket, object, 'date_details.json')

  def read_json(self, file):
    return pd.read_json(file)
  