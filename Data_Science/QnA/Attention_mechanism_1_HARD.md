# Advanced Attention Mechanism – 10 Toughest Questions and Answers

## 1. What is the core mathematical idea behind the attention mechanism?
**Answer:**  
Attention computes a **weighted sum of values (V)** based on the **compatibility between queries (Q)** and **keys (K)**.  
\[
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]
This lets models focus on **relevant information dynamically**, depending on the task and input.

---

## 2. Why is the dot-product scaled by \sqrt{d_k} in scaled dot-product attention?
**Answer:**  
Without scaling, the dot products can become **very large in high dimensions**, leading to:
- Extremely small gradients after softmax
- Slower or unstable learning  
Scaling by \sqrt{d_k} prevents this by normalizing the variance of the dot product.

---

## 3. How does multi-head attention differ from single-head attention?
**Answer:**  
- **Single-head**: Applies one attention mechanism  
- **Multi-head**: Applies attention in **parallel over multiple linear projections** of Q, K, V  
Each head captures different aspects (e.g., syntactic vs semantic relationships), which are concatenated and linearly transformed.

---

## 4. How does self-attention differ from cross-attention?
**Answer:**  
- **Self-attention**: Queries, keys, and values all come from the **same sequence**  
- **Cross-attention**: Queries come from **decoder**, while keys/values come from **encoder**  
Self-attention is used in encoders and decoders; cross-attention is used in **encoder-decoder** models like Transformers.

---

## 5. What are the limitations of soft attention and how does hard attention attempt to solve them?
**Answer:**  
- **Soft attention** is fully differentiable but may attend to irrelevant positions due to distributed weights.  
- **Hard attention** selects **discrete positions** — potentially more focused but **non-differentiable**, requiring **REINFORCE** or other sampling-based methods.  
Tradeoff: Accuracy vs trainability.

---

## 6. What is the role of attention masks in transformer models?
**Answer:**  
Attention masks:
- **Prevent attention to irrelevant tokens** (e.g., padding tokens)
- **Enforce causality** in decoder (e.g., for autoregressive generation)
Types:
- Padding mask
- Causal mask (triangular matrix)

---

## 7. How is attention computed efficiently for long sequences in recent models?
**Answer:**  
Traditional attention has **O(n²)** time/memory complexity.  
Solutions:
- **Sparse attention** (e.g., Longformer, BigBird)  
- **Low-rank approximations** (e.g., Linformer)  
- **Memory-efficient attention** (e.g., FlashAttention, Performer)  
These reduce resource usage while preserving key dependencies.

---

## 8. How do additive and multiplicative (dot-product) attention differ?
**Answer:**  
- **Additive (Bahdanau)**: Combines Q and K using a feedforward network → more expressive, better on smaller models  
- **Multiplicative (Luong)**: Uses dot products for compatibility → faster, easier to parallelize  
In practice, dot-product attention is dominant due to efficiency with GPUs.

---

## 9. Why is attention often preferred over recurrence (RNN) in modern architectures?
**Answer:**  
Attention:
- Allows **parallel computation**  
- Models **long-range dependencies** better  
- Avoids vanishing gradient issues  
RNNs process sequentially → slower and harder to scale. Attention dominates in **transformers, vision, audio, and beyond**.

---

## 10. How does cross-modal attention work in models like Vision-Language Transformers?
**Answer:**  
Cross-modal attention:
- Aligns information from **different modalities** (e.g., image regions and text tokens)  
- Query: one modality (e.g., text)  
- Key/Value: another (e.g., image embeddings)  
Used in models like **CLIP**, **ViLBERT**, **BLIP**, where multimodal grounding is required.
