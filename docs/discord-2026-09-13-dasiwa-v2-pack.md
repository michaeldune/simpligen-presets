# Discord note — MiniMax H3 (DaSiWa Hybrid v2) 1.0.0 — 2026-09-13 (posted, with the 35 s announcement video)

New pack: **MiniMax H3 (DaSiWa Hybrid v2)** — Darksidewalker's Hybrid Turbo v2 (published 09-11). Same idea as the
DaSiWa Hybrid pack (one int8 ConvRot checkpoint for T2V + I2V + R2V, distillation baked in, nothing to install), new
weights: FL2VA with a baked REF2VA delta and a retuned distillation blend.

Why a second DaSiWa pack instead of an update: it is a different look, not a faster one. Bake 2026-09-13 on a 4070 Ti,
same seed/prompts/graphs as the v1 pack:
- 4 steps: softer and darker than v1 (portrait Laplacian 96 vs 160). Not a swap.
- **8 steps (default, ~100 s per 5 s at 480p)**: cleanest skin of every H3 turbo we ship - no oily sheen, no blown key
  light, defined eyes and lips. v1 reads bright, high-contrast, crunchy; keep it for speed, use v2 for faces.
- Identity held on all three reference sets (solo, two-person, person + location).
- The 20-step non-distilled Hybrid v2 gives the same look at 200 s; not shipped.

Needs a Civitai API key (free model, sign-in required). Store sync within 6 h; zip on Releases for pre-1.52.

Side note from T8star-Aix's video on the same two models (0Hd52KfBfcU): don't stack TenStrip's Singularity LoRA on
DaSiWa/10Eros bases, and on these bases the larryvrh EMA turbo LoRA wants 1.0 in the refine pass for action but 0.5 or
lower for dialogue close-ups, or faces go oily. Nothing in our packs does either.
