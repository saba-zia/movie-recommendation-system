import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity


@st.cache_data
def build_similarity_matrix(ratings):
    user_movie_matrix = ratings.pivot_table(
        index="userId",
        columns="movieId",
        values="rating"
    )

    user_movie_filled = user_movie_matrix.fillna(0)

    movie_similarity = cosine_similarity(user_movie_filled.T)

    movie_similarity_df = pd.DataFrame(
        movie_similarity,
        index=user_movie_filled.columns,
        columns=user_movie_filled.columns
    )

    return movie_similarity_df


def recommend_similar_movies(movie_id, movies, movie_similarity_df, n=10):
    similar_movies = (
        movie_similarity_df[movie_id]
        .sort_values(ascending=False)
        .reset_index()
    )

    similar_movies = similar_movies.rename(
        columns={
            "movieId": "movieId",
            movie_id: "similarity_score"
        }
    )

    similar_movies = similar_movies.merge(
        movies,
        on="movieId",
        how="left"
    )

    similar_movies = similar_movies[
        similar_movies["movieId"] != movie_id
    ]

    recommendations = similar_movies[
        ["title", "genres", "similarity_score", "tmdbId"]
    ].head(n)

    return recommendations