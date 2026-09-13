# Note draft — unsupported GPU reaches the queue with no explanation (to Sharmystic, 2026-09-13)

_Posted to Sharmystic by Michael 2026-09-13 ~13:39 EDT._

Hi Sharmystic, a small one from a user's diagnostics bundle today (ngoctuongphan, 1.60.2, engine v0.34.2).

**What happened:** they have a **GTX 1080 Ti** (compute capability 6.1). The engine's torch 2.11.0+cu128 ships kernels for
sm_75 and up only, and it prints that warning at every startup:

```
NVIDIA GeForce GTX 1080 Ti with CUDA capability sm_61 is not compatible with the current PyTorch installation.
The current PyTorch install supports CUDA capabilities sm_75 sm_80 sm_86 sm_90 sm_100 sm_120.
```

Install, engine start and the preset downloads all succeeded. Then every job failed within 0.5-60 s with
`torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device`. That happened in the H3
Image text encoder (comfy_kitchen int8 embedding) and in the H3 GGUF i2v run, so it's every preset, not one.

**What the user saw:** the queue card reads "Generation failed in the engine. Details: [ERROR] [INFO] Prompt executed in
0.56 seconds". It shows the last INFO line instead of the exception, so nothing points at the GPU. They spent a day on
it and asked in the forum.

**Suggestions, your call:**
1. At engine start, read `torch.cuda.get_device_capability()` against `torch.cuda.get_arch_list()` (or catch that
   UserWarning) and show a plain "Your GPU (GTX 1080 Ti) is not supported for local generation; use Cloud" banner,
   and maybe gate local Generate on it.
2. Optionally, for Pascal/Maxwell cards, install the **cu126** torch build instead. PyTorch still publishes
   `torch-2.11.0+cu126` for cp311, and torch's own startup warning on these cards says "Please install PyTorch with a
   following CUDA configurations: 12.6". I haven't tested it on a 10-series card, and it may not be worth it: those cards
   lack fast fp16/bf16 and the int8/fp8 kernels the H3 presets use, so it would mostly help small image models. Plus
   whatever comfy_kitchen / Sage wheels do on cu126. Users are finding Reddit guides telling them to pip-swap torch by
   hand (with a cu121 index that has no wheels for current Python), so either an official path or a clear "not
   supported" message would save them from breaking the engine.
3. When a job fails, prefer the `!!! Exception during processing !!!` line over "Prompt executed in N seconds" for the
   queue card's Details. That would have made this one self-explanatory.
