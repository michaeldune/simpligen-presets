# SimpliGen Community Preset Packs

Custom local preset packs for [SimpliGen](https://www.simpligen.io/), covering image models across SDXL, Pony, Illustrious, SD 1.5, Anima, Krea 2, Flux (1 & 2), Z-Image — plus a Wan 2.2 image-to-video pack.

**16 packs · 57 presets.** Each pack ships as a self-contained zip with a `readme.html` (model download links + destination folders), a one-click `install.cmd` (full pack or single preset, with auto-download of models), the pack JSON, workflows, and preview thumbnails.

> **Distribution:** end users download zips from the shared Google Drive folder (link posted on the SimpliGen Discord — see `DISCORD-ANNOUNCEMENT.md`). This repo is the source of truth the zips are built from.

## Pack catalog

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
| Moody Models | 5 | Z-Image / Flux | NSFW-biased/uncensored |
| Z-Image | 1 | Z-Image | Semi-real/anime |
| Wan 2.2 I2V (GGUF) | 1 | Wan 2.2 14B (video) | Image-to-video, Q4 GGUF, 12 GB-friendly — **not zip-distributable yet** |

## Building the zips

```
python build-zips.py
```

Generates `community-<slug>.zip` per pack into `D:\SimpliGen-Backups\zips\` (readme.html + install.cmd/ps1 + pack JSON + workflows + previews). Video packs are skipped — the generator currently supports image packs only.

The installer prompts for a **Civitai API token** (required by Civitai for downloads) and a **HuggingFace token** where needed, verifies downloads, and reports failures honestly.

## Layout

```
packs/<slug>/
├── <slug>-pack.json     ← pack manifest (relative previews/ paths)
├── workflows/*.json     ← ComfyUI API-format workflows with {{placeholders}}
└── previews/*.jpg       ← 640×640 thumbnails
```

## Authoring

See `CUSTOM-PRESET-AUTHORING-GUIDE.md` — architecture detection, workflow families, the `simpligen_lora_1` LoRA marker, pack schema, thumbnails, installer conventions, and validation.

Key conventions:
- Models install to `%APPDATA%\simpligen\engine\models\<subfolder>\` — checkpoints→`checkpoints\`, UNet/GGUF→`diffusion_models\`, **CLIP/text encoders→`clip\`**, VAE→`vae\`.
- Pack names carry the `Community — ` prefix so they group together in SimpliGen's picker.
- JSON is UTF-8 **without BOM**; installed `previewImage` uses absolute `local-file:///` URIs, source uses relative paths.
