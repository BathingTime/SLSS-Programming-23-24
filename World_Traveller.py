# World Traveller Bot
# Sunny Lin
# Nov 3, 23

from time import sleep

# All 7 continents:
continents=('Asia','Europe','North America','South America','Australia','Africa','Antarctica')

# Initialise a variable for how many continents they have been to.
conts_been_to=0

# Ask the user for their name and store it in a variable.
user_name=input(f'What\'s your name? ').lower().capitalize().strip(' ,.!?')
sleep(1)

print(f'Hello, {user_name}! It\'s nice to meet you!')
sleep(1)

# Ask for user if they have been to the 7 continents and count how many they have been to.
for continent in continents:
    if input(f'Have you been to {continent}? ').lower().strip(' ,.!?')=='yes':
        conts_been_to+=1

# Output how may continents they have been to.
print(f'I see, you\'ve been to {conts_been_to}/{len(continents)} continents!')