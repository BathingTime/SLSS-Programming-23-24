# Cookies
# Sunny Lin
# Nov 22, 23

from math import sqrt
import random
import turtle

# Get screen dimensions.
screen=turtle.Screen()
width=screen.window_width()/2
height=screen.window_height()/2

# Construct baker turtle.
baker=turtle.Turtle()
baker.speed(0)
baker.pu()

while True:
    # Make a random radius for the cookie.
    radius=random.randint(10,100)

    # Get random x and y coordinates for the cookie.
    cookie_x=random.randint(-width,width)
    cookie_y=random.randint(-height,height)

    # Draw the cookie at that position.
    baker.goto(cookie_x,cookie_y-radius)

    # Get random colours for the cookie and outline.
    baker.color(random.random(),random.random(),random.random())
    baker.fillcolor(random.random(),random.random(),random.random())

    # Draw the circle.
    baker.seth(0)
    baker.pd()
    baker.begin_fill()
    baker.circle(radius)
    baker.pu()
    baker.end_fill()

    # Add 5 chips.
    for _ in range(radius//5):
        # Get a random colour for the chip.
        baker.color(random.random(),random.random(),random.random())

        # Create random x and y coordinates for the chip.
        chip_x=random.randint(-radius,radius)
        chip_y=random.randint(-radius,radius)

        # Keeping generating new coordinates until it is inside the cookie.
        while sqrt(abs(chip_x)**2+abs(chip_y)**2)>radius:
            chip_x=random.randint(-radius,radius)
            chip_y=random.randint(-radius,radius)

        # Stamp a chip at that position.
        baker.goto(chip_x+cookie_x,chip_y+cookie_y)
        baker.seth(random.randint(0,360))
        baker.stamp()