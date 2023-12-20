# Images Example
# Sunny Lin
# Dec 13, 23

from PIL import Image
from random import randint

import Colour_Helper

def greenscreen(subject_name:str,background_name:str)->None:
    with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{subject_name}.jpg') as subject:
        with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{background_name}.jpg') as background:
            for y in range(subject.height):
                for x in range(subject.width):
                    if Colour_Helper.is_green(subject.getpixel((x,y))):
                        subject.putpixel((x,y),background.getpixel((x,y)))
            subject.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/greenscreen.jpg')

def binary(im_name:str)->None:
    with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}.jpg') as im:
        for y in range(im.height):
            for x in range(im.width):
                if Colour_Helper.is_light(im.getpixel((x,y))):
                    im.putpixel((x,y),(255,255,255))
                else:
                    im.putpixel((x,y),(0,0,0))
        im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/binary.jpg')

def grayscale(im_name:str)->None:
    with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}.jpg') as im:
        for y in range(im.height):
            for x in range(im.width):
                new_rgb=Colour_Helper.gray_scale(im.getpixel((x,y)))
                im.putpixel((x,y),tuple([new_rgb]*3))
        im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/grayscale.jpg')

def contrary(im_name:str)->None:
    with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}.jpg') as im:
        for y in range(im.height):
            for x in range(im.width):
                im.putpixel((x,y),Colour_Helper.contrary(im.getpixel((x,y))))
    im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/contrary.jpg')

def random(im_name:str)->None:
    new_rgb={}
    for current in range(0,256):
        new_rgb[current]=randint(0,255)
    with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}.jpg') as im:
        for y in range(im.height):
            for x in range(im.width):
                im.putpixel((x,y),tuple(new_rgb[rgb] for rgb in im.getpixel((x,y))))
        im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/random.jpg')

def random2(im_name:str)->None:
    new_rgb={}
    for current in range(0,255//10+1):
        new_rgb[current]=randint(0,255)
    with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}.jpg') as im:
        for y in range(im.height):
            for x in range(im.width):
                im.putpixel((x,y),tuple(new_rgb[rgb//10] for rgb in im.getpixel((x,y))))
        im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/random2.jpg')

def random3(im_name:str)->None:
    new_rgbs=[]
    for _ in range(3):
        new_rgb={}
        for current in range(0,255//10+1):
            new_rgb[current]=randint(0,255)
        new_rgbs.append(new_rgb)
    with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}.jpg') as im:
        for y in range(im.height):
            for x in range(im.width):
                current=im.getpixel((x,y))
                random_rgb=[]
                for pos_rgb in range(3):
                    random_rgb.append(new_rgbs[pos_rgb][current[pos_rgb]//10])
                im.putpixel((x,y),tuple(random_rgb))
        im.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/random3.jpg')

def scramble(im_name:str)->None:
    rows,cols=1,400
    grid=[[(x,y) for x in range(cols)] for y in range(rows)]
    for y in range(rows):
        for x in range(cols):
            new_pos=(randint(0,rows-1),randint(0,cols-1))
            grid[y][x],grid[new_pos[0]][new_pos[1]]=grid[new_pos[0]][new_pos[1]],grid[y][x]
    with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}.jpg') as im1:
        width,height=im1.width//cols,im1.height//rows
        with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}.jpg') as im2:
            for grid_y in range(rows):
                for grid_x in range(cols):
                    for im_y in range(height):
                        for im_x in range(width):
                            im2.putpixel((grid[grid_y][grid_x][0]*width+im_x,grid[grid_y][grid_x][1]*height+im_y),im1.getpixel((grid_x*width+im_x,grid_y*height+im_y)))
            im2.save('/Users/sl000268/Programming/SLSS-Programming-23-24/Images/scramble.jpg')

def wiggle(im_name:str)->None:
    ...

scramble('best_pizza')