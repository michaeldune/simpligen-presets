:art: **Community Preset Packs — Free Downloads**

A growing collection of 20+ local preset packs for SimpliGen — images, video, and sound-synced video — put together with help from Claude Code and Codex. Every pack is a one-click installer that downloads and verifies its own models.

:books: **What's in them:** <https://github.com/michaeldune/simpligen-presets#readme>
The full catalogue lives there — every pack, its presets, the architecture behind it, and measured generation times for the video presets. It's kept in step with the source, so it's always current. Check there rather than this post.

:inbox_tray: **Download:** https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest
This link is rolling — the zips are replaced on every build, so it always points at the newest set. Bookmark it and you'll never need a new link.

:octopus: **Source:** <https://github.com/michaeldune/simpligen-presets> — pack definitions, workflows, and the build script. Browse, report issues, or build the zips yourself.

**How to install**
1. Download a pack's `.zip` and unzip it
2. Open `readme.html` — it lists exactly which models that pack needs and where they go
3. Run `install.cmd` — downloads the models for you; install the whole pack or just one preset
4. Restart SimpliGen

**:clipboard: Before you install — please read**

:warning: **Disk space:** these are full local models, often 5–13 GB each, and video packs run larger. If you're tight, install one preset at a time — `readme.html` shows sizes up front.

:key: **Civitai / HuggingFace tokens:** some models need a free API token or a license acceptance. The installer prompts for both; press Enter to skip, and you'll get manual download links in `readme.html` instead.

:wrench: **Custom ComfyUI nodes:** a few packs need one extra manual step — cloning a node into ComfyUI's `custom_nodes` folder. Each pack's `readme.html` names the exact repo and any gotchas. If a preset won't load, check this first.

:rotating_light: **Engine version:** a handful of presets need a recent SimpliGen engine. `readme.html` calls this out per pack — update SimpliGen if a model refuses to load.

:scales: **Licensing:** **Flux 2 Klein** is built on Black Forest Labs' FLUX.2 [klein] weights — **non-commercial**, personal and research use only. Everything else is fine for general use.

:white_check_mark: The installer clearly flags any model that failed or was skipped — no silent failures.

Enjoy — feedback and bug reports welcome! :raised_hands:
