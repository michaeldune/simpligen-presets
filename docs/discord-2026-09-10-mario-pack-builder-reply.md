# Reply draft — MarioOliveira, "preset/pack builder" thread (2026-09-10)

Thanks Mario, this is exactly the kind of gap report I wanted. I read both of your builders and checked what the app actually does, and you are right on all three counts: the guide had no upscale section, it never said where each `{{placeholder}}` comes from, and the "corrupted" toast tells you nothing.

**Guide v5 is up** (same link): https://github.com/michaeldune/simpligen-presets/blob/master/CUSTOM-PRESET-AUTHORING-GUIDE.md

New §8 "Tool presets: Upscale / Enhance" covers what you asked for:
- the two fields that make a preset show up on the Enhance page (`"kind": "tool", "tool": "upscale"`) — without them the preset lands in the generation pickers and Enhance never lists it
- the full image/video tool schema (`supportedScales` vs `targetResolutions`, `maxOutputPixels`, `acceptsReferenceImages: {max: 1}` for pictures, `{{video_file}}` for clips, the `requirements.gpu` gate)
- §8.2, the part an AI cannot guess: the app substitutes ONE flat context = every key in your `image`/`video` block + the job's `scale`/`targetResolution` + the uploaded filenames + computed sizes. So any field you put in the block becomes `{{that_field}}` — but only the declared model keys (`upscaler`/`checkpoint`/`unet`/`clip`/`vae`/`extraModels[]` …) are downloaded. A filename that is only in the workflow is never fetched, and on a clean PC the job dies with "Value not in list" before it starts. (That exact bug was in my own Krea Flux pack until this morning.)
- a "preset types at a glance" table (generate image / edit / video / upscale image / upscale video), a minimal restoration graph, and a fresh-install test recipe

**About "A preset pack is corrupted":** that message means a `.json` file in the presets folder is not valid JSON at all — the schema is not even looked at yet. Export your logs (Settings → Export logs) and search the newest `session-*.log` for `is CORRUPTED`; that line names the file and the parser error. Usual culprits: a UTF-16 file (`Out-File` in Windows PowerShell 5.1 writes UTF-16 by default), a BOM, a UI-format ComfyUI export renamed to `.json`, or a builder project/save file sitting next to the packs. Every `*.json` directly in that folder is parsed as a pack. Send me that log line and I will tell you which one it is.

**One thing in your v3 installer to fix:** `install-<pack>.ps1` reads the pack with `Get-Content` in Windows PowerShell 5.1 without `-Encoding UTF8`, then re-saves it through `ConvertTo-Json`. I ran that path on one of my packs: the JSON stays valid, but every non-ASCII character is mangled (`—` becomes `â€”`, icons become `âœ¨`). Read with `-Encoding UTF8` or do the `previewImage` rewrite in a real JSON library. Otherwise your v3 emits the right upscale shape (`kind`/`tool`, `image`/`video` block, `supportedScales`, `targetResolutions`, `maxOutputPixels`, `extraModels`, `extensions`) — the remaining failures are going to be a placeholder with no source, or a model the pack does not declare, both covered in §8.2 and the new failure-guide rows.

There is also a new script in the repo, `tests/check_declared_weights.py`: point it at a pack folder and it lists every weight filename a workflow uses that the manifest does not declare.

For Adonis specifically: if you post the API-format workflow and the model links, I will turn it into a pack and ship it in the community repo with credit.
