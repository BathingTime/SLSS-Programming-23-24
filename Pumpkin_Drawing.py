# Pumpkin Drawing
# Sunny Lin
# Oct 31, 23

import turtle
import random

screen=turtle.Screen()
screen.bgcolor("black")

# # Whole pumpkin
# pumpkin=turtle.Turtle()
# pumpkin.ht()
# pumpkin.color("orange")
# pumpkin.dot(200)

# # The turtle to "carve" the pumpkin
# carver=turtle.Turtle()

# # "Flatten" the lower part of the pumpkin
# carver.pu()
# carver.setpos(-200,-100)
# carver.pensize(60)
# carver.pd()
# carver.forward(600)
# carver.pensize(2)

# # Nose
# carver.pu()
# carver.setpos(0,0)
# carver.dot(10)
# carver.forward(15)

# screen.mainloop()

turtle.speed(0)

# while True:
#     turtle.color(random.random(),random.random(),random.random())
#     turtle.pu()
#     turtle.goto(random.randint(-screen.window_width()//2,screen.window_width()//2),random.randint(-screen.window_height()//2,screen.window_height()//2))
#     turtle.right(random.randint(1,360))
#     turtle.pensize(random.randint(1,100))
#     turtle.pd()
#     turtle.circle(random.randint(1,500))

# turtle.color('white')
# num=1
# direction1=0
# direction2=0
# while True:
#     turtle.forward(num)
#     turtle.pu()
#     turtle.backward(num)
#     direction1=(direction1+num)%360
#     turtle.seth(direction1)
#     turtle.pd()
#     turtle.forward(num)
#     turtle.seth(direction1)
#     num+=1
#     direction2+=1

turtle.color('white')
num=1
while True:
    turtle.forward(50)
    turtle.left(num)
    num+=1