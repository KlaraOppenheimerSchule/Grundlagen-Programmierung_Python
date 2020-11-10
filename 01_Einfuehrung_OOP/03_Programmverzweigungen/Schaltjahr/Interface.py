# coding=<utf-8>

from Year import Year


class Interface:

    def __init__(self):
        self.__year = Year()

    def projectInterface(self):

        print('########################################################################')
        print('############################## Year Validator ##########################')
        print('########################################################################')

        print(self.__year.validateYear(self.__year.getYear()))

        print('Weiteres Jahr ueberpruefen? \n')

        answer = input('J/N')

        if answer == "J" or answer == "j" or answer == "yes":
            self.projectInterface()
        elif answer == 'N' or answer == 'n' or answer == 'no':
            exit()
