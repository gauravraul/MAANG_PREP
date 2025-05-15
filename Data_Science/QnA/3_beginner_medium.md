# Data Science - Day 3: Data Collection and Preprocessing (Medium Questions)

## 1. What are the differences between primary and secondary data sources?
**Answer:**  
- **Primary data** is collected firsthand by the researcher (e.g., surveys, experiments).  
- **Secondary data** is collected by someone else and reused (e.g., public datasets, company reports).

---

## 2. What is the difference between imputation and deletion in handling missing data?
**Answer:**  
- **Imputation** fills missing values using statistical methods (mean, median, etc.).  
- **Deletion** removes rows or columns with missing values from the dataset.

---

## 3. What is one-hot encoding and when is it used?
**Answer:**  
One-hot encoding transforms categorical variables into binary columns. It’s used when converting non-numeric labels into a format suitable for ML algorithms.

---

## 4. How can outliers be detected in a dataset?
**Answer:**  
Outliers can be detected using:
- Visualization tools (boxplots, scatter plots)  
- Statistical methods (Z-score, IQR)

---

## 5. What is the role of the ETL process in data preprocessing?
**Answer:**  
**ETL (Extract, Transform, Load)** is a process that:
- Extracts data from sources  
- Transforms it into a usable format  
- Loads it into storage or analytics platforms

---

## 6. What are categorical and numerical features? Give examples.
**Answer:**  
- **Categorical features** are non-numeric and represent categories (e.g., gender, country).  
- **Numerical features** are measurable quantities (e.g., age, salary).

---

## 7. What is normalization, and how is it different from standardization?
**Answer:**  
- **Normalization** scales data to a range (usually 0 to 1).  
- **Standardization** centers data with mean 0 and standard deviation 1.

---

## 8. What are some challenges of collecting data through web scraping?
**Answer:**  
- Website structure changes  
- Rate limiting or blocking  
- Legal and ethical concerns  
- Data inconsistency and noise

---

## 9. Why should data be shuffled before splitting into training and testing sets?
**Answer:**  
Shuffling ensures the distribution of the data is random and unbiased, preventing systematic patterns from leaking into the model.

---

## 10. What is feature scaling and why is it necessary?
**Answer:**  
Feature scaling transforms data into a consistent scale to prevent features with large ranges from dominating models like k-NN or SVM.
