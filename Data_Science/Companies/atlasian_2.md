# Atlassian Lead Data Scientist – Sample Question 2 & Detailed Answer

## **Question**
Jira and Confluence contain millions of documents, comments, tickets, and logs.  
You are asked to design an **AI-powered semantic search system** that returns the most relevant results across Jira issues, Confluence pages, and team conversations *in real time*, even when users search using vague or incomplete queries.

**Explain how you would build:**
1. The retrieval pipeline  
2. The ranking system  
3. How to handle different data modalities (tickets, pages, chats)  
4. How you would evaluate and measure success  
5. How you would scale and monitor the system  

---

## **Detailed Answer**

### **1. Retrieval Pipeline (RAG-Style Architecture)**

To power cross-product semantic search:

#### **a. Data Ingestion & Indexing**
- Extract text from **Jira** issues (summary, description, comments)
- Extract content from **Confluence** pages (body, headers, metadata)
- Index **Slack/Teams-style** conversations if integrated  
- Convert all items into **dense vector embeddings**

#### **b. Embedding Model**
- Use a domain-adapted transformer (e.g., fine-tuned on engineering & documentation text)
- Multi-modal embeddings for:
  - Text content  
  - Metadata (project names, tags, components)  
  - User interactions (clicks, comments, edits)

#### **c. Vector Store**
- Use a scalable vector DB (FAISS, Milvus, Pinecone)
- Partition by product type (Jira, Confluence)  
- Maintain both:
  - **Approximate nearest neighbour (ANN)** index (fast)
  - **Exact index** for small high-precision subsets

#### **d. Query Understanding**
- Semantic parsing to detect:
  - User intent (“bug fix”, “design doc”, “performance issue”)
  - Product context (Jira issue vs. page vs. sprint)
- Query expansion via:
  - Synonym mappings  
  - Historical user behaviour  
  - Team vocabulary

This forms the **first-stage retrieval** returning 100–300 documents.

---

### **2. Ranking System (Re-ranking Layer)**

After retrieval, we re-rank results for **precision**.

#### **a. Cross-Encoder Re-ranker**
- Use a BERT-based cross-encoder that jointly encodes **query + document**
- Produces highly precise relevance scores  
- Handles vague queries better

#### **b. Multi-Signal Ranking Model**
Combine signals:
- Semantic similarity score  
- Metadata match quality (project, team, label)  
- User intent match  
- Recency score (freshness)  
- User personalization features  
- Click-through rate priors

This model can be:
- XGBoost ranker  
- LightGBM ranker  
- Or a transformer-based ranking head

#### **c. Final Output**
Return only 5–10 high-quality results with explanations like:
- “This page is relevant because it mentions similar errors in your project.”  
- “This issue belongs to the same component and sprint.”

---

### **3. Handling Different Data Modalities**

#### **Jira Issues**
- Highly structured  
- Extract fields: components, labels, priority, issue type  
- Use hierarchical embeddings  
  - Issue summary  
  - Description  
  - Comments  

#### **Confluence Pages**
- Long documents  
- Break into chunks (512–1024 tokens)  
- Use hierarchical embeddings (page embedding + chunk embeddings)

#### **Chat Logs**
- Short messages  
- Use conversation windows (4–10 messages)  
- Add speaker, role, timestamps

#### **Metadata Handling**
- Encode metadata as:
  - Learnable embeddings  
  - One-hot + numerical features  
  - Graph embeddings (project graph)

---

### **4. Evaluation & Success Metrics**

#### **Offline Metrics**
- **NDCG@K**, **MRR**, **Recall@K**  
- First-token latency (P95 & P99)  
- Cross-product consistency (Jira/Confluence/chat mix quality)

#### **Online Metrics**
- Click-through rate (CTR)  
- Success rate: “Did the user stop searching after clicking?”  
- Reduced time to find relevant documents  
- Search abandonment rate  
- Personalized ranking adoption

#### **Relevance Judgment**
- Use:
  - Human-labeled relevance sets  
  - Pairwise preference labeling  
  - Implicit feedback (clicks, dwell time)

---

### **5. Scaling & Monitoring**

#### **Scalability Approaches**
- Sharded vector index (per product or team)  
- Distributed index across nodes  
- Caching top-K results for popular queries  
- Keeping embeddings updated via:
  - Incremental updates  
  - Daily batch refresh

#### **Monitoring**
- Embedding drift  
- Query distribution drift  
- Index freshness  
- Latency:
  - ANN retrieval latency  
  - Re-ranker latency  
  - End-to-end latency < 200ms target

#### **Failure Handling**
- Fallback to keyword search (BM25)  
- Safe degradation when embedding pipeline fails  
- Confidence scoring to avoid misleading results

---

## **Final Takeaway**
This question tests whether a Lead Data Scientist can:

- Design production-grade **semantic search**  
- Understand **retrieval + ranking** systems  
- Handle multi-modal, cross-product enterprise data  
- Think in terms of **latency, relevance, scaling, and UX**  
- Work at the intersection of ML + search infrastructure + product thinking

If you can explain this clearly, you're showing strong mastery for an Atlassian-level Lead DS role.

---
