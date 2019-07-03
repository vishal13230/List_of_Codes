import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-3J42FK3\SQLEXPRESS;'
                      'Database=AdventureWorks;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM Production.Product')

dt = pd.DataFrame(cursor)



for row in cursor:
    print(row)