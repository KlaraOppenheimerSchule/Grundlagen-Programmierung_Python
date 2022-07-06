from typing import Type

class Animal:
    def __init__(self, *, name: str):
        self.__name = name
    
    def getName(self) -> str:
        return self.__name


class Cat(Animal):
    ...


class Dog(Animal):
    ...


class Blume:
    def __init__(self, *, name: str):
        self.__name = name


class PetOwner:
    def __init__(self, animal_class: Type[Animal]):
        self.__myAnimal=animal_class
    
    def getPetName(self)-> str:
        return self.__myAnimal.getName()

def make_animal(animal_class: Type[Animal], name: str) -> Animal:
       return animal_class(name=name)


wuffi=make_animal(Dog, "Paulchen")
kaetzchen=make_animal(Cat,"Maunzi")

#Soll Fehler bei mypy-Prüfung erzeugen
narzisse=make_animal(Blume, "Narzischen")

christoph=PetOwner(wuffi)

print(wuffi.getName())
