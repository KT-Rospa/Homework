
# Author: Kacper Trela
# Date: Nov 2024
# Hex to Decimal

num = input("Enter a hexidecimal number: ").upper()

numList = list(num)
numList.reverse()
numListDec = []
counter = 0
numLength = len(numList)



while counter < numLength:
    if num[counter] == "A":
        numListDec.append(10)
    elif num[counter] == "B":
        numListDec.append(11)
    elif num[counter] == "C":
        numListDec.append(12)
    elif num[counter] == "D":
        numListDec.append(13)
    elif num[counter] == "E":
        numListDec.append(14)
    elif num[counter] == "F":
        numListDec.append(15)
    else:
        numListDec.append(int(num[counter]))
    counter += 1

counter2 = 0
total = 0

numListDec.reverse()

while counter2 < numLength:
    total += (numListDec[counter2]*(16**counter2))
    counter2 += 1

print("The decimal value of",num,"is",total)


counter3 = 0
decList = []
num2= total

while num2 != 0:
    rem = num2 % 2
    decList.append(rem)
    num2 = num2 // 2
    
decList.reverse()

print(num," to binary is ", *decList, sep = '')
    
    
        

