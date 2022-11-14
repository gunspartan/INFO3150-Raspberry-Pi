import sqlite3

DB_NAME = "facial-recognition.db"

# connection
conn = sqlite3.connect(DB_NAME)
curs = conn.cursor()

for row in curs.execute("SELECT * FROM users"):
	print(row)

conn.close()
