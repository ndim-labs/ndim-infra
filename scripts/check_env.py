"""Week 0 environment check. Run on every machine (local GPU and Colab) before Phase 1.

    uv run python scripts/check_env.py            # local
    !python scripts/check_env.py                  # Colab

Prints the hardware/software facts everyone should paste into the research log,
and, if WANDB_API_KEY is set, logs a tiny test run to your W&B account.
"""

import os
import platform
import sys
import time

import torch

WANDB_ENTITY = os.environ.get("WANDB_ENTITY")  # None = your personal W&B account
WANDB_PROJECT = os.environ.get("WANDB_PROJECT", "ndim-week0-setup")


def gpu_report():
    if not torch.cuda.is_available():
        print("CUDA: NOT available -- training will run on CPU. Fix this before Phase 1.")
        return {}
    props = torch.cuda.get_device_properties(0)
    vram_gb = props.total_memory / 1024**3
    info = {
        "gpu": props.name,
        "vram_gb": round(vram_gb, 1),
        "compute_capability": f"{props.major}.{props.minor}",
        "bf16": torch.cuda.is_bf16_supported(),
        "cuda_runtime": torch.version.cuda,
    }
    for k, v in info.items():
        print(f"{k:>20}: {v}")
    return info


def matmul_tflops(dtype, n=4096, iters=20):
    a = torch.randn(n, n, device="cuda", dtype=dtype)
    b = torch.randn(n, n, device="cuda", dtype=dtype)
    for _ in range(3):
        a @ b
    torch.cuda.synchronize()
    t0 = time.perf_counter()
    for _ in range(iters):
        a @ b
    torch.cuda.synchronize()
    return 2 * n**3 * iters / (time.perf_counter() - t0) / 1e12


def main():
    print(f"{'python':>20}: {sys.version.split()[0]}")
    print(f"{'platform':>20}: {platform.platform()}")
    print(f"{'torch':>20}: {torch.__version__}")
    info = gpu_report()

    if info:
        dtype = torch.bfloat16 if info["bf16"] else torch.float16
        info["matmul_tflops"] = round(matmul_tflops(dtype), 1)
        print(f"{'matmul_tflops':>20}: {info['matmul_tflops']} ({dtype})")

    if os.environ.get("WANDB_API_KEY"):
        import wandb

        run = wandb.init(entity=WANDB_ENTITY, project=WANDB_PROJECT, job_type="env-check", config=info)
        run.log({"matmul_tflops": info.get("matmul_tflops", 0)})
        run.finish()
        print(f"W&B: logged env-check: {run.url}")
    else:
        print("W&B: WANDB_API_KEY not set -- skipped test run")


if __name__ == "__main__":
    main()
