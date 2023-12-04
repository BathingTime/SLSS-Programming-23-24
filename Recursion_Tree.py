# Recursion Tree
# Sunny Lin
# Dec 4, 23

import turtle

# CONSTS:
ANGLE=30
FACTOR=.9
START=100

level=int(input('What level is the tree: '))

screen=turtle.Screen()

def leaf():
    # Draw two leaves.
    turtle.left(90)
    turtle.color('green')
    turtle.stamp()
    turtle.left(180)
    turtle.stamp()
    turtle.color('brown')
    turtle.left(90)

def grow(togo,length):
    if togo:
        turtle.forward(length)
        if togo-1:
            turtle.left(ANGLE)
            grow(togo-1,length*FACTOR)
            turtle.right(ANGLE*2)
            grow(togo-1,length*FACTOR)
            turtle.left(ANGLE)
        else:
            leaf()
        turtle.backward(length)
    else:
        leaf()

turtle.speed(0)
turtle.color('brown')
turtle.width(2)
turtle.left(90)

grow(level,START)

screen.mainloop()