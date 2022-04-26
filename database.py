

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CSMS"
)

mycursor = mydb.cursor()

if mydb.is_connected():
  print('connected with the database')
else:
  print('Eror in connecting with database!')


mycursor.execute("CREATE TABLE node1 (temperature FLOAT(255), humidity FLOAT(255) time DATETIME(255))")
