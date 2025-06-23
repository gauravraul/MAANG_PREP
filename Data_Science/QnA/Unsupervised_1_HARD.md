# Advanced Unsupervised Learning – 10 Toughest Questions and Answers

## 1. How do K-Means and Gaussian Mixture Models differ in their assumptions and results?
**Answer:**  
- **K-Means** assumes spherical clusters with equal variance, uses hard assignments, and minimizes Euclidean distance.
- **GMM (Gaussian Mixture Models)** assumes data is generated from a mixture of Gaussians, allows soft assignments (probabilities), and can model elliptical clusters with different covariance matrices.

---

## 2. What are the limitations of using silhouette score as a clustering evaluation metric?
**Answer:**  
- Assumes convex clusters and may not work well with complex shapes (e.g., moon-shaped clusters).
- Sensitive to cluster density and distance metric.
- Doesn’t handle overlapping or unevenly sized clusters well.

---

## 3. What is the “curse of dimensionality” and how does it impact unsupervised learning?
**Answer:**  
As dimensions increase:
- Distance metrics become less meaningful.
- Data becomes sparse, and clusters become less distinct.
- Algorithms like K-Means and DBSCAN suffer in performance.  
**Solution**: Apply dimensionality reduction (PCA, t-SNE, UMAP) before clustering.

---

## 4. Compare PCA and t-SNE in terms of objectives and use cases.
**Answer:**  
- **PCA**: Linear, preserves global variance, good for compression and linear decorrelation.
- **t-SNE**: Nonlinear, preserves local structure, great for visualization but poor for downstream modeling.
PCA is deterministic; t-SNE is stochastic and unsuitable for high-dimensional interpretability.

---

## 5. How does DBSCAN detect clusters and what are its advantages over K-Means?
**Answer:**  
DBSCAN groups points based on **density** using `eps` (radius) and `minPts`.  
Advantages:
- No need to specify number of clusters.
- Detects **arbitrary-shaped** clusters.
- Handles **noise and outliers** well.
Limitations: Struggles with varying densities and high dimensions.

---

## 6. What is the role of eigenvalues in PCA, and how do they relate to variance?
**Answer:**  
Eigenvalues from the covariance matrix in PCA represent the **amount of variance** captured along the corresponding eigenvectors (principal components).  
- Larger eigenvalues → more variance captured.
- Scree plot helps in deciding how many components to retain.

---

## 7. How does an autoencoder differ from PCA, and when would you prefer one over the other?
**Answer:**  
- **PCA**: Linear, interpretable, fast.
- **Autoencoder**: Nonlinear, capable of capturing complex patterns, but harder to interpret.  
Use autoencoders for **images, text, or nonlinear manifolds**, and PCA for **tabular, low-dimensional, interpretable data**.

---

## 8. What is the EM algorithm and how is it used in unsupervised learning?
**Answer:**  
**EM (Expectation-Maximization)** is used to estimate parameters in models with latent variables (e.g., GMMs):  
- **E-step**: Estimate responsibilities (latent probabilities).  
- **M-step**: Maximize expected log-likelihood given responsibilities.  
Iteratively improves parameter estimates until convergence.

---

## 9. How do Variational Autoencoders (VAEs) perform unsupervised learning?
**Answer:**  
VAEs learn a **probabilistic latent space** by combining autoencoders with variational inference:  
- Uses a **latent prior (usually Gaussian)**  
- Optimizes a loss combining **reconstruction loss** and **KL-divergence** between encoder distribution and prior.  
Generates new data and learns disentangled representations.

---

## 10. Why is clustering considered an ill-posed problem, and how do you address it?
**Answer:**  
Clustering lacks ground truth and objective evaluation:
- No "correct" number of clusters.
- Different algorithms can produce different results.
To address this:
- Use **domain knowledge**.
- Evaluate multiple metrics (e.g., silhouette, Davies-Bouldin).
- Use **ensemble clustering** or **stability-based methods**.
