import abc

class Gewässer(metaclass=abc.ABCMeta):
    def __init__(self, name, schiffbarkeit, schadstoffbelastung):
        self.name = name
        self.schiffbarkeit = schiffbarkeit
        self.schadstoffbelastung = schadstoffbelastung

        def getName(self):
            return self.name

        def setName(self, name):
            self.name = name

        def getSchadstoffbelastung(self):
            return self.schadstoffbelastung

        def setSchadstoffbelastung(self, schadstoffbelastung):
            self.schadstoffbelastung = schadstoffbelastung

        def getSchiffbarkeit(self):
            return self.schadstoffbelastung

        def setSchiffbarkeit(self, schadstoffbelastung):
            return self.schadstoffbelastung

        @abc.abstractmethod
        def getVerlauf(self):
            pass


class Meer(Gewässer):
    def __init__(self, name, schiffbarkeit, schadstoffbelastung, flaeche):
        super().__init__(name, schiffbarkeit, schadstoffbelastung)
        self.flaeche = flaeche

    def getFlache(self):
        return self.name

    def setFlache(self, name):
        self.name = name

    def getVerlauf(self):
        return 0


class Fluss(Gewässer):
    def __init__(self, name, schiffbarkeit, schadstoffbelastung, laenge, muendung):
        super().__init__(name, schiffbarkeit, schadstoffbelastung)
        self.laenge = laenge
        self.muendung = muendung

    def getLange(self):
        return self.laenge

    def setLange(self, laenge):
        self.laenge = laenge

    def getMundung(self):
        return self.muendung

    def setMundung(self, muendung):
        self.muendung = muendung

    def getVerlauf(self):
        self.meineLaenge = self.laenge
        if (isinstance(self.muendung, Fluss)):
            self.meineLaenge = self.meineLaenge + self.muendung.getVerlauf()
        return self.meineLaenge


nordsee = Meer("Nordsee", True, 800, 842000)
elbe = Fluss("Elbe", True, 1094, 500, nordsee)
moldau = Fluss("Moldau", True, 430, 700, elbe)
havel = Fluss("Havel", True, 334, 870, elbe)
berounka = Fluss("Berounka", False, 138, 450, moldau)

print(berounka.getVerlauf())
print(nordsee.getVerlauf())
