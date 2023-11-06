# Semester Evaluator Bot
# Sunny Lin
# Nov 3, 23

# Initialise a variable for the total rates.
total_rates=0

# Ask the user how many courses they are taking and store it in a variable.
courses_taking=int(input('How many courses are you taking? '))

# Ask the user what they rate each course out of 5 and record it.
for course in range(courses_taking):
    total_rates+=int(input(f'How do you rate course {course} out of 5? '))

# Calculate the average rating.
ave_rate=round(total_rates/courses_taking,2)

# Respond based on what the average rating is.
if ave_rate<=1:
    print(f'{ave_rate}? Ouch.')
elif 1<ave_rate<3:
    print(f'{ave_rate}? Not a bad semester.')
if 3<=ave_rate:
    print(f'{ave_rate}? Glad to hear that!')