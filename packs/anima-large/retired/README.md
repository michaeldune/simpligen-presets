# Pawhibited Anima 2.9B v1.0 - retired 2026-11-18

This card was removed from the **Anima Large** pack in 1.0.3. The card itself
works; its checkpoint can no longer be downloaded.

## What happened

The model (Civitai model **3020561**, version **3429588**, by Meiyue with
CatgirlContraband) was deleted from Civitai, along with the CatgirlContraband
account. The download URL, the model page and the version page all return 404,
and the store's sync reported "pin resolution failed" for the pack from
2026-11-17 onwards.

There is no other source. comfy.icu and civitaiarchive still list the file
(`Pawhibited.safetensors`, sha256
`422436633524c29a9f2f8a32f57b9699f939e5746c0d7ecd5a3bdd5139585b22`), but their
only download link points back at the deleted Civitai URL. civitaiarchive tracks
copies by hash, so a re-upload would show up there:
https://civitaiarchive.com/models/3020561?modelVersionId=3429588

## Installing it by hand

You need the checkpoint first: `pawhibitedAnima29b_v10.safetensors` (5.84 GB,
the sha256 above). Use a copy you already have and put it in your
`diffusion_models` folder.

Then:

1. Rename `pawhibited-anima-29b-v1.retired-preset.json` to
   `pawhibited-anima-pack.json`.
2. Copy it into `%APPDATA%\simpligen\presets\`.
3. Copy `pawhibited-anima-29b-v1.json` into
   `%APPDATA%\simpligen\presets\workflows\`.
4. Copy `pawhibited-anima-29b-v1.jpg` into
   `%APPDATA%\simpligen\presets\previews\`.
5. Open the pack JSON and change `previewImage` to the absolute form SimpliGen
   expects:
   `local-file:///C:/Users/<you>/AppData/Roaming/simpligen/presets/previews/pawhibited-anima-29b-v1.jpg`
6. Restart SimpliGen.

It also needs the Qwen 0.6B text encoder and Qwen-Image VAE that every Anima
card shares. If any Anima pack is installed you already have them.

## If the model comes back

Move the card back into `anima-large-pack.json`, the preview back to
`previews/` and the workflow back to `workflows/`, restore its name in the pack
description and the README row, bump the pack version, and delete this folder.
