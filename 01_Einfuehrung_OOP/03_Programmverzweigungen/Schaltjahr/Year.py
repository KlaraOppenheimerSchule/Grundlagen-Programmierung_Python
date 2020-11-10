class Year:

    def getYear(self):
        year = input('Bitte ein Jahr eingeben: \n')
        return year

    def validateYear(self, year):

        if year % 400 == 0:
            return 'Das eingegebene Jahr ist ein Schaltjahr'
        elif year % 4 == 0 & year / 4 % 100 != 0:
            return 'das Jahr ist ein Schaltjahr'
        else:
            return 'das Jahr ist kein Schaltjahr'
