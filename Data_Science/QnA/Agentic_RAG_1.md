# 10 Critical Thinking Questions and Answers on Agentic RAG

---

## 1. How does Agentic RAG differ from traditional RAG in architecture and capability?

**Answer:**  
Traditional RAG retrieves documents once and uses them in a single generation step.  
Agentic RAG introduces:
- **Multi-step retrieval loops**: The agent can iteratively reformulate queries.
- **Reasoning between steps**: Enables planning what to retrieve next.
- **Tool usage**: Agents use APIs, databases, or structured data in addition to vector stores.

Agentic RAG is **goal-driven**, whereas classic RAG is **query-driven**.

---

## 2. What are the benefits of adding an agent loop to the RAG paradigm?

**Answer:**  
- **Adaptive querying**: Agents can refine queries based on intermediate results.
- **Dynamic memory**: Store and retrieve intermediate thoughts and documents.
- **Decomposition**: Agents can split the main goal into subqueries and merge retrieved knowledge.

This leads to **higher factual accuracy**, **contextual relevance**, and **less hallucination** in complex tasks.

---

## 3. What role does planning play in Agentic RAG, and how can it fail?

**Answer:**  
Planning determines:
- The order of retrieval
- The relevance of sources
- The transformation of intermediate knowledge

Failures occur when:
- Goals are poorly specified
- Agents overfit to irrelevant intermediate context
- There's no grounding or stopping criterion

Solution: Add **tree-of-thought planning** or **planner-evaluator modules**.

---

## 4. Why is grounding especially challenging in Agentic RAG?

**Answer:**  
Agents may:
- Retrieve **too many** or **irrelevant** documents
- Fail to **explicitly cite** sources
- Mix memory, search, and generation without tracking provenance

Grounding improves when:
- Each retrieved chunk is **tagged and cited**
- There’s a **retrieval-to-claim mapping**
- Evaluators score **source coverage**

---

## 5. How can retrieval quality influence the reasoning chain in Agentic RAG?

**Answer:**  
Low-quality retrieval leads to:
- Flawed reasoning
- Irrelevant planning
- Hallucinated conclusions

High-quality retrieval enables:
- Precise follow-up queries
- Justifiable reasoning
- Faithful summarization

Thus, **retrieval becomes a first-class citizen**, not a pre-step.

---

## 6. In what scenarios does Agentic RAG significantly outperform traditional RAG?

**Answer:**  
- **Multi-hop question answering**
- **Enterprise search over multiple tools**
- **Scientific or legal document synthesis**
- **Personalized assistants with persistent memory**

Anywhere **adaptive retrieval + strategic reasoning** is needed over static QA tasks.

---

## 7. How do memory and episodic storage enhance Agentic RAG systems?

**Answer:**  
- **Memory** stores previous queries, thoughts, and relevant docs.
- Agents can avoid re-querying or contradicting earlier content.
- **Long-term memory** enables better performance over sessions and topics.

This leads to **coherent multi-turn interactions** and continuity in thought.

---

## 8. What evaluation metrics are unique or critical to Agentic RAG?

**Answer:**  
Beyond standard metrics like BLEU or ROUGE:
- **Faithfulness**: Is the final answer traceable to retrieved facts?
- **Recall@k**: Were the correct documents retrieved?
- **Retrieval efficiency**: How many iterations were needed?
- **Grounding density**: Percent of claims linked to evidence.

Human + LLM evaluation loops are often needed.

---

## 9. What are the most common failure modes of Agentic RAG pipelines?

**Answer:**  
- **Over-retrieval**: Too many docs, causing distraction.
- **Query drift**: Agents forget the original goal.
- **Memory bloat**: Retrieval from irrelevant past context.
- **Hallucinated synthesis**: Agent invents rather than cites.

Solutions include:
- Query summarization checkpoints
- Chunk deduplication
- Retrieval scoring + reranking

---

## 10. How can you improve an Agentic RAG system's ability to handle ambiguous or vague questions?

**Answer:**  
- Use **clarifying agents** to ask follow-up questions.
- Maintain a **task planner** that can disambiguate based on retrieved context.
- Employ **uncertainty scoring** to trigger fallback actions or human-in-the-loop review.

This enables safe handling of **underspecified** tasks in critical domains (e.g., medicine, law).
