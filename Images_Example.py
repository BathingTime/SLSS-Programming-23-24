# Images Example
# Sunny Lin
# Dec 13, 23

from PIL import Image

import Colour_Helper

# with Image.open('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/kid-green.jpg') as subject:
#     with Image.open('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/beach.jpg') as background:
#         # Iterate through each row of pixel in the picture.
#         for y in range(subject.height):
#             # Iterate through each pixel of each row.
#             for x in range(subject.width):
#                 # If the current pixel is green, switch it with its corresponding background pixel.
#                 if Colour_Helper.is_green(subject.getpixel((x,y))):
#                     subject.putpixel((x,y),background.getpixel((x,y)))

#         # Save the image.
#         subject.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/greenscreen_example.jpg')

with Image.open('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/best_pizza.jpg') as im:
    # Iterate through each row of pixel in the picture.
    for y in range(im.height):
        # Iterate through each pixel of each row.
        for x in range(im.width):
            # Change the current pixel to white if it is light or black if it is dark.
            if Colour_Helper.is_light(im.getpixel((x,y))):
                im.putpixel((x,y),(255,255,255))
            else:
                im.putpixel((x,y),(0,0,0))

    # Save the image.
    im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/binary_example.jpg')