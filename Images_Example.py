# Images Example
# Sunny Lin
# Dec 13, 23

from PIL import Image

import Colour_Helper

with Image.open('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/kid-green.jpg') as subject:
    with Image.open('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/beach.jpg') as background:
        # Outer loop is top->bottom.
        for y in range(subject.height):
            # Inner loop is left->right.
            for x in range(subject.width):
                # If the current pixel is green:
                if Colour_Helper.is_green(subject.getpixel((x,y))):
                    # Switch the current pixel with the corresponding background pixel.
                    subject.putpixel((x,y),background.getpixel((x,y)))

        # Save the image.
        subject.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/output.jpg')