# Data Science - Day 4: Exploratory Data Analysis (EDA) - Hard Questions

## 1. How would you handle high cardinality categorical variables during EDA?
**Answer:**  
- Group rare categories into “Other”  
- Use frequency or target encoding  
- Visualize top-k frequent categories  
- Consider dimensionality reduction techniques if needed

---

## 2. What is Simpson’s Paradox and how can it affect EDA conclusions?
**Answer:**  
Simpson’s Paradox occurs when trends in different groups reverse when combined. It can mislead interpretations if subgroup effects are not analyzed separately.

---

## 3. How can PCA be used in EDA?
**Answer:**  
Principal Component Analysis reduces dimensionality while preserving variance, helping visualize high-dimensional data and detect structure or outliers.

---

## 4. What is the difference between covariance and correlation?
**Answer:**  
- **Covariance** measures how two variables vary together but is scale-dependent.  
- **Correlation** standardizes this to a -1 to 1 range, making it easier to interpret.

---

## 5. How would you handle multicollinearity discovered during EDA?
**Answer:**  
- Remove or combine highly correlated variables  
- Use dimensionality reduction (e.g., PCA)  
- Calculate VIF (Variance Inflation Factor) and drop variables with high VIFs

---

## 6. Describe a case where EDA revealed a data quality issue that could have harmed the model.
**Answer:**  
Example: EDA shows identical values in a variable that should vary (e.g., timestamps all the same), indicating logging failure. Training on such data would produce misleading results or overfitting.

---

## 7. What are the limitations of using visualizations alone during EDA?
**Answer:**  
Visualizations can:
- Be subjective or misleading without statistical context  
- Miss patterns in high-dimensional data  
- Overlook underlying biases or outliers unless paired with summary stats

---

## 8. How do you differentiate between causation and correlation during EDA?
**Answer:**  
EDA reveals correlation but not causation. Establishing causation requires experimental design or domain knowledge, not just EDA.

---

## 9. How would you visualize and interpret interactions between three variables?
**Answer:**  
Use:
- 3D scatter plots  
- Facet grids (e.g., Seaborn’s `FacetGrid`)  
- Color-coding or grouping in 2D plots  
- Pivot tables or grouped boxplots

---

## 10. How can EDA be automated while preserving interpretability?
**Answer:**  
Use libraries like:
- `pandas-profiling`  
- `sweetviz`  
- `dtale`  
These generate detailed reports, but interpretation still requires domain understanding and caution against blindly trusting auto-generated insights.
