# SimpliGen preset packs: agent instructions

This repository holds community preset packs for [SimpliGen](https://www.simpligen.io/), a desktop app that runs ComfyUI workflows locally. A **pack** is one JSON manifest plus its workflows and preview pictures, in `packs/<slug>/`. A **preset** is one entry in a pack, the thing a user picks in the app. Always say "preset" to the user.

The reference for everything below is `CUSTOM-PRESET-AUTHORING-GUIDE.md` (**the guide**). It is long; read the sections each step names, when you reach that step.

## Making a preset for the user

The usual request is "make me a SimpliGen preset for this model or workflow". SimpliGen has no import button: a preset exists only as a pack file the app loads at startup. Work through these steps in order. Each step ends at its **Done when** line.

1. **Find out what they want.** Ask for the model (a Civitai or Hugging Face link, or a file they already have) or a ComfyUI workflow they exported in API format (ComfyUI: Workflow > Export (API)), whether it makes pictures or video, and what it should be good at.
   Done when you have the exact model file name, a direct download URL for every file the workflow loads, and the media type.
2. **Research the model** (the guide §3). Read the base architecture from the file's safetensors header, not its name, and take sampler, steps, CFG, resolution and prompt style from the creator's published settings.
   Done when you can name the architecture and every generation setting, each with its source.
3. **Start from the nearest working pack** (the guide §2, §4). Pick a pack in `packs/` with the same architecture and media type, read its manifest and workflow, and copy their shape.
   Done when you have named the pack you are copying and why it matches.
4. **Write the pack** in a new folder `packs/<slug>/`, with a slug no existing pack uses:
   - the workflow in ComfyUI API format with `{{placeholders}}` (the guide §4, §8.2), the `simpligen_lora_1` LoRA node (§5), and every custom node declared with a `pinnedCommit` (§7.6);
   - the manifest (§6 for images, §7 for video) with a `promptFamily` (§6.4), a description written for a person choosing a preset, ending in a `Model format:` line (§6.5);
   - one 640x640 JPEG preview per preset (§11), ideally rendered by the preset itself after step 7, so a placeholder is fine at first.
   Done when every file the manifest names exists and both JSON files parse.
5. **Validate** (the guide §13). Run, from the repo root:
   - `python tests/check_declared_weights.py` (or `uv run python ...`): must exit 0.
   - `python tests/check_declared_extensions.py` with SimpliGen open (it asks the engine on `127.0.0.1:8199`): must print `gaps: 0`.
   Check that no JSON file starts with a UTF-8 BOM.
   Done when all three pass.
6. **Install it locally** (the guide §1, §12). Read SimpliGen's data folder (`data_dir` in the `settings` table of `%APPDATA%\simpligen\simpligen.db`; if it is not set, the folder is `%APPDATA%\simpligen`). Copy the manifest to `<data_dir>\presets\`, the workflows to `<data_dir>\presets\workflows\` and the previews to `<data_dir>\presets\previews\`, then change each installed `previewImage` to an absolute `local-file:///` URL. Ask the user to quit and reopen SimpliGen.
   Done when the preset is listed in the app (the user sees it, or your SimpliGen MCP tools list it), and the newest `%APPDATA%\simpligen\logs\session-*.log` has a higher `Loaded N preset packs` count than before. A pack that fails to load shows in the Preset Store with the file name and the reason.
7. **Generate once.** The user opens the preset and clicks **Install preset locally**, which downloads the models from the URLs in the manifest. Then run one generation: through SimpliGen's MCP `generate` tool if the user has connected you to SimpliGen (preset id `<packId>:<presetId>`, settings inside `options`), otherwise by asking the user to press Generate.
   Done when a finished picture or video exists and you have looked at it.

Report what you built, where the files are, and how long the test took. A file copy is not a finished preset; step 7 is.

## Guardrails

- **Always:** write JSON as UTF-8 without a BOM, through a JSON library rather than text replacement; keep the source copy (relative `previews/` paths) and the installed copy (absolute paths) in step.
- **Ask the user first:** before installing custom ComfyUI nodes, changing any pack you did not create, or running anything that downloads more than a few GB outside the app.
- **Leave alone:** the app's own files and the official packs in the presets folder (they carry `i18nId` or `characterContract`). Commit, push or open a pull request only when the user asks for it.

## Traps

- **Every placeholder must be filled.** A `{{name}}` the manifest does not supply fails the run with `missing render settings {{name}}`; the guide §8.2 lists where each value comes from.
- **Numbers stay bare in the workflow** (`"width": {{width}}`), text stays quoted (`"unet_name": "{{unet}}"`). That file is not valid JSON until substituted, so a script that edits it must replace placeholders with sentinels before parsing (the guide §2.6).
- **Text encoders go in `clip\`**, not `text_encoders\` (the guide §1).
- **A model the manifest does not declare is never downloaded**, so the preset works on your machine and fails on everyone else's with `Value not in list`.
- **A new or changed manifest needs a full app restart**; a changed workflow file does not.
