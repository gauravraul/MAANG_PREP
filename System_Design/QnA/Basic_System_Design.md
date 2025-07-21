# Basic System Design Interview – Questions and Answers

## 1. What is System Design?

**Answer:**  
System Design is the process of defining the architecture, components, modules, interfaces, and data flow of a system to satisfy specific requirements. It helps plan how the system will scale, handle failures, store data, and serve users efficiently.

---

## 2. What are the different types of System Design?

**Answer:**  
1. **High-Level Design (HLD):** Focuses on architecture, components, and their relationships.
2. **Low-Level Design (LLD):** Deals with class diagrams, detailed logic, database schema, etc.

---

## 3. What are some key components in system design?

**Answer:**  
- Load balancers  
- Application servers  
- Databases (SQL/NoSQL)  
- Caches (Redis, Memcached)  
- Message Queues (Kafka, RabbitMQ)  
- CDNs  
- APIs  
- Authentication/Authorization services

---

## 4. What is a Load Balancer and why is it used?

**Answer:**  
A load balancer distributes incoming network traffic across multiple servers to ensure reliability and performance. It prevents any one server from becoming a bottleneck.

---

## 5. What is horizontal vs vertical scaling?

**Answer:**  
- **Vertical scaling:** Add more power (CPU, RAM) to a single server.  
- **Horizontal scaling:** Add more servers to handle load. Horizontal scaling is more robust and fault-tolerant.

---

## 6. What is caching and where can it be used?

**Answer:**  
Caching stores frequently accessed data in a fast storage layer (e.g., in-memory) to improve performance and reduce database load. Common caching points:
- Client-side (browser)
- CDN (edge)
- Server-side (Redis, Memcached)
- Database query result cache

---

## 7. What is CAP Theorem?

**Answer:**  
CAP Theorem states that a distributed system can only guarantee **two out of three**:
- **Consistency** (every read receives the latest write)
- **Availability** (every request receives a response)
- **Partition Tolerance** (system continues working despite network failures)

---

## 8. What is the difference between SQL and NoSQL databases?

**Answer:**
- **SQL** databases (MySQL, PostgreSQL): Structured, relational, ACID-compliant.
- **NoSQL** databases (MongoDB, Cassandra): Flexible schema, distributed, eventually consistent.

Use SQL for structured data and complex queries, NoSQL for scalability and semi-structured data.

---

## 9. How do you handle failures in distributed systems?

**Answer:**
- Replication (data stored in multiple places)
- Health checks and auto-restarts
- Timeouts and retries
- Circuit breakers
- Failover strategies (e.g., switching to backup servers)

---

## 10. How would you design a URL Shortener like bit.ly?

**Answer:**  
Basic approach:
- User inputs a long URL.
- Generate a short, unique key (e.g., using base62 encoding).
- Store mapping in a database: `{ shortKey -> longURL }`
- Redirect user to longURL when shortKey is accessed.
- Add caching for frequently accessed URLs.
- Ensure unique shortKey generation using hashing or counters with collision resolution.

---
