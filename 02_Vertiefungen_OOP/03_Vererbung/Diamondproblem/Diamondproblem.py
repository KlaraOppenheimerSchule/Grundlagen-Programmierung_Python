class Fahrzeug():
    def __init__(self, anzahlSitze, hoechstGeschwindigkeit):
        self.anzahlSitze = anzahlSitze
        self.hoechstGeschwindigkeit = hoechstGeschwindigkeit


class Wasserfahrzeug(Fahrzeug):
    def __init__(self, anzahlSitze, hoechstGeschwindigkeit):
        super().__init__(anzahlSitze, 60)

    def fortbewegen(self):
        print("Bewege mich wie ein Wasserfahrzeug")


class Landfahrzeug(Fahrzeug):
    def __init__(self, anzahlSitze, hoechstGeschwindigkeit):
        super().__init__(anzahlSitze, 180)

    def fortbewegen(self):
        print("Bewege mich wie ein Landfahrzeug")


class Amphibienfahrzeug(Landfahrzeug, Wasserfahrzeug):
    pass


beispiel = Amphibienfahrzeug(5, 300)
beispiel.fortbewegen()
print(beispiel.hoechstGeschwindigkeit)

mro_str = '\n'.join(repr(cls) for cls in Amphibienfahrzeug.mro())
print(mro_str)
