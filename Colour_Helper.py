# Colour Helper
# Sunny Lin
# Dec 13, 23

def is_green(pixel:tuple)->str:
    '''
    Return if a pixel is green.

    Params:
    • pixel:tuple = the pixel to be checked.
    '''

    return pixel[0]<120 and pixel[1]>180 and pixel[2]<120

def is_light(pixel:tuple)->bool:
    '''
    Return if a pixel is light.

    Params:
    • pixel:tuple = the pixel to be checked.
    '''

    return pixel[0]>127 and pixel[1]>127 and pixel[2]>127

def gray_scale(pixel:tuple)->int:
    '''
    Return the rgb value for the gray-version of a pixel.

    Params:
    • pixel:tuple = the pixel to be checked.
    '''

    return (pixel[0]+pixel[1]+pixel[2])//3

def contrary(pixel:tuple)->tuple:
    '''
    Return the contrary version of a pixel.

    Params:
    • pixel:tuple = the pixel to be checked.
    '''

    return tuple(255-rgb for rgb in pixel)