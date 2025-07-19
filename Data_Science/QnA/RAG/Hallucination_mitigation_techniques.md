# Hallucination Mitigation Techniques – Critical Thinking Q&A

## 1. What are the primary types of hallucinations in LLMs, and how do they differ?

**Answer:**
There are two main types:
- **Intrinsic hallucinations:** The output contradicts the input context (e.g., making up facts).
- **Extrinsic hallucinations:** The output is plausible but not verifiable from any grounded source.
They differ in detectability—extrinsic hallucinations are often harder to catch and require grounding to external data.

---

## 2. How can Retrieval-Augmented Generation (RAG) help reduce hallucination in LLMs?

**Answer:**
RAG reduces hallucination by injecting retrieved, factual documents into the LLM’s context window before generation. This enables the model to reference grounded, up-to-date knowledge rather than relying solely on parametric memory. However, hallucination can still occur if:
- Retrieval is poor (irrelevant documents),
- The model doesn’t attend properly to the retrieved context.

---

## 3. How does Knowledge Graph (KG) integration help in hallucination mitigation?

**Answer:**
KGs offer structured, verified factual data. Integrating KGs allows:
- Entity linking: Ensuring the model grounds its output in real-world nodes/relations.
- Fact-checking: Comparing generated claims to KG assertions.
It requires fine-tuning or prompting the model to prioritize KG-based reasoning.

---

## 4. Explain the role of prompt engineering in minimizing hallucination.

**Answer:**
Prompts guide the LLM’s behavior. To reduce hallucination:
- Use **explicit instructions** like “only answer if certain,” or “cite sources.”
- Apply **chain-of-thought** prompting to promote step-wise reasoning.
- Use **few-shot examples** to demonstrate factual style.
Prompting can reduce hallucination but doesn’t guarantee truthfulness without grounding.

---

## 5. How does fact-checking post-generation help, and what are common methods?

**Answer:**
Post-generation fact-checking acts as a safety net:
- **Automated tools**: e.g., ClaimBuster, FactScore, Scarecrow, G-Eval.
- **Cross-checking**: Using a secondary model or API (like search) to verify claims.
- **Contrastive Decoding**: Compare outputs from multiple LLMs to identify inconsistencies.
This is computationally expensive but critical for high-stakes applications.

---

## 6. What are the trade-offs of using temperature and top-k/top-p sampling to reduce hallucination?

**Answer:**
Lower temperature or top-p values reduce randomness, making outputs more deterministic and conservative—less prone to hallucination. Trade-offs:
- Pros: More factual, controlled outputs.
- Cons: Reduced creativity, repetitive phrasing, and over-reliance on training data patterns.

---

## 7. How does grounding with structured data (e.g., SQL/DBs) reduce hallucination compared to unstructured retrieval?

**Answer:**
Structured data grounding is deterministic and queryable:
- You can directly embed the output of a database (e.g., SELECT queries) into prompts.
- Unlike unstructured RAG, there's no ambiguity or irrelevance in the retrieval process.
However, structured data lacks breadth and expressivity, so it complements but doesn’t replace unstructured sources.

---

## 8. What role does LLM fine-tuning (e.g., with RLHF or RLAIF) play in hallucination mitigation?

**Answer:**
- **RLHF (Reinforcement Learning from Human Feedback):** Encourages factual responses by rewarding grounded answers.
- **RLAIF (AI Feedback):** Scales the process by using AI judges instead of humans.
Challenges:
- Alignment with truth, not just human preferences.
- Quality of feedback signals deeply affects factuality.

---

## 9. Describe the method of "self-consistency" and how it can help detect or reduce hallucinations.

**Answer:**
Self-consistency involves generating multiple outputs for the same prompt and comparing them:
- If outputs are highly variable, hallucination risk is higher.
- Majority voting or filtering for consensus can boost factuality.
It is resource-intensive but improves reliability in multi-step reasoning or high-risk use cases.

---

## 10. How can chain-of-verification frameworks like RAGAS or TruthfulQA be used to evaluate hallucination?

**Answer:**
These frameworks assess:
- **Faithfulness**: Is the response consistent with the retrieved context?
- **Answerability**: Does the evidence justify the answer?
- **Factual correctness**: Compared to known ground truth.
They provide scores and diagnostics that can guide training or system adjustments.

---
