# Wine Quality Score Classifier - Random Forest Classifier and GridSearch

## Objective

The objective of this project is to use historical wine quality tests data to create a model that can forecast quality scores based on wine physical attributes. 

## Steps Followed

- **Importing Libraries**  
- **Importing the Dataset**  
- **Cleaning and Formatting the Data**  
- **Selectin Parameters with GridSearch**
- **Creating a Random Forest Classifier**  

- **Testing the Model**  

## **Importing Libraries and Dataset**

The following Python libraries were used in this project:

- **pandas** – for data manipulation and analysis  
- **matplotlib.pyplot** – for data visualization  
- **scikit-learn (sklearn)** – for machine learning tasks including:
  - `train_test_split` – to split the dataset into training and testing sets
  - `RandomForestClassifier` – to build a random forest classifier model
  - `classification_report`, `accuracy_score`, `confusion_matrix` - to test model accuracy
  - `GridSearchCV` – for hyperparameter tuning
  - `plot_tree` - to visualize random forest classifer tree

After importing the libraries, the data sets (CSV files) were uploaded and converted into a DataFrame.

## **Cleaning and Formatting the Data**

Minimal data clenaing was needed due to the high quality of the data set. 

## **Selectin Parameters with GridSearch**

`GridSearch` was used to find the best parameters within these guidelines:

```python
# Find best parameters
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2']
}

# Create random forest model
rf = RandomForestClassifier(random_state=42)

# Run grid search to find best parameters
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, 
                           cv=5, scoring='accuracy', n_jobs=-1)
```

## **Creating a a Random Forest Classifier**

A random forest classifier was used to forecast wine quality scores.  

> Random forest is a commonly-used machine learning algorithm, trademarked by Leo Breiman and Adele Cutler, that combines the output of multiple decision trees to reach a single result. Its ease of use and flexibility have fueled its adoption, as it handles both classification and regression problems. (IBM, 2025).  

## **Testing the Program**

After making predictions with the random forest model, its accuracy was testing using the following metric:

```python
# Print accuracy score
print("Accuracy:", accuracy_score(y_test, y_pred))
```

## **References**
[IBM - What is random forest?](https://www.ibm.com/think/topics/random-forest)