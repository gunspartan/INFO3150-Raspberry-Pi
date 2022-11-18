from DBController import DBController

db = DBController()

db.addUser("Barack Obama", "img/obama.jpg", True)
db.addUser("Joe Biden", "img/biden.jpg", False)

db.close()
