import pyodbc
import pandas as pd

cnx_string = "Driver={ODBC Driver 17 for SQL Server};Server=sql\EXPRESS,1433;Database=master;UID=myUsername;PWD=MyPass@word;"
cnx = pyodbc.connect(cnx_string)

query = "SELECT TOP(10) * FROM INFORMATION_SCHEMA.TABLES"

print(pd.read_sql(query, cnx))
