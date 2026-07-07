# SimpliGen Custom Local Preset Authoring Guide (v2)

A practical guide for building **local** SimpliGen preset packs: researching an image model, writing the preset pack + ComfyUI **API-format** workflow, adding a thumbnail and LoRA support, installing safely on Windows, and verifying the result. Written for a capable coding agent or a hands-on user.

A preset is **done** only when SimpliGen loads the pack, shows its thumbnail, and a test generation produces an image — not when files are copied. Examples assume a ~12 GB VRAM GPU; adjust `requirements` and step counts for your hardware.

---

## 1. Locations
```text
Installed packs:      %APPDATA%\simpligen\presets\<pack>.json
Installed workflows:  %APPDATA%\simpligen\presets\workflows\<id>.json   (shared across packs)
Installed thumbnails: %APPDATA%\simpligen\presets\previews\<id>.jpg     (shared)
Engine models root:   %APPDATA%\simpligen\engine\models\
                        checkpoints\  diffusion_models\  clip\  vae\  loras\  ...
Logs:                 %APPDATA%\simpligen\logs\session-*.log
Engine model-path map: %APPDATA%\simpligen\engine\ComfyUI\extra_model_paths.yaml
```
- Keep editable **source copies + installers** in one folder per pack, **outside** the app's program directory (`%LOCALAPPDATA%\Programs\simpligen\...`) — that directory can be reset on app updates. Anywhere stable works (a docs folder, another drive, etc.).
- `extra_model_paths.yaml` maps **both** `text_encoders:` and `clip:` to the **`clip\`** folder, so text encoders (e.g. `qwen_3_06b_base.safetensors`) live in `engine\models\clip\`, not `text_encoders\`. Check there when validating encoders.
- Do not modify `resources\app.asar` or official packs (those carry `i18nId`/`characterContract` fields). Custom packs are just JSON in `%APPDATA%\simpligen\presets`.
- If the system drive is tight, model folders can be relocated to another drive via Windows **directory junctions** (`mklink /J`) — transparent to the app, which keeps using the normal `engine\models\...` paths.

---

## 2. Required agent behavior
1. Inspect an existing working pack of the same family before writing a new one.
2. Verify exact model version, base architecture, filename, VAE/encoder/custom-node needs, CLIP skip, sampler/scheduler, steps/CFG, prompt conventions, native resolutions.
3. Prefer the creator's published generation metadata over generic assumptions.
4. One self-contained source folder per pack.
5. Use a ComfyUI **API-format** workflow (flat node map), not a UI graph export.
6. Validate every JSON with a parser.
7. Install via an idempotent Windows installer.
8. Write JSON as UTF-8 **without BOM**; preserve Unicode/emoji.
9. Add the LoRA marker node (§5) and a `tagline` (§6) to every preset.
10. Confirm model/pack/workflow/thumbnail all exist; restart SimpliGen; check the newest log.
11. Don't claim success on file copy alone — confirm the pack loads and ideally that a test generation completes.

---

## 3. Research the model
For Civitai, the public API is easier to parse than the web page. (Note: Civitai **requires auth to download** model files — download via the site/logged-in client; HuggingFace files are open and can be fetched directly.)
```powershell
$m = Invoke-RestMethod 'https://civitai.com/api/v1/models/<ID>'
$ver = $m.modelVersions | Select-Object -First 1
$ver | Select-Object name, baseModel
$ver.files | ? {$_.type -eq 'Model'} | Select-Object name, @{n='GB';e={$_.sizeKB/1MB}}
$ver.images | ? {$_.meta.sampler} | Select-Object -First 3 -Expand meta   # sampler/steps/cfg/clip skip
$ver.images | ? {$_.type -eq 'image'} | Sort-Object nsfwLevel | Select -First 1 -Expand url  # cleanest thumb
```
Record: base model, exact filename, full-checkpoint vs UNet-only, VAE/encoder/custom-node needs, CLIP skip, sampler/scheduler, steps/CFG, native sizes, recommended prompt prefix + negative. Image metadata is usually the best source for settings.

### Detect architecture from the safetensors header (don't trust the name)
Read the header (first 8 bytes = little-endian header length, then that many bytes of UTF-8 JSON) and inspect key prefixes:
- `conditioner.embedders.*` + `first_stage_model.*` → **SDXL / Illustrious / Pony** full checkpoint (~6.5 GB).
- `cond_stage_model.*` + `first_stage_model.*` → **SD 1.5** full checkpoint (~2 GB).
- `*.blocks.*adaln_modulation_cross_attn*` (prefix `net.` or `model.diffusion_model.`) → **Anima / Cosmos** UNet-only (~4 GB); load via `UNETLoader`.
- `model.diffusion_model.blocks.*attn.*weight_scale` → **Krea-2** DiT (fp8 ~12 GB).
- Flux / Z-Image / Qwen / Boogu are their own UNet/DiT families.

---

## 4. Workflow families (ComfyUI API format)
SimpliGen substitutes these placeholders at generation time:
```text
{{checkpoint}} {{unet}} {{clip}} {{vae}} {{prompt}} {{negative_prompt}}
{{width}} {{height}} {{seed}} {{steps}} {{cfg}} {{denoise}}
```
Any extra `image.<key>` field in the pack is also exposed as `{{key}}`. Sampler names are machine ids: `euler`, `euler_ancestral`, `dpmpp_2m`, `dpmpp_2m_sde`, `dpmpp_2s_ancestral`, `dpmpp_sde`, `er_sde`. Schedulers: `normal`, `karras`, `simple`, `exponential`, `lcm`.

**4.1 Conventional checkpoint** (most SD 1.5 / SDXL): `CheckpointLoaderSimple` → encoders → `KSampler` → `VAEDecode` (vae from `["4",2]`) → `SaveImage`.

**4.2 CLIP Skip 2** (Illustrious, Pony, most anime): insert between CLIP and both encoders, and route both encoders to it:
```json
"10": { "inputs": { "stop_at_clip_layer": -2, "clip": ["4", 1] }, "class_type": "CLIPSetLastLayer" }
```

**4.3 External VAE** (e.g. SD 1.5 anime, which looks washed-out on its baked VAE → use `kl-f8-anime2`): add `VAELoader { "vae_name": "{{vae}}" }`, point `VAEDecode.vae` at it, and set `"vae"` in the pack.

**4.4 UNet + encoder + VAE (Anima / Cosmos):**
```text
UNETLoader → ModelSamplingAuraFlow {shift:3} → KSampler (er_sde / simple)
CLIPLoader {type:"stable_diffusion"}  (Qwen 0.6B encoder)
VAELoader  (Qwen-Image VAE)
Positive text preamble: "You are an assistant designed to generate <high quality / anime> images based on textual prompts. <Prompt Start>\n{{prompt}}"
```
Files go in their own folders: UNet → `diffusion_models\`, encoder → `clip\`, VAE → `vae\`. Turbo/distilled variants: ~12–16 steps, CFG 1.

**4.5 Krea-2 DiT:** `UNETLoader {weight_dtype:"default"}` + `CLIPLoader {type:"krea2"}` (Qwen3VL encoder) + `VAELoader` (Qwen-Image VAE); positive `CLIPTextEncode` → `ConditioningZeroOut` for the negative (CFG 1); `KSampler euler / simple, 8 steps, cfg 1`. No `ModelSamplingAuraFlow`.

**4.6 Two-pass hi-res:** base KSampler → `VAEDecode` → `ImageScaleBy {lanczos, 1.5}` → `VAEEncode` → 2nd KSampler (denoise ~0.1, ~4 steps) → `VAEDecode` → SaveImage.

**4.7 Custom nodes:** clone the repo into `engine\ComfyUI\custom_nodes\` (the bundled engine loads custom nodes; rgthree, KJNodes, RES4LYF ship by default). SimpliGen has no custom UI slider, so to expose a node parameter you can repurpose the `steps`/`cfg` slider (route `{{cfg}}` into the node param and hardcode the sampler cfg).

**Minimal checkpoint workflow** (add the LoRA marker from §5):
```json
{
  "4": { "inputs": { "ckpt_name": "{{checkpoint}}" }, "class_type": "CheckpointLoaderSimple" },
  "5": { "inputs": { "width": "{{width}}", "height": "{{height}}", "batch_size": 1 }, "class_type": "EmptyLatentImage" },
  "6": { "inputs": { "text": "{{prompt}}", "clip": ["4", 1] }, "class_type": "CLIPTextEncode" },
  "7": { "inputs": { "text": "{{negative_prompt}}", "clip": ["4", 1] }, "class_type": "CLIPTextEncode" },
  "3": { "inputs": { "seed": "{{seed}}", "steps": "{{steps}}", "cfg": "{{cfg}}", "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": "{{denoise}}", "model": ["4",0], "positive": ["6",0], "negative": ["7",0], "latent_image": ["5",0] }, "class_type": "KSampler" },
  "8": { "inputs": { "samples": ["3",0], "vae": ["4",2] }, "class_type": "VAEDecode" },
  "9": { "inputs": { "filename_prefix": "<preset-id>", "images": ["8",0] }, "class_type": "SaveImage" }
}
```

---

## 5. LoRA support — the `simpligen_lora_1` marker (add to every preset)
SimpliGen shows the user LoRA picker only if the workflow contains a node with **id `simpligen_lora_1`**, class **`Power Lora Loader (rgthree)`**, titled "SimpliGen User LoRAs". Place it right after the model/clip source; route everything downstream through it (transparent passthrough when no LoRA is selected).
```json
"simpligen_lora_1": {
  "inputs": {
    "PowerLoraLoaderHeaderWidget": { "type": "PowerLoraLoaderHeaderWidget" },
    "➕ Add Lora": "",
    "model": ["4", 0],
    "clip":  ["4", 1]
  },
  "class_type": "Power Lora Loader (rgthree)",
  "_meta": { "title": "SimpliGen User LoRAs" }
}
```
Wiring: redirect every consumer of the checkpoint model output `[ckpt,0]` → `["simpligen_lora_1",0]` and clip output `[ckpt,1]` → `["simpligen_lora_1",1]`; the marker itself points back to the loader. For **UNet families**, the marker takes model from `UNETLoader[,0]` and clip from `CLIPLoader[,0]`. VAE is not routed through the marker.
- Preserve the `➕` key — write JSON with UTF-8 (no BOM), don't let it get mangled.
- Subgraph-namespaced workflows (node ids like `75:70`, e.g. some Flux `SamplerCustomAdvanced` graphs) don't take this flat marker cleanly — wire LoRA there manually in the graph editor or skip.
- LoRA compatibility: SDXL-family LoRAs (incl. Illustrious, Pony) load on any SDXL/Illustrious/Pony preset (effect varies off the native base). They do NOT load on SD 1.5 / Krea-2 / Anima / Z-Image. There is no reliable cross-architecture LoRA conversion — retrain for the target base.

---

## 6. Pack schema
```json
{
  "id": "<slug>-pack",
  "name": "<display name>",
  "version": "1.0.0",
  "author": "<creator>",
  "description": "<desc>",
  "tags": ["Local", "<family>", "<style>"],
  "presets": [{
    "id": "<preset-id>",
    "name": "<display name>",
    "tagline": "<short plain line shown under the name in the store/pickers>",
    "icon": "✨",
    "previewImage": "previews/<preset-id>.jpg",          // SOURCE = relative; INSTALLED = local-file:/// absolute
    "description": "<short desc>",
    "tags": ["<style>", "<family>", "Local"],
    "enabled": true,
    "template": "sdxl",                                    // "booru" for danbooru-tag anime models
    "ui": { "visibleFields": ["content","aspectRatio","shotType","environment","lightingSource","atmosphere"] },
    "image": {
      "supports": ["local"], "provider": "comfyui",
      "displayModel": "<name>", "baseModels": ["sdxl"],
      "workflow": "workflows/<preset-id>.json",
      "checkpoint": "<file>.safetensors",                  // OR "unet" + "clip" + "vae" for UNet families
      "checkpointUrl": "https://civitai.com/api/download/models/<verId>",  // or unetUrl/clipUrl/vaeUrl
      "steps": 30, "cfg": 7, "denoise": 1,
      "negativePrompt": "<neg>",
      "resolutionOverrides": {
        "1:1": {"width":1024,"height":1024}, "2:3": {"width":832,"height":1216}, "3:2": {"width":1216,"height":832},
        "3:4": {"width":896,"height":1152}, "4:3": {"width":1152,"height":896},
        "9:16": {"width":768,"height":1344}, "16:9": {"width":1344,"height":768}
      },
      "controls": { "steps": {"min":20,"max":45,"step":1}, "cfg": {"min":3,"max":10,"step":0.5} },
      "requirements": { "minVramGB":8, "recommendedVramGB":12, "minRamGB":16, "sizeGB":6.5 }
    }
  }]
}
```
- **Resolutions:** SD 1.5 = 512-based (512/512, 512/768, 768/512); SDXL/Illustrious/Pony = 1024-based. All dimensions divisible by 8. Use the creator's buckets when published.
- **`template`:** `booru` for tag-trained anime, `sdxl` for natural language.
- Filenames, pack id, preset id, workflow reference, and installer destinations must agree exactly (lowercase hyphenated ids).

---

## 7. Reference settings by family (examples)
| Family | Sampler / scheduler | Steps | CFG | Notes |
|---|---|---:|---:|---|
| SDXL realism | dpmpp_2m / karras (or dpmpp_2m_sde) | 30 | 6–7 | no clip skip, baked VAE, natural language |
| Illustrious | euler_ancestral / normal | 28–30 | 5–6 | CLIP Skip 2, quality-tag prefix |
| Pony V6 | euler_ancestral | 25 | 7 | CLIP Skip 2, score-tag prefix |
| SD 1.5 anime | dpmpp_2m / karras | 30 | 7 | CLIP Skip 2, external kl-f8-anime2 VAE, 512-base |
| Anima (Cosmos) | er_sde / simple, ModelSamplingAuraFlow shift 3 | 16 (turbo ~12) | 1 | UNet + Qwen 0.6B encoder + Qwen-Image VAE, preamble |
| Krea-2 turbo | euler / simple | 8 | 1 | DiT, Qwen3VL encoder, Qwen-Image VAE, ConditioningZeroOut negative |

---

## 8. Prompt conventions
- **SDXL realism:** pass `{{prompt}}` directly; put defect terms in `negativePrompt`.
- **Illustrious anime:** `masterpiece, best quality, amazing quality, ultra detailed, ... {{prompt}}` + CLIP Skip 2.
- **Pony V6:** `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, {{prompt}}` (photoreal Pony mixes often need NO score tags). Don't force a `source_*` tag globally.
- **SD 1.5 anime:** `masterpiece, best quality, highly detailed, anime, {{prompt}}`.
- **Anima/Krea:** use the model preamble (§4). Don't apply it to plain SD/SDXL checkpoints.
- **Figure/age safety:** avoid words like "tiny" (with fairy/wings themes they skew childlike); add explicit adult framing ("tall, full-grown adult, 21"). Note: uncensored realism mixes may ignore clothing prompts even with strong negatives — that's a model bias, not a prompt bug.

---

## 9. Thumbnails — 640×640 JPEG (q90), keep them small (~0.1 MB)
Center-crop "cover" to 640×640, JPEG q90. Never store full-resolution previews (they bloat the pack and slow the store). Resize with System.Drawing, loading from a **MemoryStream** so the source file isn't locked (lets you overwrite in place). When converting PNG→JPG, update the `previewImage` reference in both source (relative) and installed (absolute) and delete the old PNG. No text/logos/watermarks; one coherent image. For NSFW models, pick a low-`nsfwLevel` showcase image, an earlier clean version, or a neutral placeholder.

Source uses a relative path; the **installed** pack must use an absolute local-file URL:
```text
local-file:///C:/Users/<user>/AppData/Roaming/simpligen/presets/previews/<preset-id>.jpg
```
The installer rewrites this dynamically (relative paths render as broken cards).

---

## 10. BOM-safe, portable installer (`install-<slug>.cmd`)
Uses `%~dp0` so it restores from anywhere it's placed, copies into `%APPDATA%\simpligen`, rewrites `previewImage` to an absolute URL, and writes JSON UTF-8 **without BOM**:
```bat
@echo off
setlocal
set "SOURCE=%USERPROFILE%\Downloads\<checkpoint>.safetensors"
set "ENGINE=%APPDATA%\simpligen\engine\models"
set "PRESETS=%APPDATA%\simpligen\presets"
if not exist "%SOURCE%" goto :missing
if not exist "%ENGINE%\checkpoints" mkdir "%ENGINE%\checkpoints"
if not exist "%PRESETS%\workflows" mkdir "%PRESETS%\workflows"
if not exist "%PRESETS%\previews"  mkdir "%PRESETS%\previews"
echo Installing <model name>...
copy /Y "%SOURCE%" "%ENGINE%\checkpoints\<checkpoint>.safetensors" >nul || goto :error
copy /Y "%~dp0<pack>.json" "%PRESETS%\<pack>.json" >nul || goto :error
copy /Y "%~dp0workflows\<preset-id>.json" "%PRESETS%\workflows\" >nul || goto :error
copy /Y "%~dp0previews\<preset-id>.jpg" "%PRESETS%\previews\" >nul || goto :error
powershell -NoProfile -ExecutionPolicy Bypass -Command "$p='%PRESETS%\<pack>.json'; $u=New-Object System.Text.UTF8Encoding($false); $j=[IO.File]::ReadAllText($p,$u) | ConvertFrom-Json; foreach($pr in $j.presets){ $leaf=Split-Path ($pr.previewImage -replace 'local-file:///','') -Leaf; $pr.previewImage='local-file:///'+(Join-Path ('%PRESETS%\previews') $leaf).Replace('\','/') }; [IO.File]::WriteAllText($p,($j | ConvertTo-Json -Depth 30),$u)"
echo. & echo Done. Restart SimpliGen. & echo. & pause
exit /b 0
:missing
echo Checkpoint not found in Downloads. & pause & exit /b 1
:error
echo Installation failed. & pause & exit /b 1
```
**Encoding warning:** PS 5.1 `Set-Content -Encoding UTF8` writes a **BOM**, which SimpliGen rejects (`Unexpected token '﻿'`). Always use `[IO.File]::WriteAllText` + `New-Object System.Text.UTF8Encoding($false)`. Don't change `|` to `^|` inside the quoted `-Command`.

### Distributable packs (share with other users)
For sharing on Discord, build a self-contained zip per pack: `readme.html` + `install.cmd` + `install.ps1` + `<pack>.json` + `workflows/` + `previews/`. The `readme.html` lists each model's download link **and destination subfolder**, flags shared/gated/Civitai/HF models, and shows VRAM + sizes. The `install.cmd` wraps `install.ps1`, offers a menu (`[0]` all presets, `[1..N]` a single preset), copies files, rewrites `previewImage` to an absolute `local-file:///` URI, and can **auto-download models**.

Auto-download gotchas (these will bite the recipient, not you):
- **Civitai requires an API token.** Bare `civitai.com/api/download/models/<id>` returns **HTTP 401** with no token. Prompt the user for a token (made at `civitai.com/user/account` → API Keys) and append it as a query param: `?token=<t>` (use `&` if the URL already has a `?`). HuggingFace uses an `Authorization: Bearer <token>` header instead.
- **Report failures honestly.** A `try/catch` around the download isn't enough — also verify the file exists and is non-zero (`throw` otherwise), collect every failed/skipped model, and print that summary at the end. Never print "Installed" unconditionally; a 401 that's swallowed makes the user think the model downloaded when it didn't.
- **The single-preset menu choice is destructive by design.** Picking `[3]` rewrites the installed `<pack>.json` to contain *only* that preset (so the pack shows one card). To get the whole pack back, the user must re-run and choose `[0]`. Document this so it's not mistaken for a wipe bug.
- **Models go in `engine\models\<sub>\`, not `engine\ComfyUI\models\`** — make sure both the installer copy target and the readme's manual-install instructions use the correct path.

---

## 11. Validation
- Parse pack + workflow JSON. Confirm **no BOM** (`bytes[0..2] != EF BB BF`) and emoji/icon intact.
- Cross-refs: workflow file exists; `previewImage` resolves; primary model present (checkpoint in `checkpoints\`, unet in `diffusion_models\`, encoder in **`clip\`**, vae in `vae\`).
- Every workflow `{{placeholder}}` has a pack value or is a runtime value. Common mistakes: `{{vae}}`/`{{unet}}` with no matching pack field; filename case; wrong workflow folder; a CLIP-skip node present but one encoder still on raw CLIP; sampler display name instead of machine id; missing `simpligen_lora_1`.
- After install: restart SimpliGen, check the newest `session-*.log` for "Loaded N preset packs" and no "Failed to load preset pack". Run a test generation and confirm an output image.

---

## 12. Organization conventions (optional, for large collections)
- **Group by purpose within architecture** (e.g. SDXL Realism vs SDXL Art & Anime; Illustrious Realism vs Anime). Packs cannot be nested — a pack holds a flat preset list.
- **To group your own packs on the selection screen, use a common name prefix** (e.g. `MyTag — <name>`). SimpliGen's store search matches pack **name / description / base-model / preset-name — NOT the `tags` array** (tags are cosmetic chips). So a prefix is searchable and clusters packs together; a leading non-typeable symbol is not useful (you can't search it).
- Give every preset a short `tagline` (shown under the name in recent app versions).

---

## 13. Failure guide
- **Preset missing:** check newest log. Causes: BOM, malformed JSON, duplicate/bad id, missing required fields, app not fully restarted. `Unexpected token '﻿'` = BOM.
- **Broken thumbnail:** installed `previewImage` must be an absolute `local-file:///` URL and the JPG must exist in `presets\previews`.
- **Generation fails immediately:** wrong checkpoint name/folder; checkpoint vs UNet mismatch; missing VAE/encoder; node class not in the installed ComfyUI; unsubstituted placeholder; wrong sampler id; CLIP-skip miswire. Also: the engine **caches its model list at startup**, so a newly added model file isn't visible until SimpliGen is fully restarted.
- **Poor quality:** verify CLIP skip, the creator's prefix/negative, native resolution, sampler/scheduler/steps/CFG, correct VAE, and whether the creator used a hi-res second pass you haven't implemented. Don't mask a missing hi-res pass by inflating steps/CFG.

---

## 14. Agent working practices
- Do JSON edits and file deletions in a real language (e.g. Python `json` with `ensure_ascii=False`, `os.remove`, `shutil.rmtree`) rather than fragile shell one-liners.
- Keep source and installed copies in sync on every change (source = relative `previewImage`, installed = absolute).
- Pack `id` stays stable; only the display `name` carries any grouping prefix.
- After adding/removing model files, the user must fully restart SimpliGen before the engine sees them.

---

## 15. Final principle
Treat a preset as a small integration, not a label on a checkpoint. The checkpoint, prompt encoding, model sampling, VAE, resolution, workflow graph, LoRA marker, installer encoding, thumbnail URL, and SimpliGen loader must all agree. Most failures come from one layer being locally correct but incompatible with the next.
