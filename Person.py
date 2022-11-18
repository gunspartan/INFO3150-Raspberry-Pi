from DBController import DBController

class Person:
  def __init__(self, userId, name, image, blacklisted):
    self.userId = userId
    self.name = name
    self.image = image
    self.blacklisted = blacklisted

  def getName(self):
    return self.name

  def setName(self, newName):
    self.name = newName

  def getImage(self):
    return self.image

  def setImage(self, newImage):
    self.image = newImage

  def getBlacklisted(self):
    return self.blacklisted

  def setBlacklisted(self, newBlacklisted):
    self.blacklisted = newBlacklisted

  def readInfo(self):
    print("\nName of Person: " + self.name +
          "\nImage Path: " + self.image +
          "\nBlacklist Status: " + str(self.blacklisted) +
          '\n')

  def addToDB(self):
    database = DBController()
    database.addUser(self.name, self.image, self.blacklisted)
    database.close()