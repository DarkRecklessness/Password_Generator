def passcheck(password, usebigsymbol, usenumbers, usespecsymbols):
    flag1 = False
    flag2 = True
    flag3 = True
    flag4 = True
    if usebigsymbol == "y":
        flag2 = False
    if usenumbers == "y":
        flag3 = False
    if usespecsymbols == "y":
        flag4 = False
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i in password:
            flag1 = True
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if i in password:
            flag2 = True
    for i in "1234567890":
        if i in password:
            flag3 = True
    for i in "+-/*!&$#?=@<>":
        if i in password:
            flag4 = True
    if flag1 == True and flag2 == True and flag3 == True and flag4 == True:
        return False
    else:
        return True

import random

line_count = sum(1 for line in open('passwords.txt'))

symbol = "abcdefghijklmnopqrstuvwxyz"
lenp = int(input("Password length: "))
usebigsymbol = input("Use big symbol? y / n: ")
usenumbers = input("Use numbers? y / n: ")
usespecsymbols = input("Use specsymbols? y / n: ")
if usebigsymbol == "y":
    symbol += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if usenumbers == "y":
    symbol += "1234567890"
if usespecsymbols == "y":
    symbol += "+-/*!&$#?=@<>"
platform = input("Platform: ")
login = input("Login: ")

file = open("passwords.txt", "a")

password = ""
while passcheck(password, usebigsymbol, usenumbers, usespecsymbols):
    password = ""
    for j in range(lenp):
        password += random.choice(symbol)
print(password)
if line_count != 0:
    file.write("\n")
    file.write("\n")
file.write("Platform: " + platform + "\n")
file.write("Login: " + login + "\n")
file.write("Password: " + password)
file.close()
