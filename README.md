# Movie Recommendation System

## Project Overview

This project implements a movie recommendation system using collaborative filtering techniques on the MovieLens dataset.

The objective is to explore how recommender systems work by building a complete recommendation pipeline, starting from raw user ratings and ending with personalized movie recommendations.

The project was developed in Python using Pandas, NumPy, Scikit-Learn, and Jupyter Notebook.

---

## Dataset

The project uses the MovieLens dataset, which contains:

* User IDs
* Movie IDs
* Movie titles
* User ratings

Each user can rate multiple movies on a scale from 0.5 to 5.0 stars.

---

## Stage 1: Data Loading and Exploration

The first step was loading the dataset and exploring its structure.

Tasks completed:

* Loaded ratings data
* Loaded movie metadata
* Inspected missing values
* Checked dataset dimensions
* Explored rating distributions
* Examined user activity and movie popularity

Purpose:

To understand the data before building recommendation models.

---

## Stage 2: User-Movie Matrix Construction

A user-item interaction matrix was created.

Rows represent:

* Users

Columns represent:

* Movies

Values represent:

* Ratings

Example:

| User   | Movie A | Movie B | Movie C |
| ------ | ------- | ------- | ------- |
| User 1 | 5       | 4       | 0       |
| User 2 | 3       | 0       | 5       |

Missing ratings were filled with zeros.

Purpose:

This matrix is the foundation of collaborative filtering.

---

## Stage 3: Cosine Similarity Between Users

User similarity was computed using Cosine Similarity.

Cosine similarity measures how similar two users are based on their rating behavior.

Values range from:

* 1 → identical preferences
* 0 → unrelated preferences
* -1 → opposite preferences

Purpose:

To identify users with similar movie tastes.

---

## Stage 4: User-Based Collaborative Filtering

For a target user:

1. Find the most similar users.
2. Collect their ratings.
3. Use those ratings to generate recommendations.

Example:

If User A and User B have very similar tastes, movies liked by User B can be recommended to User A.

Purpose:

Generate personalized recommendations using neighboring users.

---

## Stage 5: Singular Value Decomposition (SVD)

Dimensionality reduction was applied using Singular Value Decomposition (SVD).

SVD decomposes the user-movie matrix into latent factors that capture hidden relationships between users and movies.

Benefits:

* Reduces noise
* Compresses information
* Captures hidden preference patterns
* Improves recommendation quality

Purpose:

Create a more powerful collaborative filtering model.

---

## Stage 6: User Similarity in Latent Space

After applying SVD:

* User feature vectors were generated.
* Cosine similarity was calculated again using latent features.

This produces similarity scores based on hidden preferences rather than only explicit ratings.

Purpose:

Find users with similar underlying interests.

---

## Stage 7: Personalized Movie Recommendations

Recommendations were generated using:

1. The most similar users found in latent space.
2. Their average movie ratings.
3. Removal of movies already watched by the target user.
4. Ranking remaining movies by predicted score.

Example recommended movies:

* Terminator 2: Judgment Day (1991)
* The Godfather (1972)
* Blade Runner (1982)
* Aliens (1986)
* The Sixth Sense (1999)
* Die Hard (1988)

Purpose:

Provide personalized unseen movie recommendations.

---

## Stage 8: Evaluation

The recommendation model was evaluated using Root Mean Squared Error (RMSE).

RMSE measures the difference between:

* Original ratings
* Ratings reconstructed by SVD

Formula:

RMSE = sqrt(MSE)

Result:

RMSE = 0.352

Interpretation:

A lower RMSE indicates better reconstruction quality.

An RMSE of 0.352 suggests that the SVD model captures the rating patterns effectively and produces reasonable predictions.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* SciPy
* Jupyter Notebook
* Matplotlib

---

## Skills Demonstrated

This project demonstrates:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Matrix manipulation
* Cosine similarity
* Collaborative filtering
* Recommendation systems
* Singular Value Decomposition (SVD)
* Model evaluation with RMSE
* Data analysis using Python

---

## Future Improvements

Possible future enhancements include:

* Item-based collaborative filtering
* Content-based recommendations
* Hybrid recommender systems
* Precision@K evaluation
* Recall@K evaluation
* nDCG evaluation
* Interactive web application using Streamlit

---

## Author

Saba Zia Naserani
Bachelor's Student in Artificial Intelligence and Computer Science
