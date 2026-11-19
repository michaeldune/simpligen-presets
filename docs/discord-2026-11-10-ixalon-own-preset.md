Found it. Three things in the zip:

1. **The workflow lost its placeholders.** In sickollie.json every `{{...}}` slot is gone: the prompt is the literal word "prompt", and width, height, seed, steps, cfg, denoise and upscale are all `null`. SimpliGen fills a card by swapping those `{{prompt}}`, `{{width}}` etc. strings, so even once the card showed up it would not render. The LoRA loader key also came out garbled ("âž• Add Lora" instead of "➕ Add Lora"), which looks like the file went through a Windows-1252 save somewhere.

2. **The installer menu is hard-coded.** install.ps1 is generated for exactly ten cards in a fixed order. Your card went in third, so menu entry [3] *says* sickOllie but copies Realia's workflow and picture, and VXP Beta 3 dropped off the menu. Only [0] (all) installs the right files. Choosing a single card also rewrites krea-2-pack.json with just that card, so the other ten disappear on the next start.

3. **Typo:** the encoder URL starts with `hhttps://`.

Easier route: don't edit our pack. Ours updates from the store and the zip is a month old (1.8.0). A card of your own lives best in its own little pack, so I've made you one: **sickollie-krea2.zip** (attached). It's your card and picture on our current Krea 2 workflow with the slots intact, under its own pack id, so nothing of ours touches it. Run install.cmd, press Enter (or paste your presets folder if you moved SimpliGen's data folder), restart SimpliGen, and look for the pack "sickOllie Krea 2". It downloads nothing, so your D:\models files stay as they are.

If your own copy still doesn't show at all, two things would tell me why: which number you picked in the installer, and whether krea-2-pack.json is actually in the presets folder of your data folder (default %APPDATA%\simpligen\presets).
