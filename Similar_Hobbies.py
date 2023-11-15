# Similar Hobbies
# Sunny Lin
# Nov 14, 23

# Introduction.
print('Please enter hobbies, separated by spaces.')

# First person's hobbies.
person_1_hobbies=input('Person 1: ').lower().split()

# Second person's hobbies.
person_2_hobbies=input('Person 2: ').lower().split()

# Initialise the sim score.
sim_score=0

# Iterate through the first person's hobbies.
for hobby in person_1_hobbies:
    # If person 2 also has the same hobby, increment the sim score.
    if hobby in person_2_hobbies:
        sim_score+=1

# Print out the result.
print(f'You have {sim_score} hobbies in common!')