Good question, and it wasn't written down anywhere you could see. With the next store update, every community card's description ends with a "Model format" line, so the info button tells you straight away.

I read each model file's own header to get these, not its file name, because names lie: three files called "ConvRot" (Ray Krea2 Mid Aesthetic and both Ideogram 4 Instant cards) turned out to be plain int8. Those cards say so.

What the labels mean:
- **int8 ConvRot**: int8 with a rotation applied before quantizing, meant to keep more of the original quality than plain int8 at the same size. The official H3 files use it, as do most H3, LTX 2.5, MOSS and Qwen-Image 2.1 cards and many Krea 2 finetunes.
- **plain int8**: int8 without the rotation.
- **fp8**: 8-bit float weights.
- **bf16 / fp16, not quantized**: full-size weights. Most SDXL, Pony, Illustrious, SD 1.5 and Anima cards.
- **GGUF Q8_0 / Q4_0 / Q4_K_M**: GGUF quants. Q8 is close to the original, Q4 is smaller and loses more.

A few are mixed and say so (for example REDgraft is mostly int8 ConvRot with some 4-bit layers). Cards that run two big models, like the song + album art cards, name both.
