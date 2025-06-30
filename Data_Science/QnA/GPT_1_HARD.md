# Advanced GPT (Generative Pre-trained Transformer) – 10 Toughest Questions and Answers

## 1. What distinguishes GPT from BERT at the architectural and training level?
**Answer:**  
- **GPT**: Uses a **decoder-only transformer** trained with **causal (autoregressive) language modeling**, predicting the next token given left context.  
- **BERT**: Uses an **encoder-only** model trained with **masked language modeling** and **next sentence prediction**, leveraging bidirectional context.  
GPT is generative, BERT is primarily discriminative.

---

## 2. How does causal attention in GPT work, and why is it critical?
**Answer:**  
Causal (masked) attention ensures that each token can only attend to **previous tokens**, preserving autoregressive behavior.  
This:
- Prevents future token leakage during training
- Enables left-to-right generation  
Implemented using a **triangular attention mask**.

---

## 3. Why is GPT considered a zero-shot and few-shot learner?
**Answer:**  
GPT (especially GPT-3/4) is trained on a massive corpus with **no task-specific fine-tuning**.  
It can:
- Generalize to unseen tasks with **only instructions or examples in the prompt**  
- Achieve **zero-shot**, **one-shot**, or **few-shot** learning using in-context examples

---

## 4. What are the key challenges with scaling GPT to billions of parameters?
**Answer:**  
- **Memory and compute costs** grow quadratically with model size and sequence length  
- **Training stability** becomes harder (e.g., gradient explosion, longer convergence)  
- Requires **parallelism strategies**: model parallelism, pipeline parallelism, tensor parallelism  
- **Inference latency** increases → harder real-time deployment

---

## 5. How does GPT handle long-range dependencies in text?
**Answer:**  
- GPT uses **self-attention**, allowing any token to attend to all previous ones  
- Captures long-range context better than RNNs  
- However, standard GPT is limited by **fixed context length** (e.g., 2048 or 4096 tokens)  
Extensions like **GPT-4 Turbo**, **Longformer**, or **Transformer-XL** address this.

---

## 6. What are the risks of GPT-style models in real-world deployment?
**Answer:**  
- **Hallucination**: Generates plausible but incorrect facts  
- **Bias**: Reflects societal and training data biases  
- **Toxicity**: Can produce harmful or offensive text  
- **Security**: Susceptible to prompt injection, adversarial attacks  
Mitigation: alignment, RLHF, filtering, guardrails, and interpretability tools

---

## 7. How does in-context learning differ from traditional fine-tuning?
**Answer:**  
- **Fine-tuning**: Updates model weights using labeled examples  
- **In-context learning**: Keeps weights frozen and leverages **prompt-based examples**  
GPT models use attention over the prompt to mimic learning behavior **without parameter updates**.

---

## 8. How does GPT represent knowledge without an explicit knowledge base?
**Answer:**  
GPT stores **distributed knowledge** in its parameters via:
- Training on massive text corpora (books, code, papers)  
- Statistical co-occurrence and pattern learning  
Unlike knowledge graphs, GPT doesn’t retrieve — it **generates** based on learned associations.

---

## 9. How is temperature and top-k/top-p sampling used during GPT inference?
**Answer:**  
- **Temperature** controls randomness (low → deterministic, high → diverse)  
- **Top-k sampling** selects randomly from the top *k* likely tokens  
- **Top-p (nucleus) sampling** selects from top *p* cumulative probability mass  
These affect creativity, coherence, and diversity of generated outputs.

---

## 10. What architectural modifications improve GPT’s performance at scale?
**Answer:**  
Several innovations improve performance:
- **Rotary positional embeddings (RoPE)** over sinusoidal embeddings  
- **Multi-query attention** (reduces memory)  
- **Parallel transformer blocks** or **Mixture-of-Experts (MoE)** layers  
- **FlashAttention** for speed and memory efficiency  
These enable GPT to scale efficiently to 100B+ parameters.
