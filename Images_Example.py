# Images Example
# Sunny Lin
# Dec 13, 23

from PIL import Image

import Colour_Helper

with Image.open("/Users/sl000268/Programming/SLSS-Programming-23-24/Images/kid-green.jpg") as im:
    # Outer loop is top->bottom.
    for y in range(im.height):
        # Inner loop is left->right.
        for x in range(im.width):
            # Detects if the current pixel is green.
            if Colour_Helper.pixel_to_string(im.getpixel((x,y))):
                print("GREEN PIXEL!!!!")
            else:
                print("UNKNOWN PIXEL")