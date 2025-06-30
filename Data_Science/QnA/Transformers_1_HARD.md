# Advanced Transformer Architecture – 10 Toughest Questions and Answers

## 1. What core design changes make Transformers superior to RNNs for sequence modeling?
**Answer:**  
Transformers:
- Replace recurrence with **self-attention**, enabling **parallel computation**
- Allow modeling of **long-range dependencies** via attention over all tokens
- Use **positional encodings** to retain order information  
This improves scalability, stability, and accuracy over RNNs/LSTMs, especially on long sequences.

---

## 2. Why are positional encodings necessary in Transformers?
**Answer:**  
Self-attention is **order-invariant** by default.  
**Positional encodings** (either sinusoidal or learned) inject **sequence order** information so the model can distinguish the position of tokens.  
Without them, the model can't infer syntax, context, or relative order.

---

## 3. What is the role of layer normalization in Transformers and why is it applied before the sublayer (Pre-LN)?
**Answer:**  
**LayerNorm** stabilizes training by normalizing inputs across features.  
- **Pre-LN** (used in modern transformers) applies normalization **before** attention/feedforward blocks  
Benefits:
- Improved gradient flow
- Better stability in deep transformers  
Pre-LN is now the standard over original **Post-LN** (used in vanilla Transformer paper).

---

## 4. What causes quadratic complexity in attention and how is it being addressed?
**Answer:**  
In standard attention:  
\[
\text{complexity} = O(n^2 \cdot d)
\]
where *n* = sequence length.  
**Memory/time explode** for long inputs.  
Solutions:
- **Sparse attention** (Longformer, BigBird)  
- **Low-rank approximations** (Linformer)  
- **Kernelized attention** (Performer)  
- **Efficient implementations** (FlashAttention)

---

## 5. What is the function of the Feedforward layer (FFN) in Transformer blocks?
**Answer:**  
FFN is applied **independently** to each token after attention.  
It adds **non-linearity and depth**:
\[
\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2
\]
FFNs increase the model’s **representation power** and are responsible for **token-wise transformations**.

---

## 6. How does multi-head self-attention improve learning over single-head attention?
**Answer:**  
Multi-head attention projects inputs into **multiple subspaces**, allowing the model to:
- Learn different **types of relationships** (e.g., syntactic vs semantic)
- Attend to **different parts** of the sequence simultaneously  
Final output: Concatenated outputs from all heads + projection → richer representations.

---

## 7. What is label leakage and how is it prevented in transformer decoders?
**Answer:**  
In generation tasks, the decoder should **not see future tokens** during training.  
**Causal masks (triangular masks)** are applied to:
- Mask future positions in self-attention
- Ensure the model learns to generate **autoregressively**

---

## 8. How do Transformers handle variable-length sequences during training and inference?
**Answer:**  
- Use **padding tokens** to equalize length in batches  
- **Padding masks** ensure these tokens are **ignored in attention and loss**  
- During inference (e.g., decoding), generation is **step-by-step**, often using beam search or sampling.

---

## 9. Why is the Transformer decoder autoregressive, and what alternatives exist?
**Answer:**  
Autoregressive decoders:
- Generate one token at a time using previously generated tokens  
- Are **more accurate** but **slow**  
Alternatives:
- **Non-autoregressive transformers** (e.g., NAT) generate all tokens in parallel → faster but less fluent  
- Used in speed-critical applications like real-time translation.

---

## 10. How are Transformers adapted for vision tasks (e.g., ViT)?
**Answer:**  
Transformers are applied to vision by:
- Dividing an image into **patches** (e.g., 16x16)
- Flattening and projecting patches into embeddings  
- Adding positional encodings  
This **Vision Transformer (ViT)** model processes image patches like tokens, enabling success on classification, detection, segmentation tasks.
