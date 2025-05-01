# Movie Recommender Program

## Objective

The objective of this project is to create a movie recommender program. A movie dataset from [GroupLens](https://grouplens.org) was utilized. This dataset includes the name, year of release, and genre(s) of thousands of movies.

## Steps Followed

- **Importing Libraries**  
- **Importing the Dataset**  
- **Cleaning and Formatting the Data**  
- **Creating a Recommender Program**  
- **Testing the Program**  

## **Importing Libraries and Dataset**

Two libraries were used: `pandas` and `cosine_similarity` from `sklearn.metrics.pairwise`. After importing the libraries, the movie dataset (a CSV file) was uploaded and converted into a DataFrame.

## **Cleaning and Formatting the Data**

The dataset included movie names, release years, and genre(s) in a single column. The following transformations were applied:

- The **movie name** and **year of release** were split into separate columns.  
- The **genre column**, which contained multiple genres in one cell, was expanded into multiple columns using one-hot encoding (`get_dummies()`).  

## **Creating a Recommender Program**

Cosine similarity was used to compute similarity scores between movies based on genre.  

> Cosine similarity is a mathematical metric that measures the similarity between two vectors in a multi-dimensional space by calculating the cosine of the angle between them (Wikipedia, 2025).  

- If two movies have **identical genres**, their cosine similarity score is **1.0**.  
- If two movies are **completely different**, their cosine similarity score is **0**.  

A **genre similarity matrix** was created using the `cosine_similarity()` method from `sklearn.metrics.pairwise`.  

A function was developed to:  
1. Accept a movie name as input.  
2. Look up the movie in the dataset.  
3. Find the **top 10 most similar movies** using cosine similarity.  
4. Display an **error message** if the movie is not found.  

The similarity scores were extracted and sorted. The top 10 most similar movies (excluding the user-input movie itself) were returned.

## **Testing the Program**

The program was tested and the outcomes were acceptable:  

- Displayed an **error message** when a movie was not found.  
- Provided a **list of similar movies** when a valid movie was entered.  

## **References**
[Wikipedia - Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)