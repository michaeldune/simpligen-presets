<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="SimpliGen Community Preset Packs: 109 ready-to-run presets in 31 packs. One zip, one click, models auto-downloaded into SimpliGen.">
</p>

Custom local preset packs for [SimpliGen](https://www.simpligen.io/), covering image models across SDXL, Pony, Illustrious, SD 1.5, Anima, Krea 2, Flux (1 & 2), Z-Image and SeFi — plus video: MiniMax H3 packs (text/image/reference-to-video with synchronized audio), LTX 2.5 image-to-video and lip-sync packs, and a Wan 2.2 image-to-video pack.

**Getting a pack takes three steps:** download the pack zip from the [Releases page](https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest), unzip it, and run `install.cmd`. The installer downloads the models for you, verifies them, and the pack appears in SimpliGen's preset picker under `Community — `.

> This repo is the source of truth the zips are built from — and now the distribution point too. The `packs-latest` release is rolling: its assets get replaced each time `build-zips.py` runs, so the same link always has the current set. End users never need to clone it.

<p align="center">
  <img src="./assets/readme/section-catalog.svg" width="100%" alt="01 — Pack catalog: 31 packs, 109 presets.">
</p>

**Image packs**

| Pack | Presets | Architecture | Notes |
|---|---|---|---|
| SDXL Realism | 5 | SDXL 1.0 | Photoreal, baked VAE, no CLIP skip |
| SDXL Art & Anime | 5 | SDXL 1.0 | Stylized/anime |
| Pony Anime | 4 | Pony (SDXL) | CLIP Skip 2, score tags |
| Pony Realistic | 3 | Pony (SDXL) | Photoreal/semi-real |
| Illustrious Realism | 6 | Illustrious (SDXL) | Photoreal & semi-real |
| Illustrious Anime | 8 | Illustrious (SDXL) | Anime, incl. V-Pred models |
| SD 1.5 Anime | 3 | SD 1.5 | External kl-f8-anime2 VAE, 512-base |
| Reij's Merges | 6 | Illustrious (SDXL) | reijlita merge family |
| Anima Anime | 5 | Anima (Cosmos) | UNet + Qwen encoder + Qwen-Image VAE |
| Anima Realism | 3 | Anima (Cosmos) | Same stack, photoreal |
| Krea 2 Identity Edit | 2 | Krea 2 Turbo + Identity Edit LoRA v1.2 | **Image editing.** Hand it a photo and an instruction in plain English. Identity Edit changes one thing and leaves the rest alone; Identity Lock holds a face while you re-stage a character sheet into a new scene, transfer a face between two images, or do virtual try-on. Takes one or two reference images — image 1 is the scene, image 2 is the subject. Shares the Krea 2 checkpoint, encoder and VAE with the Krea 2 pack, so the only new download is a 1.83 GB LoRA. No masked inpainting: SimpliGen presets cannot pass a mask |
| Krea 2 | 9 | Krea 2 DiT | Six uncensored mixes at 8–10 steps, plus three trained finetunes: Muse v3.5 Extended (clean SFW editorial, real steps/CFG range, ships 12 steps / CFG 1.5), FinalCut v2 (matte skin instead of Krea gloss, native up to 2432×1920, NSFW-capable) and Binyuan Portrait v3.2 (East Asian portrait realism). Renders at native ~2 MP (1408×1408 and equivalents) plus an Upscale slider with a 4-step refine pass, matching the official Krea 2 Turbo preset; 2 MP costs ~5 s more than 1 MP on a 4070 Ti |
| Krea Flux | 1 | Flux.1 Krea (GGUF) | CSG Foundation, low-VRAM |
| Flux 2 Klein | 2 | Flux 2 | 9B + 4B, 4-step distilled — **non-commercial license (BFL)**. A third preset, MiracleIn NSFW, was retired 2026-08-30 when Civitai's author put paid access on every version of that checkpoint; it is kept in `packs/flux2-klein/retired/` for manual install |
| Ideogram 4 | 2 | Ideogram 4 (INT8) | Best-in-class text rendering; UltraReal photo + Graphic/Poster tiers — **requires engine 0.28+** |
| SeFi-Image | 2 | SeFi 5B (Q8) | Turbo, 4- and 8-step tiers |
| Moody Models | 5 | Z-Image / Flux | NSFW-biased/uncensored |
| Z-Image | 1 | Z-Image | Semi-real/anime |
| Hentai Mixes | 8 | SD 1.5 ×6, SDXL ×2 | Civitai anime/hentai checkpoints. SD 1.5 tier runs 512–768 with CLIP Skip 2; the SDXL pair run native 1024, one of them Pony-based (wants `score_9, score_8_up, score_7_up`) |

**Video packs**

All the MiniMax H3 packs generate video *with synchronized stereo audio*. The first four ship text-to-video, image-to-video, and reference-to-video presets off the same base weights — so adding one costs only its LoRA, not another 40 GB. **10Eros Max is the exception**: it is a different base checkpoint (a separate 20.94 GiB download), and it ships as two packs - plain and Turbo - each with text-, image- and reference-to-video.

| Pack | Presets | Architecture | Notes |
|---|---|---|---|
| MiniMax H3 (Turbo LoRA, larryvrh) | 3 | MiniMax H3 (pruned INT8) | The default: 6–8 steps, best for static/small motion. Named for the LoRA author to stay clear of SimpliGen's own official H3 Turbo pack |
| MiniMax H3 (Turbo, Fast Motion) | 3 | MiniMax H3 (pruned INT8) | 4-step tier tuned for heavy/fast motion |
| MiniMax H3 (Sol-Attn + EasyCache) | 3 | MiniMax H3 (pruned INT8) | Sparse attention + step caching at the full 20 steps. **Not a speed pick** since 1.50.0 — pick it for the no-LoRA path, and for the R2V preset, which is the crash-free route for reference *video*. Needs Faster Attention ON |
| MiniMax H3 (Turbo, Fully Accelerated) | 3 | MiniMax H3 (pruned INT8) | Every technique stacked — Turbo + SageAttention + Sigma Shift + Spectrum + Sol-Attn. 10 steps for roughly what 6 used to cost |
| MiniMax H3 (10Eros Max) | 3 | MiniMax H3 (**non-pruned** INT8) | Different base — a separate 20.94 GiB download. Plain 20-step, T2V + I2V + R2V |
| MiniMax H3 (10Eros Max + Turbo) | 3 | MiniMax H3 (**non-pruned** INT8) | The same base at 6 steps — the fastest preset here. Shares the 20.94 GiB download with the pack above |
| Wan 2.2 I2V (GGUF) | 1 | Wan 2.2 14B | Image-to-video, Q4 GGUF, 12 GB-friendly |
| LTX 2.5 Lip-Sync (A2V) | 1 | LTX 2.5 distilled 22B | Drive a shot with your own audio. Two-pass to 1080p; 165 s for 5 s at 1920x1088. Reuses the official LTX 2.5 weights |
| LTX 2.5 REDgraft Fast 2K (T2V + I2V) | 2 | LTX 2.5 REDgraft (INT8) | Text-to-video with generated audio or image-to-video from a source image. Separate NSFW finetune; reuses the official LTX 2.5 companion stack |
| MiniMax H3 (DaSiWa Hybrid) | 3 | MiniMax H3 (int8 + ConvRot) | **The fast one.** Darksidewalker's finetune with the distillation baked in: 4 steps, no Turbo LoRA, nothing extra to install. ONE checkpoint covers T2V + I2V + R2V where every other H3 pack needs two, so it is ~19.5 GB lighter. Roughly 70-140 s per 5 s shot against ~180. Reads brighter and wider than stock — pick another H3 pack for the darker look. Needs a Civitai API key (free model, sign-in required) |
| MiniMax H3 Lip-Sync | 1 | MiniMax H3 (pruned INT8) | Audio-driven lip sync with up to 9 reference images, so a whole band stays recognisable in a wide. Trims your track to the shot automatically; 10 s default. Reuses the H3 Turbo weights |

Measured on a 12 GB RTX 4070 Ti — T2V, 5 s at 480p (864×480), one prompt and one seed across all seven, each preset at its own default step count. **SimpliGen 1.50.0, engine v0.33.1**, ~19 GB system RAM free at the start of each run:

| Preset | Steps | Time | Per step | vs. official |
|---|---|---|---|---|
| **10Eros Max + Turbo** | **6** | **67.9 s** | 5.16 s | **1.82×** |
| Turbo, Fast Motion | 4 | 80.9 s | 11.14 s | 1.53× |
| Fully Accelerated | 10 | 87.4 s | 4.86 s | 1.41× |
| Turbo | 6 | 102.7 s | 10.71 s | 1.20× |
| 10Eros Max | 20 | 119.1 s | 3.60 s | 1.04× |
| Official MiniMax H3 | 20 | 123.5 s | 3.01 s | — |
| Sol-Attn + EasyCache | 20 | 127.7 s | 4.18 s | 0.97× |

**SimpliGen 1.50.0 changed the baseline, not these packs.** 1.50.0 frees VRAM before decoding and unloads the text encoder before sampling. That took the *official* preset from 170.7 s to 123.5 s — a 28% gain — while every community pack here landed within a few percent of its pre-1.50.0 time. Nothing regressed; the thing they are measured against simply got much faster, so every ratio in this table is smaller than the one it replaces.

Two consequences worth stating rather than burying. **Sol-Attn + EasyCache is no longer a speed win** — at 0.97× it is marginally slower than the official preset, where it used to be 1.32× faster; its case now rests on output at the full 20 steps, not throughput. And the **Turbo-family gains are roughly half what they were**: Fast Motion was 2.15×, it is now 1.53×. Still a real saving, just an honest one.

Earlier figures for reference, measured on engine v0.31.0 / SimpliGen 1.46.0: official 170.7 s, Sol-Attn 129.5 s, Turbo 103.8 s, Fully Accelerated 84.1 s, Fast Motion 79.5 s.

Engine v0.31.0 took 8–18% off every one of these versus v0.30.1, and not evenly: the two 20-step presets gained most and the low-step Turbo presets least, which is what you would expect if the work landed in per-step execution rather than fixed overhead. Treat these as one run each — a repeat of the Sol-Attn row landed within 2%, but reference-to-video conditioning has shown far wider spread, so the I2V and R2V figures quoted in individual packs are less firm than these.

**A note on 10Eros and quantisation, because the earlier version of this README got it wrong.** On pre-1.50.0 builds 10Eros beat the pruned base by 22%, and that was attributed to it skipping per-step dequantisation on the 30 layers the pruned weights store as int8. The 1.50.0 numbers show that explanation was backwards: 10Eros is *slower* per step (3.60 s vs 3.01 s), and its advantage is lower fixed overhead, not cheaper compute. The old 22% was a VRAM-pressure artifact — while the run was memory-bound, streaming behaviour dominated and masked the per-step cost. Free the memory and the pruned base's smaller footprint wins on compute, leaving 10Eros ahead by only ~4%.

Two caveats worth stating plainly. These are single runs. And **free system RAM moves these numbers more than any preset choice does** — the same preset and seed measured 47.7 s with ~20 GB free and 78.6 s with ~2.8 GB free, a 65% swing. Quote your own free RAM alongside any timing, or the comparison means very little.

Every pack is self-contained: a `readme.html` with model download links and destination folders, a one-click `install.cmd` (full pack or single preset), the pack JSON, ComfyUI workflows, and preview thumbnails.

<p align="center">
  <img src="./assets/readme/section-pipeline.svg" width="100%" alt="02 — From repo to installed preset.">
</p>

<p align="center">
  <img src="./assets/readme/workflow.svg" width="100%" alt="Pipeline: pack sources in packs/ are built by build-zips.py into zips with readme.html and install.cmd, distributed via a rolling GitHub Release, installed by install.cmd which auto-downloads and verifies models, and appear in SimpliGen's picker under the Community prefix.">
</p>

```
python build-zips.py
```

Generates `community-<slug>.zip` per pack into `D:\SimpliGen-Backups\zips\` (readme.html + install.cmd/ps1 + pack JSON + workflows + previews). Both image and video packs are built. Any preset relying on a custom ComfyUI node gets that node's repo and install caveat written into its `readme.html` automatically, from the `CUSTOM_NODES` registry at the top of the script — add an entry there when you introduce a new one.

The installer prompts for a **Civitai API token** (required by Civitai for downloads) and a **HuggingFace token** where needed, verifies downloads, and reports failures honestly.

<p align="center">
  <img src="./assets/readme/section-authoring.svg" width="100%" alt="03 — Authoring your own pack.">
</p>

Each pack lives under `packs/<slug>/`:

```
packs/<slug>/
├── <slug>-pack.json     ← pack manifest (relative previews/ paths)
├── workflows/*.json     ← ComfyUI API-format workflows with {{placeholders}}
└── previews/*.jpg       ← 640×640 thumbnails
```

See [`CUSTOM-PRESET-AUTHORING-GUIDE.md`](./CUSTOM-PRESET-AUTHORING-GUIDE.md) — architecture detection, workflow families, the `simpligen_lora_1` LoRA marker, pack schema, thumbnails, installer conventions, and validation.

Key conventions:
- Models install to `%APPDATA%\simpligen\engine\models\<subfolder>\` — checkpoints→`checkpoints\`, UNet/GGUF→`diffusion_models\`, **CLIP/text encoders→`clip\`**, VAE→`vae\`.
- Pack names carry the `Community — ` prefix so they group together in SimpliGen's picker.
- JSON is UTF-8 **without BOM**; installed `previewImage` uses absolute `local-file:///` URIs, source uses relative paths.

<p align="center">
  <a href="https://github.com/oil-oil/beautify-github-readme"><img src="./assets/readme/made-with-beautify.svg" width="300" alt="README made with beautify-github-readme"></a>
</p>
