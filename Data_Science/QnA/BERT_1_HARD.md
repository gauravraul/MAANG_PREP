# Advanced BERT – 10 Toughest Questions and Answers

## 1. What makes BERT bidirectional and how does this benefit language modeling?
**Answer:**  
BERT uses **masked language modeling (MLM)**, where random tokens are masked, and the model predicts them using **context from both left and right**.  
This **bidirectionality** allows deeper understanding of word meaning based on full sentence context — unlike left-to-right models (e.g., GPT).

---

## 2. How does BERT’s training objective differ from GPT’s?
**Answer:**  
- **BERT** uses:
  - **Masked Language Modeling (MLM)**: Predict masked tokens.
  - **Next Sentence Prediction (NSP)**: Predict if sentence B follows A.
- **GPT** uses:
  - **Causal Language Modeling (CLM)**: Predict the next token using left context only.  
BERT learns **contextual embeddings**, GPT learns to **generate**.

---

## 3. Why is the Next Sentence Prediction (NSP) task used in BERT, and what are its limitations?
**Answer:**  
NSP teaches BERT to understand **sentence relationships** (useful in QA, NLI).  
Limitations:
- Artificial (50% positive/negative pairs)
- Doesn't generalize well  
**ALBERT** and **RoBERTa** drop NSP and achieve better performance, questioning its usefulness.

---

## 4. What are the implications of masking tokens during training in BERT but not during inference?
**Answer:**  
- During training, BERT sees **[MASK]** tokens, which don’t appear during inference  
- Creates a **distribution mismatch** between training and downstream use  
This can slightly degrade performance. Some variants (e.g., ELECTRA) solve this by **replacing masked tokens** instead of masking.

---

## 5. How are input embeddings constructed in BERT?
**Answer:**  
Input embedding = sum of:
- **Token embeddings**
- **Segment embeddings** (Sentence A or B)
- **Position embeddings**  
These are fed into every encoder layer to retain token identity, sentence distinction, and order.

---

## 6. Why does BERT not have a decoder, and how does this affect its applications?
**Answer:**  
BERT uses only **Transformer encoders** → suited for **understanding tasks** (classification, QA, embedding).  
Lacks autoregressive capability → not used for **text generation** directly.  
Generative models (e.g., GPT, BART) include decoders or encoder-decoder setups.

---

## 7. How is fine-tuning different from pretraining in BERT?
**Answer:**  
- **Pretraining**: Generic language learning using MLM + NSP on large corpora  
- **Fine-tuning**: Small supervised task-specific training (e.g., sentiment classification) with **minimal changes** to architecture  
Fine-tuning adjusts **all BERT weights**, enabling transfer learning.

---

## 8. What are the challenges of using large BERT models in production?
**Answer:**  
- **High latency** and **memory usage** due to deep layers and attention  
- Limited to short sequences (usually **512 tokens**)  
- Hard to deploy on edge devices  
Solutions:
- **Distillation (DistilBERT)**
- **Quantization**
- **Pruning**
- **Longformer/Reformer** for longer inputs

---

## 9. How does BERT handle polysemy (words with multiple meanings)?
**Answer:**  
Unlike word2vec/GloVe (static embeddings), BERT produces **contextual embeddings**.  
Each token's meaning is **dynamically derived** from surrounding context → same word has different vectors depending on usage.

---

## 10. What are the key differences between BERT and RoBERTa?
**Answer:**  
RoBERTa improves BERT by:
- Removing NSP  
- Training on **larger corpora**  
- Using **dynamic masking** (masks change per epoch)  
- Longer training  
Result: RoBERTa achieves **better downstream performance**, showing BERT was undertrained.
