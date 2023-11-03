import sqlite3
import pandas as pd

# Load the data from CSV file
df = pd.read_csv('ea.csv', low_memory=False)

# Data Clean Up
df.columns = df.columns.str.strip()

# Create a connection tot the SQLite database
conn = sqlite3.connect('db.sqlite3')

# Load the data from csv file to sqlite database

df.to_sql('dashboard_extensionagents', conn, if_exists='append')

#close the connection
conn.close()