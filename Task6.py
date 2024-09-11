#Author: Kacper Trela
#Date: Sept 2024



#TASK 6
centigrade = float(input("Enter the Celcius value: "))
fahrenheit = 9/5 * centigrade + 32
print(centigrade, "degrees C =", fahrenheit, "degrees F")


"""
0,32,32
32,89.6,89.6
1000,1832.0,1832.0
-10,14.0,14.0
-40,-40.0,-40
-1000,-1768.0,-1768.0

It varifies it works becuase the outputs are the same
if you put a string it will not work because it has to be a float in order to print
"""