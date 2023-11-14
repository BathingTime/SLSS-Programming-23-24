# Parental Bot
# Sunny lin
# Nov 14, 23

# Questions:
questions=('Did you eat? ',
           'Did you study? ',
           'Did you do your laundry? ',
           'Did you call grandma? ')

# Initialise the score of goodness.
goody=0

# Iterate through the question.
for question in questions:
    # If the user answers yes, increment the score of goodness.
    if input(question).lower().strip(' ,.!?')=='yes':
        goody+=1

# Print an appropriate response.
if goody==0:
    print('I\'m coming over.')
elif 1<=goody<=2:
    print('Ok.')
else:
    print('Good!')