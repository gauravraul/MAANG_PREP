# Challenges and Limitations in RAG – Questions & Answers

## Q1. Why does RAG sometimes return incorrect or hallucinated answers even with relevant retrieved documents?

**A1.**  
The generator may not effectively ground its response in the retrieved documents due to:
- Poor fusion of retrieved context with query
- Over-reliance on its pretrained knowledge
- Lack of explicit verification mechanisms between retrieved content and output

---

## Q2. What are the main limitations of dense retrievers (like DPR) used in RAG?

**A2.**  
- **Semantic drift:** Misses important lexical cues present in user query  
- **Limited generalization to out-of-domain queries**  
- **Heavy compute and storage** for large index sizes  
- **Retraining required** when adding new domain knowledge

---

## Q3. How does context window limitation affect RAG?

**A3.**  
- Only a few top documents can be injected into the context due to token limits  
- Important info from lower-ranked documents gets truncated  
- Requires chunking + ranking + reranking strategies to mitigate loss of relevance

---

## Q4. What are the challenges in chunking documents for retrieval?

**A4.**  
- **Over-chunking:** May lose semantic completeness  
- **Under-chunking:** May reduce retrievability due to noise  
- **Lack of structure-aware chunking** (e.g., breaking at section boundaries, preserving metadata) leads to retrieval of irrelevant or incoherent fragments

---

## Q5. Why does RAG often struggle with multi-hop or reasoning-based queries?

**A5.**  
- Retrieved passages are independent; not stitched for multi-hop reasoning  
- Generator isn’t designed to perform symbolic reasoning across disparate pieces  
- Requires special multi-hop retrievers or planning-based reasoning chains

---

## Q6. What makes RAG systems hard to evaluate?

**A6.**  
- Multiple valid answers can exist (open-endedness)  
- Lack of explainability on whether answer came from retrieved docs or model memory  
- Evaluating retrieval and generation separately is hard in end-to-end setups  
- Standard metrics like BLEU/ROUGE don’t capture factual grounding

---

## Q7. What are the operational and infrastructure challenges in deploying RAG systems?

**A7.**  
- Need to maintain:
  - Vector stores (e.g., FAISS, Pinecone)
  - Index refresh pipelines  
  - Retriever-generator latency coordination  
- Expensive GPU + RAM requirements for hybrid retriever-generator architecture  
- Online update of corpus requires background indexing and synchronization

---

## Q8. How does retrieval latency impact RAG performance?

**A8.**  
- Retrieval adds a blocking I/O step before generation  
- Cold starts or large-scale vector search can significantly delay response  
- Requires optimizations like ANN (Approx. Nearest Neighbors), caching, or hybrid search (BM25 + dense)

---

## Q9. Why is document freshness a concern in RAG?

**A9.**  
- Indexes may become stale if not updated frequently  
- Requires incremental indexing pipelines, hard to do in real-time  
- Harder to maintain for user-uploaded content (e.g., personal RAG agents)

---

## Q10. How can hallucination still happen even with accurate retrieval?

**A10.**  
- Generator may prioritize fluency over factual correctness  
- Misalignment between input embeddings and the actual text content  
- Retrieved docs may be ambiguous or require disambiguation logic

---

## Q11. What is the issue with "query drift" in RAG?

**A11.**  
- Reformulation or embedding of query may lose intent  
- Particularly problematic when user query is vague or multi-intent  
- Query rewriting pipelines may fix one problem but introduce others

---

## Q12. What limitations arise when using off-the-shelf RAG pipelines like LangChain or LlamaIndex?

**A12.**  
- Limited transparency and control over internal operations (e.g., chunking, retrieval logic)  
- Tight coupling with specific vector DBs or model architectures  
- Hard to debug retrieval failures or tuning misalignment without custom hooks

---

## Q13. Can RAG fail silently? If yes, how?

**A13.**  
Yes.  
- System may retrieve irrelevant docs but still generate fluent-sounding output  
- Hallucinations are often plausible but subtly incorrect  
- User may not realize model is "making up" information due to lack of confidence estimates or provenance tagging

---

## Q14. Why is grounding detection and attribution still a limitation in RAG?

**A14.**  
- No standard way to ensure every part of the answer is supported by a specific retrieved chunk  
- Requires post-generation grounding checks or citation-based methods (e.g., Attributed QA)  
- Difficult in multi-hop, long-form, or abstractive answers

---

## Q15. How does retrieval bias affect fairness in RAG?

**A15.**  
- Biased documents in the corpus → biased retrieval → biased generation  
- Popular documents or high-frequency terms dominate top-k results  
- Hard to enforce fairness, diversity, or representational balance in search

---
