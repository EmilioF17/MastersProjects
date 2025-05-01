# Almond Pricing Forecast - Linear and Ridge Regressions

## Objective

The objective of this project is attempt to forecast almond prices utilizing a linear regression. Almond historical production & prices and US population data were obtaiend from the [USDA](https://www.ers.usda.gov/data-products/fruit-and-tree-nuts-data/fruit-and-tree-nuts-yearbook-tables). In addtion, the US Dollar Index data, which calculates the strength of the dollar against major currencies, was obtained from [Finance Yahoo](https://finance.yahoo.com/quote/DX-Y.NYB/)

## Steps Followed

- **Importing Libraries**  
- **Importing the Dataset**  
- **Cleaning and Formatting the Data**  
- **Creating a Linear Regression**  
- **Testing the Model**
- **Creating a Ridge Regression**
- **Testing the Model**  

## **Importing Libraries and Dataset**

The following Python libraries were used in this project:

- **pandas** – for data manipulation and analysis  
- **numpy** – for numerical operations  
- **matplotlib.pyplot** – for data visualization  
- **seaborn** – for statistical data visualization  
- **scikit-learn (sklearn)** – for machine learning tasks including:
  - `train_test_split` – to split the dataset into training and testing sets
  - `LinearRegression` – to build a linear regression model
  - `mean_absolute_error`, `mean_squared_error`, `r2_score` – to evaluate model performance
  - `StandardScaler` – to standardize features
  - `Ridge` – for ridge regression modeling
  - `GridSearchCV` – for hyperparameter tuning
- **statsmodels** – specifically:
  - `variance_inflation_factor` – to assess multicollinearity in features

After importing the libraries, the data sets (CSV files) were uploaded and converted into a DataFrame.

## **Cleaning and Formatting the Data**

The following steps were followed to prepare the data for modeling:

- The `almond_df`, and the `uspopulation_df` data frames were merged together.  
- The `usindex_df` was filtered to only include data from 1981 to 2024.
- All three data frames were merged together into one data frame: `almond_df`. 

## **Creating a Linear Regression**

A multiple linear regression was used to forecast the pricing of almonds.  

> In statistics, linear regression is a model that estimates the relationship between a scalar response (dependent variable) and one or more explanatory variables (regressor or independent variable). (Wikipedia, 2025).  

## **Testing the Program**

After making predictions with the linear regression model, its accuracy was testing using the following metrics:

```python
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

## **Creating a Ridge Regression**

The linear regression showed high correlation between variables. A ridge regression was used to account for that issue.  

> Ridge regression (also known as Tikhonov regularization, named for Andrey Tikhonov) is a method of estimating the coefficients of multiple-regression models in scenarios where the independent variables are highly correlated.  It is particularly useful to mitigate the problem of multicollinearity in linear regression, which commonly occurs in models with large numbers of parameters. (Wikipedia, 2025).  

Features were scaled using `StandardScaler()`. The the ridge regression model was used. 

## **Testing the Program**

The same metrics were used to test this model accuracy:

```python
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

## **References**
[Wikipedia - Linear Regression](https://en.wikipedia.org/wiki/Linear_regression)

[Wikipedia - Ridge Regression](https://en.wikipedia.org/wiki/Ridge_regression)