# Author: Kacper Trela
# Date: Nov 2024
# Hex to Decimal

num = input("Enter a hexidecimal number: ").upper()

numList = list(num)
numList.reverse()

num1 = numList.pop(0)
num2 = numList.pop(0)
num3 = numList.pop(0)

if num1 == "A":
    num1 = 10
elif num1 == "B":
    num1 = 11
elif num1 == "C":
    num1 = 12
elif num1 == "D":
    num1 = 13
elif num1 == "E":
    num1 = 14
elif num1 == "F":
    num1 = 15
else:
    num1 = int(num1)

if num2 == "A":
    num2 = 10
elif num2 == "B":
    num2 = 11
elif num2 == "C":
    num2 = 12
elif num2 == "D":
    num2 = 13
elif num2 == "E":
    num2 = 14
elif num2 == "F":
    num2 = 15
else:
    num2 = int(num2)
    
if num3 == "A":
    num3 = 10
elif num3 == "B":
    num3 = 11
elif num3 == "C":
    num3 = 12
elif num3 == "D":
    num3 = 13
elif num3 == "E":
    num3 = 14
elif num3 == "F":
    num3 = 15
else:
    num3 = int(num3)




hex1 = (int(num1 * 16**0))
hex2 = (int(num2 * 16**1))
hex3 = (int(num3 * 16**2))

hexSum = hex1 + hex2 + hex3

print(hexSum)