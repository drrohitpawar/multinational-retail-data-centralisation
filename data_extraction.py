from sqlalchemy import create_engine, URL, inspect
import database_utils
import pandas as pd
import tabula

class DataExtractor:
  def __init__(self, engine):
    self.engine = engine
  
  def list_db_tables(self):
    inspector = inspect(self.engine)
    return inspector.get_table_names()
  
  def read_rds_table(self, table_name):
    table = pd.read_sql_table(table_name, self.engine)
    return table

  def retrieve_pdf_data(self, link):
    df = tabula.read_pdf(link, stream=True, pages='all')
    return df
