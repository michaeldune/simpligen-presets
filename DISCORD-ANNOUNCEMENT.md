:art: Community Preset Packs — Free Downloads

I've put together (with a great deal of assistance from Claude Code and Codex) a collection of 20 preset packs (73 presets) for SimpliGen covering a wide range of models and styles — images, video, and now sound-synced video too. Each pack includes a one-click installer and a readme with model download links.

:new: **New — MiniMax H3 Turbo & Sol-Attn now cover T2V/I2V/R2V:** Turbo (larryvrh's LoRA + dual-schedule sampler) cuts sampling to ~6 steps; Sol-Attn (sparse attention, experimental) keeps full 20-step quality but runs faster per step. Both now support Character Dialogue, matching the official preset. Each needs one extra manual step — see below.

:arrows_counterclockwise: **Updated — downloads moved off Dropbox:** everything now lives on GitHub, source and distribution in one place. Same one-click zips, new link below. Video packs (Wan 2.2, MiniMax H3) and the custom-node pack (SeFi-Image) are also now proper one-click installs, not manual setups.

:package: What's included: (as of this moment)

Anima Anime & Realism
SDXL Realism & Art/Anime
Pony Anime & Realistic
Illustrious Realism & Anime
SD 1.5 Anime
Krea 2 (Moody Mix, RedCraft, Realia, Fascium)
Krea Flux (CSG Foundation — GGUF Flux.1 Krea)
Flux 2 Klein (9B, MiracleIn NSFW, 4B Maxx — sub-second 4-step generation)
Ideogram 4 (UltraReal photo + Graphic/Poster — needs engine 0.28+)
Z-Image
Reij's Merges
Moody Models
SeFi-Image (Semantic-First Diffusion — rendered text/posters/stylized art; needs a custom node)

**Video:**
Wan 2.2 Image-to-Video (GGUF, 12 GB-friendly)
MiniMax H3 Turbo — T2V/I2V/R2V, synced audio, ~6 steps (needs a custom node)
MiniMax H3 Sol-Attn — T2V/I2V/R2V, synced audio, sparse attention, full quality (needs a custom node, experimental)

:inbox_tray: Download: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest

:octopus: Source on GitHub: <https://github.com/michaeldune/simpligen-presets> — all pack definitions, workflows, and the zip build script. Browse the presets, report issues, or build the zips yourself.

How to install:

Download a pack's .zip and unzip it
Open readme.html to see which models you need and grab any you're missing
Run install.cmd — it will download models automatically and let you install the full pack or a single preset
Restart SimpliGen

**:clipboard: Before you install — please read:**
:warning: **Disk space:** these are full local models, some 5–13 GB per model (video packs more). If you're tight on space, install one preset at a time and check sizes in `readme.html` first.

:key: **Civitai token:** some models need a free API token — create one at <https://civitai.com/user/account> (API Keys). The installer prompts for it; no token = those models are skipped (manual links in `readme.html`).

:hugging: **HuggingFace token:** a few models need a free HF token / license acceptance. The installer prompts for this too; press Enter to skip and install manually.

:wrench: **Custom ComfyUI node required — SeFi-Image, MiniMax H3 Turbo, MiniMax H3 Sol-Attn:** these need one extra manual step — clone a custom node into ComfyUI's `custom_nodes` folder. Each `readme.html` has the repo link (SeFi has a folder-nesting gotcha, read carefully). Sol-Attn also needs SimpliGen 1.43.x+ for Triton support.

:scales: **Licensing:** **Flux 2 Klein** is built on Black Forest Labs' FLUX.2 [klein] weights — **non-commercial**, personal/research use only. Everything else is fine for general use.

:rotating_light: **Engine version — Ideogram 4 only:** needs SimpliGen's ComfyUI engine **0.28+**. Update SimpliGen first, or the model won't load.

:white_check_mark: The installer now clearly flags any model that **failed or was skipped**.

Enjoy — feedback and bug reports welcome! :raised_hands:
