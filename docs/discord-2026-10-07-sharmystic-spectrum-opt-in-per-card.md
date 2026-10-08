Hey Sharmystic, a small manifest request, no bug. Could a card declare Spectrum as supported but off by default, the way Sparse Attention became opt-in in 1.70.1? In other words the SPECTRUM chip in the generation controls would start on Off for that card, and the user can still pick On.

**Why I'm asking**
I added Faster Attention to our DaSiWa H3 packs today and tested Spectrum on them before flagging it. On the DaSiWa Turbo checkpoints it garbles speech some of the time:
- Same text-to-video shot with one scripted line, 864x480, 5 s, 8 steps, seeds 4242 / 22 / 33.
- No accelerators: the line was word for word on 6 of 6 (v2 and v3).
- Sage + Spectrum (sigma shift 12/3 and the Spectrum defaults the app injects): garbled on 1 of 3 seeds on v2 and 1 of 3 on v3. I listened to the v3 one and it is clearly garbled; the v2 one is by transcript.
- Sage alone was fine apart from one slurred word in about 15 renders.

It looks specific to DaSiWa. I ran the same line through the app on 10Eros beta5 Turbo, TaoMate, Turbo Accelerated, 10Eros beta5, Singularity, SparseRef15 and Z-Image Graft, three seeds each, accelerators off, Sage + Spectrum, and Sage + Spectrum + Sparse Attention: 57 of 57 word for word by transcript.

**What we did**
The three DaSiWa packs shipped with supportsSage only. With supportsSpectrum, a talking shot would fail about one time in three out of the box.

**What an opt-in would give**
Spectrum takes a DaSiWa v2 shot from about 82 s (Sage) to about 60 s. People making shots without dialogue would happily switch it on themselves; I just can't make it the default for that checkpoint. A per-card flag for "Spectrum available, default off" would let us offer it. Name and shape are your call.

Nothing here asks for a change to the official packs. Clips and the test scripts are on my side if you want them.
