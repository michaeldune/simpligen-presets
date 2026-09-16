:zap: **New pack: MiniMax H3 (TaoMate 3-Step)** (2 cards, T2V + I2V)

Alibaba's TaoLive team released TaoMate-H3 last week: a streaming runtime for H3 that needs 8 Hopper GPUs, plus the LoRA that makes it work in three sampling steps. The runtime is not for us, the LoRA is. This pack puts Kijai's 173 MB ComfyUI conversion of it on the standard FL2VA weights: three steps, no CFG, Euler.

What the bake said (4070 Ti, 5 s at 480p, same seeds and prompts as the Turbo Accelerated pack at its default ten steps):
- **Talking head: 50 s vs 83 s, and sharper.** Line verbatim, mouth closes on the last word.
- **Product turntable: a draw.**
- **Beach run: softer and slower.** The dog smeared and the strides shortened, matching the "slow motion" reports on Reddit.

So it is a dialogue and product card, not an action card; keep the turbo packs for anything that moves fast. No reference-to-video card because the LoRA stops using reference pictures.

Same base weights as the MiniMax H3 pack, so with that installed only the LoRA downloads. Steps slider 3 to 6. Store picks it up on its next sync.

:inbox_tray: Zip: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest
