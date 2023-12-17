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




Once data is uploaded to your own Postgresql database, \
run all the SQL files in Database_Schema_SQL to further clean the data, set correct data types, and set primary and foreign keys. \
The file names describe their function.

Once the database is set up, you can start querying the data to gather some insights. \
There is a folder named Database_Query_SQL with 9 task SQL files. \
These contain some example queries. Each file starts with a comment describing the question the query answers.


