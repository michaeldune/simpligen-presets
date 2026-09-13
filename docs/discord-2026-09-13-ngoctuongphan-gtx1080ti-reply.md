# Reply draft — ngoctuongphan, "Why can't I update to v0.30.1? / can't create a single image or video" (2026-09-13)

_NOT posted: Michael handed the thread to Sharmystic 2026-09-13 13:39 EDT. Kept for reference only._

Thanks for the logs, they show exactly what's wrong, and it isn't your install or your settings.

Your graphics card is a **GTX 1080 Ti**. The SimpliGen engine runs on PyTorch 2.11 (CUDA 12.8), and that build doesn't
support 10-series cards at all. The engine says so every time it starts:

> NVIDIA GeForce GTX 1080 Ti with CUDA capability sm_61 is not compatible with the current PyTorch installation.
> The current PyTorch install supports CUDA capabilities sm_75 sm_80 sm_86 sm_90 sm_100 sm_120.

So the moment any preset puts work on the GPU, it fails with `CUDA error: no kernel image is available for execution on
the device`. That's why every H3 Image, H3 GGUF image-to-video and edit job died within seconds, whatever resolution you
picked. Reinstalling, updating or changing presets won't change it. With the PyTorch build SimpliGen installs, the
minimum is an **RTX 20-series** card (Turing) or newer.

What you can do:
- **Use Cloud generation** in SimpliGen, on the presets that offer it. It runs on SimpliGen's servers, so your card
  doesn't matter.
- **Local generation needs a newer card for now.** You may see ComfyUI guides that say to reinstall PyTorch for
  10-series cards. PyTorch's CUDA 12.6 build does still support them (the cu121 command in those guides doesn't
  exist for newer Python versions). But swapping PyTorch inside SimpliGen's engine isn't supported, the app can put
  its own build back on the next engine update, and some of the engine's speed-up libraries are built for the newer
  version. And even working, MiniMax H3 on a 1080 Ti would be extremely slow: the card has no fast fp16/bf16 and none
  of the int8/fp8 kernels those models rely on. I've asked the SimpliGen dev whether the installer could pick the
  CUDA 12.6 build for older cards; I'll post here if that changes.

Two smaller things in your logs, unrelated to the above:
- One model download failed with "Authentication required for civitai". That file needs your Civitai API key in
  Settings.
- The v0.30.1 "installing PyTorch" hang from yesterday no longer matters: you're on engine v0.34.2 now, and it
  installed fine.
