from DBController import DBController
from Person import Person
db = DBController()

users = db.getAllUsers()
people = []
for row in users:
	person = Person(row[1], row[2], row[3])
	print(person.getName())
	print(person.getImage())
	print(person.getBlacklisted())
	people.append(person)



db.close()
