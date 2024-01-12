# Bean Helper
# Sunny Lin
# Jan 9, 24

def red(pixel:tuple)->bool:
    return 100<=pixel[0] and 0<=pixel[1]<=10 and 0<=pixel[2]<=20

def orange(pixel:tuple)->bool:
    return 200<=pixel[0] and 50<=pixel[1]<=150 and 0<=pixel[2]<=30

def yellow(pixel:tuple)->bool:
    return 200<=pixel[0] and 150<=pixel[1]<=210 and 0<=pixel[2]<=30

def green(pixel:tuple)->bool:
    return 10<=pixel[0]<=80 and 50<=pixel[1] and 0<=pixel[2]<=60

def blue(pixel:tuple)->bool:
    return 0<=pixel[0]<=110 and 20<=pixel[1]<=100 and 80<=pixel[2]

def pink(pixel:tuple)->bool:
    return 190<=pixel[0]<=240 and 60<=pixel[1]<=150 and 80<=pixel[2]<=200

def black(pixel:tuple)->bool:
    return pixel[0]<=20 and pixel[1]<=20 and pixel[2]<=20