# Star Wars Bot
# Sunny Lin
# Oct 16, 23

from time import sleep

# Introduction.
print('I will decide if you can join the Dark Side.')
sleep(1)

# Ask the user if their favourite colour is red and store that in a variable as a boolean.
like_red=input('Is red your favourite colour? ').lower().strip(' ,.!?')=='yes'
sleep(.5)

# Ask the user if they like capes and store that in a variable as a boolean.
like_capes=input('Do you like capes? ').lower().strip(' ,.!?')=='yes'
sleep(.5)

# If they either like red or capes, they are on the Dark Side.
if like_red or like_capes:
    print('Dark Side it is!')
# If they do not like red or capes, they are on the Light Side.
else:
    print('Light Side, I see.')