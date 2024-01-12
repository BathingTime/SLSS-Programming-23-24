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
                for colour in colours:
                    if colour[1](im.getpixel((x,y))):
                        colours[colour]+=1
        total=im.width*im.height
        return '\n'.join([f'{round(colours[colour]/total*100,2)}% of the image is {colour[0]}.' for colour in colours])

def show_colours(im_name:str)->None:
    with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}.jpg') as original:
        with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}.jpg') as isolated:
            for colour in (('Red',Bean_Helper.red),('Orange',Bean_Helper.orange),('Yellow',Bean_Helper.yellow),('Green',Bean_Helper.green),('Blue',Bean_Helper.blue),('Pink',Bean_Helper.pink),('Black',Bean_Helper.black)):
                for y in range(original.height):
                    for x in range(original.width):
                        if colour[1](original.getpixel((x,y))):
                            isolated.putpixel((x,y),original.getpixel((x,y)))
                        else:
                            isolated.putpixel((x,y),(255,255,255))
                isolated.save(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/Only_{colour[0]}.jpg')

print(count_colours('Jelly_Beans'))
show_colours('Jelly_Beans')