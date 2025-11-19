# Atlassian Lead Data Scientist – Sample Question 6 & Detailed Answer

## **Question**
Atlassian wants to create a **“Release Risk Prediction System”** that warns engineering managers when an upcoming release (Jira fix-version) is at high risk of:

- Missing deadlines  
- Containing too many unresolved bugs  
- Having quality issues  
- Being delayed due to dependency bottlenecks  
- Having insufficient test coverage or unstable builds  

**Design an end-to-end ML-driven system that predicts release risk and provides actionable recommendations.**  
Explain in detail:

1. How to define “release risk”  
2. The data sources required  
3. Feature engineering  
4. Predictive + heuristic components  
5. System architecture  
6. Evaluation & monitoring  
7. How you would ensure interpretability and user trust  

---

## **Detailed Answer**

### **1. Defining “Release Risk”**
Release risk is **multidimensional**, not a single score. It involves:

- **Schedule risk**  
- **Quality risk**  
- **Dependency risk**  
- **Workload risk**  
- **Testing & CI/CD risk**  
- **Bug surge / reopen risk**

Thus, create a **multi-factor risk index**:
- Score 0–100  
- Categorized into low, medium, high  
- Provide a breakdown per dimension

---

### **2. Data Sources**

#### **Jira Data**
- Issues linked to the release  
- Status transitions  
- Cycle time  
- Story points, complexity  
- Reopen rates  
- Blockers & critical bugs  
- Epics & dependencies  
- Churn (moved in/out of release)

#### **Bitbucket / Git Data**
- Commit volume  
- Commit velocity trends  
- Code churn  
- File ownership & hotspots  
- Dependency graphs  

#### **CI/CD Pipeline Data**
- Build pass/fail rates  
- Test coverage  
- Test flakiness  
- Deployment failure frequency

#### **Ops Data (optional)**
- Incident reports  
- On-call event frequency  
- Root cause summaries  

#### **Team Health Data**
- Developer workload  
- Vacation schedule (if available)  
- Context-switching patterns  

---

### **3. Feature Engineering**

#### **A. Issue-level Features**
- SLA compliance per issue  
- Time in progress  
- Bug severity distribution  
- Back-and-forth assignment  
- Comment spikes (proxy for confusion)  
- Similarity to historically risky issues  

#### **B. Release-level Aggregated Features**
- % incomplete stories  
- % critical bugs unresolved  
- Scope creep during the release  
- Story points added/removed  
- Mean cycle time trend  
- Number of blockers  
- Dependency count  
- Lead time trend  
- Change request frequency  

#### **C. Code-related Features**
- High churn files count  
- Ownership fragmentation  
- Recent bug density  
- Number of touching files in PRs  

#### **D. CI/CD Features**
- Build stability trend  
- Mean time to fix failing builds  
- Test coverage deviation  
- Test failure rate over time  

#### **E. Time-series Features**
- Velocity trend per week  
- Burndown discrepancy  
- Exponential moving average of issue completion  

---

### **4. Modelling Approach**

Use a **hybrid ML + heuristics** approach for reliability.

#### **A. Predictive Models**
1. **Binary Classification** → “Will this release miss the deadline?”  
2. **Multi-class Risk Level** → low, medium, high  
3. **Regression** → predict % of scope likely to spillover  
4. **Sequence / Time-series Models**  
   - Transformer-based time-series encoder  
   - Predict trajectory of completion vs. deadline  

#### **B. Additional Heuristics**
Some signals are too important for ML alone:
- >20% scope added within last 2 weeks → high risk  
- >5 critical bugs unresolved → high quality risk  
- Build failure rate > 30% → CI/CD risk  
- Missing tests for critical paths → quality risk  

#### **C. Ensemble Risk Scoring**
Combine:
- ML risk score  
- Heuristic risk score  
- Release manager override  

Final release risk = weighted combination, calibrated for precision.

---

### **5. System Architecture**

Event Streams (Jira, Git, CI/CD)
↓
Feature Store (offline + online)
↓
ML Pipeline (batch + near-real-time)
↓
Risk Scoring Engine
↓
Release Manager Dashboard / Notifications

#### **Batch Mode**
- Recalculate risk once a day/week based on release cadence

#### **Real-time Mode**
- Triggered when:
  - blockers appear  
  - build fails  
  - scope changes  
  - critical bug added  

#### **Deployment Options**
- AWS SageMaker or internal Atlassian ML platform  
- Containerized model server  
- Automated retraining every sprint or month  

---

### **6. Evaluation & Monitoring**

#### **Offline Metrics**
- AUC for risk classification  
- Precision/Recall for high-risk releases  
- Mean Absolute Error for spillover %  
- Confusion matrix for low/medium/high buckets  
- Calibration curves  

#### **Online Metrics**
- How many high-risk releases were actually risky  
- Reduction in last-minute escalations  
- Reduction in release delays  
- Manager feedback score  
- Time-to-detection of risks  

#### **Monitoring**
- Drift detection (team patterns change)  
- CI pipeline changes  
- Sudden spike in false positives  
- Latency & uptime of risk service  

---

### **7. User Trust & Explainability**

#### **A. Provide Component-wise Breakdown**
Example:

Release Risk Score: 78 (High)

Quality Risk: 32

Scope Risk: 20

CI/CD Risk: 15

Dependency Risk: 11


#### **B. Actionable Recommendations**
- “Fix critical bug ABC-123 before continuing development.”  
- “Reduce scope or split large story JIRA-456.”  
- “Improve test coverage in auth module.”  
- “Stabilize CI build – 45% failures in last 7 days.”  

#### **C. Use SHAP or Attention Weights**
- Highlight top drivers of risk  
- Show which historical patterns match this release  

#### **D. Transparent Data Source Indicators**
- “This prediction is based on: 231 issues, 14 builds, 18 commits, 4 critical bugs.”

#### **E. Manager Overrides**
- Users can mark prediction as wrong → feedback for retraining

---

## **Final Takeaway**
This question tests if you can:

- Combine **ML + software engineering context**  
- Build complex **release intelligence systems**  
- Understand **Jira + Bitbucket + CI/CD** ecosystems  
- Produce *actionable*, *interpretable*, and *trustworthy* insights  
- Think in terms of **architecture, UX, and reliability**  

This is a high-level Lead Data Scientist question tailored for Atlassian’s core product challenges.

---
