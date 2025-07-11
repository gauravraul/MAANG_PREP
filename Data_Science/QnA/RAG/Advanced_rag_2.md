# Advanced RAG Hands-On Answer

## Problem Recap

- High similarity scores, yet irrelevant retrieved documents
- Mostly on domain-specific legal subset
- Re-ranking is ineffective
- Answer hallucinations or shallow matches
- Latency increases during retrieval

---

## Root Causes & Fixes by Layer

### 🔹 1. Chunker Layer: Ineffective Chunking Strategy

**Issue:**  
Legal documents often contain long, hierarchical clauses. Default chunking (e.g., fixed-size windows or naive sentence tokenization) can break semantic coherence.

**Fix:**  
- Switch to **semantic-aware chunking** (e.g., using section headers, bullet structure, or clause delimiters)
- Consider **adaptive chunking** based on sentence similarity or title-aware chunking
- Tag each chunk with metadata (e.g., `section_type`, `clause_id`) for filtering during retrieval

---

### 🔹 2. Embedder Layer: Embedding Collapse or Irrelevant Representations

**Issue:**  
General-purpose embedding models (e.g., `text-embedding-ada-002`) struggle with legal jargon → resulting in **high cosine scores but poor semantic match**.

**Fix:**  
- Fine-tune the embedder on **in-domain legal corpora** using contrastive learning (e.g., SimCSE, TSDAE)
- Alternatively, switch to **domain-specialized models** (e.g., LegalBERT, Specter, or OpenLegalEmbedding)
- Perform **embedding diagnostics**: visualize with UMAP, check for cluster collapse

---

### 🔹 3. Retriever Layer: FAISS Index Inefficiencies and Latency

**Issue:**  
Retrieval slowdowns and poor results suggest:
- FAISS index may not be optimized (e.g., IVF/HNSW not tuned for dense clusters in legal text)
- Retrieval suffers from **low diversity of vectors**

**Fix:**  
- Rebuild FAISS index with better hyperparameters (`nlist`, `efSearch`) for dense legal vector clusters
- Use **hybrid retrieval** (dense + sparse via BM25 or SPLADE) to improve semantic range
- Add **filtering based on metadata tags** (jurisdiction, document type)

---

### 🔹 4. Query Layer: Poor Query-Chunk Alignment

**Issue:**  
User queries might be ambiguous or misaligned with formal legal language used in documents.

**Fix:**  
- Apply **query rewriting** using:
  - GPT-4 to reformulate user input in legal style (e.g., “How can I dissolve a partnership?” → “Legal procedure for partnership dissolution”)
  - Few-shot or zero-shot LLM rewriting chains
- Add **intent classification** + conditional retrieval pathways (e.g., different index per document subtype)

---

### 🔹 5. Reranker + Prompt Layer: Ineffective Context Usage & Misleading LLM Outputs

**Issue:**  
Reranker fails due to:
- Homogeneity in embedding space (everything looks equally relevant)
- LLM prompted with **irrelevant context**, leading to **hallucinations**

**Fix:**
- Use **cross-encoder reranking** (e.g., MiniLM, Cohere reranker) for sentence-level precision
- Implement **context weighting**: prioritize recent or jurisdiction-relevant sections
- In prompt template:
  - Add source attribution
  - Apply context verification step (“Is this chunk relevant to the question?”)
- Add **tool-augmented feedback** (e.g., vector similarity + shallow keyword overlap) before calling LLM

---

## Bonus Fixes (Systemic Improvements)

- Add a **chunk recall evaluation tool** (RAGAS, TruLens, LlamaIndex eval) to validate chunk relevance
- Use **dynamic context window** sizing based on query specificity
- Consider **per-query retriever selection** (shallow BM25 vs deep dense index)

---

## Summary Table

| Layer      | Issue                                      | Fix                                                                                   |
|------------|--------------------------------------------|----------------------------------------------------------------------------------------|
| Chunker    | Semantic misalignment                      | Semantic-aware chunking + metadata tagging                                            |
| Embedder   | General embeddings fail on legal text      | Fine-tune or switch to domain-specific embeddings                                     |
| Retriever  | Latency & false positives                  | Optimize FAISS, add hybrid (BM25 + dense) retrieval                                   |
| Query      | Poor query-chunk alignment                 | Query rewriting with GPT, intent classification, legal-style reframing                |
| Reranker   | Context irrelevance and hallucination      | Cross-encoder reranking, context filtering, verification in prompt                    |
