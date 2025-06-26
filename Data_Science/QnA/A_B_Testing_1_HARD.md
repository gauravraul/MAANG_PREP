# Advanced A/B Testing – 10 Toughest Questions and Answers

## 1. What are the assumptions behind the validity of A/B test results?
**Answer:**  
A/B tests assume:
- **Randomized assignment** of users
- **Independence** of observations (no spillover or network effects)
- **Stationarity** (no major external changes during test)
- **Sufficient sample size** for statistical power

Violating these can bias results or invalidate inference.

---

## 2. What is p-hacking, and how can it affect A/B testing outcomes?
**Answer:**  
**P-hacking** is manipulating data collection or analysis to achieve statistical significance.  
Examples:
- Repeatedly checking results mid-test
- Trying many metrics until one is significant  
It **increases Type I error** (false positives).  
**Fix**: Pre-register hypotheses and analysis plan.

---

## 3. How do you decide the required sample size before starting an A/B test?
**Answer:**  
Sample size depends on:
- **Baseline conversion rate**
- **Minimum detectable effect (MDE)**
- **Significance level (α)** (usually 0.05)
- **Power (1 - β)** (usually 0.8)

Use formulas or tools like `statsmodels.stats.power` or online calculators.

---

## 4. Explain the difference between statistical significance and practical significance.
**Answer:**  
- **Statistical significance**: Result is unlikely due to chance (p-value < α)
- **Practical significance**: The effect size is **large enough to matter** for business  
A very small improvement may be statistically significant in large samples but not practically useful.

---

## 5. How would you handle multiple hypothesis testing in an A/B test?
**Answer:**  
Testing multiple metrics increases the risk of false positives.  
**Correction methods**:
- **Bonferroni correction** (conservative)
- **Holm-Bonferroni**
- **False Discovery Rate (Benjamini-Hochberg)**

---

## 6. What is a Type I and Type II error in the context of A/B testing?
**Answer:**  
- **Type I Error (False Positive)**: Detecting a difference when none exists (α-level)
- **Type II Error (False Negative)**: Missing a real difference (β-level)

Balancing both is key to reliable test design.

---

## 7. When would you use a one-tailed vs two-tailed test in A/B testing?
**Answer:**  
- **Two-tailed**: Use when interested in **any difference** (positive or negative)
- **One-tailed**: Use when only interested in **improvement** (e.g., B > A)  
But one-tailed tests are **riskier** and should be pre-specified to avoid bias.

---

## 8. What is a sequential test, and how does it compare to fixed-horizon A/B testing?
**Answer:**  
**Sequential tests** allow continuous monitoring without inflating Type I error.  
Unlike fixed-horizon tests (analyze only at the end), sequential methods (e.g., **SPRT**, **Bayesian**, **alpha-spending**) adapt over time.  
They offer **faster decisions**, especially when differences are large.

---

## 9. What is the difference between a lift and an absolute difference in A/B test metrics?
**Answer:**  
- **Absolute difference**: p_B - p_A
- **Lift**: \frac{p_B - p_A}{p_A} \times 100 (relative increase)  
Lift is useful for marketing/business impact; absolute is better for raw metric interpretation.

---

## 10. How do you interpret A/B test results when confidence intervals overlap?
**Answer:**  
Overlapping confidence intervals **do not always imply non-significance**.  
Instead, check:
- If the **confidence interval for the difference** includes 0 → **Not significant**
- If it excludes 0 → **Statistically significant**  
Comparing separate intervals can be misleading; always analyze the **difference distribution**.
