**New MiniMax H3 pack: 8+2 Two-Pass Reference to Video**
The Real OAF asked for Deno's 8+2 workflow from Ok Todd AI's video, so here it is as two Reference cards, one on DenoMix and one on Singularity v2.

**How it works**
- 8 fast steps at a small size, a latent upscale, then the last 2 of the same 8 steps at full size with Kijai's refiner.
- The sound from the first pass is kept as is, so the second pass cannot change a spoken line.
- Reference to video only. Attach one picture per person and write the usual Ref2VA prompt.

**DenoMix** (Deno)
- Steady camera, low-key natural light, textured skin. Sits between stock H3 and Singularity v2.
- In wide shots it often frames people larger than you asked for.
- 21 GB download.

**Singularity v2** (WarmBloodAban)
- More movement, wide shots that stay wide, louder ambience, darker faces.
- No new checkpoint if you already have Singularity v2.

**Speed and sizes**
- About 3 minutes for 5 s at 768p on 12 GB. Every spoken line came out word for word in our test (12 of 12).
- 928p is for 16 GB or more. On 12 GB it runs, but 928p or a 10 s clip takes 4 to 20 minutes, because the second pass sits right at the edge of video memory.
- Not tested on 16 GB or more yet, so times from bigger cards are welcome.

Measured on a 12 GB RTX 4070 Ti with 32 GB of RAM, engine v0.43.0.
DenoMix is under the MiniMax H3 Community License, Singularity v2 is Apache-2.0.
https://huggingface.co/Deno2026/MiniMax-H3-DenoMix
