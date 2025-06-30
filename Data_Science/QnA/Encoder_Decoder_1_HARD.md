# Advanced Encoder-Decoder Architecture – 10 Toughest Questions and Answers

## 1. What is the core idea behind the encoder-decoder architecture?
**Answer:**  
The encoder-decoder framework maps **variable-length input sequences** to **variable-length outputs**.  
- **Encoder** processes the input and compresses it into a **context vector**
- **Decoder** uses the context vector to generate the output sequence  
This is the foundation of **seq2seq learning**, used in machine translation, summarization, and dialogue systems.

---

## 2. Why does the basic encoder-decoder model struggle with long input sequences?
**Answer:**  
It compresses all input information into a **single fixed-length vector**, regardless of sequence length.  
For long sequences, this creates a **bottleneck**, leading to:
- Information loss  
- Poor performance on long dependencies  
**Attention mechanisms** address this by giving the decoder access to **all encoder states**.

---

## 3. How does attention improve the encoder-decoder model?
**Answer:**  
Instead of relying only on the final encoder state, **attention** computes a **weighted sum of all encoder states**.  
Benefits:
- Better handling of long inputs  
- Allows decoder to **focus on relevant parts** of the input at each step  
- Improves accuracy, especially in translation and summarization tasks

---

## 4. What is the difference between soft and hard attention?
**Answer:**  
- **Soft attention**: Computes continuous weights (probabilities) over input tokens — **fully differentiable** and trainable with backpropagation  
- **Hard attention**: Picks discrete input positions — **non-differentiable**, usually trained with reinforcement learning  
Soft attention is more common due to ease of training.

---

## 5. What is the role of teacher forcing in encoder-decoder models?
**Answer:**  
During training, the decoder is fed the **ground-truth token** at the previous time step rather than its own prediction.  
Pros:
- Faster convergence  
- More stable training  
Cons:
- Causes **exposure bias**: At inference time, the model may struggle since it has to use its own outputs as input.

---

## 6. How does a Transformer differ from a traditional RNN-based encoder-decoder?
**Answer:**  
Transformers:
- Use **self-attention** to model dependencies  
- Enable **parallel processing** (vs sequential RNNs)  
- Have **no recurrence** — faster and more scalable  
Outperform RNNs in tasks like translation and summarization, especially with long sequences.

---

## 7. What is the significance of the context vector in encoder-decoder models?
**Answer:**  
The **context vector** summarizes the input sequence and initializes the decoder.  
In traditional seq2seq:
- It's the final hidden state of the encoder  
With attention:
- It's a **dynamic vector** computed at every decoder step  
Critical for capturing sequence meaning and alignment.

---

## 8. How do you handle variable-length outputs in encoder-decoder models?
**Answer:**  
- Use **special tokens** like `<eos>` to mark the end of a sequence  
- Train the model to **generate until `<eos>`**  
- Apply **beam search** or **greedy decoding** to control output length during inference

---

## 9. What are the limitations of encoder-decoder models in real-world tasks?
**Answer:**  
- Struggle with **very long sequences** without attention  
- Can be **data-hungry**  
- Inference is **slow** for autoregressive decoders  
- **Exposure bias** and **coverage problems** may lead to repetitions or omissions  
Modern solutions include **Transformers**, **non-autoregressive decoders**, and **coverage mechanisms**.

---

## 10. How do you evaluate encoder-decoder models effectively?
**Answer:**  
Evaluation depends on task:
- **Translation/Summarization**: BLEU, ROUGE, METEOR scores  
- **Dialogue**: Human eval + BLEU + diversity metrics  
- **Classification**: Accuracy, F1, etc.  
Also track:
- **Loss convergence**
- **Inference speed**
- **Memory usage**
