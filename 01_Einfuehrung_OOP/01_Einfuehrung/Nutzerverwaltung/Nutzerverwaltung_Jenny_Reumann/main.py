from Nutzer import *

# version 1
# print("Bitte tragen sie die Daten des zu erzeugenden Mitarbeiter ein.\n")
# vorname = input("Vorname: ")
# nachname = input("Nachname: ")
# mitarbeiter = Mitarbeiter(vorname, nachname)
# print("Nummer " + str(x) + ":  " + mitarbeiter.getVorname() + " " + mitarbeiter.getNachname())


# version 2

list = []


def add():
    print("Bitte tragen sie die Daten des zu erzeugenden Mitarbeiter ein.\n")
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    mitarbeiter = Nutzer(vorname, nachname)
    list.append(mitarbeiter)
    print("Mitarbeiter erfolgreich erstellt! \n")


def listAusgabe():
    x = 0
    print("Ihre Mitarbeiter: \n")
    for obj in list:
        x = x + 1
        print("Nummer " + str(x) + ":  " + obj.ausgabe())


#def switch(option):
#    switcher = {
#        '1': add,
#        #1: "test1",
#        '2': listAusgabe,
#        #2: "test2",
#        '3': exit
#        #3: "test3"
#    }
#    return switcher.get(option, "Invalid Number")


#switch = {'1':add}

def choices(option):
    if option == "1":
        add();
    elif option == "2":
        listAusgabe();
    elif option == "3":
        print("Wird beendet.\n")
        exit();
    else:
        print("Ungültige Eingabe!\n");



while True:
    print("Willkommen!")
    print("Bitte wähle eine der Optione aus.")
    print("1 - Mitarbeiter hinzufügen")
    print("2 - Alle Mitarbeiter ausgeben")
    print("3 - Beenden\n")
    option = input("Ihre Eingabe: ")
    print("\n")
    choices(option)

#   switch(option)
