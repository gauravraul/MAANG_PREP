# Atlassian Lead Data Scientist – Sample Question 7 & Detailed Answer

## **Question**
Confluence has millions of pages, many of which become **outdated**, **duplicated**, or **rarely accessed** over time.  
Atlassian wants to build an **AI-driven Content Lifecycle Management System** that automatically:

- Flags outdated or stale pages  
- Detects conflicting or duplicated documentation  
- Suggests updates or archiving  
- Identifies authoritative versions of documentation  
- Surfaces the most relevant content for each team  

**Design this system end-to-end.**  
Explain:

1. How you define “stale”, “duplicate”, and “authoritative” content  
2. The data you need  
3. Feature engineering  
4. ML + heuristic models  
5. Content clustering & ranking  
6. Integration inside Confluence  
7. Evaluation metrics  
8. Reliability, trust & explainability  

---

## **Detailed Answer**

### **1. Defining Key Concepts**

#### **A. Stale Content**
A page is stale when:
- It hasn’t been updated for a long time  
- It receives minimal views  
- Linked Jira issues or code references have changed  
- It fails semantic checks (“contradictory to latest docs”)  
- Owner/team hasn’t interacted with it  

#### **B. Duplicate Content**
Two pages are duplicates if:
- They describe the same feature, API, or process  
- They share large semantic overlap  
- They have similar structure/headers (detect via embeddings)  
- They have similar link graphs or reference the same objects  

#### **C. Authoritative Content**
A page is authoritative if:
- It is frequently visited  
- Maintained by a responsible team  
- Backed by recent Jira issues or code commits  
- Linked in other pages (PageRank-like approach)  
- Often referenced in search queries  
- Factual consistency score is high  

---

### **2. Data Sources**

#### **Confluence Data**
- Page text (title, body, headings)  
- Comments  
- Edit history (timestamps & authors)  
- Page links & hierarchy (parents/children)  
- View analytics (traffic)

#### **Jira & Bitbucket Integration**
- Linked issues  
- Linked pull requests  
- Referenced code paths  
- Relevant release notes

#### **User Behavior Data**
- Search queries  
- Page click patterns  
- Edit sessions  
- Reactions/engagement  

---

### **3. Feature Engineering**

#### **A. Staleness Features**
- Time since last edit  
- Time since last viewed  
- View decay rate  
- Presence of outdated keywords (deprecated, replaced, old version)  
- Jira/PR mismatch indicators  

#### **B. Duplicate Detection Features**
- Transformer embeddings of page text  
- Header-level embeddings  
- Link graph similarity  
- Cross-page semantic similarity  
- Vector cosine similarity  

#### **C. Authoritative Page Features**
- PageRank score  
- View count trend  
- Number of inbound links  
- Ownership consistency  
- Recency of edits  
- Freshness of referenced code/Jira issues  

---

### **4. Modelling Approach**

Use three parallel models:

---

#### **A. Staleness Detection Model**
- **Binary classifier** for “stale vs. fresh”  
- Uses logistic regression / XGBoost / transformer-based sequence analysis  
- Includes time-series features of views and edits  

---

#### **B. Duplicate Detection Model**
Two-stage approach:

1. **Dual-encoder retrieval model**  
   - Embed pages  
   - Retrieve top similar pages  

2. **Cross-encoder re-ranking**
   - Jointly encode content pairs  
   - Determine:
     - Exact duplicate  
     - Partial overlap  
     - Conflicting documentation  
     - Completely unrelated  

Models use contrastive learning with:
- Positive pairs (same topic)  
- Hard negatives (same domain, unrelated content)

---

#### **C. Authoritativeness Scoring**
Ensemble of:
- ML scoring  
- Link graph centrality  
- User engagement metrics  
- Update recency  
- Reference consistency with Jira/Bitbucket  

Final output:  
**Authority Score (0–100)**

---

### **5. Content Clustering & Ranking**

#### **A. Topic Clustering**
Use:
- Hierarchical clustering  
- HDBSCAN  
- K-means on page embeddings  
- Graph community detection

Clusters represent:
- Feature docs  
- API documentation  
- Onboarding guides  
- Release notes clusters  

#### **B. Ranking**
For each cluster:
- Identify authoritative page  
- Derive a “canonical representative”  
- Rank others by:
  - Overlap  
  - Freshness  
  - Engagement  
  - Edit recency  

Use ranking models such as:
- LambdaMART  
- XGBoost ranker  
- Transformer scoring head

---

### **6. Integration Inside Confluence**

#### **Where insights appear**
1. **Page sidebar insight card:**
   - “This page is likely outdated (81% confidence). Last edit: 18 months ago.”  
   - “There are 3 overlapping pages.”  

2. **Editor Mode Suggestions:**
   - “This paragraph conflicts with updated API v3 docs.”  
   - “You might want to merge with PAGE-1011.”  

3. **Space/Workspace Dashboard:**
   - Stale pages list  
   - Duplicate clusters  
   - Top authoritative docs  

4. **Search enhancement:**
   - De-rank stale content  
   - Boost authoritative content  

---

### **7. Evaluation Metrics**

#### **Offline**
- Duplicate detection: Precision@K, Recall@K, NMI of clusters  
- Staleness model: AUC, F1, calibration  
- Authority scoring: correlation with human ratings  
- Clustering quality: silhouette score  

#### **Online**
- Reduction in stale content  
- Increased adoption of authoritative documents  
- Faster content discovery  
- User satisfaction (thumbs up/down)  
- Fewer conflicting pages in search results  

---

### **8. Reliability & Explainability**

To build trust:

- Expose drivers:
  - “This page is stale because it hasn’t been updated in 540 days.”  
  - “90% of traffic has moved to PAGE-2012.”  
- Provide confidence intervals  
- Allow override (“Mark as up-to-date”)  
- Use SHAP or attention highlights  
- Human-in-the-loop: user feedback informs retraining  
- Avoid aggressive deletion suggestions—recommend merging instead  

---

## **Final Takeaway**
This question evaluates your ability to design a sophisticated **content intelligence** solution involving:

- Semantic similarity  
- Graph-based ranking  
- Temporal modelling  
- UI-centric product thinking  
- Large-scale clustering  
- Cross-product integration (Jira + Confluence + Git)

This is the type of end-to-end system Atlassian expects a **Lead Data Scientist** to architect confidently.

---
