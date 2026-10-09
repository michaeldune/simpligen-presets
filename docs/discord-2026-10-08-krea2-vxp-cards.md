**Krea 2 pack 1.8.0: two VXP Krea 2 cards**
Someone here asked for a SimpliGen preset for VXP's Krea 2 anime checkpoint. It is in the Krea 2 pack now, together with its sibling from the same beta series.

The cards:
- **VXP Krea 2 Beta 4 (Anime)**: the one that was asked for. Anime and semi-real illustration with one strong look on everything: backlight, rim-lit hair, deep shadows, a dark high-contrast grade. It turns photo prompts into illustration too, so it is not a photo card.
- **VXP Krea 2 Beta 3 (Hybrid)**: the same dark, backlit look, but it keeps photographs photographic (moody window light, real skin texture). On anime and semi-real prompts it lands close to Beta 4. It is a separate branch of the series, not an older Beta 4.

Good to know:
- Settings, since the model page gives none: 8 steps, CFG 1, euler/simple. The cards have a Steps slider (6-12) and no CFG slider: the one higher setting we tried (20 steps at CFG 3.5) came out as noise.
- We ran both against stock Krea 2 Turbo, Equinox, Moody, BF95 Dark Realism and Dark Beast on the same prompts and seeds. None of those gave this look, which is why both got a card.
- Both are uncensored. On our clothed test prompts neither one produced nudity nobody asked for, where one of the other uncensored cards did.
- A ~2 MP picture (1216x1632 and equivalents) takes about 25 seconds on a 12 GB card. They use the same workflow as the other Krea 2 cards; we have not tested the Upscale slider or LoRAs on these two yet.
- Each card downloads only its own 13.3 GB file. The text encoder and VAE on the model page are the same files the other Krea 2 cards already use.
- For plain ComfyUI: put the file in `models/diffusion_models` and load it in the standard Krea 2 Turbo workflow with the same settings. No custom nodes needed.

The author calls these experimental betas, so expect rough edges. Thanks to VXP for the models. Krea 2 Community License, plus the author's terms on the model page: https://civitai.red/models/2938537
