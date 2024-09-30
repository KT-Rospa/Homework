# Author: Kacper Trela
# Date: Sept 2024
# Lists HW 30/9/24

#Task 1:
"""
Line 5 creates a list called fruit and adds the elements to them.

Lines 8,9,10 select a random index from 0 to 4, 3 times to pick a rnadom fruit.

Lines 13,14,15 prints the random fruit.

Predicition: The output will be 3 random fruits from the list. As it picks the random fruit 3 times and prints it.

choice( ) Returns a random element from the given sequence. This could be used instead of random.randint(0,4)
"""

# import random
# 
# fruits = ['Strawberry', 'Lemon', 'Orange', 'Raspberry', 'Cherry']
# 
# selection1 = random.randint(0,4)
# selection2 = random.randint(0,4)
# selection3 = random.randint(0,4)
# 
# print(fruits[selection1])
# print(fruits[selection2])
# print(fruits[selection3])

#Task 2:

"""
I think the program will firstly print Strawberry, Lemon, Orange, Raspberry, Cherry

It will then print Apple, Melon, Raspberry, Cherry, Pineapple

"""
# fruits = ['Strawberry', 'Lemon', 'Orange', 'Raspberry', 'Cherry']
# print(fruits)
# 
# fruits[0] = 'Apple'
# fruit = 'Melon'
# fruits[1] = fruit
# fruits[2] = 'Raspberry'
# fruits[3] = fruits[4]
# fruits[4] = 'Pineapple'
# 
# print(fruits)

#Task 3

"""
It prints the elemets from index 1 to 2
It prints the elemets from index 2 to 3
It prints the elemets from index 2 to 4

It prints the elemets from index from 1 onwards
It prints the elemets from index from the start to 5


print(fruits[0:2])

The whole list would print: ['apple', 'pear', 'orange', 'banana', 'kiwi']
"""

#Task 4

"""
Prediction:						Actual:
Strawberry						Strawberry
Raspberry						Raspberry
Orange							Orange
4								Cherry
Lemon							Lemon
Cherry							Cherry
C								C
Lemon							Lemon
Lemon							Lemon



"""
fruits = ['Strawberry', 'Lemon', 'Orange', 'Raspberry', 'Cherry']

print (fruits [0])
print (fruits [3])
print (fruits [2])
print (fruits [len (fruits) -1])
print (fruits [1])

fruit = fruits [2+2]

print (fruit)
print (fruit [0])

orange = fruits [1]
print (orange)
lemon = fruits [1]
print (lemon)