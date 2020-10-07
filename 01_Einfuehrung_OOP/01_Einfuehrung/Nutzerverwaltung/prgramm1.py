infisrtname = input("Vorname")
insecondname = input("Nachname")

class user:

    def __init__(self):
        self.__firstname = infisrtname
        self.__secondname = insecondname
    def getFirstname(self):
        return self.__firstname
    def getSecondname(self):
        return self.__secondname
    def setFirstname(self, eing):
        self.__firstname = eing
    def setSecondname(self, eing):
        self.__secondname = eing

NewUser = user()

NewUser.setFirstname(infisrtname)
NewUser.setSecondname(insecondname)

print(NewUser.getFirstname(), NewUser.getSecondname())