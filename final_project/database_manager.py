import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='dont1know',
    database='players_db'
)

mycursor = mydb.cursor()
mycursor.execute('CREATE TABLE images (id INTEGER(2), pic BLOB NOT NULL)')
