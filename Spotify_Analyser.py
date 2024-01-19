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
            # If the artist is Drake, append the artist, song name, valence, and danceability as a tuple into the Drake list:
            if 'drake' in line['artist'].lower():
                drake_songs.append((line['artist'],line['song_title'],line['valence'],line['danceability']))
        
        # Increment the line number.
        line_num+=1

# Print all the Drake songs that have danceability of .5 or higher.
# for song in drake_songs:
#     if float(song[3])>=.5:
#         print(song[1])

# Sort using selection sort from smallest to biggest danceability.
for pos1 in range(len(drake_songs)-1):
    pos_smallest=pos1
    for pos2 in range(pos1+1,len(drake_songs)):
        if drake_songs[pos2][3]<drake_songs[pos_smallest][3]:
            pos_smallest=pos2
    drake_songs[pos1],drake_songs[pos_smallest]=drake_songs[pos_smallest],drake_songs[pos1]