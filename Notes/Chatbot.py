#Chatbot
#Sunny Lin
#Sep 20, 23

import random
import time

#Greet the user.
print("""Hello there!
I am a crude Chatbot, here to take to you.""")
time.sleep(1)

#Get the user's name and store it in a variable.
user_name=input("So… what is your name: ").capitalize()

#Ask the user what their favourite food is.
print(f"It is good to meet you, {user_name}.")
time.sleep(1)
fave_food=input(f"So, {user_name}, what is your favourite food: ")
time.sleep(1)

#Make a comment about their favourite food BUT NOT BE TERRIBLY REPEPTITIVE.
#Create a list of possible responses.
list_of_responses=[f"Oh. I have never tasted {fave_food} before.",
                   f"Mmmmm. {fave_food.capitalize()} sounds good.",
                   f"I heard that {fave_food} is delicious.",
                   f"{fave_food.capitalize()} is cool."]

#Choose one of those responses randomly and print out that chosen response.
print(f"{random.choice(list_of_responses)} Thanks for sharing, {user_name}.")