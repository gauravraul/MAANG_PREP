# Introduction to Data Science - Day 2: Hard Questions and Answers

## 1. How do you design a data collection strategy for a real-world problem?
**Answer:**  
Designing a strategy includes:
- Defining business goals  
- Identifying relevant data sources (internal and external)  
- Choosing collection methods (APIs, sensors, scraping, surveys)  
- Ensuring legal and ethical compliance (e.g., GDPR)  
- Planning data storage and access pipelines

---

## 2. What is data provenance and why is it important?
**Answer:**  
Data provenance refers to the origin and history of data, including how it was collected, processed, and transformed. It’s important for ensuring data quality, reproducibility, and auditability.

---

## 3. How would you handle streaming data differently from batch data?
**Answer:**  
- Use stream processing tools (e.g., Apache Kafka, Apache Spark Streaming)  
- Apply windowing functions  
- Build real-time dashboards  
- Design low-latency, fault-tolerant pipelines  
- Avoid reprocessing full datasets like in batch processing

---

## 4. What are the risks of collecting too much data?
**Answer:**  
- Increased storage and processing costs  
- Data redundancy and noise  
- Privacy concerns and legal risks  
- Analysis paralysis due to overwhelming information  
- Slower performance of models

---

## 5. How does data versioning help in a Data Science workflow?
**Answer:**  
Data versioning helps track changes in datasets, reproduce past experiments, rollback errors, and maintain consistency across team members and environments.

---

## 6. What are some strategies to ensure data quality in large-scale systems?
**Answer:**  
- Automated data validation checks  
- Schema enforcement  
- Monitoring for anomalies  
- Regular audits  
- Data deduplication and cleaning  
- Metadata management

---

## 7. What is concept drift, and how does it affect models?
**Answer:**  
Concept drift occurs when the statistical properties of the target variable change over time. It causes models to become less accurate unless they are retrained regularly.

---

## 8. How do you ensure data privacy and security when working with sensitive data?
**Answer:**  
- Anonymization and encryption  
- Role-based access control  
- Secure storage (e.g., encrypted cloud storage)  
- Compliance with legal frameworks (e.g., HIPAA, GDPR)  
- Using synthetic or federated data where appropriate

---

## 9. How would you architect a system that handles both real-time and batch analytics?
**Answer:**  
Use a **lambda architecture**:
- **Batch Layer:** Stores and processes large volumes periodically (e.g., Hadoop, Spark)  
- **Speed Layer:** Handles real-time data streams (e.g., Kafka, Flink)  
- **Serving Layer:** Merges results for end-user queries (e.g., databases, dashboards)

---

## 10. What are trade-offs between collecting data locally on devices vs. in the cloud?
**Answer:**  
- **Local:** Low latency, privacy-friendly, limited storage and processing power  
- **Cloud:** Scalable, centralized access, requires internet, higher data transfer costs, privacy and compliance risks if not handled properly
