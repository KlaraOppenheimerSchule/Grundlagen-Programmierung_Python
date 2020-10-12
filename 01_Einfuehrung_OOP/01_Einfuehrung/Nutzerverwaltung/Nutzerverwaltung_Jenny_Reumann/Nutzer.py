class Nutzer:
    def __init__(self, vorname, nachname):
        self.__vorname = vorname
        self.__nachname = nachname

    def getVorname(self):
        return self.__vorname

    def getNachname(self):
        return self.__nachname

    def setVorname(self, vorname):
        self.__vorname = vorname

    def setNachname(self, nachname):
        self.__nachname = nachname

    def ausgabe(self):
        return self.__vorname + " " + self.__nachname
