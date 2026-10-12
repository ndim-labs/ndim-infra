# Decoding Language Models — webinar series

**nDimensions.AI** · 24 episodes · every alternate day · 12 Oct → 27 Nov 2026

Each episode: **Learn** → **Hands-on** → research-log entry. Between episodes: finish the hands-on part.

## Phase 0 · Setup & Orientation

| Ep | Date | Topic | Learn | Hands-on |
|---|---|---|---|---|
| 01 | Mon 12 Oct | **Welcome to Decoding Language Models** | Roadmap, tools tour (Colab, W&B, ndim-infra) | Setup done ✅. Homework: Karpathy “Let's build GPT” + Attention paper §3 |

## Phase 1 · Foundations

| Ep | Date | Topic | Learn | Hands-on |
|---|---|---|---|---|
| 02 | Wed 14 Oct | **Language models & self-attention** | Next-token prediction, Q/K/V, causal masking | Bigram model → single attention head |
| 03 | Fri 16 Oct | **The Transformer, built** | Multi-head attention, MLP, residuals, LayerNorm | Full mini-GPT on Shakespeare (local GPU, W&B) |
| 04 | Sun 18 Oct | **Tokenization** | BPE (Karpathy tokenizer video) | Minimal BPE, then tiktoken |
| 05 | Tue 20 Oct | **Training dynamics & compute** | AdamW, LR schedule, fp16 on T4, 6·N·D | One-variable experiments in W&B |
| 06 | Thu 22 Oct | **LoRA & QLoRA** | Low-rank adaptation, NF4 quantization | Full FT vs LoRA vs QLoRA on Qwen 0.5B |
| 07 | Sat 24 Oct | **Gate 1** | Phase 1 review | Comparison table + team presentations |

## Phase 2 · Alignment & RL

| Ep | Date | Topic | Learn | Hands-on |
|---|---|---|---|---|
| 08 | Mon 26 Oct | **Base → chat: SFT** | Chat templates, instruction data, Unsloth | SFT a 7–8B model with QLoRA (Colab L4/A100) |
| 09 | Wed 28 Oct | **Evaluating models** | Held-out sets, LLM-as-judge | Evaluate the SFT model |
| 10 | Fri 30 Oct | **DPO** | Preference learning (DPO paper) | DPO on top of SFT; compare |
| 11 | Sun 01 Nov | **RL foundations** | Policy gradients → PPO (Spinning Up) | PPO on CartPole |
| 12 | Tue 03 Nov | **RLHF** | InstructGPT recipe, reward models | Reward model + PPO with TRL |
| 13 | Thu 05 Nov | **Reward hacking** | Goodhart's law in practice | Weak reward → watch it get hacked |
| 14 | Sat 07 Nov | **GRPO** | DeepSeekMath, DeepSeek-R1 | GRPO with a verifiable reward (math/JSON, Unsloth) |
| 15 | Mon 09 Nov | **Gate 2** | Phase 2 review | Team presentations |

## Phase 3 · Breadth (team splits topics, presents back)

| Ep | Date | Topic | Learn | Hands-on |
|---|---|---|---|---|
| 16 | Wed 11 Nov | **Diffusion & vision-language models** | DDPM; how VLMs see | Image LoRA / Qwen2-VL fine-tune (split) |
| 17 | Fri 13 Nov | **Shipping models** | Merge, quantize (GGUF/AWQ), vLLM, TIES/DARE | Serve our model with vLLM |
| 18 | Sun 15 Nov | **Gate 3 · Research kickoff** | Breadth showcase; scope the mini research project | Problem statement + compute plan |

## Phase 4 · Mini research: Identity-Security Reasoner

| Ep | Date | Topic | Learn | Hands-on |
|---|---|---|---|---|
| 19 | Tue 17 Nov | **Data + verifier** | Synthetic data, policy-simulator verifier | Dataset v1 + verifier |
| 20 | Thu 19 Nov | **Benchmark + baselines** | Eval design, frontier prompt baselines | Baseline results table |
| 21 | Sat 21 Nov | **SFT** | QLoRA SFT on reasoning traces | SFT model + eval |
| 22 | Mon 23 Nov | **GRPO** | Verifier as reward | GRPO run + eval vs SFT/baselines |
| 23 | Wed 25 Nov | **Interpretability** | Towards Monosemanticity, probing | Probe/SAE analysis |
| 24 | Fri 27 Nov | **Finale** | Results, write-up, demo | 🎓 Present the reasoner |
