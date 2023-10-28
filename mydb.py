import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = 'toor'
	)

# prepare a cursor project
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE dcrmDB")

print("All Done!")