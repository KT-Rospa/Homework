# Author: Kacper Trela
# Task 1 - 2 pg 30 HW

# Task 1
# input picks the two numbers
# num1 = int(input("Pick a number:"))
# num2 = int(input("Pick another number:"))
# 
# # gets the modulus of num1 and num2
# num3 = num1 % num2
# 
# # checks if num3 is less then or equal to 0 if so it will print that they do divide evenly, elif if the number is bigger than 0 it will print that they do not divide into eachother
# if num3 <= 0:
#     print(num2,"DOES evenly divide into",num1)
# elif num3 > 0:
#     print(num2,"does NOT evenly divide into",num1)

    
# Task 2
age = int(input("Enter your age:"))

if age >= 17:
    print("You ARE eligible for an Irish Drivers Licence")
elif age < 17:
    print("You are NOT eligible for an Irish Drivers Licence")