Use the YuE2 Song + Album Art card from the Song + Album Art pack in the Preset Store. I tested the LoRA tex3dtex linked on that card this morning and it works:

1. Add the LoRA with base model YuE2, using this direct link: https://huggingface.co/Mothersuperior/YuE2-instrumental-cot-full-loras/resolve/main/ar_lora_inst_v3abc_comfyui.safetensors
2. Pick it in the card's LoRA slot at strength 1. It has no trigger word.
3. Prompt: just the style as tags, for example "indie pop, warm acoustic guitar, bright piano, soft drums, electric bass, 100 bpm, uplifting".
4. Turn Character Dialogue on and put only this in it:
```
[instrumental]
```
5. Set Duration high. The LoRA likes long songs, and at 120 s one of my takes got cut off at the end.

Same prompt and seeds with and without the LoRA: without it YuE2 sang made-up lyrics on both seeds, with it both songs had no voice at all. Fair warning, the results sound fine but repeat themselves a lot, so I'd treat them as background music rather than a track to listen to on its own. You can also list sections in Dialogue instead, one per line (`[intro]`, `[verse]`, `[chorus]`, `[outro]`), but keep notes like "guitar solo" out of the brackets.

Without the LoRA, this also worked once for me: start the style with "Instrumental," end it with "-vocals, -singing, -choir", and put `[intro]`, `[instrumental]`, `[outro]` in Dialogue on separate lines.

The song arrives as an MP4 with album art, because SimpliGen has no audio-only output yet. Any video editor or ffmpeg will pull the audio out.
