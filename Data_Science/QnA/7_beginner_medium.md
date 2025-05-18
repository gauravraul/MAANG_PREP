# Data Science - Day 7: Data Preprocessing - Medium Questions

## 1. How would you handle missing values in both numerical and categorical columns?
**Answer:**  
- For numerical: use mean, median, or interpolation  
- For categorical: use mode or create a new category like "Missing"

---

## 2. What is the difference between normalization and standardization?
**Answer:**  
- **Normalization** scales data between 0 and 1 (Min-Max).  
- **Standardization** centers data to have mean 0 and standard deviation 1 (Z-score).

---

## 3. What is the purpose of one-hot encoding?
**Answer:**  
It converts categorical variables into binary columns for each category, allowing models to interpret categorical data numerically.

---

## 4. What are the problems with label encoding for nominal variables?
**Answer:**  
Label encoding assigns integer values to categories, which can falsely imply an ordinal relationship.

---

## 5. What is the impact of outliers on machine learning models?
**Answer:**  
Outliers can skew model parameters, especially in algorithms like linear regression, affecting accuracy and stability.

---

## 6. How do you detect outliers in a dataset?
**Answer:**  
Use:
- Boxplots (IQR method)  
- Z-score method  
- Visualization (scatterplots)  
- Isolation Forest or DBSCAN (for complex cases)

---

## 7. What is the difference between data cleaning and data transformation?
**Answer:**  
- **Data cleaning** fixes errors and inconsistencies.  
- **Data transformation** modifies the structure or scale of data for modeling (e.g., encoding, scaling).

---

## 8. How do you handle imbalanced categorical variables in preprocessing?
**Answer:**  
Use techniques like:
- Combining rare categories  
- Target encoding  
- SMOTE (for resampling, post-preprocessing)

---

## 9. What is log transformation and when is it used?
**Answer:**  
Log transformation reduces skewness in data. It's used when the feature has a long right tail or multiplicative relationships.

---

## 10. Why should you preprocess your training and test sets separately?
**Answer:**  
To avoid data leakage. For example, if you calculate the mean for imputation or scaling on the entire dataset, it leaks information from the test set into the training process.
