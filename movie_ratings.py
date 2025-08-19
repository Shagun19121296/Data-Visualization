import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns

movies_file = r"D:\workspace\python\Data Manipulation\Movie_ratings\ml-latest-small\movies.csv"
ratings_file = r"D:\workspace\python\Data Manipulation\Movie_ratings\ml-latest-small\ratings.csv"

# Read movies.csv (contains 'movieId', 'title', 'genres')
movies_df = pd.read_csv(movies_file, usecols=["movieId", "title", "genres"])

# Read ratings.csv (contains 'userId', 'movieId', 'rating', 'timestamp')
ratings_df = pd.read_csv(ratings_file, usecols=["movieId", "rating"])

# Merge the datasets on 'movieId'
combined_df = pd.merge(ratings_df, movies_df, on="movieId", how="inner")

most_rated_movies = combined_df["title"].value_counts().head(10)

#Top 10 highest-rated movies
average_ratings = combined_df.groupby("title")["rating"].mean()
sorted_avg_ratings = average_ratings.sort_values(ascending=False)

ratings_count = combined_df.groupby("title")["rating"].count()
movie_stats = pd.DataFrame({"avg_rating": average_ratings, "num_ratings": ratings_count})

# Filter movies with at least 50 ratings
filtered_movies = movie_stats[movie_stats["num_ratings"] >= 50].sort_values(by="avg_rating", ascending=False)

plt.figure(figsize=(7, 5))
sns.histplot(movie_stats["num_ratings"], bins=50, kde=True)
plt.xlabel("Number of Ratings")
plt.ylabel("Count")
plt.title("Distribution of Movie Ratings Count")

plt.figure(figsize=(10, 5))
sns.barplot(x=filtered_movies.head(10)["avg_rating"], y=filtered_movies.head(10).index)
plt.xlabel("Average Rating")
plt.ylabel("Movie Title")
plt.title("Top 10 Highest Rated Movies (Min 50 Ratings)")
plt.show()








