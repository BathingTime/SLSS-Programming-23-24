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

# Implement Linear Search.

names=['Anthony Maldonado', 'Randy Love', 'Christopher Valdez', 'Rodney Odom', 'Kimberly Ramos', 'Lisa Ray', 'Kevin Terry', 'Gregory Romero', 'Debbie Harris', 'Edwin Hall', 'Mark Myers', 'Lisa Long', 'Stephanie Watson', 'Katherine Fields', 'Kathryn Olson', 'Maurice Baxter', 
      'Russell Caldwell', 'Heather Griffin', 'Kara Lane', 'Mark Tucker', 'Kathryn Rodriguez', 'Rachael Daniels', 'Debra Whitaker', 'Angela Neal', 'Michelle Hall', 'Jessica Olson', 'Lynn Jensen', 'Marc Ray', 'Valerie Harris', 'Tina Webb', 'Donna Green', 'Derek Mcgee', 
      'Tammy Hall DVM', 'Christopher Johnston', 'Eric Smith', 'Matthew Lopez', 'Mary Smith', 'Dr. Heather Ramos MD', 'Eric Johnson', 'Dylan Alvarado', 'Aaron Huff', 'Robin James', 'Sandra Stevens', 'Scott Thomas', 'Philip Nelson', 'Marcus Martin', 'Mary Alexander', 
      'Jason James', 'Samantha Burch', 'Jessica Martinez', 'Jose Wright', 'Zachary Pineda', 'William Ramos', 'Shelby Hughes', 'Melanie Moore', 'Kimberly Fowler', 'Jordan Jones', 'Brenda Anderson', 'Russell Coleman', 'Jeremy Snow', 'Billy Wu', 'Jesse Rodriguez', 'Andrew Shea', 
      'Jason Castillo', 'Donald Abbott', 'Richard Cervantes Jr.', 'Jeffrey Powell', 'Angel Fernandez', 'Michelle Donovan', 'Mr. Michael Wagner DDS', 'Kimberly Gonzalez', 'Thomas Smith', 'Nichole Barnes', 'Shelly Clark', 'Ashley Ortiz', 'Jessica Lam', 'Kimberly Ray MD', 
      'Mason Kennedy', 'Whitney Harrington', 'Nicole Tran', 'Robert Montgomery', 'Ryan Gardner', 'Kimberly Silva', 'Stephanie Rivera', 'William Santos', 'Ashley Mcclain', 'Sophia Williams', 'Kevin Herring', 'Tyrone Leonard', 'Carolyn Jones', 'Stephanie Willis', 'Jon Lang', 
      'Tammy Porter', 'Robert Garcia', 'Casey Brown', 'Benjamin Aguilar', 'Nancy Norman', 'Aaron Peters', 'Blake Graham', 'Noah Harper DDS', 'Dwayne Ortiz', 'Melissa Padilla', 'Rebecca Jones', 'Michael Wood', 'Daniel Bean', 'Alexander Kaufman', 'Michael Higgins', 
      'Richard Bailey', 'Jay Cisneros', 'Lisa Acevedo', 'Sarah Hernandez', 'Bryan Jones', 'Mark Kennedy', 'Robert Caldwell', 'Larry Wolf', 'Robert Adkins', 'Wanda Doyle', 'Thomas Brown', 'Kevin Key', 'Stacey Fisher', 'Amber Hart', 'Paul Russell', 'Jacqueline David', 
      'Shannon Parker', 'Lisa Sanchez', 'Jennifer Atkins', 'Jason Woods', 'Richard Garcia', 'Luis Williams', 'Marco Weaver', 'Amy Hayes', 'Elizabeth Doyle DDS', 'Nicole Smith', 'Karen Thomas', 'Randy Reese', 'Deanna Rodriguez', 'Christian Conway', 'Craig Doyle', 
      'Dennis Oneill', 'Diane Jordan', 'Patrick Holder', 'Christina Thompson', 'Deanna Lee', 'Kathleen Davis', 'Brian Cox', 'Kristen Thomas', 'Samantha Smith', 'William Moss', 'Matthew Flowers', 'Megan Powell', 'Richard Williamson', 'Cindy Glenn', 'John Taylor', 
      'Nathaniel Lee', 'Sara Glover', 'James Jackson II', 'Carlos Henderson', 'Edward Holder', 'Whitney Hansen', 'Matthew Jacobs', 'Raymond Rodriguez', 'Christy Kennedy', 'Lisa Johnson', 'Mark Harris', 'Stephen Bowers', 'Derrick Brown', 'Stephen Schroeder', 'Martin Lawrence', 
      'Brian Reed', 'Trevor Booker', 'Ruben Johnson', 'Jeffrey Griffith', 'William Townsend', 'Cynthia Park', 'Carla Yang', 'Oscar Hartman', 'Shawn Hendricks', 'Timothy Oconnor', 'Gina Robertson', 'Jennifer Rodriguez', 'Jared Harris', 'Austin Austin', 'Nathan Golden', 
      'Samantha Flores', 'Alexis Jones', 'Susan Rice', 'Randall Holmes', 'Connie Johnson', 'Carol Young', 'Brandon Norris', 'Timothy Lester', 'Dustin Mccarthy', 'Tammy Brock', 'Heather Cummings', 'John Moreno', 'Dawn Berry', 'Jeffrey Montes', 'Joshua Smith', 'Alexa Barber', 
      'Mark Lewis']

search_name='Deanna Lee'

for name in names:
    # Check if it is the name we want.
    if name==search_name:
        print(f'We found {search_name}!')
        break
else:
    print(f'We did not find {search_name}.')

# Print out "Mr. Ubial is cool" 20 times.
for _ in range(20):
    print('Mr. Ubial is cool')

# 1. Print all even numbers between
#     1200 and 1500 inclusive.
#     Use a for loop.

for i in range(1200,1501,2):
    print(i)

# 2. Print all odd numbers between
#     -150 and 0 inclusive.

for i in range(-149,0,2):
    print(i)

# Once you have your solution,
# Copy and paste your answer in #i-made-this