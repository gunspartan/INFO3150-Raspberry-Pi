import sqlite3

class DBController:
	def __init__(self):
		self.DB_NAME = "facial-recognition.db"
		self.db = sqlite3.connect(self.DB_NAME)
		self.cursor = self.db.cursor()
		self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
			(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, image TEXT NOT NULL, blacklisted INTEGER NOT NULL)''')
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