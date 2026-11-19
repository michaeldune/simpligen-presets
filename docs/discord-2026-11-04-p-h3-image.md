**New pack: P-H3-Image - 8-megapixel pictures from MiniMax H3 (beta engine for now)**
Pruna's P-H3-Image is an image model distilled from MiniMax H3: 8 steps, about 8 megapixels per picture, on a 12 GB card. Two cards, text to image and edit.

**How it works**
- A built-in prompt writer (Qwen3.5 9B) turns your request into a full description before the picture is made, so one line is enough. Write plain sentences, and put any text you want in the picture in quotes.
- It runs the way the official ComfyUI template does: 8 steps, no CFG, no extra settings to tune.

**P-H3-Image** (text to image)
- About 8 MP: 3360x2496 at 4:3, 2176x3872 at 9:16. About 1 minute per picture on 12 GB (59-62 s in our tests).
- "a street food vendor in Hanoi at night ... a hand-painted sign reading "PHO GIA TRUYEN"" came back with the sign spelled right, checked at full size.
- The same seed can give a slightly different picture on another PC, because the prompt writer's wording can change between installs.

**P-H3-Image Edit**
- Picture 1 is the one that changes; it comes back at about 4 MP in its own shape. Pictures 2 to 4 are optional references.
- Name them in the request: "Put the steaming pot of pho from <Picture 2> on the workbench in <Picture 1>, beside the watches."
- About 1 minute with one picture (67 s). A large second picture adds time: about 2 minutes with an 8 MP one.
- "Make it night: the window is dark and the bench is lit only by a small desk lamp." kept the man, his loupe and the watches on all three seeds.
- Tested with one and two pictures. Three and four use the same setup but we have not run them yet.

**Download and engine**
- It reuses the 21 GB MiniMax H3 FL2VA model the H3 video packs already download, plus about 17 GB of its own files (the LoRA, text encoder, VAE and prompt writer).
- **Beta engine only for now:** it needs ComfyUI 0.44.0. Settings > Updates > beta, take the engine update, then install the pack.
- Peak video memory was 11.3 GB. 32 GB of system RAM recommended.

Measured on a 12 GB RTX 4070 Ti with 32 GB of RAM, engine v0.44.0.
P-H3-Image and the MiniMax H3 model are under the MiniMax H3 Community License; check it before commercial use.
Thanks to Pruna for P-H3-Image (https://huggingface.co/PrunaAI/P-H3-Image-Comfy), MiniMax for H3, and Comfy-Org for the native ComfyUI support.
