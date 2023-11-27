# Functions Practice
# Sunny Lin
# Nov 26, 23

def stars(length:int)->str:
    '''
    Returns a string of stars (*) with length <length>.

    Params:
    • length:int = number of stars in the string.
    '''

    return '*'*length

# print(stars())

def biggest_of_three(num1:float,num2:float,num3:float)->float:
    '''
    Returns the largest of three inputted floats.

    Params:
    • num1:float = first number.
    • num2:float = second number.
    • num3:float = third number.
    '''

    if num1>num2 and num1>num3:
        return num1
    if num2>num3:
        return num2
    return num3

# print(biggest_of_three(,,))

def pyramid(height:int)->str:
    '''
    Returns a string of a pyramid of stars with height <height>.

    Params:
    • height:int = height of the pyramid.
    '''

    output=''
    for stars in range(1,height+1):
        output+='*'*stars+'\n'
    if output:
        return output[:-1]
    return ''

# print(pyramid())

def pyramid_mirror(height:int)->str:
    '''
    Returns a string of a mirrored pyramid of stars with height <height>.

    Params:
    • height:int = height of the pyramid.
    '''

    output=''
    for stars in range(1,height+1):
        output+=' '*(height-stars)+'*'*stars+'\n'
    if output:
        return output[:-1]
    return ''

# print(pyramid_mirror())