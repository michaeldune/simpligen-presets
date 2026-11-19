Hi again! SimpliGen has no workflow import, so you can't load a Civitai workflow JSON or PNG directly. SimpliGen runs every workflow as a **card** (a preset), and that is why we package workflows as preset packs. Many of the community packs in the **Preset Store** started as workflows people posted, so check the Store first.

**Making your own.** You can do this, though very few people have so far. Clone our repo and have a coding agent (Claude Code, Codex, Gemini) build a pack from the workflow, following our authoring guide. The guide is written for an agent, and the repo has dozens of finished packs it can copy from:
https://github.com/michaeldune/simpligen-presets/blob/master/CUSTOM-PRESET-AUTHORING-GUIDE.md
A pack is a JSON file (the card's fields, sizes and model list) plus the workflow in ComfyUI **API format**. Civitai workflows come in the normal UI format, so open them in ComfyUI and use Export (API) first.

Your questions in order:
- **Your own models, LoRAs, VAEs, encoders:** yes. The card uses the files in your SimpliGen models folders. The pack also lists download links, so anyone else who installs it gets the files automatically.
- **Custom nodes:** yes. The pack declares each node (repo + commit) and SimpliGen installs it. Nodes that need extra Python packages take more care, and the guide covers that.
- **Missing dependencies:** the app downloads any model the pack declares before the first run. A node the pack forgot to declare shows up as a "node not found" error, which tells you what to add.
- **Editing and reuse:** the pack is plain JSON on your disk. Edit it, restart SimpliGen, and the card stays in your library.
- **Compatibility:** anything the bundled ComfyUI engine runs. SDXL, Flux, Qwen-Image 2.1 and Z-Image all have packs already. Two limits: a card has a fixed set of controls (prompt, aspect ratio, seed, reference images, LoRAs, count), and node widgets you want to change become values in the workflow rather than sliders.
