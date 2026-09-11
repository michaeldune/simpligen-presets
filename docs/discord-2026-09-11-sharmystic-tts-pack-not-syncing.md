# Note draft — store never publishes minimax-h3-tts-lipsync-pack (to Sharmystic, 2026-09-11)

Hi Sharmystic, thanks for 1.60.0, both fixes confirmed on my side (Singularity cards flipped without the 1.0.1 pin, and the pin warning is exactly what I wanted).

One more store question. Of my 43 packs the store lists 42; the only one it has never published is `minimax-h3-tts-lipsync-pack` (MiniMax H3 Emotion TTS Lip-Sync). It has been on master since 09-09, I bumped it to 1.0.1 last night in case the sync keyed on id+version after its 09-05 withdrawal, and the sync that followed picked up three other pack updates but still skipped this one. Nothing in the sync is visible to me, so I'm guessing at the reason.

What's unusual about it: 28 `extraModels` entries whose `dir` values contain dots, e.g. `TTS/IndexTTS-2.5`, `TTS/IndexTTS-2.5/hf_cache/bigvgan`, `TTS/IndexTTS-2.5/qwen0.6bemo4-merge`. That is the IndexTTS 2.5 folder layout the node expects. The app accepts interior dots since 1.59.2 (the `SAFE_DIR_SEGMENT` change), and a fresh install through the app downloads all 26 files fine. My guess is the store still validates `dir` with the pre-1.59.2 rule and drops the pack silently. Other candidates: `sizeGB: 49`, or a per-pack cap on extraModels count.

Could you check what the sync logs for that pack id? If it's the dotted-dir rule, the store validator just needs the same relaxation the app got; I'd rather not rename the folders since the node hard-codes them. And a visible rejection reason in the sync report would save this round trip next time.
