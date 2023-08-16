import pandas as pd
import random

movie_names = [
    "Inception", "The Shawshank Redemption", "The Matrix", "Interstellar", "Pulp Fiction",
    "Avatar", "Jurassic Park", "Forrest Gump", "The Godfather", "The Dark Knight",
    "Star Wars", "Titanic", "Gladiator", "The Lion King", "Fight Club",
    "Casablanca", "The Lord of the Rings", "The Avengers", "Eternal Sunshine of the Spotless Mind",
    "The Social Network", "Black Panther", "La La Land", "The Grand Budapest Hotel", "Blade Runner 2049",
    "The Incredibles", "Toy Story", "Gone with the Wind", "The Silence of the Lambs", "Shutter Island",
    "The Revenant", "The Breakfast Club", "The Princess Bride", "The Godfather Part II", "The Big Lebowski","The Good Dinosaur"
]

num_users = 10000
num_movies = len(movie_names)
data = {
    'user': [],
}

for movie in movie_names:
    data[movie] = []

for user_id in range(1, num_users + 1):
    data['user'].append(f'user{user_id}')
    for movie in movie_names:
        data[movie].append(random.randint(1, 5))

df = pd.DataFrame(data)

df.to_csv('movie_ratings_large.csv', index=False)
print("Dataset saved to 'movie_ratings_large.csv'")
