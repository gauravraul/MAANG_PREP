# Advanced Quantization in Deep Learning and LLMs – Questions & Answers

## Q1. What is the difference between post-training quantization and quantization-aware training (QAT)?

**A1.**  
- **Post-training quantization (PTQ)**: Applied after training, it converts weights/activations to lower precision (e.g., FP32 → INT8). It is fast but may degrade accuracy in sensitive models.  
- **Quantization-aware training (QAT)**: Simulates quantization effects during training to improve model robustness post-quantization. QAT generally results in better accuracy compared to PTQ.

---

## Q2. How does GPTQ work, and why is it preferred for LLM quantization?

**A2.**  
**GPTQ (Gradient Post-Training Quantization)** performs layer-wise quantization using second-order approximation (Hessian info) without retraining. It minimizes quantization error via greedy optimization and error compensation, making it efficient for large models like LLaMA and GPT.

---

## Q3. What are the trade-offs between INT8, INT4, and FP16 quantization for LLMs?

**A3.**  
| Precision | Speed | Memory | Accuracy | Hardware Support |
|----------|-------|--------|----------|------------------|
| FP16     | Medium| Medium | High     | Excellent (TPUs, GPUs) |
| INT8     | Fast  | Low    | Good     | Widely Supported |
| INT4     | Fastest| Lowest| Lower    | Limited (requires custom kernels) |

INT4 can result in higher perplexity degradation but offers massive compression.

---

## Q4. What is AWQ and how is it different from GPTQ?

**A4.**  
**AWQ (Activation-aware Weight Quantization)** uses activation-aware calibration to scale and quantize weights, targeting key activations per channel. Unlike GPTQ, it does not require Hessian approximation but focuses on minimizing the quantization error of high-activation channels.

---

## Q5. How does SmoothQuant improve quantization of LLMs?

**A5.**  
**SmoothQuant** balances activation and weight ranges by moving quantization sensitivity from activations to weights using a smoothing parameter (α). This reduces activation outliers and improves post-training INT8 quantization without the need for QAT.

---

## Q6. What are group-wise quantization and per-channel quantization? Which is better for LLMs?

**A6.**  
- **Per-channel**: Applies separate scale/zero-point per weight channel. More accurate but higher memory usage.  
- **Group-wise**: Shares quantization parameters across groups of channels. A compromise between performance and accuracy.  
For LLMs, **group-wise INT4** (used in GPTQ/AWQ) provides a good balance.

---

## Q7. How can LoRA be combined with quantized models?

**A7.**  
**LoRA (Low-Rank Adaptation)** can fine-tune quantized models by injecting learnable adapters into specific layers (e.g., attention). This enables efficient task-specific tuning while keeping the backbone quantized, reducing both memory and compute.

---

## Q8. What challenges arise during quantization of attention mechanisms?

**A8.**  
- Softmax and layer norm are sensitive to quantization error.  
- Attention scores (dot products) can overflow with lower precision.  
- Solutions: keep sensitive ops in higher precision (e.g., FP16 for softmax), use quantization-friendly kernels, or hybrid quantization.

---

## Q9. How do you evaluate the effectiveness of a quantized model?

**A9.**  
Metrics:  
- **Perplexity** (for LLMs)  
- **BLEU, ROUGE** (for NLP tasks)  
- **Latency** and **throughput** benchmarks  
- **Memory footprint**  
- **Accuracy drop** (<1–2% is acceptable)  
Tools: Intel Neural Compressor, NVIDIA TensorRT, PyTorch Quantization Toolkit, Optimum (HuggingFace).

---

## Q10. What are the latest tools for LLM quantization?

**A10.**  
- **AutoGPTQ** – Fastest GPTQ variant with easy integration.  
- **BitsAndBytes** – 8-bit and 4-bit LLMs with HuggingFace support.  
- **AWQ (by MIT)** – Open-sourced INT4 quantization with faster inference.  
- **Optimum Intel** – End-to-end LLM optimization (INT8/PTQ).  
- **TinyChat** – Mobile-optimized 4-bit transformers.

---
