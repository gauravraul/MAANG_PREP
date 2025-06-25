# Advanced DBSCAN – 10 Toughest Questions and Answers

## 1. What is the core concept behind DBSCAN’s clustering approach?
**Answer:**  
DBSCAN groups data points into clusters based on **density connectivity**:
- A point is a **core point** if it has ≥ `minPts` neighbors within `eps` distance.
- Points within `eps` of a core point are **density-reachable**.
- Clusters form by expanding from core points; **noise** is any point not density-reachable.

---

## 2. Why is DBSCAN sensitive to the choice of `eps` and `minPts`?
**Answer:**  
- **Too small `eps`**: Too many small clusters or noise
- **Too large `eps`**: Merges distinct clusters
- `minPts` must balance detecting sparse vs dense clusters  
No universal rule; often determined empirically using a **k-distance graph**.

---

## 3. Can DBSCAN detect clusters of varying density? Why or why not?
**Answer:**  
No. DBSCAN struggles with **clusters of varying density** because a single global `eps` threshold cannot fit both dense and sparse regions well.  
**Fix**: Use **HDBSCAN** (Hierarchical DBSCAN), which handles variable densities better.

---

## 4. How does DBSCAN differ from K-Means in terms of assumptions and output?
**Answer:**  
- **K-Means**: Assumes spherical, equally sized clusters; requires `k`
- **DBSCAN**: No need to specify number of clusters; detects **arbitrary shapes** and **noise**
- K-Means assigns every point to a cluster; DBSCAN can label points as **noise**

---

## 5. What is the time complexity of DBSCAN and how can it be improved?
**Answer:**  
Naïve implementation: **O(n²)** (all pairwise distance checks)  
With spatial indexing (e.g., KD-Tree, Ball Tree): **O(n log n)**  
Performance degrades in **high dimensions** where spatial trees lose efficiency.

---

## 6. Why is DBSCAN not suitable for high-dimensional data?
**Answer:**  
- **Curse of dimensionality**: Distances become less meaningful  
- Density estimation becomes unreliable  
- k-distance plots are hard to interpret  
Alternatives: Use **PCA/t-SNE/UMAP** before applying DBSCAN, or switch to **HDBSCAN**.

---

## 7. How does DBSCAN handle noise and outliers?
**Answer:**  
- Points not within `eps` of any core point or not density-reachable are labeled as **noise (-1)**.
- These are **not assigned to any cluster**, making DBSCAN robust to outliers.

---

## 8. How does DBSCAN behave with clusters that are close but not connected?
**Answer:**  
If two dense regions are close but separated by a small **low-density gap**, DBSCAN treats them as **distinct clusters**.  
But if `eps` is too large, they may be **merged incorrectly**.  
Careful tuning of `eps` is necessary.

---

## 9. How would you use a k-distance graph to choose the optimal `eps`?
**Answer:**  
Steps:
1. For each point, compute distance to its `k`-th nearest neighbor (where `k = minPts`)
2. Sort these distances in ascending order
3. Plot the sorted distances  
**Elbow/knee point** in the curve suggests a good value for `eps`.

---

## 10. Can DBSCAN be applied to streaming or online data?
**Answer:**  
Standard DBSCAN is **not incremental**, making it unsuitable for streaming.  
Alternatives:
- **Incremental DBSCAN**
- **DenStream** or **D-Stream**: Adapt DBSCAN for dynamic, evolving datasets
