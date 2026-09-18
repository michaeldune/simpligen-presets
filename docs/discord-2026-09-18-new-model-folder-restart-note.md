HELD - not sent. Draft for Sharmystic (2026-09-18).

---

Hey Sharmystic, a small first-run gap, found while adding a YuE2 Cover Song card to the Song + Album Art pack.

The card needs SheetSage2 (`AudioEncoderLoader`), which lives in `models/audio_encoders`. That folder isn't one of
SimpliGen's standard model folders, so it's declared as an `extraModels` entry with `"dir": "audio_encoders"`.
Preparing the preset downloaded it fine (`F:\SimpliGen\models\audio_encoders\sheetsage2_bf16.safetensors`,
byte-exact), and the card showed as ready. But the engine didn't restart after the download, and
`extra_model_paths.yaml` is only rebuilt when the engine starts. So the new folder wasn't mapped and
`AudioEncoderLoader` listed nothing. A render at that point would fail with "Value not in list". After one app
restart the yaml gained `audio_encoders: audio_encoders/` and everything worked. Checked on 1.63.1.

Same thing we saw with the TTS pack's `TTS` folder. Possible fixes: restart the engine after a download that creates
a new top-level model folder, or rebuild the yaml and ask the engine to rescan the folder lists before the first
render. For now the card tells people to restart once after the first download.
