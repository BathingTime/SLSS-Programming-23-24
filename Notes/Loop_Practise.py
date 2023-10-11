# Loop Practise
# Sunny Lin
# Oct 10, 23

import time

# Create a list of groceries.
groceries=['hot wheels','lego','ice-cream','video games']

# Do something for each thing in the list.
# Print it out in a pretty way.
# e.g.
#     • hot wheels
#     ———
#     • lego
#     ———
#     • etc.

# print(f'• {groceries[0]}')
# print('———')
# print(f'• {groceries[1]}')
# print('———')
# print(f'• {groceries[2]}')
# print('———')

for item in groceries:
    print(f'''• {item}
———''')

# Using the above method, create the thing below:
# *
# **
# ***
# ****
# *****
# ******

rows=['*'*stars for stars in range(1,7)]

for row in rows:
    print(row)

# Problem:
# Create a New Years Countdown that's automated
# Requirements:
#   - starts at 10
#   - counts down every second printing the second it's at
#   - instead of reaching zero, it prints out "Happy New Year"
# Example Output:
#  10
#  9
#  8
#  ...
#  1
#  Happy New Year!

for second in range(10,0,-1):
    print(second)
    time.sleep(1)
print('Happy New Year!')