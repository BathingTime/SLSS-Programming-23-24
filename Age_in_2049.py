# Age in 2049
# Sunny Lin
# Nov 3, 23

from datetime import date

# Ask the user how old they are.
user_age=int(input('How old are you? ').strip(' ,.!?'))

# Output how old they will be in 2049.
print(f'In 2049 you will be {user_age+2049-int(str(date.today()).split("-")[0])} years old.')