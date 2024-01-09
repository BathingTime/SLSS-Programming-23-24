# Winter Holidays
# Sunny Lin
# Jan 8, 24

from random import choice

# Requirements:
# • Create a function called winter_holiday().
#   • Takes one parametre — string
#   • Returns a summary of an event from your holidays.

def winter_holiday(good_or_bad:str)->str:
    '''
    Returns a summary of your winter holidays 2023-2024
    
    Params:
    • good_or_bad:str = string that indicates whether the event is good or bad.
    '''

    goods=('I went to a German Christmas market with some friends.',
           'I played Don\'t Starve Together with some friends.',
           'I got some exercise.',
           'I pet my dawg.')
    
    bads=('I lacked human interaction for more than a week.',
          'I was supposed to see a movie with my friends but I could not.',
          'I could not play Garry\'s Mod because my laptop could not support something.',
          'I impetuously left a group chat for no reason and made my ex very angry.')
    
    if good_or_bad.strip(' ,.!?').lower()=='good':
        return choice(goods)
    return choice(bads)

# Runs all the things we want to test in our .py file.
def main()->None:
    print(winter_holiday('good'))
    print(winter_holiday('bad'))

# If we are running THIS FILE using Python:
if __name__=='__main__':
    main()