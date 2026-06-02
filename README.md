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
# 🎬 CineMatch – Movie Recommendation System

[Live Demo](https://cinematch-saba.streamlit.app)

CineMatch is a movie recommendation web application that suggests movies similar to a selected title using **Item-Based Collaborative Filtering** and **Cosine Similarity**. The application integrates with **The Movie Database (TMDB) API** to display movie posters and provide a more engaging user experience.

---

## Application Preview

> Add a screenshot of your application here.

```markdown
![CineMatch Screenshot](assets/cinematch.png)
```

---

## Features

* Movie recommendation engine based on user rating patterns
* Item-Based Collaborative Filtering
* Cosine Similarity computation
* Dynamic movie poster retrieval through TMDB API
* Adjustable number of recommendations
* Interactive Streamlit user interface
* Cloud deployment with Streamlit Community Cloud

---

## Dataset

This project uses the **MovieLens Latest Small Dataset**, which contains:

* User ratings
* Movie titles
* Genre information
* Movie identifiers
* TMDB identifiers

Files used:

```text
ratings.csv
movies.csv
links.csv
```

---

## Recommendation Method

The recommendation engine follows these steps:

1. Load MovieLens ratings data
2. Create a user–movie rating matrix
3. Replace missing ratings with zeros
4. Compute cosine similarity between movies
5. Build a movie similarity matrix
6. Identify the most similar movies
7. Rank recommendations by similarity score
8. Display recommendations with movie posters

This approach allows the system to recommend movies that have received similar rating patterns from users.

---

## TMDB API Integration

Movie posters are retrieved dynamically using the TMDB API.

Workflow:

1. Retrieve TMDB IDs from the MovieLens dataset
2. Query the TMDB API
3. Extract poster information
4. Display posters inside the application
5. Show a fallback message when poster data is unavailable

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

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## TMDB API Setup

Create:

```text
.streamlit/secrets.toml
```

Add your API key:

```toml
TMDB_API_KEY = "your_api_key_here"
```

Get a free API key from:

https://www.themoviedb.org

> Note: The API key is excluded from version control using `.gitignore`.

---

## Run the Application

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

* Recommender Systems
* Collaborative Filtering
* Cosine Similarity
* Data Preprocessing
* API Integration
* Modular Python Development
* Streamlit Application Development
* Git & GitHub Workflows
* Cloud Deployment

---

## Lessons Learned

Through this project, I gained hands-on experience in building recommender systems, working with user-item interaction data, integrating third-party APIs, deploying web applications, and creating interactive data-driven applications using Streamlit.

---

## Future Improvements

Potential enhancements include:

* Content-Based Filtering
* Hybrid Recommendation Systems
* Search Autocomplete
* Movie Details Page
* Trailer Integration
* Recommendation Explanations
* User Authentication
* Recommendation Quality Evaluation (Precision@K, Recall@K, nDCG)

---

## Author

**Saba Zia Naserani**

BSc Student in Artificial Intelligence
Johannes Kepler University Linz
