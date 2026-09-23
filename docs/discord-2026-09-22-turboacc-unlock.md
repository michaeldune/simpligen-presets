# Discord update note: MiniMax H3 Turbo Accelerated 1.5.0, unlock slider (HELD, 2026-09-22)

**MiniMax H3 Turbo Accelerated (1.5.0): new "unlock" slider**

The three Turbo Accelerated cards (text, image and reference to video) now have an **unlock** slider, the same idea as SimpliGen's official H3 Unlocked cards. It applies the M3 Unlocked LoRA by The Midnight Lab on top of the turbo recipe.

- It starts at **0**, and at 0 nothing changes: same seed, same video, pixel for pixel.
- Raise it (0.5 is where the official cards sit) and it loosens the model up. Expect it to lean toward more sensual content even with an ordinary prompt.
- It adds no render time. The LoRA is a 164 MB download from Civitai with the pack.

I only added it to Turbo Accelerated: on SolAttn it barely did anything, and on the DaSiWa checkpoints it mostly reshuffled the scene without improving it.
