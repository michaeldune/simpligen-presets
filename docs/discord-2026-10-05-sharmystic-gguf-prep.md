Great news, thanks for running it properly. Everything on our side is prepared and held, nothing pushed.

**Agent route on 1.68.11:** fixed. I reran `community--wan22-i2v-gguf-pack:wan-22-i2v-gguf-q4` through the agent just now and it rendered (159 s, 5 s at 480p). The queued graph has the HighNoise and LowNoise files in the two loaders, as it should.

**Prepared, waiting for your word:**
- `krea-flux` 1.2.0 and `wan22-i2v-gguf` 1.3.0: ComfyUI-GGUF pointed at `https://github.com/molbal/ComfyUI-GGUF.git`, pinnedCommit `48de657b3aa830ae6981960e928b31cb51fd16aa`, minAppVersion 1.68.11.
- `krea-2` 1.7.0: two new Dark Beast GGUF cards (Q8 and Q4) with the same pin and minAppVersion. The old FP8 card is unchanged apart from a line saying its download is now paid.

One question on that last one: minAppVersion is per pack, so putting it on `krea-2` gates the whole pack, including the six cards that don't use GGUF. Is that the right way to do it, or would you rather the GGUF cards live in their own pack so the Krea 2 pack keeps installing on older app versions?

**GGUF text encoders:** none of ours use one. Both packs only use UnetLoaderGGUF, so the 5x slower encode and the DynamicVRAM question don't touch us.

**Krea Flux:** I had already done the repeat on city96 yesterday: three runs with the same seed, byte-identical, and the fork is byte-identical to itself too, but the two differ from each other (21-24 dB). Today I added a run on your engine (0.38, city96 6ea2651, same graph and seed): it matches my plain-ComfyUI city96 render closely (33-38 dB) and differs from the fork render by the same 21-24 dB. So city96 behaves the same in both places and the fork is the odd one out on this particular file. What I have not done is run the fork inside the engine; I can swap the folder by hand and do that if it would help. The file is `kreaCSG_foundation.gguf` (Flux.1 Krea, Q4_K with some Q5_K and BF16 tensors), in case you want to try it on your side.

Ready to pick a switch date whenever your remaining checks are done.
