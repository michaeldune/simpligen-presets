:rocket: **New pack: MiniMax H3 (FastH3 8-Step V2)** (2 cards, T2V + I2V) — **beta engine only for now**

FastVideo's FastH3 is a data-free DMD2 distillation of MiniMax H3 trained with VSA block-sparse attention: video and stereo audio in eight transformer forwards, no CFG. This pack runs Comfy-Org's int8 repack (20.6 GB, its own checkpoint, shares the text encoder and VAEs with the H3 pack) on ComfyUI's official template graph: sigma shift 10/3, comfy-kitchen attention, VSA keep 10%.

It needs the block-sparse attention node from engine **0.36**, which is on the **beta channel** today: Settings > Updates > beta, take the engine update, then the pack appears in the Store. On the stable engine the Store hides it, on purpose.

Bake on a 4070 Ti (5 s at 480p, same seeds and prompts as TaoMate 3-Step and Turbo Accelerated at ten steps): sharper on every scene, and unlike the three-step LoRA it keeps real motion in the action shot. About 80 s per five-second clip, the same wall as the 10-step turbo. Dialogue verbatim with the mouth closing on the last word; image-to-video held the presenter from the still. Three seeds, so treat it as a strong first read, not a verdict.

Text and image to video only; Ref2VA was not distilled. Steps slider 6 to 10. Store picks it up on its next sync.

:inbox_tray: Zip: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest
