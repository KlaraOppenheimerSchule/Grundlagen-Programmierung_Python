from abc import ABC, abstractmethod


class Medium(ABC):

    # @abstractmethod
    # def do_something(self):
    #    pass

    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price

        super().__init__()

    def getIsbn(self):
        return self.isbn

    def setIsbn(self, isbn):
        self.isbn = isbn

        Python - Book


class Book (Medium):

    def __init__(self, isbn, title, author, price, edition):
        self.edition = edition
        super().__init__(isbn, title, author, price)

    def getEdition(self):
        return self.edition

    def setEdition(self, edition):
        if (edition > 0):
            self.edition = edition


class DVD (Medium):

    def __init__(self, isbn, title, author, price, size):
        self.size = size
        super: __init__(isbn, title, author, price)

    def getSize(self):
        return self.size

    def setEdition(self, size):
        if (size > 0 and size < 1000):
            self.size = size

            Python - Programm


medium1 = Medium(123345678, "Mäuschen", "Klaus", 20.4)
print(medium1.getIsbn())

book1 = Book("123456789", "1984", "George Orwell", 20.4, 1)
dvd1 = DVD("123456789", "1984", "George Orwell", 20.4, 650)

print(book1.getIsbn())
