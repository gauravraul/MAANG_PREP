# Atlassian Lead Data Scientist – Sample Question 10 & Detailed Answer

## **Question**
Atlassian wants to build a **Real-Time Engineering Health Monitoring System** that tracks metrics across Jira, Bitbucket, and CI/CD tools.  
The system should detect early warning signs of:

- Slowing developer velocity  
- Increasing defect rates  
- PR review bottlenecks  
- Build flakiness or test failures  
- Rising cycle time or lead time  
- Poor code quality in critical modules  
- Team burnout or overload  

**Design a robust, production-grade ML + analytics system that predicts engineering health issues *before* they happen, and provides actionable insights to engineering managers.**

Explain:

1. The metrics & signals you’d track  
2. Data pipeline & feature engineering  
3. ML + anomaly detection models  
4. Real-time alerting logic  
5. How insights get presented in Jira  
6. Evaluation, thresholds, and trust  

---

## **Detailed Answer**

---

## **1. Metrics & Signals to Track (Engineering Health KPIs)**

This system must unify signals across:

### **A. Jira Signals**
- Sprint velocity  
- Story completion rate  
- WIP count per developer  
- Cycle time  
- Blocker count  
- Bug reopen rate  
- Issue churn (in/out of sprint)  
- Developer context switching  

### **B. Bitbucket / Code Signals**
- Commit frequency  
- Code churn  
- File hotspot analysis  
- PR review latency  
- PR comment volume  
- Number of reviewers  
- PR rejections or reworks  

### **C. CI/CD Signals**
- Build success rate  
- Build duration  
- Test coverage  
- Flaky test count  
- Deployment failure frequency  

### **D. Team Health Indicators**
- Workload imbalance  
- After-hours work  
- Sudden drop in commits  
- PTO / vacations (if allowed)  

These form the signal foundation.

---

## **2. Data Pipeline & Feature Engineering**

### **A. Data Sources**
- Jira events (webhooks, REST API, activity streams)  
- Bitbucket commits & PR metadata  
- CI/CD logs (Bitbucket Pipelines, Jenkins, GitHub Actions, CircleCI)  
- Test coverage reports  
- Team org graph (owners, component assignments)  

### **B. Feature Engineering**
#### **Time-Series Features**
- Velocity trends (EMA, slope, seasonality)  
- PR throughput  
- Bug counts per week  
- Build duration drift  
- Rolling window metrics (7-day / 14-day / sprint-long windows)

#### **Graph Features**
- Reviewer graph centrality  
- Code ownership relationships  
- Dependency hotspots

#### **Developer Load Features**
- Active tasks per dev  
- PR load per dev  
- Context switching frequency  
- After-hours activity patterns  

#### **Quality Features**
- Defect escape rate  
- Reopen patterns  
- Test coverage change  

Combine them into a unified **Engineering Health Feature Store** updated hourly or daily.

---

## **3. ML + Anomaly Detection Models**

A hybrid system combining prediction + anomaly detection is best.

### **A. Predictive Models**
#### **1. Velocity Drop Prediction**
- Regression or time-series transformer  
- Predict upcoming sprint velocity  
- Compare expected vs actual → risk score  

#### **2. PR Bottleneck Prediction**
- Classification: Will a PR exceed 24/48 hours review time?  
- Features: reviewer graph, code complexity, historical review time  

#### **3. Build Flakiness Prediction**
- Predict probability that next builds will fail  
- Use historical patterns + test signatures  

#### **4. Developer Overload Model**
- Logistic regression or GBM  
- Predict overload & burnout risk  
- Inputs: WIP, PR load, after-hours commits  

---

### **B. Anomaly Detection**
#### **Techniques**
- Isolation Forest  
- Prophet / ARIMA residual analysis  
- Autoencoder for high-dimensional signals  
- Z-score thresholds on rolling metrics  

#### **Examples**
- PR review time spikes → anomaly  
- Build duration suddenly +40% → anomaly  
- Bug reopen rate spike → anomaly  

Anomalies feed into “risk events.”

---

## **4. Real-Time Alerting Logic**

Alerts must be *actionable*, *explainable*, and *non-noisy*.

### **A. Multi-level Alert Strategy**
- **Info**: small drift, FYI  
- **Warning**: consistent negative trend  
- **Critical**: high risk model prediction + anomaly spike  

### **B. Alert Rules**
A critical alert triggers when:
- Model predicts high probability of failure AND  
- Metrics deviate beyond threshold AND  
- Team capacity is low  

Example:

Build Flakiness Risk: 87% Build Failures: +32% last 7 days Tests Added: 0 in last week Recommendation: Investigate test suite X; 6 tests flagged as flaky.

### **C. Alert Delivery**
- Jira dashboard cards  
- Slack/Teams notifications  
- Weekly email digest  
- Sprint planning panel insights  

---

## **5. Insights Presentation Inside Jira**

### **A. Jira Dashboard Widgets**
- “Team Health Score: 74/100”  
- Velocity trend charts  
- PR bottleneck timelines  
- Build stability graph  
- Sprint risk radar  

### **B. Issue/PR/Build Sidebars**
- Highlight hotspots  
- “This PR may take >48 hours to review (76% probability)”  
- “Build likely to fail due to flaky test group XYZ”

### **C. Engineering Manager Insights**
- Automatic sprint summary  
- Predicted blockers  
- Developer load distribution pie chart  
- Bottleneck analysis  

### **D. Release Dashboard**
- Pre-release risk score  
- Quality trending  
- CI stability indicators  

---

## **6. Evaluation, Thresholds & Trust**

### **A. Offline Evaluation**
- Prediction accuracy (AUC, F1, MAE depending on task)  
- Drift detection accuracy  
- False-positive/false-negative rates  

### **B. Online Metrics**
- Reduction in bottlenecks  
- Improved PR turnaround time  
- Better sprint predictability  
- Build stability improvement  
- Higher team satisfaction  

### **C. Avoiding “Alert Fatigue”**
- Adaptive thresholds  
- Rate-limiting alerts  
- Aggregation of repeated warnings  
- Allow users to mute certain categories  

### **D. Explainability**
- SHAP explanations  
- “Why did cycle time increase?” → show drivers  
- Highlight anomalous data points in charts  

### **E. Human-in-the-loop**
- Engineering managers can:  
  - Mark false alerts  
  - Adjust thresholds  
  - Provide feedback  
  - Reclassify events  

This feedback feeds continuous model improvement.

---

## **Final Takeaway**
This question tests your ability to integrate:

- ML + anomaly detection  
- Time-series modelling  
- Dev productivity metrics  
- Architecture across Jira + Bitbucket + CI/CD  
- Real-time UX in Atlassian products  
- Noise handling, trust-building, and interpretability  

This is a core **Lead Data Scientist** problem space at Atlassian—where ML meets engineering productivity intelligence.

---
