import abc

class Gewaesser(metaclass = abc.ABCMeta):
    def __init__(self, name, schiffbarkeit, schadstoff):
        self._name          = name
        self._schiffbarkeit = schiffbarkeit
        self._schadstoff    = schadstoff
        
    @abc.abstractmethod
    def get_verlauf(self):
        pass

class Meer(Gewaesser):
    def __init__(self, name, schiffbarkeit, schadstoff, flaeche):
        super().__init__(name, schiffbarkeit, schadstoff)
        self.__flaeche = flaeche

    def get_verlauf(self):
        return 0

class Fluss(Gewaesser):
    def __init__(self):
        pass

    def get_verlauf(self):
        self.__gesamtlaenge = self.__laenge
        if ( isinstance(self.__muendung, Fluss)):
            self.__gesamtlaenge = self.__gesamtlaenge + self.__muendung.get_verlauf()
        return self.__gesamtlaenge

nordsee = Meer("Nordsee", True, 800, 842000)
#elbe = Fluss("Elbe", True, 1094, 500, nordsee)
#moldau = Fluss("Moldau", True, 430, 700, elbe)
havel = Fluss
berounka = Fluss("Berounka", False, 138, 450, moldau)

print(berounka.get_verlauf())