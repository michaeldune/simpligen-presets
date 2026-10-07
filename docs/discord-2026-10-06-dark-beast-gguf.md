**Krea 2 pack 1.7.0: Dark Beast is back, as two free GGUF cards**
The creator of Dark Beast Krea 2 made the FP8 file paid on Civitai, so new installs of that card could no longer download it. molbal published free GGUF conversions of the same "Aggressive Edition" model, and the Krea 2 pack now has a card for each.

The cards:
- **Dark Beast Krea 2 (GGUF Q8)**: the replacement for the FP8 card. For the same seed it gave us the same composition and subject as the FP8 original on four of four test pictures: uncensored, bold, high contrast, 8 steps at CFG 1. A 14.6 GB download.
- **Dark Beast Krea 2 (GGUF Q4)**: the same model in an 8.3 GB file, aimed at 8 GB cards or a smaller download (we tested on 12 GB only). The heavier compression changes the picture: the same seed composes differently from the Q8 and FP8 builds, but the results were clean in our tests.

Good to know:
- Both render a ~2 MP picture (1408x1408 and equivalents) in about 40 seconds on a 12 GB card, with the same Upscale slider and LoRA slot as the other Krea 2 cards.
- If you already have the FP8 file, your old Dark Beast card keeps working exactly as before. Nothing about it changed except a note on its download.
- These cards need SimpliGen's new GGUF loader. The app switches to it by itself the first time you run one; expect a short one-time setup and an engine restart.
- The text encoder and VAE are shared with the other Krea 2 cards, so each card downloads only its own model file.

Thanks to molbal for the conversions and the loader, and to Sharmystic for coordinating the switch. Krea 2 Community License, plus the authors' terms on the model page: https://civitai.com/models/2749127
