import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv('movie_ratings_large.csv')

# Separate out the User column and the movie ratings columns
user_column = df['user']
movie_ratings = df.drop(columns=['user'])

# Preprocess the ratings using Min-Max scaling for each movie
min_max_scaler = MinMaxScaler()
min_max_normalized_ratings = min_max_scaler.fit_transform(movie_ratings)
min_max_normalized_df = pd.DataFrame(min_max_normalized_ratings, columns=movie_ratings.columns)

# Preprocess the ratings using Z-score normalization for each movie
z_score_scaler = StandardScaler()
z_score_normalized_ratings = z_score_scaler.fit_transform(movie_ratings)
z_score_normalized_df = pd.DataFrame(z_score_normalized_ratings, columns=movie_ratings.columns)

combined_preprocessed_df = pd.concat([user_column, min_max_normalized_df, z_score_normalized_df], axis=1)

combined_preprocessed_df.to_csv('movie_ratings_preprocessed.csv', index=False)

print("Combined preprocessed dataset saved to 'movie_ratings_preprocessed.csv'")
