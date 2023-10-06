#Food Suggestion Bot
#Sunny Lin
#Oct 6, 23

#A bot that asks the user what their favourite food is.
#Based on that food, it will classify the type/genre/cuisine of the food,
#then give a restaurant suggestion.

import time

#Introduce the bot to the user.
#Ask the user what their favourite food is.
print('Hello, I am here to suggest you a restaurant.')
time.sleep(1)
fave_food=input('To help me suggest a restaurant, what is your favourite food? ').lower().strip(',.!? ')
time.sleep(1)

#Italian cuisine:
italian_food=['pasta','pizza','canneloni','tiramisu']
#Dingo cuisine:
dingo_food=['dingo','dawg','sussydawg','dringue','drongue','blingue','blongue']

#If they answer with Italian food, suggest an Italian restaurant.
if fave_food in italian_food:
    print('I see that you might like Italian food.')
    time.sleep(1)
    print('I suggest Broli Kitchen.')
    time.sleep(1)
    print('''Here is their address:
186-8180 No. 2 Rd, Richmond, BC.''')
elif fave_food in dingo_food:
    print('I see that you might like Dingo food.')
    time.sleep(1)
    print('I suggest Dingo Kitchen.')
    time.sleep(1)
    print('''Here is their address:
din-go No. Din Go, Din, GO.''')
else:
    print('Sorry, I\'m not sure what kind of food that is.')
    time.sleep(1)
    print('I cannot, unfortunately, provide a suggestion.')