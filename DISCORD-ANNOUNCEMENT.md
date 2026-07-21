:art: Community Preset Packs — Free Downloads

I've put together (with a great deal of assistance from Claude Code and Codex) a collection of 16 preset packs (60+ presets) for SimpliGen covering a wide range of models and styles. Each pack includes a one-click installer and a readme with model download links.

:new: **New — Ideogram 4:** best-in-class text rendering and a wide style range from one model — photoreal, flat poster/graphic design, editorial, even anime — all from a 9.4 GB INT8 checkpoint at 8 steps. Two tiers: **UltraReal** (photo) and **Graphic/Poster** (flat design). Needs engine 0.28+ — see below.

:arrows_counterclockwise: **Updated:** installer now uses curl instead of Windows BITS — fixes old "HTTP 400" download errors. New models added across the Illustrious and Krea packs too.

:package: What's included: (as of this moment)

Anima Anime & Realism
SDXL Realism & Art/Anime
Pony Anime &  Realistic
Illustrious Realism & Anime
SD 1.5 Anime
Krea 2 (Moody Mix, RedCraft, Realia, Fascium)
Krea Flux (CSG Foundation — GGUF Flux.1 Krea)
Flux 2 Klein (9B, MiracleIn NSFW, 4B Maxx — sub-second 4-step generation)
Ideogram 4 (UltraReal photo + Graphic/Poster — needs engine 0.28+)
Z-Image
Reij's Merges
Moody Models

:inbox_tray: Download: https://www.dropbox.com/scl/fo/q6bt9h1dit7axfvq8o4j3/AD8yAlftvg2auCaunh2f5zE?rlkey=2n45wzxjjsb3o9i8eh20qz768&st=ib7k353q&dl=0

:octopus: Source on GitHub: <https://github.com/michaeldune/simpligen-presets> — all pack definitions, workflows, and the zip build script. Browse the presets, report issues, or build the zips yourself.

How to install:

Download a pack's .zip and unzip it
Open readme.html to see which models you need and grab any you're missing
Run install.cmd — it will download models automatically and let you install the full pack or a single preset
Restart SimpliGen

**:clipboard: Before you install — please read:**
:warning: **Disk space:** these are full local image models. Some packs pull **5–13 GB per model**, and a few packs reference several. If you're tight on disk space, install one preset at a time rather than a whole pack, and check the model sizes listed in each pack's `readme.html` first.

:key: **Civitai token:** some models need a **free API token** to download. Create one at <https://civitai.com/user/account> (API Keys) — the installer prompts for it. No token = those models are skipped (`readme.html` has manual links).

:hugging: **HuggingFace token:** a few models live on HuggingFace and may need a free HF access token / license acceptance. The installer prompts for this too; press Enter to skip and install manually.

:scales: **Licensing:** The **Flux 2 Klein** pack is built on Black Forest Labs' FLUX.2 [klein] weights, which are **non-commercial** — personal/research use only. Everything else is fine for general use.

:rotating_light: **Engine version — Ideogram 4 only:** needs SimpliGen's ComfyUI engine **0.28+** (native INT8). Update SimpliGen first, or the model won't load. Everything else works on any engine version.

:white_check_mark: The installer now tells you clearly if any model **failed or was skipped**, so you won't be left thinking everything downloaded when it didn't.

:test_tube: **In the works (advanced / manual setup, not in the one-click packs yet):**
• **SeFi-Image 5B** — Semantic-First Diffusion, unreal at rendered text/posters and stylized art. Needs a custom ComfyUI node, so it's manual for now.
• **Wan 2.2 Image-to-Video (GGUF)** — animate a still image, runs on 12 GB. Video packs aren't one-click yet.
Ping me if you want a hand setting either up.

Enjoy — feedback and bug reports welcome! :raised_hands:
