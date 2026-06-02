import streamlit as st

from src.data_loader import load_data
from src.recommender import build_similarity_matrix, recommend_similar_movies
from src.poster_fetcher import get_poster_url


st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide"
)


st.markdown("""
<style>
.stApp {
    background-color: #0f172a;
}

.main-title {
    text-align: center;
    font-size: 56px;
    font-weight: 800;
    color: #ffffff;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 40px;
}

.movie-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 22px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.30);
    border-left: 6px solid #f97316;
}

.movie-title {
    font-size: 22px;
    font-weight: 700;
    color: #ffffff;
}

.movie-info {
    font-size: 15px;
    color: #cbd5e1;
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 50px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)


st.markdown(
    """
    <div class="main-title">🎬 CineMatch</div>
    <div class="subtitle">Find movies similar to the ones you love.</div>
    """,
    unsafe_allow_html=True
)


movies, ratings = load_data()
movie_similarity_df = build_similarity_matrix(ratings)


st.sidebar.title("⚙️ Settings")

number_of_recommendations = st.sidebar.slider(
    "Number of recommendations",
    min_value=5,
    max_value=20,
    value=10
)

st.sidebar.info(
    "CineMatch uses item-based collaborative filtering and cosine similarity."
)


selected_movie = st.selectbox(
    "Search a movie:",
    movies["title"].sort_values().values
)

selected_movie_id = movies[
    movies["title"] == selected_movie
]["movieId"].values[0]

selected_movie_data = movies[
    movies["movieId"] == selected_movie_id
].iloc[0]

selected_poster_url = get_poster_url(
    selected_movie_data["tmdbId"]
)


st.markdown("### Selected Movie")

col1, col2 = st.columns([1, 4])

with col1:
    st.image(selected_poster_url, width=150)

with col2:
    st.markdown(f"### 🎬 {selected_movie_data['title']}")
    st.write(f"Genres: {selected_movie_data['genres']}")
    st.write(f"Movie ID: {selected_movie_id}")


if st.button("🎯 Recommend"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend_similar_movies(
            selected_movie_id,
            movies,
            movie_similarity_df,
            number_of_recommendations
        )

    st.subheader("Recommended Movies")

    for _, row in recommendations.iterrows():
        poster_url = get_poster_url(row["tmdbId"])

        col1, col2 = st.columns([1, 4])

        with col1:
            st.image(poster_url, width=130)

        with col2:
            st.markdown(
                f"""
                <div class="movie-card">
                    <div class="movie-title">🎥 {row['title']}</div>
                    <p class="movie-info"><b>Genres:</b> {row['genres']}</p>
                    <p class="movie-info"><b>Similarity Score:</b> {row['similarity_score']:.3f}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


st.markdown(
    """
    <div class="footer">
        Built with Python, Pandas, Scikit-Learn and Streamlit.
    </div>
    """,
    unsafe_allow_html=True
)