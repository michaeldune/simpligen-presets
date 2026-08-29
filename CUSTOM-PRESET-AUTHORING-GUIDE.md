# SimpliGen Custom Local Preset Authoring Guide (v4)

A practical guide for building **local** SimpliGen preset packs: researching a model, writing the preset pack + ComfyUI **API-format** workflow, adding a thumbnail and LoRA support, installing safely on Windows, and verifying the result. Covers both **image** and **video** presets. Written for a capable coding agent or a hands-on user.

A preset is **done** only when SimpliGen loads the pack, shows its thumbnail, and a test generation produces output — not when files are copied. Examples assume a ~12 GB VRAM GPU; adjust `requirements` and step counts for your hardware.

---

## 1. Locations
```text
Installed packs:      %APPDATA%\simpligen\presets\<pack>.json
Installed workflows:  %APPDATA%\simpligen\presets\workflows\<id>.json   (shared across packs)
Installed thumbnails: %APPDATA%\simpligen\presets\previews\<id>.jpg     (shared)
Engine models root:   %APPDATA%\simpligen\engine\models\
                        checkpoints\  diffusion_models\  clip\  vae\  loras\  ...
Engine custom nodes:  %APPDATA%\simpligen\engine\ComfyUI\custom_nodes\
Logs:                 %APPDATA%\simpligen\logs\session-*.log
Engine model-path map: %APPDATA%\simpligen\engine\ComfyUI\extra_model_paths.yaml
```
- Keep editable **source copies + installers** in one folder per pack, **outside** the app's program directory (`%LOCALAPPDATA%\Programs\simpligen\...`) — that directory can be reset on app updates. Anywhere stable works (a docs folder, another drive, etc.).
- `extra_model_paths.yaml` maps **both** `text_encoders:` and `clip:` to the **`clip\`** folder, so text encoders (e.g. `qwen_3_06b_base.safetensors`) live in `engine\models\clip\`, not `text_encoders\`. Check there when validating encoders.
- Do not modify `resources\app.asar` or official packs (those carry `i18nId`/`characterContract` fields). Custom packs are just JSON in `%APPDATA%\simpligen\presets`.
- If the system drive is tight, model folders can be relocated to another drive via Windows **directory junctions** (`mklink /J`) — transparent to the app, which keeps using the normal `engine\models\...` paths.

---

## 2. Required agent behavior
1. Inspect an existing working pack of the same family (and same media type — image or video) before writing a new one.
2. Verify exact model version, base architecture, filename, VAE/encoder/custom-node needs, CLIP skip, sampler/scheduler, steps/CFG, prompt conventions, native resolutions.
3. Prefer the creator's published generation metadata over generic assumptions.
4. One self-contained source folder per pack.
5. Use a ComfyUI **API-format** workflow (flat node map), not a UI graph export.
6. Validate every JSON with a parser. Prefer `{{placeholder}}` **inside a quoted string value** (`"steps": "{{steps}}"`) over bare (`"values.c": {{width}}`) — SimpliGen resolves either, but a bare placeholder is not valid JSON and breaks any tooling (including `build-zips.py`) that parses the workflow directly. **Both forms are in shipped workflows**, though: across this repo's 100 workflows, `width`, `height`, `prompt` and `ref_2_enabled` appear bare, everything else quoted. So write quoted where you have the choice, but *any tool you write must handle both* — and must preserve which form each placeholder used. Substitute quoted `"{{x}}"` and bare `{{x}}` with **different sentinels** and invert each separately; a single blind substitution turns `"unet_name": "{{unet}}"` into `""sentinel""` on the way in, or drops the quotes on the way out. Assert after the round trip that every placeholder name survived *with the same quoting*.
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
Record: base model, exact filename, full-checkpoint vs UNet-only, VAE/encoder/custom-node needs, CLIP skip, sampler/scheduler, steps/CFG, native sizes, recommended prompt prefix + negative. Image metadata is usually the best source for settings. For video/LoRA-accelerator models found as ComfyUI workflow exports (Civitai "Workflows" resource type, or a linked custom-node repo's README), the node graph itself and the repo's README are the best source — check the repo's own `pyproject.toml`/`requirements.txt` for real dependencies rather than assuming.

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
Any extra `image.<key>` or `video.<key>` field in the pack is also exposed as `{{key}}`. Sampler names are machine ids: `euler`, `euler_ancestral`, `dpmpp_2m`, `dpmpp_2m_sde`, `dpmpp_2s_ancestral`, `dpmpp_sde`, `er_sde`, `res_multistep`. Schedulers: `normal`, `karras`, `simple`, `exponential`, `lcm`, `beta`.

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

**4.7 Custom nodes:** clone the repo into `engine\ComfyUI\custom_nodes\` (the bundled engine loads custom nodes; rgthree, KJNodes, RES4LYF ship by default). SimpliGen has no custom UI slider, so to expose a node parameter you can repurpose the `steps`/`cfg` slider (route `{{cfg}}` into the node param and hardcode the sampler cfg). See §7.3 for the two very different *kinds* of "custom node dependency" — a git clone is not always the whole story.

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
- If a pack adds its own baked-in accelerator LoRA (e.g. a "turbo" LoRA, §7), that node is **separate** from `simpligen_lora_1` and goes further downstream in the chain — the user LoRA marker still comes first, right after the model/clip source.

---

## 6. Pack schema (image presets)
```json
{
  "id": "<slug>-pack",
  "name": "<display name>",
  "version": "1.0.0",
  "author": "<creator>",
  "nsfw": false,                                           // REQUIRED - drives the store's "Hide mature" filter
  "description": "<desc>",
  "tags": ["Local", "<family>", "<style>"],
  "minComfyuiVersion": "v0.33.0",                          // optional; blocks install on older engines
  "addedAt": "2026-08-24",                                 // optional ISO date, for "Latest" ordering
  "presets": [{
    "id": "<preset-id>",
    "name": "<display name>",
    "tagline": "<short plain line shown under the name in the store/pickers>",
    "icon": "✨",
    "previewImage": "previews/<preset-id>.jpg",          // SOURCE = relative; INSTALLED = local-file:/// absolute
    "description": "<short desc>",
    "tags": ["<style>", "<family>", "Local"],
    "enabled": true,
    "template": "sdxl",                                    // "booru" tag-trained anime, "wan-video" video
    "promptStyle": "natural",                              // optional; pairs with template
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

## 7. Video presets

Video presets follow the same overall pack shape as image ones (§6), but the per-preset media block is called **`video`** instead of `image`, and both the schema and the typical workflow graph differ enough to warrant their own section. Cross-reference, all shipped and working in this repo: `packs/wan22-i2v-gguf/` (dual-expert GGUF, image-to-video), `packs/minimax-h3-10eros-turbo/` (single checkpoint + baked accelerator LoRA, three variants off one model file), and `packs/minimax-h3-solattn/` (the fullest example of reference inputs — nine image slots, audio and video references).

**7.1 Video pack schema.** A `video` block replaces `image`, with these differences:
```json
"video": {
  "supports": ["local"],
  "displayModel": "<name>",
  "baseModels": ["<family>"],
  "workflow": "workflows/<preset-id>.json",
  "duration": { "type": "slider", "min": 5, "max": 15, "default": 5, "step": 1, "unit": "seconds", "vramScalesWithDuration": true },

  // ---- User inputs. See 7.5 - getting these wrong rejects the render before it starts.
  "acceptsReferenceImages": { "min": 1, "max": 2,
                              "slotLabels": ["First frame", "Last frame (optional)"] },
  "acceptsReferenceAudios": { "min": 0, "max": 3 },
  "acceptsReferenceVideos": { "min": 0, "max": 3, "soundtrack": true },
  "acceptsAudio": true,                                  // a single audio track (lip-sync presets)
  "requiresImage": false,                                // legacy single-image flag; prefer acceptsReferenceImages

  // Single-checkpoint models (e.g. MiniMax H3): same core fields as image packs,
  // plus audio_vae for models that emit a synced audio stream
  "unet": "<file>", "unetUrl": "...", "clip": "<file>", "clipUrl": "...", "vae": "<file>", "vaeUrl": "...",
  "audio_vae": "<audio_vae_file>",                       // exposed as {{audio_vae}}; still needs an extraModels entry to download
  "spatialUpscaler": "<file>", "spatialUpscalerUrl": "...",   // two-pass latent upscale presets
  // Extra model files beyond the core fields (audio VAEs, baked accelerator LoRAs) go here -
  // each entry is its own download, `dir` is the exact engine\models\<dir>\ subfolder name:
  "extraModels": [
    { "dir": "vae",   "filename": "<audio_vae_file>", "url": "..." },
    { "dir": "loras", "filename": "<turbo_lora_file>", "url": "..." }
  ],

  // Dual-expert models (e.g. Wan 2.2 high/low-noise) use arrays instead of single unet/clip/vae fields:
  "unets": [ { "filename": "<high_noise_file>", "url": "..." }, { "filename": "<low_noise_file>", "url": "..." } ],
  "loras": [ { "filename": "<high_noise_lora>", "url": "...", "strength": 1 }, { "filename": "<low_noise_lora>", "url": "...", "strength": 1 } ],

  "steps": 20,
  "negativePrompt": "",
  "controls": { "steps": { "min": 10, "max": 30, "step": 1, "affectsCost": true } },
  "extensions": [ { "name": "<custom-node-repo-name>", "url": "https://github.com/...",
                    "pinnedCommit": "<40-char sha>",     // see 7.6 - shared across packs
                    "description": "<why it's needed>" } ],

  // ---- Accelerators the APP owns. Declare support; do not bake the node in. See 7.7.
  "supportsSage": true,
  "supportsSolAttn": true,
  "supportsSpectrum": true,

  "resolutionOptions": [                                  // NOT resolutionOverrides - a list of tiers, each gated by VRAM
    { "label": "480p", "minVramGB": 12, "aspects": { "16:9": {"width":864,"height":480}, "1:1": {"width":640,"height":640} } },
    { "label": "720p", "minVramGB": 16, "aspects": { "16:9": {"width":1280,"height":720} } }
  ],
  "defaultResolutionTier": 0,                             // index into resolutionOptions, not a label
  "reclaimVramBeforeDecode": true,                        // unload the model before VAE decode on tight cards
  "vramModel": { "floorGB": 8, "gbPerMpSecond": 0.38 },   // lets the app predict VRAM from resolution x duration
  "requirements": { "minVramGB": 12, "recommendedVramGB": 16, "minRamGB": 48, "sizeGB": 41, "notes": "<free-text caveats>" }
}
```
Key differences from image presets, spelled out:
- `resolutionOptions` (array of `{label, minVramGB, aspects}` tiers) replaces `resolutionOverrides` (flat aspect→size map) — video models often have a VRAM-gated ladder of supported resolutions, not one fixed native size.
- `duration` (slider config) has no image equivalent.
- A single checkpoint model uses the same `unet`/`clip`/`vae` core fields as an image UNet-family pack, **plus** `extraModels[]` for anything beyond those three (most commonly an audio VAE and/or a baked accelerator LoRA).
- A dual-expert model (two diffusion models sharing one CLIP/VAE, e.g. Wan's high-noise/low-noise split) uses `unets[]`/`loras[]` arrays instead of singular `unet`/`lora` fields.
- `extensions[]` (not `requirements.notes` alone) is where you list required custom nodes for the reader's benefit; **also** register the node's real `class_type` name(s) in `build-zips.py`'s `CUSTOM_NODES` dict (§11) so the generated installer readme actually warns about it — `extensions[]` in the pack JSON is documentation, `CUSTOM_NODES` in the generator is what makes that documentation actually appear in the shipped zip.

**7.2 Typical video workflow shape** (single-checkpoint, text-to-video, audio-synced — e.g. MiniMax H3):
```text
UNETLoader → CLIPLoader → simpligen_lora_1 (§5) → [optional: accelerator LoRA node] →
  ├─→ BasicGuider (conditioning) ─┐
  └─→ BasicScheduler (steps)      ├─→ SamplerCustomAdvanced (+ RandomNoise, KSamplerSelect) →
                                   ┘     VAEDecode (video) + VAEDecodeAudio (audio) →
                                         CreateVideo (fps, audio) → SaveVideo
```
This `RandomNoise`/`BasicGuider`/`KSamplerSelect`/`BasicScheduler`/`SamplerCustomAdvanced` chain (rather than a single `KSampler` node) is the common pattern for models with more exotic sampling needs (flow-matching schedules, dual video/audio streams). A dual-expert model (Wan-style) instead runs two `KSamplerAdvanced` passes in sequence (high-noise steps, then low-noise steps) between a shared conditioning stage and a shared `VAEDecodeTiled`.

**7.3 Custom node dependencies: two very different tiers.** Not every "clone this repo" requirement is equally risky:
- **Pure-Python, no extra pip deps** (e.g. `ComfyUI-MiniMax-H3-Turbo`): `git clone` into `custom_nodes\`, restart, done. Check the repo's `pyproject.toml` `dependencies = []` (or absence of a `requirements.txt` beyond stdlib/torch/comfy internals) to confirm this before promising it'll be simple.
- **Needs a compiled Python package too** (e.g. `sageattention`, which some SageAttention-based nodes require): this is a materially bigger ask. On Windows, `pip install sageattention` from PyPI typically wants to compile from source, which needs `nvcc` (CUDA Toolkit) and a matching MSVC linker — **SimpliGen's bundled Python has neither**, and its embeddable-Python distribution also lacks `Python.h`/`python3XX.lib`, which additionally blocks Triton's own JIT compiler (a dependency of some SageAttention code paths) from working even if a prebuilt `sageattention` wheel installs cleanly. Prebuilt Windows wheels exist for some exact torch/CUDA/Python combinations (search GitHub releases, e.g. the `woct0rdho/SageAttention` and `woct0rdho/triton-windows` forks) but are not guaranteed to match your exact engine build. **Verify a specific node's actual runtime dependency chain before shipping a preset that depends on it** — a node existing and importing successfully does not mean its default configuration will run without a compiler toolchain this app doesn't have.

**7.5 Reference inputs: the `acceptsReference*` fields.** This is the single easiest way to ship a preset that cannot run at all. A video workflow that takes user pictures carries placeholders like `{{ref_image_1}}`, `{{ref_image_2}}`, `{{ref_2_enabled}}`. **Those are filled from the preset's `acceptsReference*` declarations, not from the workflow.** Omit them and generation is rejected before a single step runs, with `missing render settings {{ref_2_enabled}}, {{ref_image_1}}, ...`. Nothing about the workflow file looks wrong; the pack is what is incomplete.

Two shapes are in use, and the distinction matters more than the names suggest:
```json
// First/last frame ("image to video"). The plate IS the first frame of the clip.
"acceptsReferenceImages": { "min": 1, "max": 2,
                            "slotLabels": ["First frame", "Last frame (optional)"] }

// Reference to video. The plate is READ and set aside - it never appears in the output.
"acceptsReferenceImages": { "min": 0, "max": 9,
                            "slotLabels": ["Reference 1", ... "Reference 9"] },
"acceptsReferenceAudios": { "min": 0, "max": 3 },
"acceptsReferenceVideos": { "min": 0, "max": 3, "soundtrack": true }
```
- What SimpliGen labels **"image to video" is first/last-frame** — which is what the `FL2VA` in checkpoint names such as `minimax_h3_fl2va_*` refers to. It optionally takes a *last* frame too, which is worth exposing.
- **Reference-to-video takes a different prompt.** With a first frame, the picture already established the setting, so the prompt only has to describe motion. With a reference there is no first frame and nothing to inherit: the prompt must describe the whole shot — setting, action, and camera — or you get a person standing still in a grey nowhere.
- **First/last frame images are CENTRE-CROPPED to the output shape** (`ImageScale` with `crop: "center"`), not letterboxed. A 896×1152 portrait plate rendered at 16:9 864×480 loses 57% of its height, and what goes is the top — i.e. the head. Match the aspect ratio to the source picture, or crop the picture first. Say so in the preset description; users hit this and assume the model is broken.
- `ref2va` and `fl2va` are **separate checkpoints**, but an `fl2va` checkpoint *does* drive `MiniMaxH3ReferenceToVideo` — verified by A/B against the `ref2va` build at equal likeness. That matters because it means a finetune published only in `FL2VA` form (e.g. 10Eros Max) can still ship all three of T2V, I2V and R2V off one file, with no second 19.5 GB download.
- **MiniMax H3 frame counts must be 17n+5** (73, 124, 192, 277...). Any other value errors out. The shipped workflows snap to that grid with a `ComfyMathExpression` node driven by the duration slider rather than trusting the user — copy that node rather than reinventing it.

**7.6 Shared extensions and `pinnedCommit`.** `extensions[]` entries carry a `pinnedCommit` (all 62 entries across this repo do). Extensions are installed **once and shared by every pack**, so two installed packs pinning the same repo to different commits still take turns moving it: preparing a preset from pack A re-pins the extension, preparing one from pack B re-pins it back, logging `Extension 'x' is at <a>, pack pins <b> — re-pinning` each time.

- **As of app 1.54.0 that flip-flop no longer breaks anything user-visible** — it used to leave a preset reverting to "Install preset locally" after every restart. The re-pin itself still happens (the code is unchanged; only its consequence was fixed), so aligning pins is now hygiene rather than a bug fix: it saves a fetch-and-checkout every time a user switches between two of your packs.
- **A pin is now honoured on an existing checkout, not only on a fresh clone.** This is the more useful half for authors: bumping `pinnedCommit` in a pack update actually repairs an installed node now, where previously a checkout cloned once drifted forever while the engine moved underneath it. So a pin bump is a real remediation channel for "this node broke against the current ComfyUI".
- Still prefer a commit that is current rather than whatever was latest the day you built the pack — an older pin can drag a shared extension *backwards* past a fix other packs depend on.

**7.7 Accelerators the app owns — declare, don't bake.** SageAttention, Sol-Attn and Spectrum are injected by SimpliGen at render time when the preset declares `supportsSage` / `supportsSolAttn` / `supportsSpectrum`. **Do not put the corresponding node (e.g. `PathchSageAttentionKJ`) in the workflow.** If you bake it in, the app sees the workflow as already controlling that accelerator and withholds its own handling — which also disables its crash-recovery path, so a card that can't run the accelerator has no way to fall back. Declaring instead of baking lets the app withdraw the accelerator and retry. Note the node's provider still has to be installed (`ComfyUI-KJNodes` for Sage), so keep it in `extensions[]` even though it appears nowhere in your graph.

**7.8 Testing a video preset via MCP:** `mcp__simpligen__generate` with `mediaType: "video"`, then poll with `wait_for_result`/`get_job` — note `wait_for_result` has its own internal timeout shorter than any `timeoutSeconds` you pass it, so a timeout error there does **not** mean the job failed; check `get_job` or the session log directly for real progress before concluding anything. Compare actual per-step timing (grep the session log for the `it/s]`/`s/it]` progress lines, or check the completed job's `createdAt`/`completedAt`) against any baseline you're trying to beat — don't trust a community-claimed speedup number without reproducing it on this hardware.

---

## 8. Reference settings by family (examples)
| Family | Sampler / scheduler | Steps | CFG | Notes |
|---|---|---:|---:|---|
| SDXL realism | dpmpp_2m / karras (or dpmpp_2m_sde) | 30 | 6–7 | no clip skip, baked VAE, natural language |
| Illustrious | euler_ancestral / normal | 28–30 | 5–6 | CLIP Skip 2, quality-tag prefix |
| Pony V6 | euler_ancestral | 25 | 7 | CLIP Skip 2, score-tag prefix |
| SD 1.5 anime | dpmpp_2m / karras | 30 | 7 | CLIP Skip 2, external kl-f8-anime2 VAE, 512-base |
| Anima (Cosmos) | er_sde / simple, ModelSamplingAuraFlow shift 3 | 16 (turbo ~12) | 1 | UNet + Qwen 0.6B encoder + Qwen-Image VAE, preamble |
| Krea-2 turbo | euler / simple | 8 | 1 | DiT, Qwen3VL encoder, Qwen-Image VAE, ConditioningZeroOut negative |
| MiniMax H3 (video) | res_multistep / simple | 20 (turbo LoRA ~6-8) | 1 | UNet + 32B Qwen3VL encoder + video/audio VAE, synced stereo audio; frame count must be 17n+5 |
| MiniMax H3 PDD Acc (video) | res_multistep / simple | 8 (fixed) | 1 | Alibaba's official distill; own node pack + `pdd_acc` model dir. Distills do NOT stack with a turbo/lightx2v LoRA |
| Wan 2.2 (video, dual-expert) | euler / simple, dual KSamplerAdvanced pass | 4 (2 high + 2 low, lightx2v LoRA) | 1 | GGUF dual high/low-noise UNets, shared clip/vae |
| LTX 2.5 (video) | — (two-pass, latent spatial upscaler) | — | 1 | Gated HF repo (§11); INT8 ConvRot build; separate video and audio VAEs |

---

## 9. Prompt conventions
- **SDXL realism:** pass `{{prompt}}` directly; put defect terms in `negativePrompt`.
- **Illustrious anime:** `masterpiece, best quality, amazing quality, ultra detailed, ... {{prompt}}` + CLIP Skip 2.
- **Pony V6:** `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, {{prompt}}` (photoreal Pony mixes often need NO score tags). Don't force a `source_*` tag globally.
- **SD 1.5 anime:** `masterpiece, best quality, highly detailed, anime, {{prompt}}`.
- **Anima/Krea:** use the model preamble (§4). Don't apply it to plain SD/SDXL checkpoints.
- **Video (MiniMax H3 style):** prompts describe a timeline, not a single frame — shots, camera motion, dialogue/speaker tags, and separate `overall_soundscape`/`non_diegetic_music` fields if the model supports audio. Treat it as writing a short shot list, not an image prompt.
- **Figure/age safety:** avoid words like "tiny" (with fairy/wings themes they skew childlike); add explicit adult framing ("tall, full-grown adult, 21"). Note: uncensored realism mixes may ignore clothing prompts even with strong negatives — that's a model bias, not a prompt bug.

---

## 10. Thumbnails — 640×640 JPEG (q90), keep them small (~0.1 MB)
Center-crop "cover" to 640×640, JPEG q90. Never store full-resolution previews (they bloat the pack and slow the store). Resize with System.Drawing, loading from a **MemoryStream** so the source file isn't locked (lets you overwrite in place). When converting PNG→JPG, update the `previewImage` reference in both source (relative) and installed (absolute) and delete the old PNG. No text/logos/watermarks; one coherent image. For NSFW models, pick a low-`nsfwLevel` showcase image, an earlier clean version, or a neutral placeholder. **For video presets**, extract a representative frame from a real test-generation output with `ffmpeg` (`-ss <timestamp> -vframes 1 -vf "scale=640:640:force_original_aspect_ratio=increase,crop=640:640"`) rather than redistributing a frame from someone else's showcase video.

Source uses a relative path; the **installed** pack must use an absolute local-file URL:
```text
local-file:///C:/Users/<user>/AppData/Roaming/simpligen/presets/previews/<preset-id>.jpg
```
The installer rewrites this dynamically (relative paths render as broken cards).

---

## 11. BOM-safe, portable installer (`install-<slug>.cmd`)
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
For sharing with others, build a self-contained zip per pack: `readme.html` + `install.cmd` + `install.ps1` + `<pack>.json` + `workflows/` + `previews/`, then host the zips wherever suits you (GitHub Releases, Dropbox, etc. — being able to update the same link in place, rather than a versioned one-off, keeps a Discord/announcement post from going stale). The `readme.html` lists each model's download link **and destination subfolder**, flags shared/gated/Civitai/HF models, and shows VRAM + sizes. The `install.cmd` wraps `install.ps1`, offers a menu (`[0]` all presets, `[1..N]` a single preset), copies files, rewrites `previewImage` to an absolute `local-file:///` URI, and can **auto-download models**.

If you're using a generator script like this repo's `build-zips.py`: it detects required custom nodes by scanning each workflow JSON for `class_type` values against a hardcoded registry (`CUSTOM_NODES` dict). **A pack whose custom node isn't in that registry doesn't get flagged** — the generated readme just silently omits any "you need to install X first" warning, and the resulting zip installs a preset that will fail the first time someone tries to generate with it. When you add a pack that needs a custom node, register its `class_type`(s) there too, not just in the pack JSON's own `extensions[]` field — the two are separate and both matter. Also make sure any workflow JSON your generator has to parse (not just SimpliGen at runtime) keeps `{{placeholders}}` inside quoted strings (§2.6) — a generator that can't parse the workflow can't detect its custom-node needs either, and may silently produce an incomplete or misleading readme instead of erroring loudly.

Auto-download gotchas (these will bite the recipient, not you):
- **Civitai requires an API token.** Bare `civitai.com/api/download/models/<id>` returns **HTTP 401** with no token. Prompt the user for a token (made at `civitai.com/user/account` → API Keys) and append it as a query param: `?token=<t>` (use `&` if the URL already has a `?`). HuggingFace uses an `Authorization: Bearer <token>` header instead.
- **Gated HuggingFace repos need a licence acceptance, not just a key.** Some repos (e.g. `Lightricks/LTX-2.5`, `gated: "auto"`) serve their repo page to anyone but return **401** on the model files unless the requesting account has accepted the licence. **App 1.54.0 routes every HuggingFace 401/403 to the "Model Access Required" dialog with a link to the repo, whether or not a key is on file** (`const gated = service === 'huggingface'`) — on the reasoning that public HF weights never 401, so any auth failure there means a gate. Before 1.54.0 a keyless 401 went to the API-key prompt instead and the user just watched a download restart forever; if you support older app versions, that is what a bug report of "download never finishes" means. Either way, **say it in the pack description** with the repo URL — a description is the only thing that reaches someone before they hit the wall. Approval on `gated: auto` is instant, and partials are kept across the failure, so a retry resumes. Check a repo's gate state with `https://huggingface.co/api/models/<owner>/<repo>` and read the `gated` field before shipping. One caveat outside anyone's control: the licence link on the gate form is the *publisher's* to get right — Lightricks' pointed at a `LICENSE.md` that does not exist, 404ing for everyone, while the actual file is `LICENSE` in a different repo. A 404 there does not block acceptance; the link and the Accept button are separate controls.
- **Report failures honestly.** A `try/catch` around the download isn't enough — also verify the file exists and is non-zero (`throw` otherwise), collect every failed/skipped model, and print that summary at the end. Never print "Installed" unconditionally; a 401 that's swallowed makes the user think the model downloaded when it didn't.
- **The single-preset menu choice is destructive by design.** Picking `[3]` rewrites the installed `<pack>.json` to contain *only* that preset (so the pack shows one card). To get the whole pack back, the user must re-run and choose `[0]`. Document this so it's not mistaken for a wipe bug.
- **Models go in `engine\models\<sub>\`, not `engine\ComfyUI\models\`** — make sure both the installer copy target and the readme's manual-install instructions use the correct path.

---

## 12. Validation
- Parse pack + workflow JSON. Confirm **no BOM** (`bytes[0..2] != EF BB BF`) and emoji/icon intact.
- Cross-refs: workflow file exists; `previewImage` resolves; primary model present (checkpoint in `checkpoints\`, unet in `diffusion_models\`, encoder in **`clip\`**, vae in `vae\`, LoRAs in `loras\`).
- Every workflow `{{placeholder}}` has a pack value or is a runtime value. Common mistakes: `{{vae}}`/`{{unet}}` with no matching pack field; filename case; wrong workflow folder; a CLIP-skip node present but one encoder still on raw CLIP; sampler display name instead of machine id; missing `simpligen_lora_1`; (video) reference placeholders with no `acceptsReference*` declaration (§7.5); (video) a bare unquoted `{{placeholder}}` that breaks strict JSON parsing.
- **Model-presence checks must follow directory junctions.** If model folders were relocated (§1), `engine\models\diffusion_models` and friends are reparse points, and both PowerShell's `Get-ChildItem -Recurse` and a naive `os.walk` **skip them by default** — every relocated model reads as missing. Resolve each junction's target (`(Get-Item <path> -Force).Target`) and scan those roots explicitly. The mirror-image error is just as easy: walking *both* the junction path and its target double-counts every file, which will inflate any size total you report by 2×.
- After install: restart SimpliGen, check the newest `session-*.log` for "Loaded N preset packs" and no "Failed to load preset pack". Run a test generation and confirm real output (an image file, or for video, a playable file with the requested duration — check via `ffprobe`, since duration sliders often get frame-quantized and don't land on the exact requested number of seconds).

---

## 13. Organization conventions (optional, for large collections)
- **Group by purpose within architecture** (e.g. SDXL Realism vs SDXL Art & Anime; Illustrious Realism vs Anime). Packs cannot be nested — a pack holds a flat preset list.
- **To group your own packs on the selection screen, use a common name prefix** (e.g. `MyTag — <name>`). SimpliGen's store search matches pack **name / description / base-model / preset-name — NOT the `tags` array** (tags are cosmetic chips). So a prefix is searchable and clusters packs together; a leading non-typeable symbol is not useful (you can't search it).
- **But a prefix only survives a manual install.** Packs installed from a catalogue have the `Community — ` prefix **stripped**, deliberately: the store card carries its own "Community" badge, and stripping makes packs sort by subject instead of clustering every community pack under "C". Keep the prefix in your source (it still helps people installing the zip by hand), and expect it to disappear for everyone else. **App 1.54.0 also badges community packs in the model pickers**, not just on store cards, so a stripped name is no longer ambiguous against an official pack of the same name — that had made a community "Krea 2" indistinguishable from the official one. Two packs can still share a display name, so if yours collides with an official pack, a distinguishing name is still kinder than relying on the badge.
- **Store-installed and hand-installed copies of the same pack coexist.** A catalogue install lands under id `community--<slug>-pack`; the repo's own installer lands under `<slug>-pack`. Different ids, so the app treats them as unrelated and shows both, with the hand-installed one frozen at whatever version it was. After moving a pack into a catalogue, remove the local copy or you accumulate stale duplicates — and be aware the local copy may be the *newer* one until the catalogue ingests your release.
- Give every preset a short `tagline` (shown under the name in recent app versions).

---

## 14. Failure guide
- **Preset missing:** check newest log. Causes: BOM, malformed JSON, duplicate/bad id, missing required fields, app not fully restarted. `Unexpected token '﻿'` = BOM.
- **Broken thumbnail:** installed `previewImage` must be an absolute `local-file:///` URL and the JPG must exist in `presets\previews`. A plain file-copy sync from source→installed silently reverts this — always reapply the absolute-path rewrite after any sync, image or video pack alike.
- **Generation fails immediately:** wrong checkpoint name/folder; checkpoint vs UNet mismatch; missing VAE/encoder; node class not in the installed ComfyUI; unsubstituted placeholder; wrong sampler id; CLIP-skip miswire; (video) a required custom node was never actually cloned in, or imports but its own further dependency (e.g. a compiled Python package) isn't installed — check the session log for an `ImportError`/`ModuleNotFoundError` near engine startup, not just at generation time. Also: the engine **caches its model list at startup**, so a newly added model file, or a newly cloned custom node, isn't visible until SimpliGen is fully restarted.
- **"Missing render settings {{ref_image_1}}, {{ref_2_enabled}}":** the workflow has reference slots the preset doesn't declare — add the `acceptsReference*` fields (§7.5). Nothing is wrong with the workflow.
- **"Failed to convert an input value to a FLOAT" on `h3_duration`:** a duration was never supplied, so `{{duration}}` resolved to nothing. Slider defaults are not applied when generating through the MCP — pass `durationSeconds` explicitly.
- **Subject's head cut off in an image-to-video result:** aspect mismatch, not a model failure. First/last frame plates are centre-cropped to the output shape (§7.5).
- **Downloads that restart forever:** a gated HuggingFace repo with no API key configured (§11). Check the repo's `gated` field.
- **Poor quality:** verify CLIP skip, the creator's prefix/negative, native resolution, sampler/scheduler/steps/CFG, correct VAE, and whether the creator used a hi-res second pass you haven't implemented. Don't mask a missing hi-res pass by inflating steps/CFG.
- **Uninstalling a pack never deletes model weights.** `deletePresetPack` removes the pack JSON, its DB rows, previews and workflows, then returns — it does not touch `engine\models\`. It guards shared previews and shared workflows, but has no equivalent guard for models because it never deletes them. So reinstalling a pack costs nothing in re-downloads; and reclaiming model space is always manual, and always needs a check that no *other* installed pack references the file first.

---

## 15. Agent working practices
- Do JSON edits and file deletions in a real language (e.g. Python `json` with `ensure_ascii=False`, `os.remove`, `shutil.rmtree`) rather than fragile shell one-liners.
- Keep source and installed copies in sync on every change (source = relative `previewImage`, installed = absolute).
- Pack `id` stays stable; only the display `name` carries any grouping prefix.
- After adding/removing model files, or cloning/removing a custom node, the user must fully restart SimpliGen before the engine sees the change.
- Before promising a speed/quality claim from a community workflow or node, verify it against the actual installed engine (imports cleanly, runs on real hardware, produces real output) rather than relaying the claim — see §7.3/§7.4.

---

## 16. Final principle
Treat a preset as a small integration, not a label on a checkpoint. The checkpoint, prompt encoding, model sampling, VAE, resolution, workflow graph, LoRA marker, installer encoding, thumbnail URL, and SimpliGen loader must all agree. Most failures come from one layer being locally correct but incompatible with the next.
