# Turtle Example
# Sunny Lin
# Nov 21, 23

import turtle

# CONSTS:
FORWARD_MAG=100
TURN_DEG=90

# Create a turtle that can be moved around the screen.

# Make a turtle object.
michael_angelo=turtle.Turtle()

# Get some input from the user.
print('''To give commands, type:
F — go forward.
L — turn left.
R — turn right.''')

# Repeat forever until the user says "stop."
done=False

while not done:

    command=input('Where should I go? ').strip(' ,.!?').lower()

    # Move the turtle around based on that input.
    if command=='f':
        michael_angelo.forward(FORWARD_MAG)
    elif command=='l':
        michael_angelo.left(TURN_DEG)
    elif command=='r':
        michael_angelo.right(TURN_DEG)
    elif command=='stop':
        done=True
    else:
        print('Not a valid command.')