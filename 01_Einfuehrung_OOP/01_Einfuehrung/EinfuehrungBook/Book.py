class Book:
    def __init__(self, isbn, title, author, price):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__price = price

    def getIsbn(self):
        return self.__isbn

    def setIsbn(self, isbn):
        self.__isbn = isbn


buch = Book("123456789", "1984", "George Orwell", 20.6)
print(buch.getIsbn())
