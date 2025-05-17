# Data Science - Day 5: Feature Engineering - Hard Questions

## 1. What is multicollinearity and how can it impact a model?
**Answer:**  
Multicollinearity occurs when two or more features are highly correlated. It can make model coefficients unstable and reduce interpretability, especially in linear models.

---

## 2. How does PCA (Principal Component Analysis) relate to feature engineering?
**Answer:**  
PCA is a dimensionality reduction technique that transforms original features into uncorrelated components while retaining most of the data variance. It helps reduce noise and multicollinearity.

---

## 3. Explain how embeddings work for categorical variables.
**Answer:**  
Embeddings represent high-cardinality categorical variables as dense vectors in lower-dimensional space, typically learned during training in deep learning models.

---

## 4. What is feature drift and how can it be detected?
**Answer:**  
Feature drift occurs when the statistical properties of a feature change over time, potentially degrading model performance. It can be detected using population stability index (PSI) or KL divergence.

---

## 5. How can SHAP values help in feature engineering?
**Answer:**  
SHAP (SHapley Additive exPlanations) values explain feature importance and interactions, guiding the creation or elimination of features based on their true impact on model predictions.

---

## 6. How do you create time-based features for a time series model?
**Answer:**  
You can extract features like:
- Hour, day, month, weekday  
- Lag features  
- Rolling averages  
- Time since an event or season indicators

---

## 7. What is the impact of feature scaling on distance-based algorithms like KNN?
**Answer:**  
Unscaled features can dominate distance calculations, leading to biased predictions. Scaling ensures all features contribute equally.

---

## 8. Describe a situation where feature engineering solved a data leakage problem.
**Answer:**  
In a churn model, using “last login date” calculated after the prediction period introduces leakage. Instead, a proper feature like “days since last login before cutoff date” avoids this.

---

## 9. What are hashing tricks in feature engineering?
**Answer:**  
Hashing tricks convert categorical variables into fixed-size vectors using a hash function, useful for high-cardinality features in large datasets with memory constraints.

---

## 10. How do tree-based models handle feature engineering differently than linear models?
**Answer:**  
Tree-based models are robust to outliers, don’t need feature scaling, and can automatically capture non-linear relationships and feature interactions without extensive manual engineering.
