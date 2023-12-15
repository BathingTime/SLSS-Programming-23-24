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