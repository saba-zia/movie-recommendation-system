# 🎬 CineMatch

A movie recommendation web application built with Python and Streamlit.

CineMatch recommends movies similar to a selected movie using Item-Based Collaborative Filtering and Cosine Similarity. The application also integrates with The Movie Database (TMDB) API to display movie posters and create a more interactive user experience.

---

## 🚀 Live Features

* Search and select a movie
* Generate similar movie recommendations
* Display movie posters using TMDB API
* Show similarity scores
* Adjustable number of recommendations
* Modern Streamlit user interface
* Responsive movie recommendation cards

---

## 📊 Dataset

This project uses the MovieLens Latest Small Dataset.

The dataset contains:

* User ratings
* Movie titles
* Movie IDs
* Genre information
* TMDB movie identifiers

Files used:

* ratings.csv
* movies.csv
* links.csv

---

## 🧠 Recommendation Method

The recommendation engine uses:

### Item-Based Collaborative Filtering

Instead of finding similar users, the system finds movies that receive similar rating patterns from users.

### Workflow

1. Load movie ratings data
2. Create a User-Movie Matrix
3. Fill missing ratings with zeros
4. Compute Cosine Similarity between movies
5. Build a Movie Similarity Matrix
6. Find the most similar movies to the selected movie
7. Display recommendations ranked by similarity score

---

## 📸 TMDB Integration

Movie posters are fetched dynamically using the TMDB API.

Steps:

1. Retrieve TMDB IDs from the MovieLens links dataset
2. Query the TMDB API
3. Extract poster paths
4. Display posters inside the Streamlit application

If a poster is unavailable, a placeholder image is shown.

---

## 🏗️ Project Structure

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

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/movie-recommendation-system.git
cd movie-recommendation-system
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 TMDB API Setup

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
TMDB_API_KEY = "your_api_key_here"
```

You can obtain a free API key from:

https://www.themoviedb.org

Important:

Do not commit your API key to GitHub.

The file is ignored using:

```gitignore
.streamlit/secrets.toml
```

---

## ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-Learn
* Streamlit
* Requests
* TMDB API
* MovieLens Dataset

---

## 📚 Skills Demonstrated

This project demonstrates:

* Data preprocessing
* Exploratory data analysis
* Recommender systems
* Item-based collaborative filtering
* Cosine similarity
* API integration
* Modular Python development
* Streamlit web application development
* Git and GitHub workflows

---

## 🔮 Future Improvements

Potential future enhancements:

* Search bar with autocomplete
* Content-based filtering
* Hybrid recommender system
* User authentication
* Movie details page
* Trailer integration
* Recommendation explanations
* Precision@K and Recall@K evaluation
* Deployment on Streamlit Community Cloud

---

## 👩‍💻 Author

Author

Saba Zia Naserani
Bachelor Student in Artificial Intelligence
Johannes Kepler University Linz