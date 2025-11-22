# Atlassian Lead Data Scientist – Sample Question 9 & Detailed Answer

## **Question**
Atlassian receives millions of **customer support tickets** across Jira Service Management (JSM).  
They want to build an **Automated Triage & Smart Routing System** that:

- Classifies tickets into the correct support queue  
- Predicts ticket priority/severity  
- Extracts entities (product, feature, module, error code)  
- Summarizes the user’s message for agents  
- Assigns the best agent/team based on expertise & past performance  
- Detects escalations early  
- Handles multilingual requests  

**Design this end-to-end triage, routing, and summarization system for JSM.**  
Explain:

1. Problem framing  
2. Data and features  
3. NLP + ML architecture  
4. Summarization & entity extraction  
5. Real-time routing algorithm  
6. Multilingual handling  
7. Feedback loop & continuous improvement  
8. Evaluation & monitoring  

---

## **Detailed Answer**

---

### **1. Problem Framing**

Each incoming ticket could require:

- **Classification** (product, category, issue type)  
- **Prioritization** (severity)  
- **Routing** (best agent/team)  
- **Summarization** (concise version for agents)  
- **Proactive escalation detection** (predicting SLA breach)

This becomes a **multi-task system**:

- Multi-class classification  
- Multi-label classification  
- Regression (severity scoring)  
- Named entity extraction  
- Sequence summarization  
- Ranking for routing  

---

### **2. Data & Feature Engineering**

#### **A. Ticket Text**
- Subject  
- Description  
- Attachments (logs, screenshots → OCR + text extraction)  
- Inline system messages  

#### **B. Metadata**
- Reporter profile  
- Product type  
- Region/language  
- SLA parameters  
- Past tickets from same customer  

#### **C. Behavioral & Historical Data**
- Agent performance stats (resolution time, quality)  
- Past similar tickets and their resolutions  
- Similarity of error codes or stack traces  

#### **D. Organizational Graph**
- Team → product mapping  
- Agent → expertise graph  
- Past successful routing patterns  
- On-call rotations  

---

### **3. NLP + ML Architecture**

A **two-layer architecture** works best.

---

#### **A. Layer 1: Text Understanding Layer**
Use:
- A multilingual transformer (mBERT, XLM-R, or domain-tuned Llama/BERT)  
- Fine-tuned to:
  - Classify category  
  - Predict severity  
  - Extract entities  
  - Detect escalation risk  
  - Embed ticket for retrieval  

Output:
- Category probabilities  
- Severity score  
- Slot-filled structured fields  
- Ticket embeddings  
- Escalation risk score  

---

#### **B. Layer 2: Routing Layer**
Routing isn’t just classification.  
It must consider:

- Team capacity  
- Agent workload  
- Expertise match  
- Historical resolution success  
- SLA urgency  

A **ranking model** predicts the best team/agent.

Ranking features:
- Similarity of ticket to agent’s solved issues  
- Agent availability  
- Predicted severity × SLA time left  
- Expertise-strength embedding  

Model options:
- XGBoost ranker  
- LightGBM ranker  
- Neural ranking network  

Output:  
- Ranked list of agents/teams  

---

### **4. Summarization & Entity Extraction**

#### **A. Summarization**
Use an LLM with RAG:

Input:
- Raw ticket  
- Attached logs  
- Detected entities  
- Similar past tickets

Output:
- 1–2 sentence summary  
- Optional: steps to reproduce (if detected)

#### **B. Entity Extraction**
Use:
- Transformer-based NER  
- Custom dictionaries for error codes, API names, modules  
- Rules for stack traces

Entities extracted:
- Product (Jira, Confluence, Bitbucket…)  
- Module/component  
- Error code  
- Customer tier  
- Impact (“System down”, “Major slowdown”)  

These entities feed the routing model and severity predictor.

---

### **5. Real-Time Routing Algorithm**

#### **Routing Steps**
1. **Extract text & metadata**  
2. **Infer category & severity**  
3. **Retrieve similar resolved tickets**  
4. **Score agents/teams** using ranking model  
5. **Check availability & capacity constraints**  
6. Output:
   - Best agent/team  
   - Confidence  
   - Explanation:  
     “Assigned to Team-X due to 95% similarity with Ticket-1459 they resolved.”

#### **Latency Target**
- Inference: < 200 ms  
- Retrieval: < 50 ms  
- Total routing decision: < 300 ms  

---

### **6. Multilingual Handling**

Support comes from:

#### **A. Multilingual Transformer**
- mBERT/XLM-R for embeddings & classification  
- Translate-to-English fallback for low-resource languages

#### **B. Domain-Specific Translation**
- Fine-tune a translation model on support ticket corpus  
- Ensure error codes & technical terms don’t get mistranslated

#### **C. Language-Specific Routing**
- Route tickets to language-capable agents when possible

---

### **7. Feedback Loop & Continuous Learning**

#### **A. Explicit Feedback**
- Agents can mark wrong routing  
- Downgrade/upgrade severity  
- Edit extracted entities  
- Rate summarization accuracy

#### **B. Implicit Feedback**
- Resolution time  
- Reassignments (routing failure indicators)  
- SLA breaches  
- Escalations  
- Frequency of manual overrides  

#### **C. Active Learning**
- Prioritize ambiguous tickets for manual review  
- Use human QA to curate difficult cases  
- Periodic retraining every week / sprint  

---

### **8. Evaluation & Monitoring**

#### **Offline Metrics**
- Category classification accuracy  
- Severity prediction MAE  
- Precision@K for routing  
- NER F1 score  
- Summarization ROUGE/BERTScore  
- Escalation model AUC  

#### **Online Metrics**
- First-touch resolution rate  
- Reduction in manual reassignments  
- SLA compliance improvement  
- Agent satisfaction  
- Customer satisfaction (CSAT)  
- Time-to-first-response reduction  

#### **Monitoring**
- Model drift  
- Language drift  
- Hallucination rate in summaries  
- Latency spikes  
- Ticket mis-routing alerts  

---

## **Final Takeaway**
This question tests your ability to architect a **complex, multi-task ML system** that interacts with:

- NLP  
- Retrieval  
- Ranking  
- Summarization  
- Entity extraction  
- Human feedback  
- Real-time operational workflows  

This is the type of high-impact platform intelligence Atlassian expects from a **Lead Data Scientist**.

---
