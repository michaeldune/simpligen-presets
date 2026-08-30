# MiracleIn NSFW (Klein 9B) — retired 2026-08-30

This preset was removed from the **Flux 2 Klein** pack. Nothing about it is
broken; its checkpoint just stopped being downloadable by a program.

## What happened

On 2026-08-27 the model's author enabled Civitai **paid access** on
[model 2453960](https://civitai.com/models/2453960) — and on *every* version of
it, 1.0 through 4.3, not just the one we shipped. The file now costs 10,000
Buzz.

SimpliGen's installer cannot express that. It reads Civitai's payment refusal as
a rejected API key, asks you for the key again, reports it saved successfully,
and never begins the download. Re-entering a fresh read-only key changes
nothing, because the key was never the problem.

There is no free version of this model left to point the preset at, so it cannot
stay in a one-click pack.

## Installing it by hand

You need the checkpoint first: `miracleinNSFWGeneration_30Bf16Fp8.safetensors`
(8.46 GB, model **2453960**, version **2986788**). Buy it with Buzz, or use a
copy you already have. Put it in your `diffusion_models` folder.

Then:

1. Rename `miraclein-nsfw-9b.retired-preset.json` to
   `miraclein-klein-pack.json`.
2. Copy it into `%APPDATA%\simpligen\presets\`.
3. Copy `flux2-klein-9b.json` into `%APPDATA%\simpligen\presets\workflows\`
   (it is the same workflow the live Klein presets use — if you already have the
   Flux 2 Klein pack installed, it is there already and you can skip this).
4. Copy `miraclein-nsfw-9b.jpg` into `%APPDATA%\simpligen\presets\previews\`.
5. Open the pack JSON and change `previewImage` to the absolute form SimpliGen
   expects:
   `local-file:///C:/Users/<you>/AppData/Roaming/simpligen/presets/previews/miraclein-nsfw-9b.jpg`
6. Restart SimpliGen.

It also still needs the shared Flux 2 companion models the Klein pack uses — the
Qwen3-8B encoder and the Flux 2 VAE. If the Flux 2 Klein pack is installed you
already have them.

## If the model ever goes free again

Move the preset back into `flux2-klein-pack.json`, restore the preview to
`previews/`, drop the RETIRED note from its description, bump the pack version,
and delete this folder.
