# Author: Kacper Trela
# Date: Oct 2024
# Boolean HW

#Task 2
"""
1 and 0
0 or 0
1 and 0
0 or 1
0 or 1
"""

#Task 4
import random

number = random.randint(1,10)

guess = int(input("Pick a number from 1 to 10: "))

if guess == number:
    print("Well done! You win!")
elif guess != number:
    print("You lost!")

print("Goodbye!")
