Makes sense, and happy to move in step with you. We'll hold our GGUF packs until you say your side is going out, so nothing ends up half on one repo and half on the other.

I went ahead and tried molbal's fork today, in a separate plain ComfyUI (v0.37.2), not in SimpliGen's engine, at commit `48de657b3aa830ae6981960e928b31cb51fd16aa`:

- **Wan 2.2 I2V GGUF** (our card's graph, two Q4 models): renders, and the frames are bit-identical to city96 at `6ea2651` on the same ComfyUI.
- **Krea Flux** (kreaCSG_foundation.gguf): renders. Same composition as city96, with small detail differences (lettering on a sign changed). I only ran one seed per prompt and did not check whether city96 repeats itself exactly, so I can't say yet that the fork is the cause.
- **Dark Beast Krea 2 GGUF** (the one that started this): Q8 and Q4 both load and render. Q8 is very close to the original fp8 file; Q4 gives a different composition but a clean picture.

Not tested: the fork inside your engine (0.38.0), the app path, or your H3 GGUF packs.

Ours that need to move with you: `krea-flux` and `wan22-i2v-gguf` (both pin city96 at `6ea2651`), plus a new Dark Beast GGUF card for the Krea 2 pack.

Two things that would help us line up:
1. Which repo URL and commit will you pin? We'll use exactly the same in ours.
2. Do you want ours pushed before your release, at the same time, or after you give the word? I'd rather not bump them early and have the store publish them against the old loader.
