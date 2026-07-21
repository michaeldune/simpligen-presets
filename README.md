<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="SimpliGen Community Preset Packs: 57 ready-to-run presets in 16 packs. One zip, one click, models auto-downloaded into SimpliGen.">
</p>

Custom local preset packs for [SimpliGen](https://www.simpligen.io/), covering image models across SDXL, Pony, Illustrious, SD 1.5, Anima, Krea 2, Flux (1 & 2), Z-Image — plus a Wan 2.2 image-to-video pack.

**Getting a pack takes three steps:** download the pack zip from the shared Dropbox folder (link posted on the [SimpliGen Discord](./DISCORD-ANNOUNCEMENT.md)), unzip it, and run `install.cmd`. The installer downloads the models for you, verifies them, and the pack appears in SimpliGen's preset picker under `Community — `.

> This repo is the source of truth the zips are built from. End users never need to clone it.

<p align="center">
  <img src="./assets/readme/section-catalog.svg" width="100%" alt="01 — Pack catalog: 16 packs, 57 presets.">
</p>

| Pack | Presets | Architecture | Notes |
|---|---|---|---|
| SDXL Realism | 4 | SDXL 1.0 | Photoreal, baked VAE, no CLIP skip |
| SDXL Art & Anime | 4 | SDXL 1.0 | Stylized/anime |
| Pony Anime | 4 | Pony (SDXL) | CLIP Skip 2, score tags |
| Pony Realistic | 3 | Pony (SDXL) | Photoreal/semi-real |
| Illustrious Realism | 5 | Illustrious (SDXL) | Photoreal & semi-real |
| Illustrious Anime | 7 | Illustrious (SDXL) | Anime, incl. V-Pred models |
| SD 1.5 Anime | 3 | SD 1.5 | External kl-f8-anime2 VAE, 512-base |
| Reij's Merges | 6 | Illustrious (SDXL) | reijlita merge family |
| Anima Anime | 4 | Anima (Cosmos) | UNet + Qwen encoder + Qwen-Image VAE |
| Anima Realism | 2 | Anima (Cosmos) | Same stack, photoreal |
| Krea 2 | 4 | Krea 2 DiT | Uncensored mixes, 8–10 step distilled |
| Krea Flux | 1 | Flux.1 Krea (GGUF) | CSG Foundation, low-VRAM |
| Flux 2 Klein | 3 | Flux 2 | 9B + 4B, 4-step distilled — **non-commercial license (BFL)** |
| Ideogram 4 | 2 | Ideogram 4 (INT8) | Best-in-class text rendering; UltraReal photo + Graphic/Poster tiers — **requires engine 0.28+** |
| Moody Models | 5 | Z-Image / Flux | NSFW-biased/uncensored |
| Z-Image | 1 | Z-Image | Semi-real/anime |
| Wan 2.2 I2V (GGUF) | 1 | Wan 2.2 14B (video) | Image-to-video, Q4 GGUF, 12 GB-friendly — **not zip-distributable yet** |

Every pack is self-contained: a `readme.html` with model download links and destination folders, a one-click `install.cmd` (full pack or single preset), the pack JSON, ComfyUI workflows, and preview thumbnails.

<p align="center">
  <img src="./assets/readme/section-pipeline.svg" width="100%" alt="02 — From repo to installed preset.">
</p>

<p align="center">
  <img src="./assets/readme/workflow.svg" width="100%" alt="Pipeline: pack sources in packs/ are built by build-zips.py into zips with readme.html and install.cmd, distributed via a Dropbox link posted on Discord, installed by install.cmd which auto-downloads and verifies models, and appear in SimpliGen's picker under the Community prefix.">
</p>

```
python build-zips.py
```

Generates `community-<slug>.zip` per pack into `D:\SimpliGen-Backups\zips\` (readme.html + install.cmd/ps1 + pack JSON + workflows + previews). Video packs are skipped — the generator currently supports image packs only.

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
