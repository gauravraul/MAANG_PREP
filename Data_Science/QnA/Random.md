# Random Advanced RAG (Retrieval-Augmented Generation) Questions and Answers

## 1. How can you implement fallback retrieval strategies in a RAG pipeline?

**Answer:**  
Fallback retrieval can be implemented by cascading retrievers—starting with a dense retriever and falling back to a sparse one (e.g., BM25) when confidence is low. You can also rerun queries with relaxed constraints or query expansion to improve retrieval hit rate.

---

## 2. What are the pros and cons of using ColBERT-style late interaction models in RAG?

**Answer:**  
**Pros:** Efficient indexing, scalable to large corpora, flexible query-document scoring.  
**Cons:** Slower inference due to late interaction overhead, requires token-level matching logic, harder to fine-tune jointly with the generator.

---

## 3. How does cross-attention between retrieved documents and decoder tokens improve generation?

**Answer:**  
Cross-attention allows the decoder to directly attend to token-level details in retrieved documents, enabling more grounded and contextually accurate generation. It supports fine-grained alignment between evidence and response tokens.

---

## 4. Why is re-ranking important in RAG pipelines, and what models are commonly used?

**Answer:**  
Re-ranking improves retrieval precision by evaluating the semantic fit of documents post initial retrieval. Common re-rankers include BERT, monoT5, and Cross-Encoders, which score documents more accurately based on the query.

---

## 5. How does chunk overlap size affect retrieval performance?

**Answer:**  
Larger overlap increases context preservation across chunks but at the cost of redundancy and higher token usage. It improves recall for queries that span chunk boundaries but can degrade efficiency.

---

## 6. In a multilingual RAG system, what challenges arise and how are they mitigated?

**Answer:**  
Challenges include cross-lingual embedding alignment, uneven corpus distribution, and language detection. Solutions involve using multilingual retrievers (e.g., mBERT, LaBSE), language-specific indexing, and dynamic query translation.

---

## 7. What is vector drift in the context of RAG and how do you detect it?

**Answer:**  
Vector drift occurs when embedding distributions shift due to retriever updates or data domain changes. It's detected by monitoring embedding norms, cosine similarity distributions over time, and retrieval quality degradation.

---

## 8. How can caching be used in RAG for faster inference?

**Answer:**  
Caching query embeddings, retrieval results, and even full generation outputs for repeated inputs can dramatically reduce latency. Memoization techniques and semantic caching with approximate matches are effective.

---

## 9. What is hard negative mining and how does it improve retriever training?

**Answer:**  
Hard negatives are misleading documents that seem relevant but are not. Including them during training forces the retriever to better discriminate between closely related but irrelevant content, boosting precision.

---

## 10. What are common pitfalls in evaluating RAG systems with exact match or BLEU?

**Answer:**  
Exact match and BLEU fail to capture semantic relevance, penalize paraphrasing, and ignore evidence grounding. Better metrics include faithfulness scores, answer attribution (e.g., provenance-based), and human evaluation.

---
