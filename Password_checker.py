# Password strenght checker
# Author: Francesca
password = input("Type a password to check its strength: ")

if len(password) < 6:
    print("Password strenght: weak")
elif len(password) < 10:
    print("Password strenght: medium")
else:
    print("Password strenght: strong")
