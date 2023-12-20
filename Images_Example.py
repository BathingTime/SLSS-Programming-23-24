# Images Example
# Sunny Lin
# Dec 13, 23

from PIL import Image
from random import randint

import Colour_Helper

# Greenscreen

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

# Binary

# with Image.open('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/best_pizza.jpg') as im:
#     # Iterate through each row of pixel in the picture.
#     for y in range(im.height):
#         # Iterate through each pixel of each row.
#         for x in range(im.width):
#             # Change the current pixel to white if it is light or black if it is dark.
#             if Colour_Helper.is_light(im.getpixel((x,y))):
#                 im.putpixel((x,y),(255,255,255))
#             else:
#                 im.putpixel((x,y),(0,0,0))

#     # Save the image.
#     im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/binary_example.jpg')

# Gray-scale

# with Image.open('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/best_pizza.jpg') as im:
#     # Iterate through each row of pixel in the picture.
#     for y in range(im.height):
#         # Iterate through each pixel of each row.
#         for x in range(im.width):
#             # Change the current pixel to its gray-scaled version.
#             new_rgb=Colour_Helper.gray_scale(im.getpixel((x,y)))
#             im.putpixel((x,y),tuple([new_rgb]*3))

#     # Save the image.
#     im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/grayscaled_example.jpg')

# Contrary

# with Image.open('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/best_pizza.jpg') as im:
#     # Iterate through each row of pixel in the picture.
#     for y in range(im.height):
#         # Iterate through each pixel of each row.
#         for x in range(im.width):
#             # Change the current pixel to its contrary version.
#             im.putpixel((x,y),Colour_Helper.contrary(im.getpixel((x,y))))

#     # Save the image.
#     im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/contrary_example.jpg')

# Random

# new_rgb={}

# for current in range(0,256):
#     new_rgb[current]=randint(0,255)

# with Image.open('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/best_pizza.jpg') as im:
#     # Iterate through each row of pixel in the picture.
#     for y in range(im.height):
#         # Iterate through each pixel of each row.
#         for x in range(im.width):
#             # Change the current pixel to its contrary version.
#             im.putpixel((x,y),tuple(new_rgb[rgb] for rgb in im.getpixel((x,y))))

#     # Save the image.
#     im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/random_example.jpg')

# Random 2

# new_rgb={}

# for current in range(0,255//10+1):
#     new_rgb[current]=randint(0,255)

# with Image.open('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/best_pizza.jpg') as im:
#     # Iterate through each row of pixel in the picture.
#     for y in range(im.height):
#         # Iterate through each pixel of each row.
#         for x in range(im.width):
#             # Change the current pixel to its contrary version.
#             im.putpixel((x,y),tuple(new_rgb[rgb//10] for rgb in im.getpixel((x,y))))

#     # Save the image.
#     im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/random2_example.jpg')

# Random 3

new_rgbs=[]

for _ in range(3):
    new_rgb={}
    for current in range(0,255//10+1):
        new_rgb[current]=randint(0,255)
    new_rgbs.append(new_rgb)

with Image.open('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/best_pizza.jpg') as im:
    # Iterate through each row of pixel in the picture.
    for y in range(im.height):
        # Iterate through each pixel of each row.
        for x in range(im.width):
            # Change the current pixel to its contrary version.
            current=im.getpixel((x,y))
            random_rgb=[]
            for pos_rgb in range(3):
                random_rgb.append(new_rgbs[pos_rgb][current[pos_rgb]//10])
            im.putpixel((x,y),tuple(random_rgb))

    # Save the image.
    im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/random3_example.jpg')