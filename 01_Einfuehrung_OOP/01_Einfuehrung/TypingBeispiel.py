from pyexpat import version_info
import typing

def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting("Bianca"))
print(greeting(23))


#Typeanalysetool installieren, dann findet die Typprüfung vor Ausführung statt
#pip install mypy
