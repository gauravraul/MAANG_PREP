# Advanced Model Evaluation – 10 Toughest Questions and Answers

## 1. Why is accuracy not a reliable metric for imbalanced datasets?
**Answer:**  
Accuracy can be misleading in imbalanced datasets.  
Example: In a dataset with 95% negatives, predicting everything as negative gives 95% accuracy, but zero recall for the minority class.  
**Better metrics**: Precision, Recall, F1-score, ROC-AUC, PR-AUC.

---

## 2. What is the difference between ROC-AUC and PR-AUC, and when should each be used?
**Answer:**  
- **ROC-AUC**: Measures true positive rate vs false positive rate.  
  - Useful when **both classes are equally important**.
- **PR-AUC**: Measures precision vs recall.  
  - More informative in **highly imbalanced datasets** (focuses on positive class performance).

---

## 3. Explain the concept of calibration in probabilistic classifiers.
**Answer:**  
Calibration refers to how well a model’s predicted probabilities match the true likelihood.  
- A model that predicts 0.8 should be correct ~80% of the time.  
- **Calibrated models**: Logistic Regression  
- **Uncalibrated models**: Random Forest, SVM  
- Techniques: **Platt Scaling, Isotonic Regression**

---

## 4. What is the difference between cross-validation and bootstrap validation?
**Answer:**  
- **Cross-validation (e.g., k-fold)**: Divides data into k subsets, trains on k–1 and tests on the remaining.
- **Bootstrap**: Samples with replacement and evaluates on out-of-bag samples.  
Bootstrap is more useful for **small datasets** or **estimating variance** of performance.

---

## 5. How does class imbalance affect Precision, Recall, and F1-score?
**Answer:**  
- **Precision**: Falls when many false positives.
- **Recall**: Falls when many false negatives.
- **F1-score**: Harmonic mean of precision and recall, penalizes imbalance in either.  
Class imbalance skews these metrics → use **macro/weighted averaging** or **resampling techniques**.

---

## 6. Why is it dangerous to use the test set repeatedly during model selection?
**Answer:**  
Repeatedly evaluating on the test set leads to **data leakage** and **overfitting to the test set**, resulting in optimistic performance estimates.  
**Proper method**: Use **validation set** for tuning and reserve **test set for final evaluation only**.

---

## 7. What is Cohen’s Kappa and how does it improve upon accuracy?
**Answer:**  
Cohen’s Kappa measures inter-rater agreement **adjusted for chance**:  
\[
\kappa = \frac{p_o - p_e}{1 - p_e}
\]
Where p_o is observed agreement and p_e is expected agreement by chance.  
Kappa is useful in **imbalanced datasets** and **multi-class problems**.

---

## 8. Explain the trade-off between Precision and Recall using the decision threshold.
**Answer:**  
- Lowering threshold increases **recall** (more positives caught) but reduces **precision** (more false positives).
- Raising threshold does the opposite.  
The **Precision-Recall Curve** visualizes this trade-off. Choose threshold based on business context (e.g., fraud detection vs spam filtering).

---

## 9. What is the Brier Score and when is it used?
**Answer:**  
Brier Score measures the **mean squared difference** between predicted probabilities and actual outcomes:  
\[
\text{Brier Score} = \frac{1}{N} \sum_{i=1}^N (p_i - y_i)^2
\]
Used to evaluate **probabilistic predictions** in **binary classification**; lower is better. It combines both **calibration and sharpness**.

---

## 10. How would you evaluate a multi-label classification model?
**Answer:**  
In multi-label problems (samples can have multiple labels), use:
- **Subset accuracy** (strict, all labels must match)
- **Hamming loss** (fraction of wrong labels)
- **Micro / Macro averaged Precision, Recall, F1**
- **Label ranking loss or coverage error**  
Evaluation depends on whether label cardinality and order matter.
