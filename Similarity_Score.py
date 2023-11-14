# Comparing Similarity Scores
# Sunny Lin
# Nov 8, 23

# Calculate similarity scores between two people.

# Create two lists that represent the movies that people like.

ubial_fav_movies=['The Matrix',
                         'Avengers: Infinity War',
                         'The Empire Strikes Back',
                         'Infernal Affairs',
                         'Rogue One']

ben_fav_movies=['Thomas and Friends Big World BIg Adventure',
                'Infernal Affairs',
                'Rogue One',
                'Spider-man: Into the Spider-verse',
                'Guardians of the Galaxy: Volume 3']

# Initialise the similarity score.
similarity_score=0

# For each item in the first list:
for movie in ubial_fav_movies:
    # If that item is in the second list, increment the similarity score.
    if movie in ben_fav_movies:
        similarity_score+=1

# Display the results.