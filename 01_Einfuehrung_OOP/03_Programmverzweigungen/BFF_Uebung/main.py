from Bff import *
import pyfiglet


def interface():
    print('1. Freunde anzeigen')
    print('2. Freund hinzufügen')
    print('3. Freund entfernen :(')

    action = input('Wählen Sie eine Aktion aus: ')

    if action == '1':
        print('Ihre aktuellen Freunde sind: ')
        bffs = newBff.getBff()
        for x in bffs:
            print(x)

    if action == '2':
        newFriend = input('Wie lautet der Name des Freundes der hinzugefügt werden soll?: ')
        bffs = newBff.getBff()
        bffs.append(newFriend)
        newBff.setBffs(bffs)

        print('Freund' + newFriend + 'wurde hinzugefügt!')

    if action == '3':
        print('Welchen Freund möchten Sie entfernen?: ')
        for x in newBff.getBff():
            print(x)

        target = input('Eingabe: ')

        bffs = newBff.getBff()
        bffs.remove(target)


welcomeMessage = pyfiglet.figlet_format("BFF Hub!!")
print(welcomeMessage)
newBff = Bff(['Jan', 'Lukas', 'Ruwn'])
interface()


print('Wollen Sie eine weitere Aktion ausführen?', end=' ')
answer = input('J/N')

if answer == 'J' or answer == 'j' or answer == 'Ja' or answer == 'ja':
    interface()
else:
    byemessage = pyfiglet.figlet_format('GoodBye!')
    print(byemessage)
    exit()


