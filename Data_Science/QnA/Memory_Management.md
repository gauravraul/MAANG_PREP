# Advanced Memory Management in GenAI – Questions & Answers

## Q1. What is activation checkpointing and how does it help reduce memory usage?

**A1.**  
Activation checkpointing saves memory by only storing a subset of intermediate activations during forward pass and recomputing the rest during backward pass. This trades compute for memory and is crucial in training large LLMs. Popular libraries include PyTorch’s `torch.utils.checkpoint` and DeepSpeed’s `activation_checkpointing`.

---

## Q2. How does ZeRO-Offload (DeepSpeed) optimize memory during training?

**A2.**  
ZeRO-Offload partitions optimizer states and gradients across CPU and GPU memory, and selectively offloads them to CPU. This allows model training beyond the GPU memory limit. ZeRO-1/2/3 stages progressively partition optimizer states, gradients, and model weights respectively.

---

## Q3. What are KV cache optimizations in inference and why are they important?

**A3.**  
Key-Value (KV) caching stores attention layer outputs from past tokens, enabling faster autoregressive decoding by avoiding recomputation. Optimizations include:
- **Paginated caches** (e.g., vLLM)
- **FlashAttention 2**: fused attention + optimized memory layout
- **Dynamic memory pinning** for serving multiple concurrent sessions efficiently

---

## Q4. How does tensor parallelism impact memory usage, and how is it managed?

**A4.**  
Tensor parallelism splits tensors across multiple GPUs to reduce per-GPU memory footprint. It increases bandwidth requirements and synchronization overhead. Tools like Megatron-LM and NVIDIA’s FasterTransformer manage memory-efficient layout and communication.

---

## Q5. What is parameter sharding and how is it implemented in HuggingFace Accelerate or DeepSpeed?

**A5.**  
Parameter sharding divides large model weights across devices or nodes.  
- **HuggingFace Accelerate** uses `FullyShardedDataParallel` (FSDP) to shard model states across GPUs.  
- **DeepSpeed ZeRO-3** shards optimizer states, gradients, and model parameters.  
Both avoid full model replication on each device.

---

## Q6. What are memory fragmentation issues in GenAI, and how can they be mitigated?

**A6.**  
Frequent allocation/deallocation of GPU memory (e.g., dynamic batching) causes fragmentation.  
Mitigation:
- Use preallocated memory pools (`torch.cuda.set_per_process_memory_fraction`)
- Static batch sizes
- Custom allocators like NVIDIA’s `CUDA Caching Allocator`

---

## Q7. How does FlashAttention reduce memory consumption during inference?

**A7.**  
FlashAttention rewrites attention to compute directly in GPU SRAM without materializing large attention matrices.  
- **O(n^2) → O(n)** memory  
- Lower peak memory and higher bandwidth usage  
- Critical in inference for long-context LLMs like Claude/GPT-4-128k

---

## Q8. How do quantization and LoRA impact memory usage during training and inference?

**A8.**  
- **Quantization** (INT8/INT4): Reduces model size and memory bandwidth use.  
- **LoRA**: Adds low-rank adapters (~1–5% of total weights), allowing frozen backbone.  
Combined, they enable fine-tuning massive models on consumer GPUs (e.g., 24–48GB).

---

## Q9. How does memory-efficient attention (ME-Attn) differ from standard attention?

**A9.**  
ME-Attn breaks the attention computation into blocks/chunks to reduce memory spikes.  
Variants:
- Chunked attention (Performer)
- Linear attention (Linformer, Longformer)
- FlashAttention-like fused ops  
It allows long-context processing without exploding memory.

---

## Q10. What are some runtime profiling tools used to monitor and manage memory usage in GenAI pipelines?

**A10.**  
- **PyTorch Profiler / `torch.cuda.memory_summary()`**  
- **NVIDIA Nsight Systems / Nsight Compute**  
- **Deepspeed memory profiler**  
- **HuggingFace Accelerate memory tracker**  
- **TensorBoard + memory plugins**

---
