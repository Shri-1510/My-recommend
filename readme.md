# Movie Recommendation System

This project implements a movie recommendation system using collaborative filtering and cosine similarity. It generates movie recommendations for users based on their ratings and preferences. The dataset used for this system is generated using Python and includes movie ratings provided by randomly generated users.

## Getting Started

### Prerequisites

- Python 3.x
- pandas library
- scikit-learn library

Install the required libraries using the following command:

```bash
pip install pandas scikit-learn
Dataset Generation
The dataset is generated using the dataset_generation.py script. This script creates a movie ratings dataset with randomly generated user ratings and saves it as movie_ratings_large.csv. It includes a list of movie names, first names, and last names to generate random user names.

Preprocessing
The preprocessing of the generated dataset is performed using the preprocess.py script. This script applies Min-Max scaling and Z-score normalization on the ratings. The preprocessed dataset is saved as movie_ratings_preprocessed.csv.

Recommendation System
The recommendation system is implemented in the recommend.py script. It interacts with the user, prompting them to enter a user ID and providing movie recommendations based on collaborative filtering and cosine similarity. Users can provide feedback on each recommendation to refine the suggestions.

Usage
Generate the dataset using dataset_generation.py.
bash
Copy code
python dataset_generation.py
Preprocess the dataset using preprocess.py.
bash
Copy code
python preprocess.py
Run the recommendation system using recommend.py.
bash
Copy code
python recommend.py
Notes
The generated dataset includes randomly generated user names and ratings for movies.
The recommendation system uses collaborative filtering and cosine similarity to provide movie recommendations.
License
This project is licensed under the MIT License.