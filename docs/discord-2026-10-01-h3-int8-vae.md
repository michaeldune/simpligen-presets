**MiniMax H3 packs: faster decoding, same picture**
Every community MiniMax H3 pack (24 packs, including Viggle Animate and Motion Transfer) now uses the official int8 ConvRot video VAE instead of the fp16 one. Decoding the finished video is about 2.5 times faster, which takes roughly 10 to 35 seconds off each render on a 12 GB card.

The picture doesn't change. We rendered eight kinds of H3 card both ways with the same seed and inputs (text, image and reference to video, Video Refine, Clip Chaining, Two-Stage, Viggle, Motion Transfer) and the results match, including the cards that feed in your own pictures and clips.

What to expect:
- Every H3 pack shows "Update available". Updating downloads the new VAE once (2.8 GB) and every pack shares it.
- The old fp16 VAE (5.2 GB) stays on your disk. Other presets, including the official H3 ones, may still use it, so leave it unless you're sure nothing does.
- If a card stops right after updating with "Value not in list", restart SimpliGen once so it picks up the new file.
