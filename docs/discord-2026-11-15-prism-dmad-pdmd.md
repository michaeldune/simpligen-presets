**New pack: MiniMax H3 (PRISM DMAD PDMD)**
OliviaRossi's PRISM merge (Singularity v2 and 10Eros Max) with the DMAD and PDMD distillations built in, as requested by Atropheus and RHR. Three cards: text, image and reference to video, all in the Video Studio. No LoRA to load and nothing extra to install.

**The look**
Textured and lively: grittier skin, bigger expressions and more motion than the Hybrid DMAD PDMD pack on the same prompts. It also follows a camera move (push-in, dolly) more closely.

**Steps and speed**
- 8 steps by default (euler, simple, shift 12/3, no CFG). The slider goes from 4 to 10.
- In the app on a 12 GB card at 480p, a five-second shot takes about 65 to 75 s at 8 steps on all three cards, and about 40 s at 4.
- The author suggests the beta57 scheduler. It needs an extra node pack, and in our test it gave nearly the same picture as simple, so the cards use simple.

**What we checked**
- Scripted lines came out word for word at 4, 6, 8 and 10 steps.
- Reference to video: people stay recognisable (hair, skin, clothes) over three seeds, but the face is held less closely than on the Hybrid DMAD PDMD pack.
- Locations: a wide picture of an empty place worked every time (4 of 4). A close-up of an object in its setting brought only the object. Give it the whole place.

**Download**
The cards use the author's smaller W6A8 file, 14.8 GB from Hugging Face, so no Civitai key is needed. Same pictures as the 18.9 GB int8 file in our test, and about 10% faster. If you already have another H3 pack, that file is the only new download.

Measured on a 12 GB RTX 4070 Ti with Faster Attention on.
Thanks to OliviaRossi for the merge, and to the DMAD and PDMD authors for the distillations.
