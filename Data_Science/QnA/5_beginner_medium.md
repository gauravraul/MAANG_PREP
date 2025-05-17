# Data Science - Day 5: Feature Engineering - Medium Questions

## 1. What is the difference between normalization and standardization?
**Answer:**  
- **Normalization** scales values between 0 and 1 (Min-Max Scaling).  
- **Standardization** transforms data to have zero mean and unit variance (Z-score).

---

## 2. When would you use label encoding instead of one-hot encoding?
**Answer:**  
Label encoding is used when categorical variables have an inherent order (ordinal variables), like "low", "medium", "high".

---

## 3. What are interaction features?
**Answer:**  
Interaction features are created by combining two or more features to capture relationships, such as multiplying or concatenating them.

---

## 4. What is target encoding?
**Answer:**  
Target encoding replaces a categorical variable with the average value of the target for each category.

---

## 5. What are polynomial features?
**Answer:**  
Polynomial features are created by raising numeric features to a power or multiplying features to capture non-linear relationships.

---

## 6. How does domain knowledge help in feature engineering?
**Answer:**  
Domain knowledge can guide meaningful feature creation, such as combining time and location to create a "rush hour" feature in traffic data.

---

## 7. What is feature selection, and why is it useful?
**Answer:**  
Feature selection is the process of choosing the most relevant features. It helps reduce overfitting, speeds up training, and improves model performance.

---

## 8. How can correlation be used in feature engineering?
**Answer:**  
Highly correlated features (multicollinearity) can be dropped or combined to avoid redundancy and instability in models.

---

## 9. How do you handle high cardinality categorical features?
**Answer:**  
Techniques include frequency encoding, target encoding, embedding, or grouping infrequent categories into “Other”.

---

## 10. What is the difference between filter, wrapper, and embedded methods in feature selection?
**Answer:**  
- **Filter**: Select features using statistical tests (e.g., correlation).  
- **Wrapper**: Use model performance (e.g., recursive feature elimination).  
- **Embedded**: Feature selection occurs during model training (e.g., Lasso).
