import yaml
from sqlalchemy import create_engine

class DatabaseConnector:

  def read_db_creds(self, file):
    with open(file, 'r') as stream:
      try:
        data=yaml.safe_load(stream)
        return data
      except yaml.YAMLError as error:
        return error
      
  def init_db_engine(self, file):
    """Initialise and create database engine."""

    creds = self.read_db_creds(file)
    database = creds['database']
    DATABASE_TYPE = 'postgresql'
    DBAPI = 'psycopg2'
    HOST = database['RDS_HOST']
    USER = database['RDS_USER']
    PASSWORD = database['RDS_PASSWORD']
    DATABASE = database['RDS_DATABASE']
    PORT = database['RDS_PORT']
    engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
    return engine
  
  def upload_to_db(self, dataframe, table_name, file='my_db_creds.yaml'):
    """Uses engine method upload input data to database"""
    
    engine = self.init_db_engine(file)
    dataframe.to_sql(table_name, engine)

