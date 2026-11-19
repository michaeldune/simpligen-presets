**New pack: MiniMax H3 (Regenerate 1080p) - NVIDIA's open H3 regenerate pass, on a 12 GB card**
NVIDIA released Open-H3-Regenerate-2K this week, an open replacement for H3's paid 2K regenerate service. One card: drop a finished H3 clip in Reference Video 1, paste the brief that made it, and the first 5 seconds come back at **1920x1088** with the clip's own soundtrack. It upscales the clip's latent, then re-renders it in three steps with NVIDIA's refiner, so it adds detail that was never in the source: hair strands, knit, skin, readable lettering on book spines.

Measured on a 12 GB RTX 4070 Ti, against the Video Refine card run at the same 1080p size:
- **From a 480p clip, about 3x sharper faces.** Two people at a cafe table, faces about 60 px tall in the source: curls, eyes and teeth come back crisp.
- **From a 768p close-up, about 1.3x on the face and 2x on the background.**
- **On a soft, dark shot, only a small gain.** It sharpens what is there; it cannot invent light.
- **About 7 to 10 minutes per clip** (9.5 through the app).

**We changed one thing from NVIDIA's recipe, and you should know why.** It starts from 91% noise, so it regenerates rather than polishes. Run as published, a close-up of a young man came back as a different, older man, on two seeds out of two. The card feeds your clip's first frame back in as an anchor, and with it the same person held on all three test clips, and on both seeds of the close-up. Small changes still happen: we saw added stubble, and a woman's lowered eyes came back open. If a clip must stay exactly as it is, use the Video Refine card.

Good to know:
- **It needs most of 32 GB of system RAM.** Close other apps first, especially anything else holding AI models (another ComfyUI, for example). With one open, the same 7-minute job took 15 to 46 minutes.
- **Pick the aspect ratio that matches your clip** (16:9, 9:16 or 1:1). The duration slider is ignored: it always takes the first 5 s.
- **1080p, not 2K.** 2560x1440 is not tested on 12 GB, so the card does not offer it.
- NVIDIA's full mix also stacks the lightx2v Turbo and LMS Sharp LoRAs. It is sharper still, but it ran out of RAM on a 32 GB machine and one render took over half an hour, so the card uses the refiner alone.
- Downloads: the 5.9 GB refiner and the 0.7 GB upscaler on top of the H3 FL2VA base most H3 packs already use; 47 GB if you have nothing H3 yet.
- MiniMax H3 Community License.

Thanks to NVIDIA for Open-H3-Regenerate-2K (https://huggingface.co/Efficient-Large-Model/Open-H3-Regenerate-2K), Kijai for the refiner-only extraction the card downloads (https://huggingface.co/Kijai/MiniMax-H3-experimental), and LBH-123-AI for the 3D latent upscaler (https://huggingface.co/LBH-123-AI/Minimax_h3_latent_Upscaler).
