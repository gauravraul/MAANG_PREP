# Data Science - Day 6: Feature Selection - Hard Questions

## 1. How does multicollinearity affect feature selection in linear models?
**Answer:**  
Multicollinearity inflates variance of coefficient estimates, making it hard to determine the effect of individual features. It can lead to misleading interpretations and unstable models.

---

## 2. Explain how SHAP values can be used for feature selection.
**Answer:**  
SHAP values quantify each feature's contribution to predictions. Features with consistently low SHAP values across samples can be removed with minimal impact on model performance.

---

## 3. What is the difference between forward selection and backward elimination?
**Answer:**  
- **Forward selection** starts with no features and adds them one at a time based on performance gain.  
- **Backward elimination** starts with all features and removes the least important ones iteratively.

---

## 4. How can dimensionality reduction techniques like PCA or t-SNE be misused in feature selection?
**Answer:**  
PCA and t-SNE are **feature extraction**, not selection. Using them blindly can reduce interpretability and discard meaningful original features.

---

## 5. How does feature selection differ for linear models versus tree-based models?
**Answer:**  
- Linear models are sensitive to multicollinearity and require scaling and regularization for feature selection.  
- Tree models handle non-linearity and feature interaction but may overfit to noisy features without pruning or importance thresholds.

---

## 6. What are stability selection methods in feature selection?
**Answer:**  
Stability selection repeatedly applies feature selection on bootstrapped samples and selects features that consistently appear. It improves robustness against data variation.

---

## 7. What are the challenges of feature selection in high-dimensional datasets (e.g., genomics)?
**Answer:**  
- Curse of dimensionality  
- Overfitting due to too many irrelevant/noisy features  
- Computational complexity  
- Difficulty identifying meaningful patterns without domain knowledge

---

## 8. How would you perform feature selection for imbalanced datasets?
**Answer:**  
Use performance metrics like AUC, F1-score during selection. Also, avoid features that separate majority/minority classes by chance (e.g., due to imbalance).

---

## 9. What is information gain and how is it used in feature selection?
**Answer:**  
Information gain measures the reduction in entropy when splitting on a feature. It’s used in decision trees to rank and select informative features.

---

## 10. How does the use of cross-validation in wrapper methods prevent overfitting?
**Answer:**  
Cross-validation ensures selected features perform well on unseen data, reducing the risk of overfitting to a specific train/test split.
