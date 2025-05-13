# Introduction to Data Science - Hard Questions and Answers

## 1. How do you handle imbalanced datasets in classification problems?
**Answer:**  
Techniques include:
- Resampling (oversampling minority class or undersampling majority class)  
- Using different evaluation metrics (e.g., F1-score, AUC)  
- Applying algorithms like SMOTE  
- Using ensemble methods (e.g., Random Forest, XGBoost with class weights)

---

## 2. Explain the bias-variance tradeoff in machine learning.
**Answer:**  
- **Bias:** Error due to overly simplistic assumptions; leads to underfitting.  
- **Variance:** Error due to too much complexity; leads to overfitting.  
A good model balances both to minimize total error.

---

## 3. What is overfitting and how can it be prevented?
**Answer:**  
Overfitting occurs when a model performs well on training data but poorly on unseen data. Prevention techniques include:
- Cross-validation  
- Regularization (L1/L2)  
- Pruning (in decision trees)  
- Reducing model complexity  
- More training data

---

## 4. Describe a real-world situation where predictive modeling could fail and why.
**Answer:**  
In credit risk modeling during an economic crisis, historical data may not represent current trends, making the model unreliable due to concept drift or non-stationarity.

---

## 5. What is the difference between batch learning and online learning?
**Answer:**  
- **Batch Learning:** The model is trained on the entire dataset at once.  
- **Online Learning:** The model is updated continuously as new data arrives, useful for streaming or real-time applications.

---

## 6. How does regularization improve model performance?
**Answer:**  
Regularization adds a penalty to the loss function to discourage overly complex models and prevent overfitting.  
- **L1 (Lasso):** Can lead to feature selection by shrinking some coefficients to zero.  
- **L2 (Ridge):** Shrinks coefficients but keeps all features.

---

## 7. What is cross-validation, and why is it important?
**Answer:**  
Cross-validation involves splitting the dataset into multiple folds to train and validate the model on different subsets. It ensures the model generalizes well to unseen data and helps avoid overfitting.

---

## 8. What is the curse of dimensionality in Data Science?
**Answer:**  
As the number of features increases, the volume of the feature space grows exponentially, making the data sparse and models less effective. It leads to increased computational cost and lower model performance.

---

## 9. How would you measure model performance in a multi-class classification problem?
**Answer:**  
Common metrics include:
- Accuracy  
- Precision, Recall, and F1-score (micro, macro, and weighted)  
- Confusion matrix  
- ROC-AUC (one-vs-rest approach)

---

## 10. What are some ethical concerns in Data Science?
**Answer:**  
- Data privacy and security  
- Algorithmic bias and fairness  
- Transparency and interpretability  
- Informed consent for data collection  
- Potential misuse of predictive systems (e.g., in hiring or policing)
