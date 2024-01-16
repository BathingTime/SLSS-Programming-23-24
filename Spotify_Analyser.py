# Spotify Analyser
# Sunny Lin
# Jan 16, 24

import csv

# Search for all Drake songs (linear search).

# Make a list for all Drake songs.
drake_songs=[]

# Open the file.
with open('/Users/sl000268/Programming/SLSS-Programming-23-24/spotify.csv') as dataFile:
    # Create a csv reader object.
    csv_reader=csv.DictReader(dataFile)

    # Create a counter for the current line number.
    line_num=0

    # For every line in the file:
    for line in csv_reader:
        # If it is the first line, print out all the headings.
        if line_num==0:
            print(f'The columns are: {", ".join(line)}')
        else:
            # If the artist is Drake, append the artist, song name, and danceability as a tuple into the Drake list.:
            if 'drake' in line['artist'].lower():
                drake_songs.append((line['artist'],line['song_title'],line['danceability']))
        
        # Increment the line number.
        line_num+=1

# Print all the Drake songs that have danceability of .5 or higher.
for song in drake_songs:
    if float(song[2])>=.5:
        print(song[1])