from pathlib import Path

# File Exercises
# Sunny Lin
# Nov 15, 23

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("/Users/sl000268/Programming/SLSS-Programming-23-24/data_example.csv", encoding="utf-8") as f:
    f.readline()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file.

with open("/Users/sl000268/Programming/SLSS-Programming-23-24/data_example.csv", encoding="utf-8") as f:
    f.readline()
    print(f.readline())

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.

with open("/Users/sl000268/Programming/SLSS-Programming-23-24/data_example.csv", encoding="utf-8") as f:
    for line in f:
        print(line[:-1])

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.

with open("/Users/sl000268/Programming/SLSS-Programming-23-24/data_example.csv", encoding="utf-8") as f:
    for line in f:
        print(line[:-1].split(','))

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.

chicken_adobo_likes=0

with open("/Users/sl000268/Programming/SLSS-Programming-23-24/data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        if line.split(',')[1]=='Chicken Adobo':
            chicken_adobo_likes+=1

print(f'{chicken_adobo_likes} person(s) like chicken adobo.')

# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".

start_with_a=0

with open("/Users/sl000268/Programming/SLSS-Programming-23-24/data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        if line[0]=='A':
            start_with_a+=1

print(f'{start_with_a} person(s) have names that start with "A."')

# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?

from_guangzhou=0

with open("/Users/sl000268/Programming/SLSS-Programming-23-24/data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        if line[:-1].split(',')[4]=='Guangzhou':
            from_guangzhou+=1

print(f'{from_guangzhou} person(s) are from Guangzhou.')

# Problem 6:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.

even_number=0

with open("/Users/sl000268/Programming/SLSS-Programming-23-24/data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        if int(line.split(',')[3])%2==0:
            even_number+=1

print(f'{even_number} person(s) have even credit card numbers.')

# Problem 7:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?

foods_seen=[]
best_food_num=0

with open("/Users/sl000268/Programming/SLSS-Programming-23-24/data_example.csv", encoding="utf-8") as f:
    foods=list(map(lambda line:line.split(',')[1],list(f)[1:]))
    for food in foods:
        if food not in foods_seen:
            current_food_num=foods.count(food)
            if current_food_num>best_food_num:
                best_food_num=current_food_num
                best_food=food
            foods_seen.append(food)

print(f'The most popular food is {best_food.lower()}.')