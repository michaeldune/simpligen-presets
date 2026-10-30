**New pack: MOSS-Image Edit HQ - the same edit card, on an Apache-2.0 LoRA**
One card, and it exists for one reason: **the licence**. The MOSS-Image Edit card runs chinoll's edit LoRA, which is excellent and declares no licence at all for its weights. This pack runs akhaliq's MOSS-Image-Edit-HQ (armV5) instead, which is Apache-2.0, so if you need a clean licence on everything you install, install this one. **It is an alternative, not a replacement** - the original card is not going anywhere, and if the licence does not matter to you, keep using it.

**It is also not an upgrade, and we would rather tell you than let you find out.** We ran the two LoRAs head to head on the same pictures, instructions and seeds - 3 pictures x 3 kinds of instruction x 2 seeds each, plus the author's own recommended settings on HQ, 54 renders in all:
- **chinoll holds the untouched part of the picture closer, in 8 of the 9 picture+instruction pairs.** Told to recolour a shop front and keep the "GOLDEN CRUST" sign, or to relight a portrait and keep the face, chinoll drifts the kept region about a fifth less on average. HQ runs warmer and a little looser.
- **HQ wins the heavy restyle.** Photo to watercolour on the portrait is the one pair it takes.
- **Lettering is a dead draw.** "GOLDEN CRUST" came back letter-exact in all nine shopfront arms on **both** LoRAs - a flat recolour, a rainy evening and a flat-vector restyle included. Neither one loses the thing MOSS is best at.
- **Speed is near enough the same**: about 20 s per picture on a 12 GB card, against about 18 s for the original.

**495 MB** on top of the three base weights the MOSS-Image pack already downloads, so if you have that pack this is a small extra. 30 steps, CFG 1. **Beta engine only** for now (Settings > Updates > beta, app 1.76.2 and up) - it needs ComfyUI 0.43.0, same as the other two edit cards.

Good to know:
- **CFG is fixed at 1 on purpose.** The author's model card recommends CFG 3 with 50 steps. We ran that: on these INT8 weights it costs 2.4x the time and visibly drifts faces - washed skin with freckling the source does not have, blown golden hour, the watercolour face fading to a pale sketch. The author states the pipeline wants roughly 20 GB in bf16, so that is very likely an INT8 effect rather than anything wrong with their recipe - but on the weights this card ships, CFG 1 is the better picture, so there is no slider.
- **Running it yourself in ComfyUI? Feed the reference at full size.** The model card mentions references being downscaled to 384 px; pre-shrinking here destroys lettering - at a 384 max edge the sign came back as gibberish, at 512 the shot was reframed. The same is true of the original edit card. Our graph scales the reference to the output size.
- **Say what to keep, not just what to change** - same as the other edit cards. "Change only the dark green paintwork to deep navy blue. Keep both signs, their lettering, the bread in the window and the brickwork exactly as they are."
- **Pick the aspect ratio that matches your picture.** Another ratio centre-crops it first and the edit gets looser.
- armV6 is published too; the author says it did not improve on v5, so the card ships v5.
- This is an **unofficial community fine-tune** of MOSS-Image-SFT, not an OpenMOSS release.

Thanks to akhaliq for the LoRA (https://huggingface.co/akhaliq/MOSS-Image-Edit-HQ), chinoll for the original edit LoRA this was measured against (https://huggingface.co/chinoll/Moss-Image-Edit), OpenMOSS for MOSS-Image, and Comfy-Org for the repacks and the native ComfyUI support both cards run on.
