import yaml
from sqlalchemy import create_engine, URL

class DatabaseConnector:

  def __init__(self):
    pass

  def read_db_creds(self, file):
    with open(file, 'r') as stream:
      try:
        d=yaml.safe_load(stream)
        return d
      except yaml.YAMLError as e:
        return e
      
  def init_db_engine(self, file):
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
  
  def upload_to_db(self, dataframe, table_name):
    DATABASE_TYPE = 'postgresql'
    DBAPI = 'psycopg2'
    HOST = 'localhost'
    USER = 'postgres'
    PASSWORD = '1M45t01d7'
    DATABASE = 'sales_data'
    PORT = 5432
    engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
    dataframe.to_sql(table_name, engine)

