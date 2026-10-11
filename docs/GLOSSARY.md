# Glossary

Each term: abbreviation, definition, formula and an example. Examples use our own Week 0 numbers wherever possible.

---

## GPU — Graphics Processing Unit

**Definition:** a processor with thousands of small cores that run the same math on many numbers at once. Neural-network training is mostly that kind of math, so GPUs train models 10–100× faster than CPUs.

**Formula:**
`peak speed ≈ cores × clock speed × operations per core per clock`

**Example:** the Tesla T4 has 2,560 CUDA cores plus 320 Tensor Cores (special units for matrix math). Its advertised peak is 65 TFLOPS in fp16; we measured **24.9**. Real code usually reaches 30–50% of peak.

---

## VRAM — Video Random Access Memory

**Definition:** the GPU's own memory. Everything the GPU works on (model weights, gradients, optimizer state, the data batch, intermediate activations) must fit here, or you get a `CUDA out of memory` error.

**Formula:**
- Just running a model: `memory ≈ parameters × bytes per parameter`
- Full training with the Adam optimizer in mixed precision: `memory ≈ parameters × 16 bytes` **+ activations**
  (2 B weights + 2 B gradients + 4 B fp32 master copy + 8 B Adam state)

**Example:** Qwen 0.5B (0.5 billion parameters):
- running it in fp16: 0.5B × 2 B = **1 GB** → fits anywhere
- full fine-tune: 0.5B × 16 B = **8 GB** + activations → does **not** fit the laptop (6 GB), fits the T4 (14.6 GB)
- That's why LoRA/QLoRA exist (Phase 1, week 3): they train only a small part of the model.

---

## FLOP / FLOPS / TFLOPS — Floating-Point Operation(s) per Second

**Definition:** a FLOP is one math operation (add or multiply) on decimal numbers. FLOPS is how many the hardware does per second. TFLOPS = **tera**-FLOPS = trillions (10¹²) per second.

**Formula:**
`TFLOPS = total FLOPs ÷ seconds ÷ 10¹²`

**Training-time estimate** (the most useful formula in this glossary):
`training FLOPs ≈ 6 × N × D` (N = parameters, D = training tokens)
`time ≈ training FLOPs ÷ (TFLOPS × 10¹² × utilization)`, where utilization is typically 0.3–0.5

**Example:** our Week 1 nanoGPT (N ≈ 10.7M parameters) trained on D ≈ 82M tokens:
6 × 10.7×10⁶ × 82×10⁶ ≈ 5.3×10¹⁵ FLOPs.
On the T4: 5.3×10¹⁵ ÷ (24.9×10¹² × 0.4) ≈ **530 s ≈ 9 minutes**.

---

## Matmul — Matrix Multiplication

**Definition:** multiplying two grids of numbers. Every layer of a neural network, including attention, is mostly matmuls, so matmul speed ≈ training speed.

**Formula:**
`C = A × B`, where `C[i][j] = Σₖ A[i][k] × B[k][j]`
FLOPs for (m×k) × (k×n): `2 × m × k × n` (one multiply + one add per term)

**Example:** our speed test multiplies two 4096×4096 matrices, 20 times:
2 × 4096³ × 20 ≈ 2.75×10¹² FLOPs. At 24.9 TFLOPS that takes **0.11 s**.
In attention (Week 1), `scores = Q × Kᵀ` is a matmul.

---

## fp32 / fp16 / bf16 — Floating-Point formats (32-bit, 16-bit, Brain Float 16)

**Definition:** ways of storing decimal numbers in bits. Fewer bits use half the memory and run faster on Tensor Cores, but lose precision or range.

**Formula:** `value = (−1)^sign × 2^(exponent − bias) × 1.mantissa`

| Format | Bits (sign / exponent / mantissa) | Bytes | Largest value | Notes |
|---|---|---|---|---|
| fp32 | 1 / 8 / 23 | 4 | ~3.4×10³⁸ | Default; precise but slow and big |
| fp16 | 1 / 5 / 10 | 2 | 65,504 | Fast; small range → needs *loss scaling* to avoid overflow |
| bf16 | 1 / 8 / 7 | 2 | ~3.4×10³⁸ | Same range as fp32, less precise; stable, but needs compute capability ≥ 8.0 |

**Example:**
- 1B-parameter model weights: fp32 = 4 GB, fp16/bf16 = 2 GB.
- In fp16, 70,000 overflows to `inf`, so training breaks without loss scaling. In bf16 it's fine.
- Week 0: bf16 on the T4 (no bf16 hardware) → **2.5 TFLOPS**; fp16 → **24.9 TFLOPS**.
- **Mixed precision** = do the math in fp16/bf16, keep a master copy of the weights in fp32. That's what we'll use (`torch.autocast`).

---

## Compute capability (CC)

**Definition:** NVIDIA's version number for a GPU's architecture. It decides which features (bf16, FlashAttention, fp8) the GPU supports.

**Formula:** `CC = major.minor`. Rules of thumb: bf16 and FlashAttention-2 need **CC ≥ 8.0**; fp8 needs **CC ≥ 8.9**.

**Example:**

| GPU | Architecture | CC | bf16? |
|---|---|---|---|
| Tesla T4 (Colab) | Turing | 7.5 | No → use fp16 |
| RTX 3050 Laptop (ours) | Ampere | 8.6 | Yes |
| L4 (Colab) | Ada Lovelace | 8.9 | Yes (+ fp8) |
| A100 (Colab) | Ampere | 8.0 | Yes |

In code: `torch.cuda.get_device_capability()` → `(7, 5)` on the T4.

---

## CUDA — Compute Unified Device Architecture

**Definition:** NVIDIA's software platform that lets programs (like PyTorch) run code on the GPU. You need a matching NVIDIA driver plus a PyTorch build compiled for a CUDA version.

**Formula:** compatibility rule: `driver's CUDA version ≥ PyTorch's CUDA version`

**Example:** your laptop's driver supports CUDA 13.3, and we installed `torch 2.14.1+cu130` (CUDA 13.0), so 13.3 ≥ 13.0 ✅.
Check in code: `torch.cuda.is_available()` → `True`; `torch.version.cuda` → `'13.0'`.

---

## W&B — Weights & Biases

**Definition:** a website plus Python library that records every training run (settings, metrics, charts, system stats) so the team can compare runs later. It now runs on CoreWeave's site (Forge).

**Formula (the code pattern):**
```python
import wandb
run = wandb.init(entity="ndim-labs", project="p1-nanogpt", config={"lr": 3e-4})
for step in range(steps):
    wandb.log({"loss": loss})
run.finish()
```

**Example:** Week 0's three runs (`charmed-pond-1`, `earthy-valley-2`, `resilient-tree-3`) are in `ndim-labs / ndim-week0-setup`. The bar chart showed the bf16 bug at a glance.

**Related terms:** *entity* = team or user (`ndim-labs`); *project* = one experiment group; *run* = one execution of a script.

---

## Colab Pro & CU — Compute Units

**Definition:** Google Colab is a hosted Jupyter notebook with free or paid cloud GPUs. Colab Pro is the paid tier, billed in **compute units (CU)** that each GPU type burns at a different hourly rate.

**Formula:** `GPU hours available = compute units ÷ CU per hour`

**Example** (approximate rates; check your Colab usage page):

| GPU | ≈ CU/hour | Hours from 100 CU |
|---|---|---|
| T4 | 2 | ~50 |
| L4 | 5 | ~20 |
| A100 | 12 | ~8 |

Rule: debug on the laptop or a T4, and spend A100 hours only on real runs. Disconnect the runtime when you're done, because idle sessions still burn CUs.

---

## Quick reference

| Abbreviation | Stands for |
|---|---|
| GPU | Graphics Processing Unit |
| CPU | Central Processing Unit |
| VRAM | Video Random Access Memory |
| FLOP(S) | Floating-Point Operation(s) (per Second) |
| TFLOPS | Tera (10¹²) FLOPS |
| fp32 / fp16 | 32-bit / 16-bit floating point |
| bf16 | Brain Floating Point 16 (designed by Google Brain) |
| CC | Compute Capability |
| CUDA | Compute Unified Device Architecture |
| W&B | Weights & Biases |
| CU | Compute Unit (Colab billing) |
| OOM | Out Of Memory |
