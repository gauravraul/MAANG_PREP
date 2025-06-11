# Advanced Linear Regression – 10 Toughest Questions and Answers

## 1. Why is multicollinearity a problem in linear regression, and how do you detect and address it?
**Answer:**  
Multicollinearity occurs when independent variables are highly correlated, making coefficient estimates unstable and inflating standard errors.  
**Detection:**  
- Variance Inflation Factor (VIF)  
- Condition number  
**Solutions:**  
- Remove/reduce correlated predictors  
- Use PCA or Ridge regression

---

## 2. Derive the closed-form solution of Ordinary Least Squares (OLS) and state its assumptions.
**Answer:**  
The OLS solution is:  
**β̂ = (XᵀX)⁻¹Xᵀy**  
**Assumptions:**  
1. Linearity  
2. Independence of errors  
3. Homoscedasticity  
4. No multicollinearity  
5. Normality of residuals (for inference)

---

## 3. What happens when (XᵀX) is not invertible in OLS? How do you fix it?
**Answer:**  
If **XᵀX is singular** (i.e., not full rank), the closed-form solution doesn't exist.  
**Fixes:**  
- Remove redundant features  
- Use regularization (Ridge/Lasso)  
- Add small identity matrix (Tikhonov regularization)

---

## 4. How does Ridge regression differ from OLS and what’s its geometric interpretation?
**Answer:**  
Ridge regression minimizes:  
**L = RSS + λ‖β‖²**  
It shrinks coefficients by adding L2 penalty, reducing variance.  
**Geometrically**, it constrains the solution within a sphere around the origin, promoting smaller weights.

---

## 5. Why does Lasso regression produce sparse solutions?
**Answer:**  
Lasso minimizes:  
**L = RSS + λ‖β‖₁**  
L1 regularization leads to sharp corners in constraint geometry (a diamond), which promotes exact zero coefficients, resulting in sparsity.

---

## 6. What is heteroscedasticity and how does it affect linear regression?
**Answer:**  
Heteroscedasticity means that the variance of residuals is not constant across observations. It violates OLS assumptions, leading to inefficient estimates and biased standard errors.  
**Detection:** Residual plots, Breusch–Pagan test  
**Correction:** Use robust standard errors or transform the target variable.

---

## 7. Explain the Gauss-Markov Theorem.
**Answer:**  
Under OLS assumptions (excluding normality), the Gauss-Markov theorem states that the OLS estimator **β̂** is the **Best Linear Unbiased Estimator (BLUE)**, i.e., has the minimum variance among all linear unbiased estimators.

---

## 8. What is the role of the hat matrix (H) in regression and its properties?
**Answer:**  
**H = X(XᵀX)⁻¹Xᵀ** projects **y** onto the column space of **X**.  
Properties:  
- Symmetric and idempotent (H = Hᵀ, H² = H)  
- Used to compute fitted values: **ŷ = Hy**  
- Diagonal elements (leverages) identify influential points

---

## 9. How do you identify and handle influential data points in linear regression?
**Answer:**  
Use:  
- **Leverage**: High leverage points are far in feature space  
- **Cook’s Distance**: Measures influence on fitted values  
**Action:**  
- Investigate data quality  
- Try robust regression  
- Use diagnostics to decide if removal is justified

---

## 10. Compare OLS, Ridge, Lasso, and Elastic Net in terms of bias-variance trade-off.
**Answer:**  
- **OLS**: Low bias, high variance (overfits on multicollinearity or noise)  
- **Ridge**: Adds bias, reduces variance, shrinks coefficients  
- **Lasso**: Adds bias, reduces variance, performs variable selection  
- **Elastic Net**: Combines L1 and L2; balances between shrinkage and sparsity
