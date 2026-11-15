# Decoding Language Models — webinar series

**nDimensions.AI** · 24 episodes · weekly on **Fridays** (Ep 03 on Tue 17 Nov) · 12 Oct 2026 → Fri 09 Apr 2027

Each episode: **Learn** → **Hands-on** → research-log entry. Between episodes: finish the hands-on part.

## Phase 0 · Setup & Orientation

| Ep | Date | Topic | Learn | Hands-on |
|---|---|---|---|---|
| 01 | Mon 12 Oct | **Welcome to Decoding Language Models** | Roadmap, tools tour (Colab, W&B, ndim-infra) | Setup done ✅. Homework: Karpathy [“Let's build GPT”](https://www.youtube.com/watch?v=kCc8FmEb1nY) + [Attention paper](https://arxiv.org/html/1706.03762v7) §3 |

## Phase 1 · Foundations

**Repo:** [ndim-labs/p1-gpt-from-scratch](https://github.com/ndim-labs/p1-gpt-from-scratch) · **Status:** ✅ organizer preparation done · ✅ 1.0 session done · 🟡 next: **1.1a, Tue 17 Nov**
Phase 1 goes from *watching* a GPT being built, to *building* our own, to *adapting* a real pretrained model.
Schedule reset on 15 Nov 2026: 1.1a on Tuesday 17 Nov, then one webinar every Friday.

| Ep | Date | Stage | Format | Topic | Content | Code |
|---|---|---|---|---|---|---|
| 02 | ✅ Done | **1.0 · Preparation** | Live group session | Basics + the Attention paper | Language-model basics and a guided walk through [Attention Is All You Need](https://arxiv.org/html/1706.03762v7) §3, while everyone runs Karpathy's [`gpt_dev.ipynb`](https://github.com/ndim-labs/p1-gpt-from-scratch/tree/main/1.0-preparation) | Karpathy's, Shakespeare |
| 03 | Tue 17 Nov | **1.1a** | Webinar, live coding | From data to self-attention | Data → bigram → attention trick → self-attention (paper §3.2) | Our improved notebook |
| 04 | Fri 20 Nov | **1.1b** | Webinar, live coding | The full Transformer | Multi-head → Block → full GPT → training (paper §3.1, 3.3, 3.5) | Our improved notebook |
| 05 | Fri 27 Nov | **1.2** | Webinar + build | Serious nanoGPT → Shaer-GPT (شاعر) | Our own GPT on classical Arabic poetry with nanoGPT-quality training; the Arabic token tax; nanoGPT as the answer key | Ours, Arabic |
| 06 | Fri 04 Dec | **1.3** | Webinar + build | Full fine-tune vs LoRA vs QLoRA | Qwen 0.5B, the same data three ways: the bridge to Phase 2 ([LoRA](https://arxiv.org/abs/2106.09685), [QLoRA](https://arxiv.org/abs/2305.14314)) | Hugging Face `peft` |
| 07 | Fri 11 Dec | **Gate 1** | Review | Phase 1 review | Shaer-GPT demo + fine-tuning comparison table + team presentations | — |

**Self-paced extras** (optional, alongside 1.0): Karpathy's [“Let's build GPT”](https://www.youtube.com/watch?v=kCc8FmEb1nY) · [ng-video-lecture](https://github.com/karpathy/ng-video-lecture) · [nanoGPT](https://github.com/karpathy/nanoGPT) README

**Ready for 1.1a when** the notebook runs and the 1.0 homework questions are answered ([1.0 README](https://github.com/ndim-labs/p1-gpt-from-scratch/tree/main/1.0-preparation#homework-after-the-session)).

## Phase 2 · Alignment & RL

| Ep | Date | Topic | Learn | Hands-on |
|---|---|---|---|---|
| 08 | Fri 18 Dec | **Base → chat: SFT** | Chat templates, instruction data, Unsloth | SFT a 7–8B model with QLoRA (Colab L4/A100) |
| 09 | Fri 25 Dec | **Evaluating models** | Held-out sets, LLM-as-judge | Evaluate the SFT model |
| 10 | Fri 01 Jan 2027 | **DPO** | Preference learning (DPO paper) | DPO on top of SFT; compare |
| 11 | Fri 08 Jan 2027 | **RL foundations** | Policy gradients → PPO (Spinning Up) | PPO on CartPole |
| 12 | Fri 15 Jan 2027 | **RLHF** | InstructGPT recipe, reward models | Reward model + PPO with TRL |
| 13 | Fri 22 Jan 2027 | **Reward hacking** | Goodhart's law in practice | Weak reward → watch it get hacked |
| 14 | Fri 29 Jan 2027 | **GRPO** | DeepSeekMath, DeepSeek-R1 | GRPO with a verifiable reward (math/JSON, Unsloth) |
| 15 | Fri 05 Feb 2027 | **Gate 2** | Phase 2 review | Team presentations |

## Phase 3 · Breadth (team splits topics, presents back)

| Ep | Date | Topic | Learn | Hands-on |
|---|---|---|---|---|
| 16 | Fri 12 Feb 2027 | **Diffusion & vision-language models** | DDPM; how VLMs see | Image LoRA / Qwen2-VL fine-tune (split) |
| 17 | Fri 19 Feb 2027 | **Shipping models** | Merge, quantize (GGUF/AWQ), vLLM, TIES/DARE | Serve our model with vLLM |
| 18 | Fri 26 Feb 2027 | **Gate 3 · Research kickoff** | Breadth showcase; scope the mini research project | Problem statement + compute plan |

## Phase 4 · Mini research: Identity-Security Reasoner

| Ep | Date | Topic | Learn | Hands-on |
|---|---|---|---|---|
| 19 | Fri 05 Mar 2027 | **Data + verifier** | Synthetic data, policy-simulator verifier | Dataset v1 + verifier |
| 20 | Fri 12 Mar 2027 | **Benchmark + baselines** | Eval design, frontier prompt baselines | Baseline results table |
| 21 | Fri 19 Mar 2027 | **SFT** | QLoRA SFT on reasoning traces | SFT model + eval |
| 22 | Fri 26 Mar 2027 | **GRPO** | Verifier as reward | GRPO run + eval vs SFT/baselines |
| 23 | Fri 02 Apr 2027 | **Interpretability** | Towards Monosemanticity, probing | Probe/SAE analysis |
| 24 | Fri 09 Apr 2027 | **Finale** | Results, write-up, demo | 🎓 Present the reasoner |
