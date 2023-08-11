import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
# test
def load_data(filename):
    df = pd.read_csv(filename)
    df.set_index('user', inplace=True)
    return df

# Calculate similarity matrix
def calculate_similarity_matrix(data):
    similarity_matrix = cosine_similarity(data.T.fillna(0))  # Transpose data for item-based similarity
    return similarity_matrix

# Get a single movie recommendation for a specific user
def get_single_movie_recommendation(user, data, similarity_matrix, previous_recommendations=None):
    user_ratings = data.loc[user].values.reshape(-1, 1)
    weighted_ratings = similarity_matrix.dot(user_ratings)
    recommendations = data.columns[weighted_ratings.flatten().argsort()[::-1]]

    if previous_recommendations:
        recommendations = [movie for movie in recommendations if movie not in previous_recommendations]

    return recommendations[0]

def main():
    data = load_data('movie_ratings_preprocessed.csv')  
    similarity_matrix = calculate_similarity_matrix(data)

    user = input("Please enter your userid: ")
    previous_recommendations = []
    liked_recommendation = False

    while not liked_recommendation:
        recommendation = get_single_movie_recommendation(user, data, similarity_matrix, previous_recommendations)
        print(f"Recommended movie: {recommendation}")

        response = input("Did you like the recommendation? (yes/no): ")
        if response.lower() in ['yes','y']:
            print("Great choice!")
            liked_recommendation = True
        else:
            print("Let's try another recommendation.")
            previous_recommendations.append(recommendation)

if __name__ == "__main__":
    main()
