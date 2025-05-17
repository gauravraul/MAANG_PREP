# Data Science - Day 6: Feature Selection - Easy Questions

## 1. What is feature selection?
**Answer:**  
Feature selection is the process of choosing the most relevant features from a dataset to improve model performance and reduce complexity.

---

## 2. Why is feature selection important?
**Answer:**  
It helps:
- Improve model accuracy  
- Reduce overfitting  
- Speed up training  
- Make models more interpretable

---

## 3. What is the difference between feature selection and feature extraction?
**Answer:**  
- **Feature selection** chooses a subset of existing features.  
- **Feature extraction** creates new features from existing ones (e.g., PCA).

---

## 4. Name one simple statistical method used for feature selection.
**Answer:**  
Correlation analysis can be used to identify and remove highly correlated features.

---

## 5. What are filter methods in feature selection?
**Answer:**  
Filter methods use statistical techniques (like correlation or chi-squared tests) to select features independently of any machine learning model.

---

## 6. What is variance thresholding?
**Answer:**  
It removes features with low variance, assuming that constant or near-constant features provide little useful information.

---

## 7. What does the `SelectKBest` method do in scikit-learn?
**Answer:**  
It selects the top **k** features based on a scoring function like chi-squared, ANOVA F-value, or mutual information.

---

## 8. What kind of features can chi-squared test be used on?
**Answer:**  
Chi-squared test is used on categorical features and categorical targets.

---

## 9. Why should you remove features with many missing values?
**Answer:**  
Too many missing values reduce data quality and can introduce bias or unreliability into the model.

---

## 10. How can visualizations help in feature selection?
**Answer:**  
Visual tools like heatmaps or boxplots can reveal correlations, distributions, or outliers, helping identify redundant or uninformative features.
