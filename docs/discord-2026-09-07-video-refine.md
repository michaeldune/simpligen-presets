:sparkles: **New today: three Video Refine packs — upscale a clip you already rendered**

Until now every Community pack made a new video. These three take a **finished clip** (drop it in Reference Video 1) and hand it back bigger and sharper, with the original soundtrack muxed back untouched. Same clip, three different engines, so you can pick by shot:

:film_frames: **MiniMax H3 (Video Refine)** — stays inside H3. Paste the brief that made the clip; it re-renders at 672p or 768p using Alibaba's official PDD 8-step distill at a quarter denoise, in overlapping 73-frame windows so up to 15 s runs in one go. Steadiest motion of the three because it's the same model that made the footage. Can't fix a face the source already lost. ~160 s for 5 s on a 12 GB 4070 Ti.

:frame_photo: **LTX 2.5 (Video Refine, MSR)** — hands the clip to LTX 2.5. Doubles it with the latent upsampler to 720p or 1080p and re-renders the detail, with one to four face pictures (plus an optional background plate) held by Licon's Multi-Subject-Reference LoRA so nobody drifts. Prompt is LTX style — one plain paragraph, not the H3 brief. Crisper, more LTX-looking, works on clips from any source. ~155 s for 5 s at 1080p. Needs the gated LTX 2.5 weights (free HF token + licence click), same files the other LTX packs use.

:microscope: **VOSR 2.0 (Video Refine)** — no video model at all. VOSR 2.0 is a one-step image super-resolution model; every frame is restored on its own, exactly 2x, no prompt, no references. Sharpest of the three by a wide margin on a same-clip bake-off, face held, but the slowest (~2 s per 480p frame) and per-frame, so it can shimmer on fast motion. Best for static or slow shots. :warning: **First render downloads 7 GB** into the engine with no progress bar — it looks stuck for a few minutes, let it finish.

**Which one?**
• Real motion, want it to look like H3 made it → H3 Video Refine
• Want 1080p, or a face needs a reference to hold, or the clip isn't from H3 → LTX 2.5 Video Refine
• Static talking head, maximum sharpness, can wait → VOSR 2.0 Video Refine

All three were verified inside SimpliGen on a 12 GB card; measured numbers and the bake-off results are in each pack's notes.

:shopping_cart: Store: `Community — ` prefix, syncs within a few hours.
:inbox_tray: Zips: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest
:books: Catalogue: <https://github.com/michaeldune/simpligen-presets#readme>

:wrench: Each of the three needs one custom node cloned into `custom_nodes` (the pack's `readme.html` names it). Big thanks to @Sharmystic — the model-folder autoscan in the last update is what let the PDD-based packs ship at all. :raised_hands:

(Also today: the **MiniMax H3 PDD Acc 8-Step** pack is now fully verified in-app and bumped to 1.0.1 — Alibaba's official 8-step distill for T2V/I2V/R2V, ~110 s for 5 s at 480p.)
