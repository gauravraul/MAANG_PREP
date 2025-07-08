# 10 Critical Thinking Questions and Answers on MLOps

---

## 1. How does MLOps differ from traditional DevOps, and why is it necessary?

**Answer:**  
While DevOps focuses on **software deployment and lifecycle**, MLOps manages the **entire ML lifecycle**, which includes:
- Data versioning
- Model training
- Model evaluation
- Continuous monitoring post-deployment

ML systems are **data-dependent**, **non-deterministic**, and require **experimentation tracking** — areas DevOps doesn’t fully address.

---

## 2. Why is reproducibility a major challenge in ML systems, and how does MLOps solve it?

**Answer:**  
ML results depend on:
- Data version
- Model architecture
- Training code and hyperparameters
- Random seeds

MLOps introduces tools like **DVC**, **MLflow**, and **Weights & Biases** to track:
- Datasets
- Model artifacts
- Experiments

This ensures results can be traced, reproduced, and audited.

---

## 3. What are the key components of a production-ready MLOps pipeline?

**Answer:**  
A robust MLOps pipeline includes:
- **Data ingestion and validation**
- **Feature engineering and transformation**
- **Model training and evaluation**
- **Model versioning and registry**
- **CI/CD for model deployment**
- **Monitoring (data drift, performance degradation)**

Tools: Airflow, Kubeflow, MLflow, Tecton, Seldon, etc.

---

## 4. How do you handle data drift and concept drift in production ML systems?

**Answer:**  
**Data drift**: Changes in input data distribution  
**Concept drift**: Change in the underlying relationship between features and labels

MLOps handles this by:
- Logging input distributions over time
- Using statistical tests (e.g., KS test, PSI)
- Setting up **alerts** and **retraining pipelines** triggered by drift detection

---

## 5. Why is monitoring in ML systems more complex than in traditional software?

**Answer:**  
ML system monitoring involves:
- Model accuracy over time
- Input/output data distributions
- Latency, throughput
- Data quality metrics

Unlike software bugs, ML performance **degrades silently** (e.g., due to drift), so MLOps requires **custom dashboards and alerting systems** for predictive performance.

---

## 6. What are the challenges of model deployment in real-time vs. batch settings?

**Answer:**  
**Real-time deployment challenges**:
- Low-latency inference
- Model serving infrastructure (e.g., TensorFlow Serving, TorchServe)
- Online feature stores

**Batch deployment challenges**:
- Scheduling (e.g., daily retraining)
- Synchronizing features with predictions
- Managing massive data loads

MLOps must support both use cases with scalable pipelines.

---

## 7. How do you ensure version control for datasets and models?

**Answer:**  
- Use **DVC** (Data Version Control) or LakeFS for dataset snapshots  
- Register models with **MLflow Model Registry** or **SageMaker Model Registry**
- Store metadata about training runs (e.g., commit ID, hyperparams, data hash)

Versioning allows reproducibility, rollback, and better collaboration.

---

## 8. What role do feature stores play in MLOps, and what problems do they solve?

**Answer:**  
Feature stores manage **feature consistency** between:
- Training and inference
- Batch and real-time processing

They:
- Serve features with low latency
- Track feature lineage
- Promote reuse across teams

Examples: Tecton, Feast, Vertex AI Feature Store

---

## 9. How do you manage experiment tracking and collaboration in large ML teams?

**Answer:**  
Use tools like:
- **MLflow**
- **Weights & Biases**
- **CometML**

These help:
- Track hyperparameters, metrics, and artifacts
- Share experiments and results
- Maintain leaderboards for performance comparison

Proper tagging and metadata ensure clarity and reproducibility.

---

## 10. What are the main ethical and operational risks in MLOps pipelines?

**Answer:**  
Ethical and operational risks include:
- **Bias in models** due to data imbalance
- **Unexplainable decisions**
- **Data privacy breaches**
- **Model abuse or drift post-deployment**

MLOps must enforce:
- Regular bias audits
- Governance for sensitive data
- Human-in-the-loop review
- Clear model explainability layers
