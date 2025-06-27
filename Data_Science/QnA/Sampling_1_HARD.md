# Advanced Sampling – 10 Toughest Questions and Answers

## 1. What is the difference between probability and non-probability sampling, and why does it matter?
**Answer:**  
- **Probability sampling**: Every unit has a known, non-zero probability of selection (e.g., simple random, stratified, cluster).  
- **Non-probability sampling**: Selection is subjective or based on convenience (e.g., quota, snowball).  
Only **probability sampling** allows valid **statistical inference** and **confidence intervals**.

---

## 2. How does stratified sampling improve over simple random sampling?
**Answer:**  
**Stratified sampling** divides the population into homogeneous groups (strata) and samples from each.  
Benefits:
- Reduces **variance** in estimates  
- Ensures **representation** of key subgroups  
Especially useful when some strata are small or critical to the analysis.

---

## 3. What is sampling bias, and what are its common sources?
**Answer:**  
**Sampling bias** occurs when the sample systematically differs from the population, leading to invalid inferences.  
Common causes:
- Undercoverage (e.g., phone surveys miss homeless people)  
- Nonresponse bias  
- Convenience sampling  
- Self-selection bias

---

## 4. Why is sample size more important than population size for estimation?
**Answer:**  
The accuracy of a sample depends on its **size**, not the population (except for very small populations).  
Standard error decreases with sample size as:  
\[
SE \propto \frac{1}{\sqrt{n}}
\]
Even in a population of millions, a few thousand well-sampled points suffice for good estimates.

---

## 5. What is the design effect and why is it important in complex sampling?
**Answer:**  
**Design effect (DEFF)** quantifies how much the sampling variance increases due to complex designs (e.g., clustering) vs simple random sampling:  
\[
DEFF = \frac{\text{Variance (complex)}}{\text{Variance (SRS)}}
\]
Used to adjust standard errors and calculate effective sample size in surveys.

---

## 6. When should you use cluster sampling, and what are its trade-offs?
**Answer:**  
**Use** when:
- Population is geographically dispersed  
- Full list of individuals is unavailable  
**Trade-offs**:
- More feasible logistically  
- **Higher variance** than SRS or stratified sampling  
Combining it with stratification can improve efficiency.

---

## 7. How does bootstrapping relate to sampling, and when is it useful?
**Answer:**  
**Bootstrapping** is **resampling with replacement** from a dataset to approximate the sampling distribution of a statistic.  
Used when:
- Analytical solutions for variance/confidence intervals are hard  
- Data is small or non-normal  
Powerful for **non-parametric inference**.

---

## 8. What is oversampling and when is it necessary?
**Answer:**  
**Oversampling** intentionally samples certain subgroups more than their natural occurrence to ensure adequate representation (e.g., rare events, minorities).  
Post-stratification weights adjust for oversampling to avoid bias in population-level estimates.

---

## 9. How do weighting and post-stratification correct sampling imbalances?
**Answer:**  
Weights adjust for:
- Unequal probabilities of selection  
- Non-response  
- Oversampling  
**Post-stratification** aligns sample distributions with known population distributions using weights.  
Crucial for accurate survey inference.

---

## 10. What is the finite population correction (FPC), and when should it be applied?
**Answer:**  
FPC adjusts variance estimates when sampling **without replacement** from a **small finite population**:  
\[
FPC = \sqrt{\frac{N - n}{N - 1}}
\]
Where `N` is the population size and `n` is the sample size.  
Needed when n/N > 0.05, otherwise negligible.
