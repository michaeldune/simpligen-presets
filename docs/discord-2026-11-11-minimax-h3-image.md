**New pack: MiniMax H3-Image (open weights) - beta engine for now**
MiniMax's own open-weight image model, three cards: text to image at 4 MP, text to image at 16 MP, and edit.

**How it works**
- A built-in prompt writer (Qwen3.5 9B) turns your request into a full description first, so one line is enough. Put any text you want in the picture in quotes.
- 6 steps, run the way the official ComfyUI template does. Nothing to tune.
- The LoRA slot takes H3 video LoRAs: it is the same model without the sound. Style LoRAs worked in testing.

**MiniMax H3-Image** (4 MP) and **MiniMax H3-Image 16 MP**
- 4 MP is 2368x1760 at 4:3, about 50 s. 16 MP is 4736x3552, the size MiniMax recommends, about 80 s.
- A chalkboard reading "FRESH CROISSANTS 2.50" and a poster titled "MONTE LUCE" came back letter-exact.

**MiniMax H3-Image Edit**
- Picture 1 is the one that changes and keeps its shape at about 4 MP. Pictures 2 to 4 are optional; name them in the request: "Put the fox book from <Picture 2> on the table in <Picture 1>."
- About 2 minutes with one or two pictures, about 3 with four.
- With several pictures it can tidy away things you did not mention (plates on a table). Say what must stay.

**Download and engine**
- Reuses the H3 text encoder the H3 video packs already download, plus about 29 GB of its own files.
- **Beta engine only for now:** it needs ComfyUI 0.45.0. Take the beta engine update, then install the pack.
- Peak video memory 11.3 GB. 32 GB of system RAM recommended.

Measured on a 12 GB RTX 4070 Ti, engine 0.45.0.
H3-Image is under the MiniMax-H3-Image Community License, which differs from H3's; check it before commercial use.
Thanks to MiniMax for H3-Image and Comfy-Org for the ComfyUI support.
