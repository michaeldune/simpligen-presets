:sparkles: **New pack: MiniMax H3 Emotion TTS Lip-Sync** (needs SimpliGen 1.59.2)

Type the line, pick the mood, get the character saying it. **IndexTTS 2.5** clones the voice you put in the audio slot and speaks your quoted dialogue with the emotion you name, and **MiniMax H3** lip-syncs your reference character to that speech, all in one generation.

How it works:
• **Audio slot** = a voice sample, 3-10 s of clean speech. It is cloned, not lip-synced.
• **Reference images** = the character(s), up to nine, same as the Lip-Sync pack.
• **Prompt** = a normal H3 shot description with the line in double quotes. The first quoted run is what gets spoken.
• **Emotion** = an optional `[emotion: angry, clipped]` style tag anywhere in the prompt, plain words. Without it the mood is copied from the voice sample.

Verified on a 12 GB 4070 Ti: a 6 s angry line at 864x480 with one reference image, ~3 min end to end, and the output transcribes word-perfect against the written line with the mouth on the words. The preset adds the `<Audio 1>: fully_copy` binding for you; that line is what makes H3 reproduce the speech instead of inventing its own words.

:warning: Things to know
• **Update to SimpliGen 1.59.2 first.** IndexTTS keeps its weights in folders with a dot in the name, and older app versions silently skipped every one of the 26 files. Thanks to SharMystic for turning that around in a day. Verified today on a clean install: the app downloads all 7.7 GB itself and the preset runs.
• Adds the comfyui-indextts25-T8 node, which pins the engine's transformers to the 4.x line. 1.59.2 now holds it there on purpose, so other packs keep working.
• Fresh install needs ~49 GB free on your models drive (H3 pruned INT8 + Turbo LoRA + TTS). If you already run the Lip-Sync pack it is only the 7.7 GB of TTS weights.
• English lines only. Keep it to one or two sentences per shot; a line longer than the duration gets cut.
• If the first run cannot find the TTS weights, restart SimpliGen once. The models/TTS folder is registered at engine start.

:shopping_cart: Store: `Community — MiniMax H3 Emotion TTS Lip-Sync`, syncs within a few hours.

---

:sparkles: **Krea 2 Finetunes 1.1.0: Kreamania V8 joins the pack**

A fourth card in the trained-checkpoints pack: **Adel_AI's Kreamania Variant 8**, a refinement trained directly on Krea 2 (not a merge, and not derived from the earlier Kreamania variants). The author's two goals for V8 are rebalanced, more volumetric lighting and a real cut in Krea 2's wet-skin look, with NSFW left intact. Both held in our test: matte, freckled skin under raking window light, and dust and mist that read as volume, ~55 s at 2 MP on a 4070 Ti.

• Ships at the author's 10 steps / CFG 1. Same native ~2 MP sizes and the same gated Upscale slider (1.1-2x adds a 4-step detail-refine pass) as the rest of the pack.
• fp8 build, 12.8 GB. Shares the encoder and VAE with every other Krea 2 preset, so that file is the whole cost.
• Honest caveat from the author: a random artifact has persisted since V7 and a different seed clears it.
• Sits next to FinalCut v2, which exists for the same matte-skin reason. Kreamania is the warmer, more volumetric of the two; FinalCut the cooler and flatter. Try both on the same seed.

Existing cards are untouched. If you have the pack, take the 1.1.0 update in the store and the new card appears.

:shopping_cart: Store: `Community — Krea 2 Finetunes` 1.1.0, syncs within a few hours.
:inbox_tray: Zips: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest
:books: Catalogue: <https://github.com/michaeldune/simpligen-presets#readme>

Credit to Adel_AI for Kreamania, T8mars for the IndexTTS 2.5 ComfyUI nodes and the Comfy mirror of the weights, and index-tts for the model.
