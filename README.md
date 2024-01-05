# Multinational Retail Data Centralisation

## Overview:
This project is intended for a multinational company that sells various goods across the globe.
Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.
In an effort to become more data-driven, the organisation would like to make its sales data accessible from one centralised location.
The first goal will be to produce a system that stores the current company data in a database so that it can be accessed from one centralised location and acts as a single source of truth for sales data.
The database will then be queried to get up-to-date metrics for the business.

## Project Info:
- Technologies: Python, APIs, PostgreSQL, Pgadmin4, Pandas, AWS RDS
- Developed a system that extracts retail sales data from different data sources: PDF documents, an AWS RDS database, RESTful API, JSON, and CSV files.
- Thoroughly processed and cleansed a substantial volume of 100k+ records, preparing the data for modeling within a star-based database schema.
- Conducted in-depth analysis of the processed data, unveiling valuable insights relevant to the retail industry for enhancing business operations and decision-making processes. 

## Instructions:

- Clone repository to a directory of choice:
```bash
git clone https://github.com/drrohitpawar/multinational-retail-data-centralisation.git
```
- Install required python packages:
```bash
pip install -r requirements.txt
```
- Ensure to populate "my_db_creds.yaml" with your target database credentials.
- Ensure java is installed on your local machine (needed for certain packages)
- Run main.py
```bash
python main.py
```
- This will retrieve the data from various sources, clean it, and upload it to your database. This will take some time.
- Now that the data is cleaned and uploaded, run all the SQL files in Database_Schema_SQL to further clean the data, set correct data types, and set primary and foreign keys.
- The file names describe their function.


- Once the database is set up, you can start querying the data to gather some insights. 
- There is a folder named Database_Query_SQL with 9 task SQL files. 
- These contain some example queries. Each file starts with a comment describing the question the query answers.

## Project Structure

- DatabaseConnector - in database_utils.py - contains all methods necessary for connecting and uploading to SQL databases
- DataExtractor - in data_extraction.py - contains all methods necessary for retrieving data from various sources
- DataCleaning - data_cleaning.py - contains all methods necessary for cleaning individual pandas DataFrames

## Tools Used

### SQL Alchemy

SQLAlchemy was used to connect to both the AWS and local SQL databases. In database_utils.py:
```bash
from sqlalchemy import create_engine
```
```bash
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
HOST = database['RDS_HOST']
USER = database['RDS_USER']
PASSWORD = database['RDS_PASSWORD']
DATABASE = database['RDS_DATABASE']
PORT = database['RDS_PORT']
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
```
Credentials were read from a yaml file.

### Tabula

Tabula is a simple tool for reading tables from pdf files and converting them to a pandas DataFrame or CSV/TSV/JSON file. It was utilized here to extract the card details data frame from a PDF link.
```bash
def retrieve_pdf_data(self, link):
  """Returns pandas df from input pdf link"""
  df = tabula.read_pdf(link,pages='all')
  df = pd.concat(df)
  return df
```
### Boto3

Boto3 python package was used to download both a json and csv file from an AWS S3 storage bucket. These files were later read as pandas dataframes.
```bash
def extract_from_s3(self, address):
  """Downloads csv file from input AWS S3 link"""
  s3 = boto3.client('s3')
  path_parts = address.replace('s3://', '').split('/')
  bucket = path_parts[-2]
  object = path_parts[-1]
  s3.download_file(bucket, object, 'products.csv')
```
### Requests

In order to connect to API endpoints, Requests was used to make HTTPS GET requests.

```bash
def retrieve_stores_data (self, endpoint, headers):
  """Returns data from link"""
  response = requests.get(endpoint, headers=headers)
  return response.text
```

### Pandas

Pandas is a powerful and widely-used Python library for data manipulation and analysis. It provides data structures, such as DataFrames and Series, that allow you to easily handle and manipulate structured data. It was used extensively in this project to read data from different formats and to clean data in DataCleaner.

```bash
def read_csv(self, file):
  """Input csv file to pandas df"""
  return pd.read_csv(file)
    
def read_json(self, file):
  """Input json file to pandas df"""
  return pd.read_json(file)
```

### Subprocesses

A separate individual Python file was created to extract and clean each table from their respective locations. A Python package named subprocesses was utilized in main.py to run all the files once main.py was run.

```bash
import subprocess

#list of files in the data folder
file_list = ['card_data.py', 'event_data.py', 'orders_data.py', 'products_data.py', 'store_data.py', 'users_data.py']
 
if __name__ == '__main__':
  #run all the files in the data column
  for file in file_list:
    subprocess.run(['python', 'scripts/' + file])
```

## Local Database Setup

For this project, I set up a Postgresql server hosted on my local machine using pgadmin4
Download link: https://www.pgadmin.org/download/

- Download PgAdmin4
- Run through the installation process
- Launch PgAdmin4
- Click on 'Add New Server'
- Once set up, click on properties to see database credentials.
- These credentials can be added to 'my_db_cred.yaml'



