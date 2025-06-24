# Advanced PCA (Principal Component Analysis) – 10 Toughest Questions and Answers

## 1. How does PCA reduce dimensionality while preserving variance?
**Answer:**  
PCA projects data onto a new set of orthogonal axes (principal components) ranked by variance.  
- The first component captures the most variance, the second the next most, etc.  
By keeping only the top `k` components, PCA reduces dimensionality while retaining the **maximum variance** possible.

---

## 2. Why does PCA require centering the data before transformation?
**Answer:**  
Centering ensures the mean of each feature is zero.  
This is crucial because:
- PCA maximizes **variance from the origin**.
- Without centering, PCA might capture mean-related direction instead of actual data spread.

---

## 3. What is the mathematical connection between PCA and the covariance matrix?
**Answer:**  
PCA computes the **eigenvectors and eigenvalues** of the **covariance matrix** of the data.  
- **Eigenvectors** = directions of principal components  
- **Eigenvalues** = amount of variance captured in those directions

---

## 4. Can PCA be used on categorical data?
**Answer:**  
No, PCA requires **numeric, continuous** variables because it relies on covariance and linear algebra operations (e.g., dot product).  
For categorical data, use alternatives like **Multiple Correspondence Analysis (MCA)** or **t-SNE with embeddings**.

---

## 5. What are the limitations of PCA?
**Answer:**  
- Assumes **linear relationships** only  
- Sensitive to **scaling and outliers**  
- Components are **not interpretable** in terms of original features  
- Fails on **nonlinear manifolds** (use t-SNE, UMAP, or kernel PCA instead)

---

## 6. How can you determine the number of principal components to retain?
**Answer:**  
Several methods:
- **Explained variance ratio** (e.g., retain components that explain 95% of variance)
- **Scree plot** (look for the "elbow")
- **Cumulative variance threshold**
- **Cross-validation** if downstream task performance matters

---

## 7. What is the geometric interpretation of PCA?
**Answer:**  
PCA finds a new **coordinate system** where:
- Axes = orthogonal directions of greatest variance (principal components)
- It **rotates** the original feature space to align data along the directions of maximal spread.

---

## 8. How is PCA different from Linear Discriminant Analysis (LDA)?
**Answer:**  
- **PCA**: Unsupervised, maximizes variance, ignores class labels  
- **LDA**: Supervised, maximizes **class separability** using **between-class and within-class scatter**  
PCA focuses on features; LDA focuses on labels.

---

## 9. What is kernel PCA and how does it extend standard PCA?
**Answer:**  
Kernel PCA uses the **kernel trick** to compute principal components in a **high-dimensional feature space** without explicit mapping.  
It enables PCA to capture **nonlinear structures** using kernels like RBF or polynomial.

---

## 10. How does PCA handle correlated features, and why is it useful in such scenarios?
**Answer:**  
PCA **decorrelates** features by projecting them into a new space where principal components are orthogonal.  
- Useful when multicollinearity exists  
- Can compress redundant information  
- Leads to better performance in models sensitive to collinearity (e.g., linear regression)
