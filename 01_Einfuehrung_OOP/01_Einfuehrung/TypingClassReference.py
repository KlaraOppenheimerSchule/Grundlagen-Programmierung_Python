from typing import Type

class Animal:
    def __init__(self, name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)

class Blume():
    ...

class PetOwner:
    def __init__(self, animal_class: Type[Animal]):
        self.__myAnimal=animal_class
    
    def getPetName(self)-> str:
        return self.__myAnimal.getName()

def checkTypeAnimal(animal_class: type[Animal]) ->bool:
    return True

wuffi=Dog("Paulchen")
kaetzchen=Cat("Maunzi")
#bluemchen=Blume()

christoph=PetOwner(wuffi)
print(christoph.getPetName())

#stefan=PetOwner(bluemchen)

#Hinweis:   Installiert man mypy (pip install mypy), kann man mit dem Konsolenbefehl mypy PfadZurDatei auch eine 
#           Typprüfung durchführen. Andernfalls sind es wirklich nur Type hints (also nur reine Hinweis für den Programmierer)
#           -> Das Problem ist jedoch, es erkennt den Typ bei der Vererbung nicht!
#           Das Beispiel baut auf folgender Quelle auf: https://adamj.eu/tech/2021/05/16/python-type-hints-return-class-not-instance/
