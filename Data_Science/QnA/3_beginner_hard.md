# Data Science - Day 3: Data Collection and Preprocessing (Hard Questions)

## 1. How would you design a robust data preprocessing pipeline for a machine learning model?
**Answer:**  
A robust pipeline includes:
- Handling missing values  
- Encoding categorical variables  
- Detecting and treating outliers  
- Feature scaling and transformation  
- Automating steps using tools like `scikit-learn Pipeline` or `FeatureUnion`

---

## 2. What are the implications of imbalanced data during preprocessing?
**Answer:**  
Imbalanced data can bias the model toward the majority class. It may require:
- Resampling (oversampling/undersampling)  
- Generating synthetic data (e.g., SMOTE)  
- Using appropriate evaluation metrics (e.g., F1-score, AUC)

---

## 3. How does multicollinearity affect preprocessing and model training?
**Answer:**  
Multicollinearity occurs when features are highly correlated. It can:
- Cause instability in regression coefficients  
- Make interpretation harder  
- Be addressed using PCA, VIF, or dropping redundant features

---

## 4. What is the difference between data augmentation and data generation?
**Answer:**  
- **Data augmentation** adds variety to existing data (e.g., rotating images, noise injection).  
- **Data generation** creates new synthetic data points from models like GANs or using statistical rules.

---

## 5. How would you preprocess text data for Natural Language Processing tasks?
**Answer:**  
Text preprocessing includes:
- Lowercasing  
- Tokenization  
- Removing stopwords and punctuation  
- Lemmatization/Stemming  
- Vectorization (TF-IDF, Word2Vec)

---

## 6. How can feature engineering be part of preprocessing?
**Answer:**  
Feature engineering creates new features from raw data to improve model performance. Examples include:
- Date-time breakdown (day, month, weekday)  
- Binning continuous variables  
- Creating interaction terms or ratios

---

## 7. How do you handle time-series data differently during preprocessing?
**Answer:**  
- Maintain temporal order (no shuffling)  
- Resample and fill missing timestamps  
- Create lag/rolling features  
- Normalize seasonality and trends  
- Train-test split based on time, not random split

---

## 8. What are some real-world issues in data collection for AI systems?
**Answer:**  
- Biased or non-representative samples  
- Data drift or concept drift  
- Privacy and legal issues  
- Incomplete or corrupted data streams  
- Cost and scalability of continuous data ingestion

---

## 9. How would you automate preprocessing for production deployment?
**Answer:**  
- Build reusable preprocessing pipelines  
- Serialize with `joblib` or `pickle`  
- Integrate with ML frameworks (e.g., TensorFlow `tf.data`, Sklearn `Pipeline`)  
- Monitor data input quality and drift over time

---

## 10. How can preprocessing techniques influence model interpretability?
**Answer:**  
Techniques like one-hot encoding or normalization may obscure feature meanings. Using:
- Label encoding or interpretable bins  
- Explainability tools (e.g., SHAP, LIME)  
- Maintaining a log of transformations  
helps maintain interpretability post-preprocessing.
