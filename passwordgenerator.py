import random

symbol = "abcdefghijklmnopqrstuvwxyz"
num = int(input("Number of passwords: "))
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

for i in range(num):
    password = ""
    for j in range(lenp):
        password += random.choice(symbol)
    print(password)

