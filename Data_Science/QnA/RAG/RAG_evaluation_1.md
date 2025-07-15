# RAG Evaluation: 10 Advanced Questions & Answers

These questions test deep understanding of how to evaluate and improve Retrieval-Augmented Generation systems.

---

## 1. How do you measure the relevance of retrieved documents in a RAG pipeline?

**Answer:**  
Use metrics like:
- **Recall@k**: Measures if the ground-truth document is among top-k retrieved.
- **Precision@k**: Measures how many of the top-k are actually relevant.
- **nDCG (Normalized Discounted Cumulative Gain)**: Considers position and relevance level of documents.
- **Embedding similarity** and **BM25 score** can also serve as proxy indicators.

---

## 2. What does “faithfulness” mean in RAG evaluation, and how do you measure it?

**Answer:**  
Faithfulness refers to whether the generated answer is **supported by retrieved documents**.

Measured by:
- **Manual annotation**: Experts verify if claims in the answer are grounded in context.
- **RAGAS (RAG Evaluation Toolkit)**: Uses LLMs to compare generation against context and score faithfulness.
- **TruLens**: Provides attribution scores per sentence.

---

## 3. How can hallucination be detected in RAG outputs?

**Answer:**
Hallucination is when the LLM generates **confident but unsupported or false claims**.

Detection methods:
- Compare generated answer to retrieved context.
- Use LLM-based verifiers like GPT-4 to ask: “Is this sentence present or implied in the provided context?”
- Track hallucination frequency using **RAGAS's faithfulness metric** or **LLM-as-a-judge** setups.

---

## 4. What is context recall, and why is it important?

**Answer:**  
Context recall = **whether relevant information was present in retrieved context**.

If the model fails to generate the correct answer, low context recall suggests the retriever is failing. Measured via:
- Exact match of expected context in retrieved chunks
- Evaluated in tools like RAGAS and LlamaIndex’s eval suite

---

## 5. What are good evaluation datasets for RAG pipelines?

**Answer:**  
Depends on task. Examples:
- **Natural Questions**, **HotpotQA**: for fact-based QA with ground truth context
- **FiQA**, **TREC CAR**: for finance or biomedical retrieval tasks
- **Custom synthetic datasets**: Generated using GPT with traceable contexts

---

## 6. How do you evaluate rerankers in a RAG pipeline?

**Answer:**
You compare retrieval performance **before and after reranking** using:
- **nDCG**, **Recall@k**, **MAP (Mean Average Precision)**
- Measure impact on final generation: does reranking improve faithfulness or answer quality?
- Ablation: run RAG with and without reranker to test its contribution

---

## 7. What role does human evaluation play in RAG?

**Answer:**  
Essential for:
- Assessing answer quality beyond automatic metrics
- Measuring perceived factuality, coherence, and completeness
- Ground-truthing attribution: “Did this sentence come from document X?”

Human feedback can be collected via Likert scales or ranking comparisons (A/B tests).

---

## 8. How can you evaluate long-context RAG systems (e.g., 100k tokens)?

**Answer:**  
Challenges:
- High compute cost
- Evaluating precision over large windows

Solutions:
- **Chunk-level attribution**: Map which chunk each sentence uses
- Use synthetic long-context QA datasets
- Apply **progressive context filtering** and evaluate precision vs. recall tradeoff

---

## 9. What is the impact of retrieval latency on evaluation?

**Answer:**  
Retrieval latency affects UX and system throughput. Key metrics:
- **P95 retrieval time**
- **End-to-end generation latency**
- Use caching, hybrid indexes, and async pipelines to reduce it

In evaluations, balance quality vs. latency by tuning:
- Top-k
- Reranker models
- Pre-filtering logic

---

## 10. What tools or frameworks can help evaluate RAG pipelines?

**Answer:**  
- **RAGAS**: Open-source framework for evaluating faithfulness, context recall, answer relevance.
- **TruLens**: Real-time tracking of attribution, generation quality, and prompt safety.
- **LangSmith (LangChain)**: Logging and evaluation with prompt chains and output traces.
- **LlamaIndex eval**: Supports chunk-level retrieval validation and QA consistency.

---
