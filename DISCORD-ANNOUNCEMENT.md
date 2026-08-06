:art: Community Preset Packs — Free Downloads

I've put together (with a great deal of assistance from Claude Code and Codex) a collection of 19 preset packs (69 presets) for SimpliGen covering a wide range of models and styles — images, video, and now sound-synced video too. Each pack includes a one-click installer and a readme with model download links.

:new: **New — MiniMax H3 Turbo:** two video presets that cut MiniMax H3's text-to-video sampling from ~20 steps down to ~6-8 while keeping the audio in sync, using larryvrh's Turbo LoRA + a custom dual-schedule sampler. One plain Turbo preset, one Turbo + EasyCache variant for a bit more speed on top. Needs one extra manual step — see below.

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
MiniMax H3 Turbo — Text-to-Video with synced audio, ~6-8 steps (needs a custom node)

:inbox_tray: Download: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest

:octopus: Source on GitHub: <https://github.com/michaeldune/simpligen-presets> — all pack definitions, workflows, and the zip build script. Browse the presets, report issues, or build the zips yourself.

How to install:

Download a pack's .zip and unzip it
Open readme.html to see which models you need and grab any you're missing
Run install.cmd — it will download models automatically and let you install the full pack or a single preset
Restart SimpliGen

**:clipboard: Before you install — please read:**
:warning: **Disk space:** these are full local models. Some packs pull **5–13 GB per model** (video packs more), and a few packs reference several. If you're tight on disk space, install one preset at a time rather than a whole pack, and check the model sizes listed in each pack's `readme.html` first.

:key: **Civitai token:** some models need a **free API token** to download. Create one at <https://civitai.com/user/account> (API Keys) — the installer prompts for it. No token = those models are skipped (`readme.html` has manual links).

:hugging: **HuggingFace token:** a few models live on HuggingFace and may need a free HF access token / license acceptance. The installer prompts for this too; press Enter to skip and install manually.

:wrench: **Custom ComfyUI node required — SeFi-Image and MiniMax H3 Turbo:** these two need one extra manual step the installer can't do for you — clone a custom node into ComfyUI's `custom_nodes` folder. Each pack's `readme.html` lists the exact repo link and, for SeFi, an important gotcha about which folder to actually copy in.

:scales: **Licensing:** The **Flux 2 Klein** pack is built on Black Forest Labs' FLUX.2 [klein] weights, which are **non-commercial** — personal/research use only. Everything else is fine for general use.

:rotating_light: **Engine version — Ideogram 4 only:** needs SimpliGen's ComfyUI engine **0.28+** (native INT8). Update SimpliGen first, or the model won't load. Everything else works on any engine version.

:white_check_mark: The installer now tells you clearly if any model **failed or was skipped**, so you won't be left thinking everything downloaded when it didn't.

Enjoy — feedback and bug reports welcome! :raised_hands:
