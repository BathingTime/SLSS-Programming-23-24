# Colour Helper
# Sunny Lin
# Dec 13, 23

from PIL import Image

def pixel_to_string(pixel:tuple)->str:
    '''
    Return if a pixel is green.

    Params:
    • pixel:tuple = the pixel to be checked.
    '''

    return pixel[0]<32 and pixel[1]>250 and pixel[2]<32