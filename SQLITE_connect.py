import sqlite3
# connect to a database or create new database
connection  = sqlite3.connect ("test.db")
 
 # create a cursor object to execute command
cursor = connection.cursor()
cursor.execute(" CREATE TABLE IF NOT EXISTS task(id INTEGER PRIMARY KEY)")

 # Insert a row
cursor.execute("INSERT INTO task VALUES (1)")
connection.commit()
connection.close()

print("SQL LITE WORKING CORRECTLY")
