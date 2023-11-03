# Olympic Judging
# Sunny Lin
# Nov 3, 23

# CONSTS:
JUDGES=5

# Initialise a variable for the total scores.
total_scores=0

# Ask the user for the scores 5 times.
for judge in range(JUDGES):
    total_scores+=float(input(f'Judge {judge+1}: ').strip(' ,.!?'))

# Calculate and output the average score.
print(f'Your Olympic score is {total_scores/JUDGES:.2f}')