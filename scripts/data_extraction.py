from sqlalchemy import inspect
import pandas as pd
import requests
import tabula
import boto3

class DataExtractor:
  
  def list_db_tables(self, engine):
    """Returns list of tables from input Database engine"""
    inspector = inspect(engine)
    return inspector.get_table_names()
  
  def read_rds_table(self, engine, table_name):
    """Returns pandas df from input sql table"""
    table = pd.read_sql_table(table_name, engine)
    return table

  def retrieve_pdf_data(self, link):
    """Returns pandas df from input pdf link"""
    df = tabula.read_pdf(link,pages='all')
    df = pd.concat(df)
    return df

  
  def list_number_of_stores(self, endpoint, headers):
    """Returns number of stores from link"""
    response = requests.get(endpoint, headers=headers)
    return response.text
  
  def retrieve_stores_data (self, endpoint, headers):
    """Returns data from link"""
    response = requests.get(endpoint, headers=headers)
    return response.text
  
  def extract_from_s3(self, address):
    """Downloads csv file from input AWS S3 link"""
    s3 = boto3.client('s3')
    path_parts = address.replace('s3://', '').split('/')
    bucket = path_parts[-2]
    object = path_parts[-1]
    s3.download_file(bucket, object, 'products.csv')

  def read_csv(self, file):
    """Input csv file to pandas df"""
    return pd.read_csv(file)
  
  def extract_json_from_s3(self, address):
    """Downloads json file from input AWS S3 link"""
    s3 = boto3.client('s3')
    path_parts = address.replace('https://', '').split('/')
    object = path_parts[-1]
    bucket = path_parts[0].split('.')[0]
    s3.download_file(bucket, object, 'date_details.json')

  def read_json(self, file):
    """Input json file to pandas df"""
    return pd.read_json(file)
  