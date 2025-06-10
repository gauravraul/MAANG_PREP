# Advanced Generative AI – 10 Toughest Questions and Answers

## 1. Explain the difference between autoregressive, autoencoding, and diffusion-based generative models.
**Answer:**  
- **Autoregressive models** (e.g., GPT, PixelRNN): Generate data sequentially, one step at a time, modeling p(x) as a product of conditionals.
- **Autoencoding models** (e.g., VAE): Encode input into latent space and decode back, optimizing likelihood with a regularization term.
- **Diffusion models**: Learn to reverse a gradual noise process to generate realistic data (e.g., Denoising Diffusion Probabilistic Models).

---

## 2. How does classifier-free guidance work in diffusion models?
**Answer:**  
Classifier-free guidance combines the outputs of a conditional and an unconditional model during sampling to steer generation toward desired outputs without requiring an external classifier, improving image/text quality and control.

---

## 3. What are the major limitations of current large language models as generative systems?
**Answer:**  
- Lack of grounding in real-time or external knowledge  
- Hallucination (confidently incorrect outputs)  
- Context window limitations  
- Costly inference  
- Inability to reason consistently across multiple steps

---

## 4. Compare the training objectives of GANs, VAEs, and Diffusion models.
**Answer:**  
- **GANs**: Minimax game between generator and discriminator. Non-probabilistic.
- **VAEs**: Maximize ELBO (Evidence Lower Bound) using reconstruction + KL divergence.
- **Diffusion models**: Minimize denoising score matching loss across noise steps; more stable but slower training and inference.

---

## 5. What is mode collapse in GANs and how can it be mitigated?
**Answer:**  
**Mode collapse** occurs when the generator produces limited types of outputs. It can be mitigated by:
- Using techniques like minibatch discrimination, unrolled GANs  
- Wasserstein loss (WGAN)  
- Better architecture/regularization and training tricks

---

## 6. How does retrieval-augmented generation (RAG) enhance generative models?
**Answer:**  
RAG augments a generative model with an external retrieval module (e.g., vector DB), fetching relevant context documents to condition generation. It improves factual accuracy, grounding, and reduces hallucination.

---

## 7. Describe how LoRA (Low-Rank Adaptation) enables efficient fine-tuning of large language models.
**Answer:**  
LoRA freezes base model weights and introduces trainable low-rank matrices in specific layers. It drastically reduces the number of trainable parameters, enabling cost-efficient, modular fine-tuning.

---

## 8. What are attention bottlenecks in transformers, and how do models like FlashAttention or Mamba address them?
**Answer:**  
Full attention is quadratic in sequence length.  
- **FlashAttention**: Computes attention in a memory-efficient tiled fashion using GPU-optimized kernels.  
- **Mamba**: Uses state-space models (SSMs) that scale linearly, offering better efficiency for long-sequence modeling.

---

## 9. Explain the role of temperature and top-k/top-p sampling in generative decoding.
**Answer:**  
- **Temperature** controls randomness in softmax. Lower = more deterministic.  
- **Top-k** limits sampling to top k tokens.  
- **Top-p (nucleus sampling)** selects smallest set of tokens with cumulative probability ≥ p. These techniques balance diversity vs. coherence.

---

## 10. What are some cutting-edge applications of multi-modal generative models (e.g., GPT-4o, Gemini, Claude)?
**Answer:**  
- Text-to-image/video generation (e.g., DALL·E, Sora)  
- Visual question answering  
- Code generation from UI screenshots  
- Audio/video dubbing with emotional matching  
- Assistive agents integrating vision, audio, and language for complex tasks (e.g., robotics, tutoring, diagnostics)
