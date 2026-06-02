import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    movies = pd.read_csv("data/raw/movies.csv")
    ratings = pd.read_csv("data/raw/ratings.csv")
    links = pd.read_csv("data/raw/links.csv")

    movies = movies.merge(
        links[["movieId", "tmdbId"]],
        on="movieId",
        how="left"
    )

    return movies, ratings