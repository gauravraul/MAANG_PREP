# 10 Random Hard GenAI Questions and Answers

---

## 1. What is the difference between Parameter-Efficient Fine-Tuning (PEFT) techniques like LoRA and QLoRA, and how do they impact training and inference?

**Answer:**  
LoRA introduces low-rank adapters during training, freezing base weights, reducing compute needs. QLoRA combines quantized base models with LoRA adapters, allowing even larger models to be trained on consumer hardware with minimal degradation. At inference, only adapters are active on top of a quantized base.

---

## 2. How do you design a hybrid RAG architecture using both dense and sparse retrievers?

**Answer:**  
You run both retrievers in parallel or sequence, combine their top-k results (union or weighted), and optionally rerank using a cross-encoder. This balances high recall (sparse) with deep semantics (dense), reducing hallucinations.

---

## 3. Explain attention head pruning and its role in optimizing transformer models.

**Answer:**  
Attention head pruning removes redundant heads (via saliency analysis or learned mask scores), reducing model size and computation. It must be done carefully to avoid harming performance, and often requires fine-tuning post-pruning.

---

## 4. Describe an approach to convert an LLM into a multimodal model.

**Answer:**  
Use a vision encoder (e.g., CLIP or ViT), project the image embeddings through a linear adapter to match the LLM’s input embedding space, prepend them as pseudo tokens to text inputs, and optionally fine-tune the full pipeline on vision-language tasks.

---

## 5. How does gradient checkpointing work and why is it useful in training large models?

**Answer:**  
Gradient checkpointing saves memory by only storing a subset of intermediate activations during the forward pass and recomputing them during backpropagation. It trades compute for memory and enables training larger models on limited GPUs.

---

## 6. In a production RAG system, what strategies do you use to detect and handle hallucinations?

**Answer:**  
Techniques include source attribution scoring, hallucination detection classifiers, retrieval confidence thresholds, evidence highlighting for validation, and fallback to extractive QA when grounding fails.

---

## 7. What are the challenges in quantizing a transformer-based decoder-only LLM and how do you resolve them?

**Answer:**  
Decoder-only models are sensitive to quantization noise due to unidirectional attention and causal masking. Use group-wise or per-channel quantization, smooth activation functions (e.g., SmoothQuant), and quantization-aware training for stability.

---

## 8. How would you use reinforcement learning (RLHF) to improve a model's factuality in a RAG setup?

**Answer:**  
Define a reward function based on fact-grounding (e.g., cosine similarity with retrieved docs, citation accuracy), then apply Proximal Policy Optimization (PPO) on top of the generator, using reward scores to fine-tune for truthful generation.

---

## 9. What is the difference between soft prompts and prefix tuning, and when would you prefer one over the other?

**Answer:**  
Soft prompts are learned embeddings prepended to inputs, while prefix tuning involves learning key-value pairs injected into attention layers. Prefix tuning often works better in larger models; soft prompts are more lightweight and flexible.

---

## 10. Explain the bottleneck that arises in large-scale retrieval systems and how FAISS indexing alleviates it.

**Answer:**  
Naive similarity search scales poorly with corpus size. FAISS uses Approximate Nearest Neighbor (ANN) algorithms (e.g., IVF, HNSW) for sublinear search time and GPU acceleration, making real-time dense retrieval feasible.

---
