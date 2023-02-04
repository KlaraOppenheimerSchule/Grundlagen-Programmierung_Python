from typing import Type

class Animal:
    def __init__(self, name: str):
        self._name = name
    
    def getName(self) -> str:
        return self._name


class Cat(Animal):
     def __init__(self, name: str):
        super().__init__(name)


class Dog(Animal):
     def __init__(self, name: str):
        super().__init__(name)
    

class Blume:
    def __init__(self, *, name: str):
        self.__name = name


class PetOwner:
    def __init__(self, animal_class: Type[Animal]):
        self.__myAnimal=animal_class
    
    def getPetName(self)-> str:
        return self.__myAnimal.getName()

#def make_animal(animal_class: Type[Animal], name: str) -> Animal:
    #   return animal_class(name=name)


#wuffi=make_animal(Dog, "Paulchen")
wuffi2=Dog("Hundi")
#kaetzchen=make_animal(Cat,"Maunzi")

#Soll Fehler bei mypy-Prüfung erzeugen
#narzisse=make_animal(Blume, "Narzischen")

christoph=PetOwner(wuffi2)

print(wuffi2.getName())
