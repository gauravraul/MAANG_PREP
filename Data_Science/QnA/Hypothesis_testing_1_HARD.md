# Advanced Hypothesis Testing – 10 Toughest Questions and Answers

## 1. Why is failing to reject the null hypothesis not the same as accepting it?
**Answer:**  
Failing to reject means the data **doesn’t provide enough evidence** against the null — not that the null is true.  
There could be:
- Insufficient power  
- Small sample size  
- Small effect size  
We **never “accept” the null**; we only say the evidence isn’t strong enough to reject it.

---

## 2. What are Type I and Type II errors, and how are they related to α and β?
**Answer:**  
- **Type I error (α)**: Rejecting a true null hypothesis (false positive)  
- **Type II error (β)**: Failing to reject a false null hypothesis (false negative)  
They trade off: decreasing α (e.g., from 0.05 to 0.01) typically **increases β**, unless the sample size increases.

---

## 3. How does increasing sample size affect p-values and hypothesis tests?
**Answer:**  
Larger sample sizes:
- Decrease **standard error**
- Make tests more **sensitive to small effects**
Even trivial differences can become **statistically significant**, which may **lack practical significance**.

---

## 4. What is statistical power and how is it calculated?
**Answer:**  
**Power = 1 – β**, the probability of correctly rejecting a false null.  
It depends on:
- Effect size  
- Significance level (α)  
- Sample size  
- Variability in the data  
Use power analysis tools (e.g., `statsmodels.stats.power`) or plots to calculate it.

---

## 5. What is the difference between one-tailed and two-tailed tests? When should each be used?
**Answer:**  
- **One-tailed**: Tests for effect in one direction only (e.g., μ > μ₀)  
- **Two-tailed**: Tests for effect in **either direction**  
Use two-tailed unless:
- You have a strong prior reason for directionality  
- You pre-specify it  
Misusing one-tailed tests inflates **Type I error**.

---

## 6. What is the p-value, and what are common misinterpretations of it?
**Answer:**  
The **p-value** is the probability of observing data as extreme as the sample (or more), **assuming the null is true**.  
Misinterpretations:
- Not the probability the null is true  
- Not the probability of repeating the result  
Correct use: compare p-value to α to make a decision.

---

## 7. How do you handle multiple hypothesis testing, and what are the consequences of not doing so?
**Answer:**  
Multiple tests increase the chance of **false positives** (inflated Type I error).  
Control methods:
- **Bonferroni correction** (divide α by number of tests)  
- **False Discovery Rate (FDR)**: e.g., Benjamini-Hochberg  
Without correction, results are misleading and not replicable.

---

## 8. What is the difference between parametric and non-parametric hypothesis tests?
**Answer:**  
- **Parametric**: Assume underlying distribution (e.g., t-test assumes normality)  
- **Non-parametric**: Make fewer assumptions, based on ranks (e.g., Mann-Whitney U, Wilcoxon)  
Use non-parametric when assumptions like normality or equal variances are violated.

---

## 9. When is a likelihood ratio test preferred over traditional hypothesis tests?
**Answer:**  
**Likelihood Ratio Tests (LRTs)** compare two nested models using the ratio of their likelihoods.  
Preferred when:
- Models are nested  
- You’re comparing full vs reduced models  
LRTs are widely used in **GLMs, logistic regression, mixed models** for testing additional predictors.

---

## 10. What is the difference between Bayesian and frequentist hypothesis testing?
**Answer:**  
- **Frequentist**: Uses p-values, confidence intervals; doesn't assign probability to hypotheses  
- **Bayesian**: Assigns prior beliefs; outputs **posterior probability** of hypotheses  
Bayesian methods allow **updating beliefs** and **direct probabilistic interpretation**, but require **priors** and more computation.
