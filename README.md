# Movie Recommendation System

## Project Overview

This project was developed as part of a university assignment on recommender systems. The goal was to explore different recommendation approaches and compare their performance using real user-movie interaction data.

During the project, I implemented and evaluated several recommendation algorithms, starting from simple baseline methods and progressing to more advanced collaborative filtering techniques.

## Objectives

The main objectives of this project were:

* Understand how recommender systems work
* Build a baseline recommendation model
* Create a user-item interaction matrix
* Implement collaborative filtering methods
* Compare different recommendation algorithms
* Evaluate recommendation quality using standard metrics

## Implemented Methods

### 1. Top Popular (Baseline)

The baseline recommender suggests the most popular movies to all users. This method does not consider personal preferences and serves as a reference point for evaluating more advanced algorithms.

### 2. Average Embedding Similarity

This content-based approach recommends movies by comparing item embeddings and finding similar movies based on their content features.

### 3. Content-Based Item KNN

A K-Nearest Neighbors model that recommends movies similar to those a user has previously interacted with.

### 4. Collaborative Filtering Item KNN

This method recommends movies based on patterns found in user interactions and similarities between items.

### 5. Singular Value Decomposition (SVD)

A matrix factorization technique that discovers hidden relationships between users and movies and generates personalized recommendations.

## Evaluation

The performance of the recommendation algorithms was evaluated using:

* Precision@K
* Recall@K
* Normalized Discounted Cumulative Gain (nDCG)

These metrics measure how relevant and useful the recommendations are for different groups of users.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* SciPy
* Jupyter Notebook
* Matplotlib

## What I Learned

Through this project, I learned how recommendation systems are built, how user-item interaction data is represented, how collaborative filtering works, and how recommendation quality can be evaluated using industry-standard metrics.

## Author

Saba Zia Naserani
