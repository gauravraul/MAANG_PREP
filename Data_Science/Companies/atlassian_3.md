# Atlassian Lead Data Scientist – Sample Question 3 & Detailed Answer

## **Question**
Atlassian wants to build a **“Team Productivity Intelligence Dashboard”** inside Jira.  
This dashboard should automatically identify patterns like:

- Sprint risk  
- Developer overload  
- Bottlenecks in workflows  
- Reopen rates  
- Scope creep  
- Stale issues  
- Team capacity problems  

**Design a system that detects these patterns *proactively* and sends insights/recommendations to engineering managers.**  
Explain your approach across:

1. Data design  
2. Feature engineering  
3. Modelling (predictive + heuristic + anomaly detection)  
4. Insight generation  
5. Deployment in Jira  
6. Evaluation + trust  

---

## **Detailed Answer**

### **1. Data Design**

To detect productivity patterns, you need a *rich, time-series view* of work done by individuals and teams.

#### **Data Sources**
- Jira issue history (status transitions, comments, assignments)
- Sprint boards  
- Workload distribution (issue assignment per user)  
- Developer velocity metrics  
- Historical sprint outcomes  
- Reopen events  
- Deployment logs (if integrated with Bitbucket)  
- Team calendars (optional)

#### **Key Data Tables**
- **Issue Timeline Table**: every transition, timestamp, actor  
- **User Workload Table**: active issues, changes over time  
- **Sprint Performance Table**: velocity, scope changes, spillovers  
- **Team Pattern Table**: historical issue behaviour

This gives the foundation for predictive modelling.

---

### **2. Feature Engineering**

#### **Issue-Level Features**
- Time in each status  
- Comment frequency  
- Issue age  
- Reopen count  
- Assignment churn  
- Linked issue complexity

#### **User-Level Features**
- Workload at every point in time  
- Work in progress (WIP)  
- Burnout risk indicators (overload patterns)  
- Contribution patterns

#### **Sprint Features**
- Planned vs. completed story points  
- Scope added mid-sprint  
- Blocker count  
- Carryover percentage  
- Flow efficiency (active time / total time)

#### **Team Features**
- Historical velocity variance  
- Average cycle time  
- Typical SLA compliance  
- Swarm patterns

---

### **3. Modelling Approach**

A **hybrid system** works best because not every insight needs a predictive model—some are direct heuristics.

#### **A. Predictive Models**
1. **Sprint Failure Prediction**
   - Model: Gradient Boosting or Time-series Transformer  
   - Target: probability of sprint spillover  
   - Features: velocity, early blockers, scope creep in week 1  

2. **Developer Overload Prediction**
   - Model: Logistic regression/GBM  
   - Target: probability user misses deadlines/gets blocked  
   - Features: WIP, context switching frequency, historical patterns  

3. **Issue Delay Prediction**
   - Sequence model using issue transitions  
   - Predict cycle time exceeding SLA

---

#### **B. Heuristic Rules (Operational Intelligence)**
- **High reopen rate** → quality issue  
- **Issue idle > X days** → stale  
- **Assignments changed > 3 times** → unclear requirements  
- **Comment rate spike** → potential escalation  
- **Scope addition > 20% mid sprint** → scope creep

These rules provide deterministic signals where predictions are unnecessary.

---

#### **C. Anomaly Detection**
- Isolation Forest / Prophet / Autoencoder-based anomaly systems for:
  - Sudden drop in team velocity  
  - Unusual assignment patterns  
  - Abnormally long cycle time  
  - Unexpected spikes in workload

This detects unknown unknowns.

---

### **4. Insight Generation Engine**

Each model or rule sends:

- **Insight** (e.g., “Sprint is likely to spillover with 78% confidence”)
- **Cause Analysis** (e.g., “Blockers increased +45% this week”)
- **Recommendation**:
  - Reassign tasks  
  - Reduce scope  
  - Add reviewers  
  - Split the story  
  - Prioritize blockers  

You must ensure insights are:

- Actionable  
- Attributable  
- Non-intrusive  
- Explainable  

---

### **5. Deployment Inside Jira**

#### **Architecture**

Event Stream → Feature Store → Prediction Engine → Insights API → Jira UI Panel

#### **Flow**
- Jira event logs feed a **streaming pipeline**  
- Features for sprint, issue, and user are refreshed regularly  
- Prediction service runs once per hour or in near-real-time  
- Insights shown in dashboards, notifications, or sidebar widgets  
- Provide explanations using SHAP/feature attributions  
- Provide controls: “Snooze insight”, “Ignore this sprint”, “Feedback: Helpful/Not helpful”

#### **Latency**
- Not real-time critical → batch predictions fine  
- Insights updated at most every few minutes or hourly

---

### **6. Evaluation & Trust**

#### **Technical Evaluation**
- Sprint risk model: AUC, Precision@K, Recall@K  
- Issue delay model: MAPE, RMSE  
- Overload prediction: F1, Recall (to avoid missing overloads)

#### **Product Metrics**
- Insight acceptance rate  
- Actions taken due to insights  
- Improvement in sprint predictability  
- Reduction in stale issues  
- Manager satisfaction surveys

#### **User Trust Measures**
- Show transparent explanations  
- Provide confidence intervals  
- Avoid “false alarms” with proper thresholds  
- Allow dismissing or correcting insights (feedback loop)

---

## **Final Takeaway**
A Lead Data Scientist at Atlassian must combine:

- **Predictive modelling**  
- **Heuristics**  
- **Anomaly detection**  
- **Streaming analytics**  
- **Product usability thinking**  
- **Team workflow understanding**

This question tests whether you can design *proactive intelligence* that sits inside complex engineering workflows—exactly what Atlassian expects from its senior technical leaders.

---
