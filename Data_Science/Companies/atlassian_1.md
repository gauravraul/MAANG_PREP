# Atlassian Lead Data Scientist – Sample Question & Detailed Answer

## **Question**
At Atlassian, many product features (like Jira recommendations, issue assignment suggestions, or intelligent search) rely on ML models that operate across multiple teams and highly unstructured text data.  
**Design an end-to-end system that automatically recommends the “next best action” for a user working on a Jira issue (e.g., assign to someone, add a label, add a component, or link to another issue).**  

Describe:
1. How you would frame the problem  
2. What data you need  
3. Modelling approach  
4. System architecture  
5. How you will evaluate & monitor it in production  
6. Trade-offs and pitfalls  

---

## **Detailed Answer**

### **1. Problem Framing**
This is a **multi-task recommendation** problem where the system predicts several possible actions a user might take next.  
It can be framed as:

- **Multi-label classification** (suggest multiple actions at once)  
- **Action ranking** (score each possible action and recommend the top-N)  
- **Contextual recommendation** (condition suggestions on user, project, and issue state)

Given Atlassian’s scale, the model needs to be **real-time**, **privacy-safe**, and **interpretable**.

---

### **2. Data Required**
You can leverage existing Jira logs:

#### **Issue-level data**
- Summary, description, comments  
- Labels, components, status transitions  
- Priority, SLA fields  
- Historical actions taken on similar issues  
- Linked issues (epics, subtasks, blockers)

#### **User-level data**
- User’s role in the project  
- User-issue interaction history  
- Workload & recently assigned issues  
- Past actions the user tends to take (action habit graph)

#### **Project-level data**
- Project metadata  
- Workflow configurations  
- Common transitions

#### **Additional behaviour logs**
- Sequence of events performed on every issue  
- Time-of-day and velocity patterns

---

### **3. Modelling Approach**

#### **Text Representation**
Because Jira issues are highly unstructured, use:

- **Transformer-based embeddings** (e.g., BERT, RoBERTa, or Atlassian’s internal embeddings)  
- Fine-tune on Jira domain language (engineering, bug reports, agile terminology)

#### **Model Type**
A **hybrid architecture** works best:

1. **Encoder**:  
   - Transformer to embed issue text  
   - GNN/Graph embeddings for issue linkage  
   - User & project embeddings

2. **Multi-task head**:  
   - One shared trunk  
   - Several task-specific heads for actions:
     - Assign action  
     - Add label  
     - Link issue  
     - Change status  
     - Add component  
   - Allows learning shared structure across actions

3. **Ranking layer**:  
   - Softmax or pairwise ranking (e.g., XGBoost-ranker on top of embeddings)

#### **Cold Start Handling**
- Use project-level priors  
- Use semantic similarity via embeddings  
- Use few-shot learning for new actions

---

### **4. System Architecture**

User Event → Event Collector → Feature Store → Model Service → Recommendation UI

**Flow:**

- **Event Collector** (client & server logs) → store user interactions  
- **Feature Store** (online + offline)  
  - Online features: recent activity, user workload  
  - Offline features: historical issue text embeddings  
- **Model Training Pipeline**
  - Data lake → ETL → Embeddings → Model training → Deployment via CI/CD  
- **Model Serving**
  - Real-time inference API  
  - <100ms latency budget  
  - Model cached in memory or served via vector DB retrieval + ranking  
- **Recommendation UI**
  - Non-intrusive suggestions inside Jira  
  - “Why am I seeing this?” explanation for trust

---

### **5. Evaluation & Monitoring**

#### **Offline Evaluation**
- AUC, Recall@K for recommended actions  
- MAP (Mean Average Precision)  
- Coverage: % of issues where meaningful suggestion exists  
- Cold-start performance on new projects

#### **Online Evaluation**
- **A/B testing**:  
  - CTR on suggestions  
  - Acceptance rate (how often suggestions are used)  
  - Reduction in user time to complete issue grooming  
  - Increase in assignment accuracy

#### **Monitoring in Production**
- Drift detection (embedding drift due to new domain language)  
- Action adoption decay  
- Latency + error rate  
- Model fairness: ensure no user/team is over-suggested

---

### **6. Trade-offs & Pitfalls**

#### **Trade-offs**
- **Accuracy vs. latency**: Large models give better semantic understanding but slower inference  
- **Personalization vs. privacy**: Must anonymize user behaviour and follow Atlassian compliance standards  
- **Explainability vs. complexity**: Transformers need interpretable layers like attention mapping or SHAP

#### **Pitfalls**
- Data leakage from future events  
- Overfitting to specific teams/projects  
- Skew due to “power users” whose action frequency dominates  
- Suggesting biased assignments (e.g., always sending tasks to same high-performer)

---

## **Final Takeaway**
This question tests your ability to think like an **Atlassian product + ML leader**:

- Deep understanding of text-heavy product ecosystems  
- Hybrid modelling techniques  
- Real-time recommender systems  
- Strong emphasis on UX, interpretability, latency, and safety  

A Lead Data Scientist must demonstrate **end-to-end ownership** from data → model → deployment → experiment → scaling.

---
