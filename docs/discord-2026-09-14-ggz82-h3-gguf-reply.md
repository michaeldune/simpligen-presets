# Reply to ggz82 - H3 GGUF quants for 8-12 GB (HELD for Michael's approval)

Posted: NOT YET.

Context: ggz82 (5:41 PM, 2026-09-14) found Abiray's 10Eros Max GGUFs and a heavily
quantized Qwen VL GGUF, asks if they can be added for the 8-12 GB range, and is
unsure about the mmproj file. Has an RTX 3060 (12 GB) that passed the app's check.

What I verified (2026-09-14):
- Abiray repos: `10Eros-Max-GGUF` (Q3_K_M 8.9 GB to Q8_0 21.6 GB, VRAM chart
  10-12 GB for Q3_K_M), `10Eros-Max-Hybrid-Beta5-GGUF` (same ladder, explicitly
  non-turbo full-step), `10Eros-Max-ref2va-Beta2-GGUF`. There is NO Turbo GGUF
  from Abiray; the header is spoofed as "wan" so City96's loader accepts it.
- Encoder GGUFs: `nif0/Qwen3-VL-32B-Instruct-MiniMax-H3-GGUF` (2-bit 6.9 GB to
  Q4_K_M 14.9 GB, needs nif0's fork of ComfyUI-GGUF, "model only for T2V, model +
  mmproj for I2V"), `Raretutor/Qwen3-VL-32B-MiniMax-H3-GGUF` (Q2, mmproj NOT
  included, llama-cpp oriented). Stock ComfyUI-GGUF never merges an mmproj for
  the qwen3vl arch, so a hand-placed sidecar does nothing.
- SimpliGen already ships an official "MiniMax H3 (Low VRAM)" pack
  (minimax-h3-gguf-pack 1.2.11) with t2v/i2v/r2v on City96's loader.
- Our 2026-09-01 bake on a 12 GB 4070 Ti: both Q3_K_M GGUF presets took 605 s and
  707 s for the same clip the int8 presets did in 90-200 s, with the worst image
  of the eleven. GGUF is a fit-it-at-all route, not a speed route, on 12 GB.

---

Nice find. Short version: on a 12 GB card the GGUFs are the slow road, not the
fast one. When we baked eleven H3 variants on a 12 GB 4070 Ti, the Q3_K_M GGUF
presets took 10-12 minutes for the clip the int8 packs finished in 1.5-3 minutes,
and the picture was the worst of the lot. The int8 packs in the catalog (Turbo
Accelerated, DaSiWa, 10Eros Max Turbo) all run on 12 GB already, so on your
3060 I would start with those. The thing that actually decides whether H3 runs
is system RAM, not VRAM: it wants roughly 32 GB. How much does your PC have?

On the specific files:

- Abiray publishes 10Eros Max, Hybrid Beta5 and ref2va Beta2 as GGUF, but none
  of them are Turbo. The Beta5 one is explicitly the full-step build, so it is
  20 steps on a 3-bit model, which is where that 10-12 minute number comes from.
- The mmproj is the vision half of the Qwen3-VL text encoder. Text-to-video only
  needs the encoder file; image and reference-to-video need the mmproj as well,
  and the stock GGUF loader does not merge it for Qwen3-VL at all. It needs a
  forked loader (nif0's) to work, which is why dropping the file in the models
  folder does nothing. Not something you did wrong.
- SimpliGen already has an official "MiniMax H3 (Low VRAM)" pack that wires the
  GGUF loader and encoder correctly, so if you want the GGUF route, install that
  instead of hand-placing files.

If you have 32 GB of RAM, try the 10Eros Max Turbo pack first and tell me the
time per clip. If you are on 16 GB, say so and I will look at what a real
8 GB-class pack would need, because that is a different problem than quantizing.
