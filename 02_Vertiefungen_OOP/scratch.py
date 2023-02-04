class Testklasse:

    def __init__(self):
        pass

    def fahre(self):
        print("Tut tut")


class TestklasseFac:

    def __init__(self):
        pass

    def baue(self):
        return Testklasse()


neueTestklasseFac= TestklasseFac()
neueTestklasse= neueTestklasseFac.baue()
neueTestklasse.fahre()