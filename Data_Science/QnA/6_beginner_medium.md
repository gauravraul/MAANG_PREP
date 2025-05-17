# Data Science - Day 6: Feature Selection - Medium Questions

## 1. What are wrapper methods in feature selection?
**Answer:**  
Wrapper methods evaluate feature subsets by training models on them and selecting the combination that yields the best model performance. Example: Recursive Feature Elimination (RFE).

---

## 2. How does Recursive Feature Elimination (RFE) work?
**Answer:**  
RFE repeatedly builds a model, removes the least important feature(s), and repeats the process until the desired number of features remains.

---

## 3. What are embedded methods in feature selection?
**Answer:**  
Embedded methods perform feature selection during model training. Example: Lasso (L1 regularization) automatically shrinks some feature coefficients to zero.

---

## 4. What is Lasso regularization and how does it help in feature selection?
**Answer:**  
Lasso adds an L1 penalty to the loss function, encouraging sparsity by reducing some coefficients to zero, effectively removing those features.

---

## 5. When would you use mutual information for feature selection?
**Answer:**  
Mutual information measures how much knowing one variable reduces uncertainty about another. It's useful for detecting non-linear relationships between features and target.

---

## 6. What is the risk of using highly correlated features in a model?
**Answer:**  
They can lead to multicollinearity, making model coefficients unstable and reducing interpretability in linear models.

---

## 7. What is the difference between univariate and multivariate feature selection?
**Answer:**  
- **Univariate** considers each feature individually with respect to the target.  
- **Multivariate** considers interactions between features and their combined effect.

---

## 8. How can cross-validation be used in feature selection?
**Answer:**  
Cross-validation ensures selected features generalize well by testing their performance across different training/test splits.

---

## 9. What is the role of feature importance in tree-based models?
**Answer:**  
Tree models (e.g., Random Forest) assign importance scores based on how much each feature reduces impurity. Features with low importance can be removed.

---

## 10. How do you choose the number of features to keep?
**Answer:**  
Common approaches:
- Use cross-validation to test performance for different feature counts  
- Set a threshold on importance or p-values  
- Select top-k features using metrics like mutual information or model performance
