from typing import Type

class Animal:
    def __init__(self, *, name: str):
        self.name = name


class Cat(Animal):
    ...


class Dog(Animal):
    ...



def make_animal(animal_class: Type[Animal], name: str) -> Animal:
    return animal_class(name=name)


animal = make_animal(Dog, "Kevin")
