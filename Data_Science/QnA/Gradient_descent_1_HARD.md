# Advanced Gradient Descent – 10 Toughest Questions and Answers

## 1. Why does gradient descent sometimes fail to converge, and how can this be prevented?
**Answer:**  
Reasons for failure:
- **Learning rate too high** → overshooting or divergence
- **Poor initialization** → stuck in bad minima
- **Saddle points** or **flat regions**  
Fixes:
- Use **learning rate schedules**, **momentum**, or **adaptive optimizers** (e.g., Adam)
- **Gradient clipping** in deep nets
- Better initialization methods (e.g., He or Xavier)

---

## 2. What is the difference between batch, stochastic, and mini-batch gradient descent?
**Answer:**  
- **Batch GD**: Uses the entire dataset each step – stable but slow.
- **Stochastic GD**: Uses 1 sample at a time – fast but noisy.
- **Mini-batch GD**: Uses small chunks – balance between speed and stability.  
Mini-batch GD is **standard in deep learning** due to hardware optimization and faster convergence.

---

## 3. Why can gradient descent be slow near minima, and how can this be improved?
**Answer:**  
Near minima, gradients become small → **slow steps**.  
Solutions:
- Use **momentum** to accelerate in consistent directions
- Switch to **second-order methods** (e.g., Newton’s Method)
- Use **adaptive learning rates** (e.g., Adam, RMSProp)

---

## 4. How does momentum help gradient descent escape saddle points and local minima?
**Answer:**  
Momentum accumulates a **velocity vector** based on past gradients, enabling:
- Faster traversal across shallow regions
- Escaping **saddle points** and **local minima** where gradients are close to zero  
It simulates **inertia**:  
\[
v_t = \beta v_{t-1} + (1 - \beta)\nabla J(\theta)
\]
\[
\theta = \theta - \alpha v_t
\]

---

## 5. Why is gradient descent sensitive to feature scaling?
**Answer:**  
If features have different scales, the **gradient steps oscillate** in skewed directions → slow or unstable convergence.  
Fix:
- Normalize or standardize features  
- Or use optimizers like **Adam** that are scale-invariant

---

## 6. What is the difference between convex and non-convex optimization in gradient descent?
**Answer:**  
- **Convex**: Global minimum exists; gradient descent is guaranteed to converge  
- **Non-convex**: Multiple local minima and saddle points  
Deep learning often involves non-convex loss functions, where gradient descent can **get stuck or wander**.

---

## 7. How do adaptive gradient methods like Adam and RMSProp work?
**Answer:**  
They adjust learning rates for each parameter:
- RMSProp: Divides by a moving average of squared gradients  
- Adam: Combines **momentum (first moment)** and **RMSProp (second moment)**  
This allows:
- Faster convergence
- Better performance on sparse and noisy data

---

## 8. How do gradient descent variants handle sparse data?
**Answer:**  
- **Adam** and **AdaGrad** adapt learning rates based on gradient history → great for sparse features  
- L1 regularization promotes sparsity, but requires careful gradient handling  
- Use **coordinate descent** or **proximal gradient methods** for highly sparse inputs

---

## 9. What is gradient explosion/vanishing and how does it affect gradient descent?
**Answer:**  
- **Vanishing gradients**: Gradients shrink as they propagate → slow/no learning (common in deep nets with sigmoid/tanh)  
- **Exploding gradients**: Gradients grow exponentially → unstable updates  
Fixes:
- **ReLU activation**, **residual connections**, **batch normalization**
- **Gradient clipping** to cap large updates

---

## 10. What are the convergence criteria for stopping gradient descent?
**Answer:**  
Common stopping conditions:
- Gradient magnitude \|\nabla J(\theta)\| is below threshold
- Change in loss |J_{t} - J_{t-1}| is small
- Maximum epochs or iterations
- Validation loss stops improving (early stopping)  
Multiple criteria are usually used for robustness.
