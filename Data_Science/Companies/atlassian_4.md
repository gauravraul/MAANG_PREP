# Atlassian Lead Data Scientist – Sample Question 4 & Detailed Answer

## **Question**
Jira users often complain about **duplicate issues** being created across teams and projects.  
Atlassian wants to build a system that **automatically detects potential duplicates**, shows them during issue creation, and prevents duplicate backlog growth.

**Design an end-to-end duplicate issue detection system for Jira.**  
Explain:

1. How you define "duplicate" in a Jira ecosystem  
2. The data and features you will use  
3. The modelling architecture  
4. The search + ranking pipeline  
5. UI integration inside Jira  
6. Evaluation & monitoring strategies  

---

## **Detailed Answer**

### **1. Defining “Duplicate” in Jira**
Jira duplicates are different from classical duplicate documents because:

- Two issues may **use different language** but describe the same problem  
- Two issues may belong to **different components** but refer to the same root cause  
- Issues may have **partial overlaps** (not exact duplicates but near-duplicates)  
- Duplicates may be:
  - Exact duplicates  
  - Semantic duplicates  
  - Related issues  
  - Same bug, different symptoms  
  - Same root cause (bug cluster)

Thus, the system must predict a **similarity spectrum**, not a binary label.

---

### **2. Data & Features**

#### **Text Features**
- Summary  
- Description  
- Steps to reproduce  
- Stack traces / logs attached  
- Comments  
- Resolution reason

#### **Metadata Features**
- Components, labels, product area  
- Reporter, assignee history  
- Issue type (bug/task/story)  
- Sprint/epic associations  
- Creation and resolution date

#### **Behavioral Features**
- How often users click & link issues as duplicates  
- “Similar issues” chosen historically (implicit feedback)

#### **Graph Features**
- Linked issues graph  
- Project/component relationship graph  
- Bug cluster similarity graph

---

### **3. Modelling Architecture**

The best architecture is a **Two-Stage Retrieval + Re-ranking System**.

#### **Stage 1: Embedding-based Retrieval**
Generate embeddings for:

- Issue text  
- Issue metadata  
- Graph embeddings (optional)

Embedding models:
- Domain-adapted BERT/RoBERTa  
- Sentence-transformers  
- Or a fine-tuned dual-encoder trained on Jira duplicate pairs

Use **contrastive learning**:
- Positive pairs: historically marked duplicates  
- Hard negatives: non-duplicate issues in the same project  
- Soft negatives: unrelated issues from other domains

Output: top 50–200 potential duplicates.

---

#### **Stage 2: Cross-Encoder Re-ranking**
For higher precision:

- Use a **cross-encoder** that jointly encodes  
  `query issue + candidate issue`  
- Compute fine-grained similarity relevance score  
- Include metadata & graph features into the input

This re-ranking model learns subtle differences between:

- Duplicate  
- Related  
- Non-related

---

### **4. Search + Ranking Pipeline**

User typing issue → Query Embedder → ANN Search → Candidate Issues → Cross-Encoder → Top-N Ranked Duplicates → UI Hints

#### **Query Understanding**
As the user types:

- Extract keywords  
- Compute semantic embedding on the fly  
- Retrieve similar issues within 20–50 ms

#### **Latency Budget**
- ANN retrieval: <10–15ms  
- Cross-encoder re-ranking: <50–70ms  
- Total end-to-end: <100ms (with batching & caching)

#### **Freshness**
- Embeddings updated incrementally every hour or daily  
- New issues indexed immediately with approximate embedding from summary

---

### **5. UI Integration Inside Jira**

#### **During Issue Creation**
- As soon as user enters a **summary**, show:

Possible duplicates:

ISSUE-123: Login fails with 500 error

ISSUE-456: Token refresh endpoint not working

ISSUE-789: Authentication timeout issue


- Indicators:
- Similarity score  
- Confidence  
- Component match  

#### **During Issue Viewing**
- Option: “This looks similar to ISSUE-1010” sidebar card  
- Suggest linking issues  
- Allow user feedback:
- “Mark as duplicate”
- “Not a duplicate” (used to retrain models)

#### **In Project Backlogs**
- Auto-cluster similar issues  
- Suggest merging duplicates  
- Show “bug clusters” to engineering managers

---

### **6. Evaluation & Monitoring**

#### **Offline Evaluation**
- Precision@5, Recall@5  
- MAP, MRR  
- Hard-negative separation accuracy  
- Duplicate cluster coherence scores  
- Ablation studies:
- text only vs. text+metadata vs. text+graph

#### **Online Evaluation**
- Duplicate linking rate  
- Reduction in backlog noise  
- Percent of issues resolved faster  
- User adoption of suggestions  
- Feedback ratios (helpful vs. not helpful)

#### **Monitoring in Production**
- Embedding drift  
- Latency distribution  
- Index freshness  
- Alert on missing clusters  
- Degraded accuracy due to vocabulary or product changes

---

## **Final Takeaway**
This question tests your ability to design a real-world **semantic similarity + retrieval + ranking system**—one of the most common and important problem spaces in Atlassian products.

A strong answer demonstrates:
- ML architecture mastery  
- Search systems knowledge  
- UX-level product thinking  
- Feedback loops + model evolution strategies  
- Understanding Jira’s text-heavy domain  

This is a top-tier Lead Data Scientist–level question at Atlassian.

---
