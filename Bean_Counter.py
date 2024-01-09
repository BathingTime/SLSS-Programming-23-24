# Bean Counter
# Sunny Lin
# Jan 9, 24

from PIL import Image

import Bean_Helper

def count_colours(im_name:str)->None:
    colours={('red',Bean_Helper.red):0,
             ('orange',Bean_Helper.orange):0,
             ('yellow',Bean_Helper.yellow):0,
             ('green',Bean_Helper.green):0,
             ('blue',Bean_Helper.blue):0,
             ('pink',Bean_Helper.pink):0,
             ('black',Bean_Helper.black):0,}
    with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}.jpg') as im:
        for y in range(im.height):
            for x in range(im.width):
                for 