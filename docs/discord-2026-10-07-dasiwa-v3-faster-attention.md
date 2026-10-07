**DaSiWa MiniMax H3: a new v3 pack, and the v1 and v2 packs get quicker**
Mr.Anderson asked two things today: is DaSiWa v3 coming, and why were the DaSiWa packs slower than 10Eros Turbo. He was right on the second one: our DaSiWa cards never picked up Faster Attention. Both are sorted.

**Faster Attention now works on the DaSiWa packs** (Settings > Advanced > Faster attention)
- **MiniMax H3 (DaSiWa Hybrid) 1.3.0**, all four cards: 67-71 s per shot with it on, about 80 s before.
- **MiniMax H3 (DaSiWa Hybrid v2) 1.2.0**, all three cards: 78-83 s with it on, about 100 s before.
- Same picture and same spoken line as before, just sooner. Nothing else in either pack changed.

**New pack: MiniMax H3 (DaSiWa Hybrid v3)**
Darksidewalker's v3 Turbo from 1 October, eight steps, one checkpoint for all three cards:
- **Text to Video**, **Image to Video** (your picture is the first frame) and **Reference to Video** (up to nine references).

What we measured against v2 (12 GB RTX 4070 Ti, 5 seconds at 480p, same prompts, seeds and references):
- Same speed as v2: 76-85 s per shot with Faster Attention on.
- Every identity held on three reference sets, and a scripted line came out word for word on three of three seeds.
- The look is different rather than plainly better. On our comparison seed v3 was darker and cleaner, with less surface grain and less movement than v2. It is an option beside v1 and v2, so try it and keep the one you like.

Good to know:
- We left the extra step-skipping accelerator (Spectrum) off on all three DaSiWa packs. It was faster again, but it garbled the spoken line on about one seed in three in our tests.
- v3 is its own 19.5 GB download and needs a Civitai API key (free model, sign-in required). The text encoder and VAEs are shared with the other MiniMax H3 packs.
- v3 is tested at eight steps only.

Thanks to Darksidewalker for the models: https://civitai.com/models/2877206
