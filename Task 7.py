#Author: Kacper Trela
#Date: Sept 2024

#Task 7

# Ask the user for the principal
principal = input("Enter principal: ")
principal = float(principal)

# Ask the user for the interest rate
rate = input("Enter rate: ")
rate = float(rate)

# Ask the use the lenght of time
time = input("Enter time in years: ")
time = float(time)

# Simple interest calculation
amount = principal * rate * time

# Display the answer
print("The interest amount is", amount)

"""
The inputs are the amount of money in the account, the rate at which
they go up, how many years they are in the account

The output is all inputs multiplied by eachother

They will not be able to multiply by eachother because they are
automatically seen as a string
"""