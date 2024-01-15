# Robot Dog
# Sunny Lin
# Jan 12, 24

from PIL import Image

def is_red(pixel:tuple)->bool:
    return 170<=pixel[0] and 10<=pixel[1]<=80 and 20<=pixel[2]<=100

def ball_centre(im_name:str)->str:
    with Image.open(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/{im_name}') as im:
        left,right,top,bottom=im.width,0,im.height,0
        for y in range(im.height):
            for x in range(im.width):
                if is_red(im.getpixel((x,y))):
                    if x<left:
                        left=x
                    if right<x:
                        right=x
                    if y<top:
                        top=y
                    if bottom<y:
                        bottom=y
        for y in range((top+bottom)//2-1,(top+bottom)//2+1):
            for x in range((left+right)//2-1,(left+right)//2+1):
                im.putpixel((x,y),(0,0,0))
        im.save(f'/Users/sl000268/Programming/SLSS-Programming-23-24/Images/Ball_Centre.jpg')
        return f'The centre of the ball is at ({(left+right)//2}, {(top+bottom)//2}) from the top-right.'

print(ball_centre('Red_Ball.jpeg'))