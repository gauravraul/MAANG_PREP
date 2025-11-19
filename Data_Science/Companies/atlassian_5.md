# Atlassian Lead Data Scientist – Sample Question 5 & Detailed Answer

## **Question**
Atlassian teams want to enable **AI-driven effort estimation** for Jira issues.  
Given issue text (summary, description), historical sprint velocity, complexity of past issues, and team patterns, the system should predict:

- Story points (1, 2, 3, 5, 8, 13…)  
- Cycle time  
- Probability of spillover  
- Confidence interval for estimation  

**Design an ML system that predicts story points and provides reliable confidence levels.**  
Explain:  
1. Problem framing  
2. Data & features  
3. Modelling architecture  
4. Handling label noise in story points  
5. Prediction calibration  
6. Deployment workflow  
7. How you would evaluate and gain user trust  

---

## **Detailed Answer**

### **1. Problem Framing**
Effort estimation in Jira is extremely noisy because:

- Story points are **team-relative**, not absolute  
- Many issues are misestimated  
- Some teams don't estimate at all  
- Same story point means different effort across projects  

Thus, we need:

- A **team-calibrated prediction model**  
- A **probabilistic prediction** (distribution, not point estimate)  
- Confidence estimation  

Frame the problem as:  
- **Ordinal regression** for story points  
- **Time-to-completion prediction** for cycle time  
- **Binary classification** for spillover risk  
- **Uncertainty modelling** for confidence intervals  

---

### **2. Data & Feature Engineering**

#### **Issue Text Features**
- Summary  
- Description  
- Steps to reproduce  
- Attachments (logs/exceptions)  
- Comments  
- Title embeddings from transformer  
- Description embeddings (long text model)

#### **Team & Project Features**
- Average velocity  
- Median story points for similar issues  
- Team-specific difficulty profile  
- Historical cycle times  
- Common components worked on  
- Sprint load patterns

#### **Issue Metadata**
- Issue type  
- Components, labels  
- Linked issues  
- Number of comments  
- Priorities  
- Time in analysis status  

#### **Graph Features**
- Issue similarity graph  
- Component-level graph  
- Dependency graph (if story depends on others)

---

### **3. Modelling Architecture**

A **multi-task modelling framework** works best:

#### **A. Base Encoder**
- Transformer encoder (e.g., BERT/SBERT/Longformer)  
- Fine-tuned on Jira text to capture engineering-specific language  
- Outputs issue embedding

#### **B. Feature Fusion**
Combine:
- Text embeddings  
- Metadata features  
- Graph embeddings  
- Team-level features  
- Historical velocity indicators

Using:
- Concatenation + MLP  
- Or a tabular-transformer fusion model

#### **C. Multi-task Head**
1. **Ordinal Regression Head** → story points  
2. **Regression/Survival Analysis Head** → cycle time  
3. **Binary Classifier** → spillover probability  
4. **Uncertainty Head** → predictive distribution

This ensures:
- Shared knowledge across tasks  
- Better generalization  

---

### **4. Handling Noisy Story Points**

Story points are not ground truth.  
To reduce noise:

#### **A. Noise-Robust Loss Functions**
- Correntropy loss  
- Focal loss  
- Beta-nll loss for probabilistic regression  
- Label smoothing for ordinal labels

#### **B. Team Normalization**
Convert story points to a **team-specific scale**:
- Use z-score normalization  
- Or map points to a universal latent scale (e.g., complexity score)  
- Then transform back to team scale

#### **C. Confidence Weighting**
- Give higher weight to issues with:
  - Less assignment churn  
  - Known components  
  - Smaller entropy in linking  
- De-emphasize noisy issues in training

---

### **5. Prediction Calibration**

Users need reliable confidence scores. Use:

#### **A. Temperature Scaling**
Fine-tune logits for calibrated probabilities.

#### **B. Quantile Regression**
Predict P10, P50, P90 cycle time.

#### **C. Bayesian Methods**
Use:
- MC Dropout  
- Deep Ensembles  
- Probabilistic layers

Output:
- 70% confidence interval for story points  
- 95% interval for cycle time  

#### **D. Model Interpretability**
Show:
- SHAP feature importance  
- Text highlights  
- Similar past issues with effort  

---

### **6. Deployment Workflow**

#### **Architecture**

Issue Created → Feature Store → Model Service → Suggest Story Points & Cycle Time → UI Cards

#### **Real-Time Prediction**
- On issue creation or during grooming  
- Provide:
  - Predicted story point  
  - Confidence interval  
  - Similar issues and their story points  
  - Probability of spillover

#### **Batch Prediction**
- For backlog grooming  
- Re-predict when sprint starts (due to context change)

#### **Human-in-the-loop**
Allow user to:
- Accept  
- Adjust  
- Ignore  
- Provide feedback ("model underestimates", "overestimates")

This feedback feeds active learning.

---

### **7. Evaluation & User Trust**

#### **Offline Metrics**
- Weighted MAE for story points  
- Spearman correlation (ordinal)  
- MAPE for cycle time  
- AUC + Recall for spillover  
- Calibration metrics (ECE, Brier score)

#### **Online Metrics**
- Acceptance rate of predictions  
- Deviation from actual story point chosen  
- Sprint spillover reduction  
- Faster grooming sessions  
- Developer satisfaction

#### **Trust Factors**
- Provide explanations  
- Show the top similar historical issues  
- Give calibrated confidence intervals  
- Avoid overconfident predictions  
- Provide "why this prediction" card  

---

## **Final Takeaway**
This question tests your expertise in:

- Handling **noisy human-generated labels**  
- Building **probabilistic & calibrated ML systems**  
- Combining textual, tabular, and team-velocity features  
- Creating **trustworthy predictions** for complex workflows  

This is a hallmark challenge at Atlassian and a top-level Lead DS interview question.

---
