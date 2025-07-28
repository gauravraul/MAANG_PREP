# Mitigation Strategies for LLMs and RAG: Critical Thinking Questions and Answers

## 1. How can we mitigate hallucinations in LLMs?

**Answer:**  
Hallucinations can be reduced using techniques such as Retrieval-Augmented Generation (RAG), grounding responses in reliable data sources, adding fact-checking pipelines post-generation, and training with human feedback (RLHF). Ensuring that prompts explicitly request sources or constraints also reduces speculative generation.

---

## 2. What strategy helps prevent outdated responses in RAG systems?

**Answer:**  
Use real-time or frequently updated data sources in the retrieval backend. Implementing periodic re-indexing of document stores and using dynamic querying mechanisms that prioritize recent documents mitigates the issue of stale outputs.

---

## 3. How can we reduce latency in RAG architectures during inference?

**Answer:**  
Optimize retrieval with approximate nearest neighbor (ANN) search libraries like FAISS or ScaNN, compress embeddings with quantization, and use caching layers for repeated queries. Also, minimize the number of retrieved documents (`k`) without sacrificing context quality.

---

## 4. What are some ways to improve context relevance in RAG pipelines?

**Answer:**  
Use hybrid retrieval (dense + sparse), fine-tune retrievers with hard negatives, apply re-ranking mechanisms like Cross-Encoders, and consider query rewriting techniques to align the intent better with document contents.

---

## 5. How can token limitations in LLMs be addressed when passing context?

**Answer:**  
Apply chunking and summarization to input documents, utilize models with larger context windows, or switch to hierarchical RAG where multiple retrievals are summarized and then passed into the LLM. Condensing long documents into structured formats (e.g., tables or bullet points) can also help.

---

## 6. How do you prevent LLMs from revealing sensitive or private information?

**Answer:**  
Apply data anonymization, enforce privacy-preserving training (e.g., differential privacy), monitor outputs for PII, and implement strict access control on logs and inference endpoints. For RAG, avoid indexing sensitive documents unless access is scoped.

---

## 7. What measures help mitigate domain shift in LLM outputs?

**Answer:**  
Fine-tune the model or retriever on domain-specific corpora, use in-context examples from the target domain, and dynamically select prompts or retrieval queries based on domain classification. Evaluate frequently with domain-specific benchmarks.

---

## 8. How can drift in the knowledge base used in RAG be managed?

**Answer:**  
Automate document ingestion pipelines with versioning, schedule periodic data refreshes, monitor performance metrics (e.g., BLEU, precision@k), and flag outdated documents based on timestamps or content drift detection algorithms.

---

## 9. How can prompt injection attacks be mitigated?

**Answer:**  
Apply prompt sanitization, input validation, user role conditioning, and test LLMs against known attack vectors. For RAG, control the retrieved documents’ trustworthiness and filter malicious content at the retrieval stage.

---

## 10. What architectural strategies ensure reliability and robustness in GenAI applications?

**Answer:**  
Use fallback mechanisms (e.g., rule-based systems when confidence is low), implement LLM ensembles, monitor output reliability scores, use evaluation gates with heuristics or classifiers, and test the system under adversarial and noisy inputs.

---
