# Data Science - Day 4: Exploratory Data Analysis (EDA) - Medium Questions

## 1. What is the difference between univariate, bivariate, and multivariate analysis?
**Answer:**  
- **Univariate**: Analysis of a single variable  
- **Bivariate**: Analysis of two variables (e.g., correlation, scatter plots)  
- **Multivariate**: Analysis of more than two variables (e.g., pair plots, PCA)

---

## 2. How do you detect outliers using IQR?
**Answer:**  
- Compute Q1 and Q3 (25th and 75th percentiles)  
- Calculate IQR = Q3 - Q1  
- Outliers lie below Q1 - 1.5×IQR or above Q3 + 1.5×IQR

---

## 3. What does a heatmap of a correlation matrix show?
**Answer:**  
It visually shows correlation coefficients between numerical variables, highlighting strong or weak relationships using colors.

---

## 4. How can you identify skewness in a distribution?
**Answer:**  
- By inspecting histograms or boxplots  
- Using `.skew()` method in Pandas  
- Skewness > 0 means right-skewed, < 0 means left-skewed

---

## 5. What are pair plots and why are they useful?
**Answer:**  
Pair plots (from Seaborn) show scatter plots for all variable combinations and histograms for each variable—useful for understanding relationships and distributions.

---

## 6. What is the difference between variance and standard deviation?
**Answer:**  
- **Variance** measures average squared deviation from the mean  
- **Standard deviation** is the square root of variance and is in the same unit as the data

---

## 7. How do you interpret a negative correlation between two variables?
**Answer:**  
As one variable increases, the other tends to decrease. A perfect negative correlation is -1.

---

## 8. Why is it important to analyze missing data patterns in EDA?
**Answer:**  
Understanding missing data patterns helps in deciding proper imputation methods and prevents biased analysis.

---

## 9. What is the role of groupby operations in EDA?
**Answer:**  
`groupby()` in Pandas is used to aggregate data by categories, making it easy to compare averages, counts, or trends across groups.

---

## 10. How can visualization mislead during EDA?
**Answer:**  
- Using inappropriate chart types  
- Ignoring scale or axis manipulation  
- Cherry-picking data ranges  
- Misleading color or label usage
