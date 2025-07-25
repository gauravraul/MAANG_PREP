# Advanced Distillation in GenAI – Questions & Answers

## Q1. What is knowledge distillation and how is it adapted for LLMs?

**A1.**  
Knowledge distillation is a model compression technique where a smaller model (student) learns to mimic a larger model (teacher). In LLMs, it's adapted by:
- Matching teacher’s logits (soft targets)
- Aligning hidden states or attention maps
- Using intermediate supervision (e.g., MiniLM-style)

---

## Q2. What is response-based vs feature-based distillation in LLMs?

**A2.**  
- **Response-based:** The student learns from teacher's output probabilities (soft labels).  
- **Feature-based:** The student mimics teacher’s internal representations like hidden states, attention weights, or even intermediate embeddings.  
Feature-based distillation is more effective for aligning deeper model behavior.

---

## Q3. How is distillation used in Retrieval-Augmented Generation (RAG)?

**A3.**  
In RAG pipelines, distillation can be applied at:
- **Retriever level:** Student retriever mimics cross-encoder or high-accuracy retriever
- **Generator level:** Student generator learns to replicate a stronger teacher's outputs using same retrieved context
This ensures low-latency RAG while preserving answer quality.

---

## Q4. How does the DistilBERT training process differ from BERT’s?

**A4.**  
DistilBERT:
- Trained using triple loss: language modeling loss + distillation loss + cosine embedding loss
- No next-sentence prediction
- 40% fewer parameters, 60% faster inference, 97% of performance
Key point: it's trained from scratch using teacher outputs and intermediate states.

---

## Q5. How can LLMs be distilled without full access to the original training dataset?

**A5.**  
- **Synthetic dataset generation:** Use teacher to generate input-output pairs (self-distillation)
- **Dataset replay or sampling:** Retain small, high-quality sample of original data
- **Knowledge transfer via prompts or reward models:** Guide student learning via prompt injection + RLHF-trained teacher

---

## Q6. What role does temperature play in soft label distillation?

**A6.**  
Temperature (T > 1) smooths the teacher’s output probabilities.  
- Reveals "dark knowledge" in less confident predictions
- Helps student learn class similarities
Formula:  
\[ p_i = \frac{e^{z_i / T}}{\sum_j e^{z_j / T}} \]  
Higher temperature → softer targets → better generalization

---

## Q7. What are some techniques to distill instruction-tuned LLMs like Alpaca or Mistral?

**A7.**  
- **Prompt distillation:** Use few-shot prompts and capture student’s behavior under different instruction styles
- **LoRA + distillation:** Freeze backbone, fine-tune adapters using teacher outputs
- **Multi-turn dialogue distillation:** Include prior context in training (important for agents)

---

## Q8. How do you evaluate the quality of a distilled GenAI model?

**A8.**  
- **Task-specific metrics:** BLEU, ROUGE, EM, F1, accuracy  
- **Distillation loss curves** over epochs  
- **Behavioral alignment:** Match hallucination rate, refusal rate, and tone  
- **Embedding similarity:** Cosine distance of hidden states or sentence embeddings

---

## Q9. What are the trade-offs between training from scratch vs distillation for GenAI?

**A9.**  
| Approach | Pros | Cons |
|----------|------|------|
| From Scratch | Full control, custom architecture | Costly, needs massive data |
| Distillation | Efficient, leverages teacher knowledge | Potential bias propagation, limited flexibility |

---

## Q10. How does TinyStories use distillation effectively for multimodal or small LLMs?

**A10.**  
TinyStories trains tiny LLMs (1M–30M params) using GPT-3.5 as teacher to generate high-quality, diverse, and age-appropriate synthetic data.  
Steps:
1. GPT-3.5 generates prompts + completions
2. Student learns via LM loss on this synthetic dataset
3. Repeating this loop produces robust tiny models for specific domains

---
