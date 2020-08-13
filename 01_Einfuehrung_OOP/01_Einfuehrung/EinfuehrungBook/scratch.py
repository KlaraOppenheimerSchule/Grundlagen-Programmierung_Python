
import os
a = "C:/Users/X230t/Documents/Meine Unterlagen/Informatik/Programmieren Powershell"
print(os.listdir(a))
print(type(a))

a = 10

if a > 10:
    print(str(a) + " is larger than 10")
else:
    print(str(a) + " is less than or equal to 10")


if a > 10:
    print(str(a) + " is larger than 10")
elif a > 5:
    print(str(a) + " is larger than 5")
