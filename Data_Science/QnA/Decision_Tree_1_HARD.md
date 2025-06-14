# Advanced Decision Trees – 10 Toughest Questions and Answers

## 1. What are the key differences between Gini Impurity and Entropy as splitting criteria?
**Answer:**  
- **Entropy**: Measures information gain using logarithms; it's more computationally expensive.  
  Formula: **–∑pᵢ log₂(pᵢ)**
- **Gini Impurity**: Measures impurity directly without logarithms; it's faster and often yields similar results.  
  Formula: **1 – ∑pᵢ²**
- Both aim to find the best split, but Gini tends to isolate the most frequent class early.

---

## 2. Why are decision trees prone to overfitting, and how can you prevent it?
**Answer:**  
Decision trees can memorize the training data if allowed to grow deep (high variance).  
**Prevention methods:**
- **Pruning (post/pre)**
- **Setting max depth, min samples split/leaf**
- **Using ensemble methods (e.g., Random Forest)**

---

## 3. Explain information gain. Why might it be biased toward features with many levels?
**Answer:**  
**Information gain = Entropy(parent) – Weighted sum of entropy(children)**  
It is biased toward features with many unique values (e.g., ID column), which may lead to overfitting.  
**Solution:** Use **Gain Ratio**, which normalizes by the intrinsic information of a split.

---

## 4. What is pruning in decision trees? Differentiate between pre-pruning and post-pruning.
**Answer:**  
- **Pre-pruning**: Stops tree growth early based on constraints (max depth, min samples).
- **Post-pruning**: Grows the full tree first, then prunes subtrees based on validation performance.  
Post-pruning usually yields better generalization but is computationally more expensive.

---

## 5. How does the CART algorithm differ from ID3 or C4.5?
**Answer:**  
- **ID3**: Uses entropy/information gain, handles categorical data only.
- **C4.5**: Extension of ID3, uses gain ratio, supports continuous features, handles missing values.
- **CART (Classification and Regression Trees)**:
  - Uses **Gini** (classification) and **MSE** (regression).
  - Produces **binary splits** only.
  - Supports pruning.

---

## 6. How does a decision tree handle missing values during training and inference?
**Answer:**  
Techniques include:
- **Surrogate splits**: Use alternate features highly correlated with the primary splitting feature.
- **Probabilistic assignment**: Assign samples to branches proportionally.
- **Imputation**: Fill missing values before training (mean, mode, etc.).

---

## 7. What is the curse of dimensionality in the context of decision trees?
**Answer:**  
In high-dimensional space, data becomes sparse, making it hard to find meaningful splits. Trees may:
- Overfit noise
- Fail to generalize  
Solution: Use dimensionality reduction or ensemble methods like Random Forests.

---

## 8. Can decision trees be used for multi-output (multi-target) prediction? How?
**Answer:**  
Yes. Decision trees can be extended for multi-output by:
- Splitting to minimize combined impurity across all targets.
- Predicting a vector at each leaf node.
Implemented in libraries like `sklearn` as `DecisionTreeRegressor(classifier)(multi_output=True)`.

---

## 9. Why are decision boundaries formed by decision trees always axis-aligned?
**Answer:**  
Decision trees split one feature at a time using a threshold → resulting boundaries are parallel to axes (vertical or horizontal cuts).  
**Limitation:** They struggle with oblique boundaries, unlike models like SVMs.

---

## 10. Explain the variance and bias characteristics of decision trees.
**Answer:**  
- **High variance**: Small changes in data → very different tree.
- **Low bias**: Capable of modeling complex relationships.  
This is why decision trees overfit easily and benefit from ensemble methods like Bagging (Random Forests) to reduce variance.
