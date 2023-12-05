# Recursion Tree
# Sunny Lin
# Dec 4, 23

import turtle

# CONSTS:
ANGLE=60
BRANCHES=3
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
    # If there are more levels to go:
    if togo:
        # Make a new branch.
        turtle.forward(length)
        # If the next level has more levels to go:
        if togo-1:
            # Turn left for the first branch.
            turtle.left(ANGLE/2)
            grow(togo-1,length*FACTOR)
            # Make BRANCH-1 more branches.
            for _ in range(BRANCHES-1):
                turtle.right(ANGLE/(BRANCHES-1))
                grow(togo-1,length*FACTOR)
            # Return to the original angle.
            turtle.left(ANGLE/2)
        else:
            leaf()
        turtle.backward(length)
    # If this is the last level:
    else:
        leaf()

turtle.speed(0)
turtle.color('brown')
turtle.width(2)
turtle.left(90)

grow(level,START)

screen.mainloop()