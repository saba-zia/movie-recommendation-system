# 🎬 CineMatch

### Live Demo

https://cinematch-saba.streamlit.app

CineMatch is a movie recommendation web application built with Python and Streamlit. The system recommends movies similar to a selected title using Item-Based Collaborative Filtering and Cosine Similarity. It also integrates with The Movie Database (TMDB) API to display movie posters and improve the user experience.

---

## Features

* Search and select a movie from the MovieLens dataset
* Generate movie recommendations based on rating similarity
* Display movie posters using the TMDB API
* Show similarity scores for recommended movies
* Adjust the number of recommendations
* Interactive web interface built with Streamlit
* Cloud deployment with Streamlit Community Cloud

---

## Dataset

This project uses the **MovieLens Latest Small Dataset**.

The dataset includes:

* User ratings
* Movie titles
* Genre information
* Movie identifiers
* TMDB identifiers

Files used in this project:

```text
ratings.csv
movies.csv
links.csv
```

---

## Recommendation Approach

The recommendation engine is based on **Item-Based Collaborative Filtering**.

Instead of finding users with similar preferences, the system identifies movies that receive similar rating patterns from users.

### Workflow

1. Load movie ratings data
2. Create a user–movie rating matrix
3. Replace missing ratings with zeros
4. Compute cosine similarity between movies
5. Build a movie similarity matrix
6. Identify the most similar movies
7. Rank recommendations by similarity score
8. Display recommendations together with movie posters

---

## TMDB API Integration

Movie posters are retrieved dynamically through the TMDB API.

Process:

1. Retrieve TMDB IDs from the MovieLens dataset
2. Send requests to the TMDB API
3. Extract poster information
4. Display posters within the application
5. Show a fallback message when no poster is available

---

## Project Structure

```text
movie-recommendation-system/
│
├── .streamlit/
│   └── secrets.toml
│
├── data/
│   └── raw/
│       ├── ratings.csv
│       ├── movies.csv
│       └── links.csv
│
├── src/
│   ├── data_loader.py
│   ├── recommender.py
│   └── poster_fetcher.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/saba-zia/movie-recommendation-system.git
cd movie-recommendation-system
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## TMDB API Setup

Create the following file:

```text
.streamlit/secrets.toml
```

Add your TMDB API key:

```toml
TMDB_API_KEY = "your_api_key_here"
```

You can obtain a free API key from:

https://www.themoviedb.org

**Note:** The API key should never be committed to GitHub. The `secrets.toml` file is excluded through `.gitignore`.

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* Streamlit
* Requests
* TMDB API
* MovieLens Dataset

---

## Skills Demonstrated

This project demonstrates:

* Data preprocessing
* Recommender systems
* Collaborative filtering
* Cosine similarity
* API integration
* Modular Python development
* Streamlit application development
* Git and GitHub workflows
* Cloud deployment

---

## Future Improvements

Potential future enhancements include:

* Content-based recommendations
* Hybrid recommender systems
* Search autocomplete
* Movie details page
* Trailer integration
* Recommendation explanations
* User authentication
* Recommendation quality evaluation (Precision@K, Recall@K, nDCG)

---

## Author

**Saba Zia Naserani**

BSc Student in Artificial Intelligence
Johannes Kepler University Linz
