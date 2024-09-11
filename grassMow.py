#Author: Kacper
#Date: Sept 2024
#Rectangular garden


gLength = float(input("How long is the garden in meters?: "))
gWidth = float(input("How wide is the garden in meters?: "))

hLength = float(input("How long is the house in meters?: "))
hWidth = float(input("How wide is the house in meters?: "))

gArea1 = gLength * gWidth
hArea = hLength * hWidth

gArea2 = gArea1 - hArea

print("Your garden is", gArea2, "meters squared")

time = round((gArea2 / 2 / 60) , 2)

print("It will take you", time, "minutes to mow your grass")

