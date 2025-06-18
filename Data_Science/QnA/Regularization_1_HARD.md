# Advanced Regularization – 10 Toughest Questions and Answers

## 1. What is the difference between L1 and L2 regularization in terms of mathematical effect and sparsity?
**Answer:**  
- **L1 (Lasso)**: Adds `λ‖β‖₁` → encourages sparsity by shrinking some coefficients to zero.  
- **L2 (Ridge)**: Adds `λ‖β‖²` → penalizes large weights but rarely makes them exactly zero.  
L1 = feature selection, L2 = weight shrinkage.

---

## 2. Why does L1 regularization lead to sparse solutions?
**Answer:**  
The geometry of the L1 norm constraint forms sharp corners (like a diamond in 2D). When minimizing the loss, the solution is likely to land on axes, setting some coefficients exactly to zero.

---

## 3. What is Elastic Net and when is it preferred over Lasso or Ridge?
**Answer:**  
Elastic Net combines L1 and L2:  
`Loss = MSE + λ1‖β‖₁ + λ2‖β‖²`  
Preferred when:
- Features are correlated (Lasso selects one randomly, Elastic Net distributes weights).
- Dataset has more features than observations (p >> n).

---

## 4. How does regularization help prevent overfitting?
**Answer:**  
Regularization constrains the model by penalizing large weights, reducing complexity.  
This discourages the model from fitting noise in the training data, improving generalization.

---

## 5. In deep learning, how does L2 regularization affect backpropagation?
**Answer:**  
L2 adds a term `λw` to the gradient:  
- Gradient update becomes: `∇Loss + λw`  
- Encourages smaller weights throughout training  
- Helps prevent exploding weights and stabilizes training

---

## 6. What is dropout and how does it serve as a regularization method?
**Answer:**  
**Dropout** randomly deactivates neurons during training (e.g., 20–50%), forcing the network to learn redundant representations.  
- Reduces co-adaptation  
- Acts like training an ensemble of subnetworks  
- Effective in deep networks to reduce overfitting

---

## 7. How does early stopping serve as a form of regularization?
**Answer:**  
**Early stopping** halts training when validation loss stops improving.  
- Prevents overfitting by not letting the model learn noise  
- Especially effective in gradient-based training where training loss always decreases

---

## 8. What is weight decay and how is it related to L2 regularization?
**Answer:**  
**Weight decay** is a technique where weights are multiplied by a factor < 1 at each step.  
Mathematically equivalent to **L2 regularization** in gradient-based methods:
- Optimizer update: `w ← w – η(∇Loss + λw)`

---

## 9. How do regularization techniques differ between linear models and neural networks?
**Answer:**  
- **Linear Models**: Use analytical regularization (L1, L2) to control feature weights.  
- **Neural Networks**: Use empirical techniques:
  - L1/L2 weight penalties
  - Dropout
  - Batch normalization
  - Early stopping  
  Regularization in deep learning is more diverse due to model complexity.

---

## 10. Why does regularization sometimes reduce training accuracy but improve test accuracy?
**Answer:**  
By constraining the model, regularization sacrifices some training performance to reduce overfitting.  
This improves generalization, leading to better performance on unseen test data – the core goal in machine learning.
