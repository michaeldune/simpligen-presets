**MiniMax H3 (FastH3 8-Step V2) pack 1.2.0: two FastH3 Trim cards**
FastVideo published FastH3 Trim yesterday: an experimental, lighter version of FastH3 V2 that keeps 42 of H3's 50 transformer blocks. The pack now has a Trim card beside each V2 card, on the same eight-step graph.

The cards:
- **MiniMax H3 Text to Video (FastH3 Trim 8-Step)**: describe a scene, get video with stereo sound.
- **MiniMax H3 Image to Video (FastH3 Trim 8-Step)**: your picture is the first frame, with an optional last frame.

What we measured against V2 (12 GB RTX 4070 Ti, 5 seconds at 480p, four scenes, three seeds each, same prompts and seeds):
- Faster: sampling took 54 s against 72 s, about 68 s against 86 s for the whole job.
- Talking heads and image-to-video looked the same as V2 in close crops, and every spoken line came out word for word.
- Product shots were clean on all three seeds.
- Wide action is where it gives ground: on a beach-run shot Trim framed the runner smaller, her face was softer at that size, and the soundtrack measured quieter.

Good to know:
- FastVideo call Trim experimental and say to use V2 when quality matters most. Think of Trim as the quicker card for talking heads, product shots and animating a still.
- It is its own 17.6 GB download. The text encoder and VAEs are shared with the other MiniMax H3 packs.
- Same requirement as the V2 cards: SimpliGen engine 0.36 or later. Text and image to video only, no reference-to-video.
- The two V2 cards are unchanged.

Thanks to FastVideo (hao-ai-lab) for the model and the ComfyUI repack. MiniMax H3 Community License: https://huggingface.co/FastVideo/FastVideo-FastH3-Trim-Comfy
