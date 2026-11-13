**New pack: MiniMax H3 (Hybrid DMAD PDMD)**
OliviaRossi's hybrid checkpoint: MiniMax H3's two base models merged into one file, FL2VA for the look and Ref2VA for following references, with the DMAD and PDMD distillations built in. Three cards: text, image and reference to video. No LoRA to load and nothing extra to install.

**The look**
Bright and crisp, with a lot of fine background detail. Beside the new DaSiWa GXS v5 pack on the same prompts it is the lighter and more detailed of the two.

**Steps**
- The cards default to 8 steps at the author's settings (euler, simple, shift 12/3, no CFG).
- The slider goes from 4, the author's fast preview, to 10 for maximum detail.
- In the app on a 12 GB card at 480p, a five-second shot takes about 90 to 115 s at 8 steps on all three cards, and about 50 s at 4.

**What we checked**
- A scripted line came out word for word on three of three seeds.
- Identity held on a solo reference and on a two-person shot, each over three seeds.
- On one seed in three, a person-plus-location shot stayed on the person's own photo and never moved to the location. Try another seed if you see that.

**Download**
One 18.9 GB file from Hugging Face, so no Civitai key is needed. If you already have another H3 pack, that file is the only new download.

Measured on a 12 GB RTX 4070 Ti with Faster Attention on.
Thanks to OliviaRossi for the merge, and to the DMAD and PDMD authors for the distillations.
