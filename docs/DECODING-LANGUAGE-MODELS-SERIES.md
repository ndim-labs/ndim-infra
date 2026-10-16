# Decoding Language Models — webinar series

**nDimensions.AI** · 24 episodes · every alternate day · started 12 Oct 2026 (dates from Ep 02 onward will be reset once Phase 1 preparation is complete)

Each episode: **Learn** → **Hands-on** → research-log entry. Between episodes: finish the hands-on part.

## Phase 0 · Setup & Orientation

| Ep | Date | Topic | Learn | Hands-on |
|---|---|---|---|---|
| 01 | Mon 12 Oct | **Welcome to Decoding Language Models** | Roadmap, tools tour (Colab, W&B, ndim-infra) | Setup done ✅. Homework: Karpathy [“Let's build GPT”](https://www.youtube.com/watch?v=kCc8FmEb1nY) + [Attention paper](https://arxiv.org/abs/1706.03762) §3 |

## Phase 1 · Foundations

**Repo:** [ndim-labs/p1-gpt-from-scratch](https://github.com/ndim-labs/p1-gpt-from-scratch) · **Status:** 🟡 preparation in progress
Phase 1 goes from *watching* a GPT being built, to *building* our own, to *adapting* a real pretrained model.
Dates for Episodes 02–07 are set once preparation is complete; later phases shift by the same amount.

| Ep | Stage | Format | Topic | Content | Code |
|---|---|---|---|---|---|
| — | **Preparation** | Solo practice | Watch, read, run | Karpathy [“Let's build GPT”](https://www.youtube.com/watch?v=kCc8FmEb1nY) · [Attention paper](https://arxiv.org/abs/1706.03762) §3 · [Colab notebook](https://colab.research.google.com/drive/1JMLa53HDuA-i7ZBmqV7ZnA3c_fvtXnx-?usp=sharing) · [ng-video-lecture](https://github.com/karpathy/ng-video-lecture) · [nanoGPT](https://github.com/karpathy/nanoGPT) README | Karpathy's, Shakespeare |
| 02 | **1.1a** | Webinar, live coding | From data to self-attention | Data → bigram → attention trick → self-attention (paper §3.2) | Our improved notebook |
| 03 | **1.1b** | Webinar, live coding | The full Transformer | Multi-head → Block → full GPT → training (paper §3.1, 3.3, 3.5) | Our improved notebook |
| 04 | **1.2 (part 1)** | Webinar + build | Serious nanoGPT → Shaer-GPT (شاعر) | Our own GPT on classical Arabic poetry; tokenization and the Arabic token tax; nanoGPT as the answer key | Ours, Arabic |
| 05 | **1.2 (part 2)** | Webinar + build | Training like nanoGPT | AdamW, warmup + cosine LR, gradient accumulation, fp16/bf16, checkpoints, W&B | Ours, Arabic |
| 06 | **1.3** | Webinar + build | Full fine-tune vs LoRA vs QLoRA | Qwen 0.5B, the same data three ways: the bridge to Phase 2 ([LoRA](https://arxiv.org/abs/2106.09685), [QLoRA](https://arxiv.org/abs/2305.14314)) | Hugging Face `peft` |
| 07 | **Gate 1** | Review | Phase 1 review | Shaer-GPT demo + fine-tuning comparison table + team presentations | — |

**Preparation is done when** the self-check in the [Phase 1 README](https://github.com/ndim-labs/p1-gpt-from-scratch#self-check-ready-for-11a) is all ticked.

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
