# Advanced Logistic Regression – 10 Toughest Questions and Answers

## 1. Why can’t we use Ordinary Least Squares (OLS) for classification tasks?
**Answer:**  
OLS assumes continuous output and homoscedastic errors, which is inappropriate for classification. It may produce probabilities outside [0, 1] and lacks the log-odds interpretation essential in binary classification.

---

## 2. Derive the cost function used in logistic regression.
**Answer:**  
Logistic regression uses the **log-loss** (cross-entropy):  
**L(θ) = -[y log(p) + (1 - y) log(1 - p)]**  
where **p = σ(θᵀx)** and σ is the sigmoid function. It penalizes incorrect predictions more harshly than squared error.

---

## 3. What is the role of the sigmoid function in logistic regression?
**Answer:**  
The sigmoid maps any real number to the (0, 1) range, enabling probabilistic interpretation of outputs, essential for binary classification:  
**σ(z) = 1 / (1 + e^(–z))**

---

## 4. Why is logistic regression not a linear classifier in the probabilistic sense?
**Answer:**  
Though the decision boundary is linear (θᵀx = 0), logistic regression models the **log-odds** as a linear function of inputs, making it **linear in logit space**, not in probability space.

---

## 5. What is the difference between log-likelihood and cross-entropy in logistic regression?
**Answer:**  
They are mathematically equivalent:  
- **Log-likelihood** is the probability of the observed data under the model.  
- **Cross-entropy** measures the difference between predicted and true distributions.  
Maximizing log-likelihood = minimizing cross-entropy.

---

## 6. How does multicollinearity affect logistic regression?
**Answer:**  
It inflates the standard errors of the coefficients, making them unreliable and sensitive to small changes. Can be mitigated with L2 regularization (Ridge) or dimensionality reduction (PCA).

---

## 7. What is quasi-complete separation and how do you handle it?
**Answer:**  
Occurs when a linear combination of predictors perfectly separates the classes, causing the MLE to diverge (infinite coefficients).  
**Fixes:**  
- Regularization (L1 or L2)  
- Removing or combining problematic variables  
- Using Bayesian logistic regression with priors

---

## 8. Why do we use maximum likelihood estimation (MLE) instead of gradient descent on squared error in logistic regression?
**Answer:**  
MLE via cross-entropy gives a convex cost function for logistic regression, leading to more stable convergence. Squared error leads to non-convexity and poor probabilistic interpretations.

---

## 9. Explain the concept and use of odds and log-odds in logistic regression.
**Answer:**  
- **Odds**: p / (1 – p)  
- **Log-odds (logit)**: log(p / (1 – p))  
Logistic regression assumes a linear relationship between log-odds and predictors, enabling interpretability of coefficients as multiplicative changes in odds.

---

## 10. How does L1 regularization affect logistic regression, and when would you prefer it over L2?
**Answer:**  
L1 (Lasso) encourages sparsity, zeroing out irrelevant features, making it ideal for feature selection.  
Prefer it when:  
- Feature space is large and noisy  
- You want a compact, interpretable model
