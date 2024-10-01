# Author: Kacper Trela
# Date: Sep 2024
# HW Task 7-9 and PG 43 Task 3


# Task 7
# userList =[]
# userName = input("Enter your full name: ")
# userList.append(userName)
# userAge = int(input("Enter your age: "))
# userList.append(userAge)
# userCountry = input("What is your country of birth: ")
# userList.append(userCountry)
# userDate = input("Enter your date of birth (dd/mm/yyyy): ")
# userList.append(userDate)
# 
# 
# print("My database for "+userName+"\n"+str(userList))
# 
# userList.reverse()

# print("My database for "+userName+"\n"+str(userList))

# Task 8
# pangram = ['The','five','boxing','wizards','jump','quickly']
# print(pangram)
# 
# # quickly jump wizards boxing five the
# pangram.reverse()
# print(pangram[0:2],end='')
# print(pangram[5:],end='')
# print(pangram[4:5],end='')
# print(pangram[3:4],end='')
# print(pangram[2:3])

# Task 9
import random as R

fruitFile = open("fruits.txt","r")

fileContents = fruitFile.read()

fruitFile.close()

fruits = fileContents.split()

print(R.choice(fruits))
print(R.choice(fruits))
print(R.choice(fruits))







