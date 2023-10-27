# Bubble Tea Popularity Algorithm
# Sunny Lin
# Oct 27, 23

# Ask 5 users what their favourite bubble tea place is.
# Print out a summary of the data.

# Helper Functions:
def cap(place):
    place=place.capitalize()
    pos=1
    while pos<len(place):
        if place[pos]==' ':
            place=place[:pos+1]+place[pos+1].upper()+place[pos+2:]
            pos+=2
        else:
            pos+=1
    return place

# CONSTS:
NUM_RESPONDENTS=5

# Like counters (initialise all counters to 0):
counters={'coco':0,
          'suntea':0,
          'chatime':0,
          'bubble queen':0}

for _ in range(NUM_RESPONDENTS):

    # Ask the user what their favourite place is and store that information.
    fave_place=input('What is your favourite bubble tea place? ').strip(' ,.!?').lower()

    # Tally/counter algorithm:
    if fave_place in counters:
        counters[fave_place]+=1
    else:
        counters[fave_place]=1

    # Repeat five times.

# Print out a summary.
print('\n'.join(map(cap,[place.capitalize()+': '+str(counters[place]) for place in counters])))