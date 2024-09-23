#Author: Kacper Trela
#Date: Sept 2024
# HW Turtle

import turtle
turtle.showturtle()
turtle.shape("turtle")
turtle.speed(100)
for i in range(0,90):
    turtle.backward(1)
    turtle.left(1)
for i in range(0,180):
    turtle.forward(1)
    turtle.right(1)
turtle.right(90)
turtle.forward(120)

turtle.exitonclick()
    
    


