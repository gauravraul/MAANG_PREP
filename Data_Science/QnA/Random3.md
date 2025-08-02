# 10 Random Hard Questions and Answers in Generative AI

---

## 1. How does rotary positional embedding (RoPE) differ from absolute and learned positional embeddings?

**Answer:**  
RoPE encodes position through sinusoidal rotation in complex space, allowing better generalization to longer contexts and extrapolation. Unlike absolute or learned embeddings, RoPE is relative and compositional, enabling models like LLaMA to generalize beyond their training sequence length.

---

## 2. What are the trade-offs between activation quantization and weight quantization in transformer models?

**Answer:**  
Weight quantization reduces memory and model size. Activation quantization impacts runtime efficiency. Activation quantization is more sensitive to distribution shifts (e.g., across layers or batches), often needing calibration. Combining both (e.g., in INT8) requires careful handling to avoid performance degradation.

---

## 3. Explain how speculative decoding improves inference throughput in large language models.

**Answer:**  
Speculative decoding involves a small draft model generating multiple tokens ahead, which are then verified by a larger model. This parallelism reduces the number of large model invocations, accelerating decoding while maintaining quality.

---

## 4. How does KV caching improve inference in auto-regressive transformers?

**Answer:**  
Key-value (KV) caching stores previously computed attention values, avoiding recomputation for prior tokens. This reduces time complexity from O(n²) to O(n) per token at inference, significantly boosting performance in long context generation.

---

## 5. What challenges arise when fine-tuning transformer models on long context lengths?

**Answer:**  
Challenges include memory explosion due to quadratic attention, gradient instability, need for longer training sequences, and positional embedding misalignment. Solutions include attention optimization (FlashAttention, Longformer), and reinitializing or extending positional embeddings (e.g., Interpolation, ALiBi).

---

## 6. How do adapter modules impact multi-task learning in LLMs?

**Answer:**  
Adapters allow task-specific tuning without modifying the base model. In multi-task settings, they enable modularity, faster convergence, and memory-efficient storage. However, interference between adapters and base weights can reduce zero-shot generalization if not carefully managed.

---

## 7. What is the purpose of cosine similarity scoring in retrieval systems?

**Answer:**  
Cosine similarity measures the angle between dense embeddings, serving as a proxy for semantic similarity. It’s used in RAG and dense retrieval systems to identify relevant documents, especially when using vector databases like FAISS or Weaviate.

---

## 8. Describe a strategy to perform continual learning in transformer models without catastrophic forgetting.

**Answer:**  
Regularization techniques like Elastic Weight Consolidation (EWC), replay buffers (storing past data), and modular adaptation (e.g., adapters, LoRA) help retain prior knowledge. These approaches prevent forgetting by selectively freezing or penalizing critical weights.

---

## 9. Why is gradient noise scale important in large-scale training?

**Answer:**  
Gradient noise scale quantifies the ratio of signal to noise in the gradient. It helps determine optimal batch size. At scale, too low a noise scale leads to poor generalization; too high causes underfitting. It's key for performance tuning.

---

## 10. How does instruction tuning differ from fine-tuning, and what are its benefits?

**Answer:**  
Instruction tuning involves training on tasks phrased as instructions, improving zero-shot and few-shot generalization. Unlike task-specific fine-tuning, it aligns the model with human-style inputs, increasing usability and reducing the need for prompt engineering.

---
