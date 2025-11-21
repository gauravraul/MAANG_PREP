# Atlassian Lead Data Scientist – Sample Question 8 & Detailed Answer

## **Question**
Atlassian wants to build a **Context-Aware Inline AI Assistant** inside Jira and Confluence that provides *real-time suggestions* while users are writing or editing content.  
This assistant should:

- Suggest relevant Jira issues or Confluence pages  
- Recommend templates, labels, or components  
- Auto-complete technical descriptions  
- Identify missing information (steps to reproduce, acceptance criteria, impact, root cause)  
- Provide quick actions (link issue, add component, assign owner, generate summary)  

**Design an end-to-end system that powers this context-aware inline assistant.**  
Explain:

1. How to understand user context in real time  
2. What data and signals the system will use  
3. Context-to-action modelling  
4. RAG (Retrieval Augmented Generation) approach  
5. Safety, privacy & access control  
6. Deployment & latency constraints  
7. Evaluation strategies  

---

## **Detailed Answer**

### **1. Understanding User Context (Real-Time Context Extraction)**

The assistant needs to read the user's current environment and detect:

#### **A. Document Context**
- Current text in editor (partial, incomplete sentences)  
- Issue description, summary, fields filled & missing  
- Page section user is typing in (heading, code block, table)  
- Historical versions of the issue/page  

#### **B. Structural Context**
- Project  
- Component  
- Issue type (bug/story/task)  
- Linked issues  
- Page parent/space hierarchy  

#### **C. User Intent Signals**
Detect intent through pattern classification:

- Bug report style?  
- RCA document?  
- Meeting notes?  
- API documentation?  
- Feature request?  

Run a lightweight **intent detection model** to classify in <20ms.

---

### **2. Data & Signals Used**

#### **A. Content Data**
- Jira issue history  
- Confluence documents  
- Embeddings of past similar issues or docs  
- Issue templates & documentation templates  

#### **B. Behavioral Data**
- Developer actions (linking, commenting, assigning)  
- Click patterns  
- Search history (within Jira/Confluence)  

#### **C. Metadata & Graph Signals**
- Issue linking graph  
- Project → component mapping  
- Team → responsibility graph  
- Code-owner mapping for Bitbucket repos  

#### **D. Real-Time Editor Signals**
- Current cursor position  
- Partial text typed  
- Missing required fields  

This enables **contextual intelligence**.

---

### **3. Context-to-Action Modelling**

The assistant must choose **what type of help** to provide.

Build a **hierarchical policy model**:

#### **A. Level 1: Intent Detection**
- Identify document type  
- Classify issue type  
- Detect missing fields  

#### **B. Level 2: Action Selection Model**
Multi-label classifier that predicts:
- Suggest related issues  
- Generate description/summary  
- Recommend labels/components  
- Offer “assign to X”  
- Provide bug root-cause structure  
- Suggest documentation templates  

Input features:
- User typing context  
- Page/issue metadata  
- Semantic embedding of text  
- Team patterns  

#### **C. Level 3: Response Generation**
Use:
- LLM for text generation (summaries, suggestions)  
- Search + ranking for relevant items  
- Rules for missing mandatory fields  

---

### **4. Retrieval-Augmented Generation (RAG) Architecture**

User typing → Context Extractor → Query Generator → Vector Search → Top-K Docs → LLM with Context → Inline Suggestions

#### **A. Query Generator**
- Convert partial text into semantic query  
- Expand using synonyms and prior issue components  
- Add project & component context  

#### **B. Vector Retrieval**
Retrieve:
- Related Jira issues  
- Relevant Confluence pages  
- Troubleshooting guides  
- API references  
- Recently visited pages  

Vector DB: FAISS/Milvus/Pinecone  
Latency target: < 30 ms

#### **C. LLM Integration**
LLM receives:
- User text  
- Retrieved context  
- Issue fields  
- Team templates  
- Project metadata  

LLM outputs:
- Summary  
- Suggested fields  
- Suggested links  
- Missing information recommendations  
- Inline auto-completion  

LLM must be **grounded**, **restricted**, and **factual**.

---

### **5. Safety, Privacy & Access Control**

Atlassian environments contain private data → system must fully respect permissions.

#### **A. Access Control Layer**
- Only retrieve issues the user has access to  
- Filter RAG context based on Confluence space permissions  
- Follow admin, project-level, and group-level access rules  

#### **B. Privacy Rules**
- Do not suggest content from private projects  
- No cross-tenant leakage  
- Sensitive content masking for PII or secure documents  
- Enterprise domain isolation  

#### **C. LLM Safety**
- Block hallucinated links  
- Validate all suggested issue keys exist  
- Restrict generation to templates + verified sources  

---

### **6. Deployment Architecture & Latency Constraints**

#### **Architecture**

Editor → Lightweight On-Client Context Encoder → Server Feature Store → Retrieval Service → LLM Service → Inline UI

#### **Latency Budget**
- Context extraction: 5–10ms  
- Retrieval: 20–30ms  
- LLM generation: 50–120ms  
- Total target: **< 200ms**  

#### **Caching**
- Per-project template cache  
- Per-team recommended component cache  
- LRU cache for recent issues/pages  

#### **Fallback**
If LLM unavailable:
- Rule-based suggestions only (fields, templates)  
- Keyword-based retrieval  

---

### **7. Evaluation & Success Metrics**

#### **Offline Evaluation**
- Precision@K for suggestion relevance  
- Coverage of recommended actions  
- Template applicability  
- Embedding quality & recall for retrieval  
- Hallucination rate  

#### **Online Evaluation**
- Acceptance rate of inline suggestions  
- Reduction in issue creation time  
- Improved issue quality (fewer back-and-forth comments)  
- Higher completeness of bug templates  
- Search-to-discovery reduction  

#### **A/B Testing**
- Compare:
  - Time to complete issue  
  - Quality of content  
  - How often users modify suggestions  
  - Engagement metrics  

#### **Qualitative**
- Developer trust  
- User satisfaction  
- Feedback from EMs & PMs  

---

## **Final Takeaway**
This question tests whether you can design a **real-time, context-aware AI system** deeply integrated into Jira & Confluence workflows.  
To excel, demonstrate skills in:

- Retrieval + LLM integration  
- Real-time inference  
- Document/issue understanding  
- Privacy & access control  
- Product-oriented ML design  
- Evaluation and UX-driven insights  

This is a high-level, real-world Atlassian Lead Data Scientist challenge.

---
