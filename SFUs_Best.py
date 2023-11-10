# SFU's Best
# Sunny Lin
# Nov 10, 23

# Load data from CSV file.
# Read it in a meaningful way.
# Link our similarity score algorithm to the data.
    
# Create a "profile" for someone that shows their favourite places at SFU.
profile=[]

# Initialise our top similarity score and their name.
top_sim_score=0
top_sim_name=''

# Open the file.
with open('./data.csv') as dataFile:
    # Throw away the header line.
    _=dataFile.readline()

    # For every line of data in the file (string):
    for line in dataFile:
        # Convert the line of data into a list.
        current_likes=line.split(',')

        # Initialise the CURRENT sim score.
        current_sim_score=0

        # Store the current person's name.
        current_name=current_likes[1]

        # Sim score algorithm:
        # For every item in our PROFILE:
        for item in profile:
            #If that item is in the data's list:
            if item in current_likes:
                # Increment the sim score.
                current_sim_score+=1

        # Print the current sim score.
        print(f'{current_name} — score: {current_sim_score}')

        # If the current score is > top sim score:
        if current_sim_score>top_sim_score:
            # Update the top sim score and top name.
            top_sim_score=current_sim_score
            top_sim_name=current_name

print(f'''TOP SIMILAR PERSON!
      {top_sim_name} — score: {top_sim_score}''')