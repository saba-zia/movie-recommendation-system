import pandas as pd
import requests
import streamlit as st


@st.cache_data
def get_poster_url(tmdb_id):
    if pd.isna(tmdb_id):
        return "https://via.placeholder.com/300x450?text=No+Poster"

    api_key = st.secrets["TMDB_API_KEY"]

    url = f"https://api.themoviedb.org/3/movie/{int(tmdb_id)}"

    response = requests.get(
        url,
        params={"api_key": api_key}
    )

    if response.status_code != 200:
        return "https://via.placeholder.com/300x450?text=No+Poster"

    data = response.json()
    poster_path = data.get("poster_path")

    if poster_path is None:
        return "https://via.placeholder.com/300x450?text=No+Poster"

    return f"https://image.tmdb.org/t/p/w500{poster_path}"