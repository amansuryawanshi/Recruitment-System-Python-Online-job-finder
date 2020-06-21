import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

db= MySQLdb.connect("hostname", "username", "password", "database_name")

cursor= db.cursor()

number_of_rows= cursor.execute("1SELECT * FROM Form.db") 

for i in range (number_of_rows):
      print (row[i])

