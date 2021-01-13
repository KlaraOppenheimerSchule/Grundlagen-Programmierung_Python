def morseTabelle():
    array = [
        ["A", "._"],
        ["B", "_..."],
        ["C", "_._."],
        ["D", "_.."],
        ["E", "."],
        ["F", ".._."],
        ["G", "__."],
        ["H", "...."],
        ["I", ".."],
        ["J", ".___"],
        ["K", "_._"],
        ["L", "._.."],
        ["M", "__"],
        ["N", "_."],
        ["O", "___"],
        ["P", ".__."],
        ["Q", "__._"],
        ["R", "._."],
        ["S", "..."],
        ["T", "_"],
        ["U", ".._"],
        ["V", "..._"],
        ["W", ".__"],
        ["X", "_.._"],
        ["Y", "_.__"],
        ["Z", "__.."],
        ["1", ".____"],
        ["2", "..___"],
        ["3", "...__"],
        ["4", "...._"],
        ["5", "....."],
        ["6", "_...."],
        ["7", "__..."],
        ["8", "___.."],
        ["9", "____."],
        ["0", "_____"],
        [".", "._._._"],
        [",", "__.__"],
        ["?", "..__.."],
        [":", "___..."],
        [";", "_._._."],
        [" ", "_..._"],
        ["/", "_.._."],
        ['"', "._.._."]
    ]
    return array


def morsen(string):
    code = morseTabelle()
    translation = ""

    for i, s in enumerate(string):
        flag = False
        for c in code:
            if c[0] == s.upper():
                flag = True
                translation = translation + "|" + c[1]
        if not flag:
            translation = translation + "|" + s

    return translation


def main():
    print("Willkommen zum Morsecodierer!")
    print("Bitte geben sie ein was kodiert werden soll!")
    string = input("Ihre Eingabe: ")
    translation = morsen(string)
    print("Übersetzung: ")
    print(translation)


main()