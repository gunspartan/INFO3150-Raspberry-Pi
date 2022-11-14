import sqlite3

class DBController:
	def __init__(self):
		self.DB_NAME = "facial-recognition.db"
		self.db = sqlite3.connect(self.DB_NAME)
		self.cursor = self.db.cursor()
		self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
			(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, image TEXT, blacklisted INTEGER)''')
		self.db.commit()

	def addUser(self, name, image, blacklisted = 0):
		self.cursor.execute('''INSERT INTO users (name, image, blacklisted) VALUES (?, ?, ?)''', (name, image, blacklisted))
		self.db.commit()
	
	def deleteUser(self, id):
		self.cursor.execute('''DELETE FROM users WHERE id = ?''', (id,))
		self.db.commit()

	def getUser(self, id):
		self.cursor.execute('''SELECT * FROM users WHERE id = ?''', (id,))
		return self.cursor.fetchone()

	def getAllUsers(self):
		self.cursor.execute('''SELECT * FROM users''')
		return self.cursor.fetchall()

	def setBlacklisted(self, id, blacklisted):
		self.cursor.execute('''UPDATE users SET blacklisted = ? WHERE id = ?''', (blacklisted, id))
		self.db.commit()

	def close(self):
		self.db.close()

# test
test = DBController()
test.addUser("test", "test.png", False)
test.addUser("test2", "test2.png", False)
test.addUser("test3", "test3.png", False)
test.addUser("test4", "test4.png", True)
test.addUser("test5", "test5.png", True)
test.addUser("test6", "test6.png", False)
for row in test.getAllUsers():
	print(row)