**DaSiWa MiniMax H3: a new v3 pack, and the v1 and v2 packs get quicker**
Mr.Anderson asked today whether DaSiWa v3 was coming and why the DaSiWa packs were slower than 10Eros Turbo. He was right: our DaSiWa cards never picked up Faster Attention. Both are sorted.

**Faster Attention now works on the DaSiWa packs** (Settings > Advanced > Faster attention)
- **MiniMax H3 (DaSiWa Hybrid) 1.3.0**, all four cards: 67-71 s per shot with it on, about 80 s before.
- **MiniMax H3 (DaSiWa Hybrid v2) 1.2.1**, all three cards: 78-83 s with it on, about 100 s before.
- Same shot as before, just sooner. Nothing else in either pack changed.
- One of our ten test renders slurred a word with the toggle on and was clean with it off. If a line comes out wrong, try another seed or switch the toggle off for that shot.

**New pack: MiniMax H3 (DaSiWa Hybrid v3)**
Darksidewalker's v3 Turbo from 1 October: eight steps, one checkpoint, three cards (**Text to Video**, **Image to Video**, **Reference to Video**).

Measured against v2 (12 GB RTX 4070 Ti, 5 s at 480p, same prompts, seeds and references):
- Same speed: 76-85 s per shot with Faster Attention on.
- Every identity held on three reference sets, and a scripted line came out word for word on three of three seeds.
- The look is different rather than plainly better: on our comparison seed v3 was darker and cleaner, with less surface grain and less movement. It sits beside v1 and v2, so try it and keep the one you like.

Good to know:
- The extra step-skipping accelerator (Spectrum) is off on all three DaSiWa packs. It was faster again, but garbled the spoken line on about one seed in three.
- v3 is its own 19.5 GB download and needs a Civitai API key (free model, sign-in required). Tested at eight steps only.

Thanks to Darksidewalker for the models: https://civitai.com/models/2877206
