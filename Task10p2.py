#Author: Kacper Trela
#Date: Sept 2024

# Program to avergae 5 randomly generated numbers
import random

low = random.randint(1,100)
high = random.randint(low,100)

# Generate 5 random numbers between low and high

n1 = random.randint(low,high)
n2 = random.randint(low,high)
n3 = random.randint(low,high)
n4 = random.randint(low,high)
n5 = random.randint(low,high)

# Compute their average
average = (n1+n2+n3+n4+n5)/5

# Add the 5 numbers and display the result
print("The average of", n1, n2, n3, n4, n5, "is", average)