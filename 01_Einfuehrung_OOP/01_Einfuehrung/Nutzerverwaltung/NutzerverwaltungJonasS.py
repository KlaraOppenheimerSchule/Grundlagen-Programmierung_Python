class User:
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName
print("##############################################################")
print("######################### neuer User #########################")
print("##############################################################")

name = input("Vorname eingeben: ")
lastName = input("Nachname eingeben: ")

newUser = User(name,lastName)

print("der volle Name des Users lautet: " + newUser.getFirstName() + " " + newUser.getLastName())