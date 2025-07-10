# Advanced RAG Hands-On Question

## Question

You’ve built a production-grade Retrieval-Augmented Generation (RAG) pipeline using a combination of:

- FAISS for dense vector similarity search over a corpus of 1 million documents.
- A custom chunking strategy with dynamic window sizes.
- LangChain for orchestration and OpenAI GPT-4 as the LLM.
- Pinecone for long-term memory indexing of conversations.
- Prompt compression to fit context into 8k tokens.
- A custom feedback loop to re-rank retrieved documents using user behavior.

**Issue:**
Your RAG chatbot gives highly irrelevant or hallucinated answers only when querying over domain-specific legal documents (~300k docs subset). You inspect the retrieval logs and notice:

- High cosine similarity scores for retrieved documents
- Poor semantic overlap between queries and results
- Re-ranking rarely helps due to homogeneous embeddings
- Retrieval latency is higher for legal subset
- Answers often quote correct-looking sections but semantically misaligned

### Based on this scenario, answer the following:

> What are the **five most likely reasons** for these symptoms (retrieval appears high scoring, but context is irrelevant), and what **hands-on changes** would you apply at **each layer** of the RAG stack (retriever, chunker, embedder, LLM, re-ranker) to address this issue without degrading performance on non-legal documents?

> Include:
- Concrete changes to chunking and embedding strategies
- Advanced techniques like query rewriting, hybrid retrieval, and prompt re-weighting
- Practical implications of embedding space collapse and semantic drift in fine-tuned LLMs

## Evaluation Criteria

- Demonstrated understanding of **semantic retrieval pitfalls**
- Awareness of **embedding space behavior in high-domain specificity**
- Knowledge of **chunk-query interaction**
- Ability to tune **vector search + reranking + prompt engineering**
- Insight into **real-world performance vs. theoretical recall**
