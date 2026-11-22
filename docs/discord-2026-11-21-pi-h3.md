**New pack: MiniMax H3 (pi-H3 2-Step)**
Lakonik's pi-H3, released today: a pi-Flow distillation of MiniMax H3 that renders in two sampling steps. Two cards, text to video and image to video (first frame, plus an optional last frame). There is no reference-to-video card, because pi-H3 is built on the FL2VA weights only.

**What is different**
The last step outputs finished pixels, so the slow video VAE decode at the end is skipped. If you already have another H3 pack on the standard weights, the only new download is the 2.2 GB adapter. The app installs the pi-Flow nodes by itself. It needs the current engine (0.45 or newer).

**Speed** (in the app, 12 GB RTX 4070 Ti, Faster Attention on)
- 5 s at 480p: 31 to 33 s, against 36.5 s for TaoMate 3-Step on the same prompt and seed.
- 5 s at 768p: about 71 s. 15 s at 480p: about 97 s.
- 15 s at 768p does not fit in 12 GB. It ran out of system memory and stalled, so pick 480p for long shots.
- Most of each run is loading models, because the app unloads them after every job. In plain ComfyUI with the models kept loaded, it took about 19 s at 480p.

**What we checked**
- The camera moved more freely than on TaoMate in two of three test seeds.
- Small faces in a crowd held up. The official workflow turns Sol-Attn on, but with this model it smeared four of five small faces in our test, so the cards keep it off.
- An occasional small face still comes out smeared. Re-roll the seed.
- Steps are fixed at two, because the adapter is trained for exactly two.

Good for fast drafts and for trying a prompt before you run a slower, higher-quality preset. In the Preset Store after the next sync.
Thanks to Lakonik for pi-H3 and the ComfyUI-piFlow nodes.
