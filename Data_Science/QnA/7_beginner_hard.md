# Data Science - Day 7: Data Preprocessing - Hard Questions

## 1. What is data leakage and how can it occur during preprocessing?
**Answer:**  
Data leakage happens when information from outside the training dataset is used to create the model, often through improper preprocessing (e.g., using test data to calculate mean for imputation).

---

## 2. How does the choice of imputation method affect model performance?
**Answer:**  
Different imputation strategies can introduce bias or reduce variance. Mean imputation may distort distributions, while model-based or KNN imputation preserves structure better but may increase complexity.

---

## 3. When would you choose robust scaling over standard scaling?
**Answer:**  
Use robust scaling when the data contains many outliers. It uses the median and interquartile range instead of mean and standard deviation.

---

## 4. Explain how time-dependent data should be preprocessed differently from static data.
**Answer:**  
In time series, preprocessing must respect temporal order. You must:
- Avoid shuffling data  
- Use time-based splitting  
- Create lag and rolling features  
- Prevent lookahead bias during imputation or scaling

---

## 5. What are some challenges in preprocessing high-dimensional datasets?
**Answer:**  
- Increased sparsity  
- High computational cost  
- Risk of overfitting  
- Feature selection becomes harder  
- Many irrelevant or redundant features

---

## 6. How would you preprocess text data for a machine learning model?
**Answer:**  
- Clean text (remove punctuation, stop words, etc.)  
- Tokenize  
- Convert to numerical format (TF-IDF, Bag-of-Words, embeddings)  
- Handle high dimensionality with truncation or dimensionality reduction

---

## 7. How does preprocessing differ for unsupervised learning tasks?
**Answer:**  
You may not know the target variable, so you rely more on:
- Scaling  
- Dimensionality reduction (e.g., PCA)  
- Encoding and cleaning without any label information  
- Clustering-specific preparation (e.g., distance metric compatibility)

---

## 8. What is quantile transformation and when is it useful?
**Answer:**  
It maps data to a uniform or normal distribution using quantiles. Useful when features have heavy skew or non-Gaussian distribution, especially for models assuming normality.

---

## 9. How would you preprocess a dataset containing both numerical and categorical features for a neural network?
**Answer:**  
- Normalize numerical features  
- Use embedding layers or one-hot encoding for categorical features  
- Handle missing values  
- Optionally batch/standardize inputs for better convergence

---

## 10. How do pipelines in libraries like scikit-learn help manage preprocessing?
**Answer:**  
Pipelines chain preprocessing and modeling steps, ensuring consistent and leak-proof transformations. They simplify code and help during cross-validation and model deployment.
