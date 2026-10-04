**Question: Krea 2 GGUF support in the engine's GGUF loader**

One of our Krea 2 cards lost its download and the only free replacement is a GGUF, which the engine can't load yet. Asking whether that is something you'd consider, no rush.

**What happened**
- `krea-2-pack:dark-beast-krea2-fp8` downloads Civitai version 3078453. The creator has since made it paid: the download now returns 403 with a valid key, and Civitai marks the version `paidAccess: permanent`. His other Krea 2 versions are paid too. People who already have the file are fine; new installs can't get it.
- molbal published a free GGUF conversion of that exact version (Civitai model 2749127, Q8_0 14.6 GB and Q4_0 8.3 GB, no key needed).

**What the engine does with it (0.38.0, app 1.67.2)**
`UnetLoaderGGUF` fails with:
```
Unexpected architecture type in GGUF file: 'krea2'
```
The engine's ComfyUI-GGUF is city96 at 6ea2651, which is still upstream's latest, and its architecture list has no `krea2`.

**What exists**
molbal/ComfyUI-GGUF (a fork, last commit 48de657 on 2026-09-20) adds `krea2` to that list, along with `qwen_image21`, `minimax_h3` and others. I have not tested it.

**Why I'm asking instead of pinning it in the pack**
ComfyUI-GGUF is shared. Your MiniMax H3 GGUF and Turbo packs use it, and two of our packs (Krea Flux, Wan 2.2 I2V GGUF) pin city96 at 6ea2651. Pointing one pack at the fork looked like a good way to flip the others to "not installed", so I left it alone.

**The question**
Is Krea 2 GGUF something you'd want the engine to support, whether by moving to the fork or some other way? If yes, I'll add a GGUF card for this model and test it against the original file. If not, I'll just mark the old card as no longer downloadable.
