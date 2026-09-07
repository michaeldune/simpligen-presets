# Video Refine Packs Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship two new SimpliGen community packs that re-render a finished MiniMax H3 clip at a higher tier: an H3-native PDD refine and an LTX 2.5 MSR refine.

**Architecture:** Each pack is one preset: a pack JSON in `packs/<slug>/`, one API-format ComfyUI workflow with SimpliGen `{{placeholders}}`, and a preview JPEG cut from the verified test render. The source clip enters through SimpliGen's Reference Video 1 slot; its soundtrack is muxed back untouched. Pack 1 follows the upstream `pdd_video_upscale_long.json` example on the ref2va base. Pack 2 follows the A2V pack's second pass with the official Multi-Reference preset's MSR nodes.

**Tech Stack:** SimpliGen 1.58+, engine ComfyUI v0.34.2, ComfyUI-MiniMax-H3-PDD-Acc @ 8335330, Comfyui_Minimax_h3_latent_Upscaler @ d7c01b9, ComfyUI-LTX2.5-MSR @ 9894117, build-zips.py, gh CLI as michaeldune.

Spec: `docs/superpowers/specs/2026-09-07-video-refine-packs-design.md`.

## Global Constraints

- Never modify a shipped preset. Both packs are new, version `1.0.0`.
- `{{width}}` and `{{height}}` stay UNQUOTED (bare numbers) in workflow JSON. Every other placeholder is a quoted string.
- Optional user-slot node ids carry the `sgopt_<slot>__` prefix so the app can prune them when the slot is empty. Reference Video 1 is required (`min: 1`) in both packs.
- Do not bake SageAttention or any accelerator node; declare `supportsSage: true` and keep ComfyUI-KJNodes in `extensions[]`.
- Register any new custom node `class_type` in `build-zips.py` `CUSTOM_NODES`.
- Verify through the SimpliGen MCP (`mcp__simpligen__generate`), never by direct engine submission. `wait_for_result` times out on its own; poll with `get_job` or watch the output folder.
- User presets load from `F:\SimpliGen\presets\` (pack JSON renamed `community--<pack-id>.json`, workflows in `workflows\`, previews in `previews\`). New packs need an app restart: `Stop-Process SimpliGen`, relaunch `C:\Users\micha\AppData\Local\Programs\simpligen\SimpliGen.exe`, wait ~50 s.
- Pushing to master releases (the Store syncs every 6 h). Push only after the test render passes. Remote is SSH alias `git@github.com-dune`; release upload needs `gh auth switch -u michaeldune`, then switch back to `michaelkpate`.
- Commit messages end with `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.

---

### Task 1: Pack 1 workflow (H3 PDD refine)

**Files:**
- Create: `packs/minimax-h3-refine/workflows/video_minimax_h3_refine_pdd.json`

**Interfaces:**
- Consumes placeholders the app fills: `{{unet}} {{clip}} {{vae}} {{audio_vae}} {{prompt}} {{width}} {{height}} {{seed}} {{ref_video_1}} {{ref_video_audio_1}}`.
- Produces: an MP4 with the source soundtrack at `video/MiniMax_H3_refine_pdd_*.mp4`.

- [ ] **Step 1: Write the workflow**

```json
{
  "h3_unet": {"inputs": {"unet_name": "{{unet}}", "weight_dtype": "default"}, "class_type": "UNETLoader", "_meta": {"title": "Load MiniMax H3 Reference (pruned int8)"}},
  "h3_clip": {"inputs": {"clip_name": "{{clip}}", "type": "minimax", "device": "default"}, "class_type": "CLIPLoader", "_meta": {"title": "Qwen3-VL Text Encoder (MiniMax)"}},
  "h3_video_vae": {"inputs": {"vae_name": "{{vae}}"}, "class_type": "VAELoader", "_meta": {"title": "Video VAE"}},
  "h3_audio_vae": {"inputs": {"vae_name": "{{audio_vae}}"}, "class_type": "VAELoader", "_meta": {"title": "Audio VAE"}},
  "simpligen_lora_1": {"inputs": {"PowerLoraLoaderHeaderWidget": {"type": "PowerLoraLoaderHeaderWidget"}, "➕ Add Lora": "", "model": ["h3_unet", 0], "clip": ["h3_clip", 0]}, "class_type": "Power Lora Loader (rgthree)", "_meta": {"title": "SimpliGen User LoRAs"}},

  "sgopt_ref_video_1__load": {"inputs": {"file": "{{ref_video_1}}"}, "class_type": "LoadVideo", "_meta": {"title": "Source clip"}},
  "sgopt_ref_video_1__trim": {"inputs": {"video": ["sgopt_ref_video_1__load", 0], "start_time": 0, "duration": 15, "strict_duration": false}, "class_type": "Video Slice", "_meta": {"title": "Trim source to 15 s"}},
  "sgopt_ref_video_1__components": {"inputs": {"video": ["sgopt_ref_video_1__trim", 0]}, "class_type": "GetVideoComponents", "_meta": {"title": "Source frames + sound"}},
  "sgopt_ref_video_audio_1__load": {"inputs": {"audio": "{{ref_video_audio_1}}"}, "class_type": "LoadAudio", "_meta": {"title": "Source soundtrack"}},

  "refine_count": {"inputs": {"image": ["sgopt_ref_video_1__components", 0]}, "class_type": "GetImageSizeAndCount", "_meta": {"title": "Source size + frame count"}},
  "refine_len": {"inputs": {"expression": "a - ((a - 5) % 17)", "values.a": ["refine_count", 3]}, "class_type": "ComfyMathExpression", "_meta": {"title": "Snap frame count down to the 17k+5 grid"}},
  "refine_frames": {"inputs": {"image": ["refine_count", 0], "batch_index": 0, "length": ["refine_len", 1]}, "class_type": "ImageFromBatch", "_meta": {"title": "Frames on the H3 grid"}},
  "refine_encode": {"inputs": {"pixels": ["refine_frames", 0], "vae": ["h3_video_vae", 0]}, "class_type": "VAEEncode", "_meta": {"title": "Encode source video"}},
  "refine_upscale": {"inputs": {"latent": ["refine_encode", 0], "model_name": "minimax_h3_latent_upscaler_3d_fp16.safetensors", "mode": "target dimensions", "mode.width": {{width}}, "mode.height": {{height}}, "align": 32, "enable_temporal_chunking": true, "force_unload": true, "device": "cuda", "precision": "fp16"}, "class_type": "MinimaxH3LatentUpscaler3D", "_meta": {"title": "H3 Latent Upscaler (3D) to the output tier"}},
  "refine_audio_encode": {"inputs": {"audio": ["sgopt_ref_video_audio_1__load", 0], "vae": ["h3_audio_vae", 0]}, "class_type": "VAEEncodeAudio", "_meta": {"title": "Encode source audio (sampler needs an audio latent)"}},
  "refine_av_join": {"inputs": {"video_latent": ["refine_upscale", 0], "audio_latent": ["refine_audio_encode", 0]}, "class_type": "LTXVConcatAVLatent", "_meta": {"title": "Join A/V latent"}},

  "h3_conditioning": {"inputs": {"clip": ["simpligen_lora_1", 1], "vae": ["h3_video_vae", 0], "audio_vae": ["h3_audio_vae", 0], "prompt": "{{prompt}}", "width": {{width}}, "height": {{height}}, "length": ["refine_len", 1], "ref_image_size": "match"}, "class_type": "MiniMaxH3ReferenceToVideo", "_meta": {"title": "MiniMax H3 conditioning (prompt describes the clip)"}},

  "h3_pdd_shift": {"inputs": {"model": ["simpligen_lora_1", 0], "shift_video": 12.0, "shift_audio": 3.0}, "class_type": "MiniMaxH3SigmaShift", "_meta": {"title": "Sigma Shift 12/3 (required by PDD)"}},
  "h3_pdd_apply": {"inputs": {"model": ["h3_pdd_shift", 0], "pdd_file": "MiniMax-H3-Ref2VA-Acc-8Step.safetensors", "nfe": "8", "lora_strength": 1.0, "head_strength": 1.0, "on_off_grid": "error"}, "class_type": "MiniMaxH3PDDAccApply", "_meta": {"title": "MiniMax H3 PDD Acc LoRA (Apply, Ref2VA)"}},
  "h3_pdd_sigmas": {"inputs": {"nfe": "8", "denoise": 0.25}, "class_type": "MiniMaxH3PDDAccScheduler", "_meta": {"title": "Refine sigmas: last 2 of 8 PDD blocks"}},
  "h3_noise": {"inputs": {"noise_seed": "{{seed}}"}, "class_type": "RandomNoise", "_meta": {"title": "Random Noise"}},
  "h3_sampler": {"inputs": {"sampler_name": "euler"}, "class_type": "KSamplerSelect", "_meta": {"title": "KSampler Select (euler)"}},
  "refine_windows": {"inputs": {"chunk_frames": 73, "temporal_overlap_frames": 22, "anchor_strength": 0.999, "motion_anchor_frames": "22", "identity_anchor_frames": 24}, "class_type": "MMH3TemporalSplitParamsV10", "_meta": {"title": "Temporal windows 73/22"}},
  "refine_sampling": {"inputs": {"model": ["h3_pdd_apply", 0], "conditioning": ["h3_conditioning", 0], "latent": ["refine_av_join", 0], "noise": ["h3_noise", 0], "sampler": ["h3_sampler", 0], "sigmas": ["h3_pdd_sigmas", 0], "cfg": 1.0, "seam_polish": "off", "color_match": true, "temporal_split_param": ["refine_windows", 0]}, "class_type": "MMH3SplitUpscale", "_meta": {"title": "Windowed PDD refine at full size"}},

  "h3_decode_video": {"inputs": {"samples": ["refine_sampling", 0], "vae": ["h3_video_vae", 0]}, "class_type": "VAEDecode", "_meta": {"title": "VAE Decode"}},
  "h3_create_video": {"inputs": {"images": ["h3_decode_video", 0], "fps": 24, "audio": ["sgopt_ref_video_audio_1__load", 0], "bit_depth": 8}, "class_type": "CreateVideo", "_meta": {"title": "Create Video (source audio untouched)"}},
  "h3_save": {"inputs": {"video": ["h3_create_video", 0], "filename_prefix": "video/MiniMax_H3_refine_pdd", "format": "auto", "codec": "auto"}, "class_type": "SaveVideo", "_meta": {"title": "Save Video"}}
}
```

- [ ] **Step 2: Validate placeholders and JSON shape**

Run:
```bash
uv run python - <<'EOF'
import json,re
p='packs/minimax-h3-refine/workflows/video_minimax_h3_refine_pdd.json'
raw=open(p,encoding='utf-8').read()
assert '"mode.width": {{width}}' in raw and '"width": {{width}}' in raw, 'width must be bare'
q=re.sub(r'(?<=[:\s,\[])\{\{(\w+)\}\}(?=\s*[,\}\]])', r'"{{\1}}"', raw)
w=json.loads(q)
ph=sorted(set(re.findall(r'\{\{(\w+)\}\}',raw)))
print(len(w),'nodes; placeholders:',ph)
refs={(k,a) for k,v in w.items() for a,b in v['inputs'].items() if isinstance(b,list) and b[0] not in w}
assert not refs, refs
print('ok')
EOF
```
Expected: `27 nodes; placeholders: ['audio_vae', 'clip', 'height', 'prompt', 'ref_video_1', 'ref_video_audio_1', 'seed', 'unet', 'vae', 'width']` then `ok`.

- [ ] **Step 3: Commit**

```bash
git add packs/minimax-h3-refine/workflows/video_minimax_h3_refine_pdd.json
git commit -m "feat(wip): MiniMax H3 Video Refine (PDD) workflow

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 2: Pack 1 pack JSON, CUSTOM_NODES registration, local install

**Files:**
- Create: `packs/minimax-h3-refine/minimax-h3-refine-pack.json`
- Modify: `build-zips.py:16-100` (`CUSTOM_NODES` dict)
- Create (temporary): `packs/minimax-h3-refine/previews/minimax-h3-refine-pdd.jpg` (placeholder copy of `packs/minimax-h3-pdd-acc/previews/minimax-h3-pdd-acc-r2v.jpg`, replaced in Task 3)

**Interfaces:**
- Produces preset id `community--minimax-h3-refine-pack:minimax-h3-refine-pdd` for the MCP.

- [ ] **Step 1: Write the pack JSON**

```json
{
  "id": "minimax-h3-refine-pack",
  "name": "Community — MiniMax H3 (Video Refine)",
  "version": "1.0.0",
  "author": "LBH-123-AI + alibaba-pai + Jalen-Brunson",
  "nsfw": false,
  "minComfyuiVersion": "v0.33.0",
  "description": "Re-render a finished MiniMax H3 clip at a higher tier without leaving H3. Drop the clip in Reference Video 1, paste the brief that made it, pick the output tier. The clip is encoded, upscaled by LBH-123-AI's trained 3D latent upscaler, then refined with Alibaba's official 8-step PDD distill at denoise 0.25 (the last two of its eight trained blocks) in 73-frame windows with 22-frame overlap, so any length up to 15 s runs in one queue. The source soundtrack is muxed back untouched; nothing is re-synthesised in the audio. Same model family as the clip, so the look, motion and cast stay H3's own. Expects 480p H3 input; it cannot repair a face the source already lost. Euler, CFG 1, 8-step grid, sigma shift 12/3, all enforced by the PDD node. Do not stack a Turbo or lightx2v LoRA in the LoRA slot.",
  "tags": ["Local", "Video", "V2V", "Upscale", "Refine", "MiniMax H3", "PDD", "8-step"],
  "presets": [
    {
      "id": "minimax-h3-refine-pdd",
      "name": "MiniMax H3 Video Refine (PDD 8-Step)",
      "icon": "🔍",
      "previewImage": "previews/minimax-h3-refine-pdd.jpg",
      "tagline": "Upscale and sharpen an H3 clip in H3 - source audio kept",
      "tags": ["Video", "V2V", "Upscale", "Refine", "PDD", "8-step"],
      "enabled": true,
      "template": "wan-video",
      "supportsDialogue": true,
      "dialogueFormat": {"placement": "inline-end", "template": " The character says{delivery}: \"{dialogue}\""},
      "description": "Drop a finished H3 clip in Reference Video 1 and paste the same brief that made it. Output is the clip re-rendered at the chosen tier with its own soundtrack, refined by Alibaba's official PDD 8-step distill at denoise 0.25 in 73-frame windows. Duration follows the clip (capped at 15 s); the slider is ignored. Input should be 480p H3; the upscaler targets the tier directly, so 768p is the sweet spot. Cannot repair a face the source already lost. Measured on a 12 GB RTX 4070 Ti at 1344x768 from an 864x480 source - see the pack notes for the numbers.",
      "video": {
        "supports": ["local"],
        "displayModel": "MiniMax H3 Reference (pruned int8) + LBH 3D Latent Upscaler + Alibaba PDD Acc refine",
        "baseModels": ["minimax-h3"],
        "workflow": "workflows/video_minimax_h3_refine_pdd.json",
        "duration": {"type": "slider", "min": 5, "max": 15, "default": 5, "step": 1, "unit": "seconds", "vramScalesWithDuration": true},
        "acceptsReferenceVideos": {"min": 1, "max": 1, "soundtrack": true},
        "unet": "minimax_h3_ref2va_pruned_int8_convrot.safetensors",
        "unetUrl": "https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors",
        "clip": "qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors",
        "clipUrl": "https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors",
        "vae": "minimax_h3_video_vae_fp16.safetensors",
        "vaeUrl": "https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors",
        "audio_vae": "minimax_h3_audio_vae_fp32.safetensors",
        "extraModels": [
          {"dir": "vae", "filename": "minimax_h3_audio_vae_fp32.safetensors", "url": "https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors"},
          {"dir": "pdd_acc", "filename": "MiniMax-H3-Ref2VA-Acc-8Step.safetensors", "url": "https://huggingface.co/alibaba-pai/MiniMax-H3-Acc-LoRAs/resolve/main/MiniMax-H3-Ref2VA-Acc-8Step.safetensors"},
          {"dir": "latent_upscale_models", "filename": "minimax_h3_latent_upscaler_3d_fp16.safetensors", "url": "https://huggingface.co/LBH-123-AI/Minimax_h3_latent_Upscaler/resolve/main/minimax_h3_latent_upscaler_3d_fp16.safetensors"}
        ],
        "extensions": [
          {"name": "rgthree-comfy", "url": "https://github.com/rgthree/rgthree-comfy.git", "pinnedCommit": "d92cad68a6e92a1c5d4032d3ac53f79ea44b08e4", "description": "Power Lora Loader, used by SimpliGen's own LoRA slot. Usually pre-installed by SimpliGen."},
          {"name": "ComfyUI-MiniMax-H3-PDD-Acc", "url": "https://github.com/Jalen-Brunson/ComfyUI-MiniMax-H3-PDD-Acc.git", "pinnedCommit": "83353308bc14dc49b2d82e263a1cafb94169b849", "description": "Loads Alibaba's official PDD acceleration LoRA (trunk + parallel-decoding head bank + trained sigma schedule with partial denoise). NOT pre-installed by SimpliGen."},
          {"name": "Comfyui_Minimax_h3_latent_Upscaler", "url": "https://github.com/LBH-123-AI/Comfyui_Minimax_h3_latent_Upscaler.git", "pinnedCommit": "d7c01b9011f2e8439493f6c02c29995a27df276f", "description": "Trained 3D latent upscaler (MinimaxH3LatentUpscaler3D) and the windowed refine sampler (MMH3SplitUpscale, MMH3TemporalSplitParamsV10). Same pin as the Two-Stage pack."},
          {"name": "ComfyUI-KJNodes", "url": "https://github.com/kijai/ComfyUI-KJNodes.git", "pinnedCommit": "3f20054214fec9f9234fd3841ae6f1e4287948f6", "description": "Provides PathchSageAttentionKJ for SimpliGen's Faster Attention injection (supportsSage). Not used by the graph itself."}
        ],
        "steps": 8,
        "negativePrompt": "",
        "supportsSage": true,
        "defaultResolutionTier": 1,
        "resolutionOptions": [
          {"label": "672p", "minVramGB": 12, "aspects": {"1:1": {"width": 928, "height": 928}, "16:9": {"width": 1216, "height": 672}, "9:16": {"width": 672, "height": 1216}, "4:3": {"width": 1056, "height": 800}, "3:4": {"width": 800, "height": 1056}, "21:9": {"width": 1408, "height": 608}}},
          {"label": "768p", "minVramGB": 12, "aspects": {"1:1": {"width": 1024, "height": 1024}, "16:9": {"width": 1344, "height": 768}, "9:16": {"width": 768, "height": 1344}, "4:3": {"width": 1184, "height": 864}, "3:4": {"width": 864, "height": 1184}, "21:9": {"width": 1536, "height": 672}}}
        ],
        "reclaimVramBeforeDecode": true,
        "requirements": {"minVramGB": 12, "recommendedVramGB": 16, "minRamGB": 32, "sizeGB": 43, "notes": "FILLED IN TASK 3 FROM THE TEST RENDER"}
      }
    }
  ]
}
```

- [ ] **Step 2: Register the windowed-refine classes in build-zips.py**

Open `build-zips.py`, find the `'MinimaxH3LatentUpscaler3D': {` entry (line 42) and add two sibling entries pointing at the same repo, copying that entry's `name`, `url` and `note` fields verbatim:

```python
    'MMH3SplitUpscale': { ...same dict as MinimaxH3LatentUpscaler3D... },
    'MMH3TemporalSplitParamsV10': { ...same dict as MinimaxH3LatentUpscaler3D... },
```

Confirm `'MiniMaxH3PDDAccApply'` and `'MiniMaxH3PDDAccScheduler'` are already keys; if `MiniMaxH3PDDAccScheduler` is missing, add it as a copy of the `MiniMaxH3PDDAccApply` entry.

Run: `grep -c "MMH3SplitUpscale\|MMH3TemporalSplitParamsV10\|MiniMaxH3PDDAccScheduler" build-zips.py`
Expected: `3` or more.

- [ ] **Step 3: Placeholder preview, then install locally and restart the app**

```bash
mkdir -p packs/minimax-h3-refine/previews
cp packs/minimax-h3-pdd-acc/previews/minimax-h3-pdd-acc-r2v.jpg packs/minimax-h3-refine/previews/minimax-h3-refine-pdd.jpg
cp packs/minimax-h3-refine/minimax-h3-refine-pack.json /f/SimpliGen/presets/community--minimax-h3-refine-pack.json
cp packs/minimax-h3-refine/workflows/video_minimax_h3_refine_pdd.json /f/SimpliGen/presets/workflows/
cp packs/minimax-h3-refine/previews/minimax-h3-refine-pdd.jpg /f/SimpliGen/presets/previews/
powershell -NoProfile -Command "Stop-Process -Name SimpliGen -Force -ErrorAction SilentlyContinue; Start-Sleep 3; Start-Process 'C:\Users\micha\AppData\Local\Programs\simpligen\SimpliGen.exe'"
```
Wait ~60 s, then `mcp__simpligen__get_status` must report `engineRunning: true`. Then `mcp__simpligen__list_capabilities` (output is large; grep the saved result file for `minimax-h3-refine-pdd` and confirm `localReady: true`). If not localReady, call `prepare_preset` with `packId: community--minimax-h3-refine-pack`, `presetId: community--minimax-h3-refine-pack:minimax-h3-refine-pdd`, `mediaType: video`, then re-check.

- [ ] **Step 4: Commit**

```bash
git add packs/minimax-h3-refine build-zips.py
git commit -m "feat(wip): MiniMax H3 Video Refine pack JSON

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 3: Pack 1 verification renders, preview, notes

**Files:**
- Modify: `packs/minimax-h3-refine/minimax-h3-refine-pack.json` (requirements.notes, description numbers)
- Replace: `packs/minimax-h3-refine/previews/minimax-h3-refine-pdd.jpg`
- Create: `D:\SimpliGen-Backups\video-refine-verify-20260907\` (renders + sheets)

- [ ] **Step 1: Upload the 5 s source and render at 768p**

`mcp__simpligen__upload_file` with `F:\SimpliGen\output\community--minimax-h3-pdd-acc-packminimax-h3-pdd-acc-r2v\2026-09-07_00001_.mp4` (the verified PDD R2V clip, 864x480, 5 s). Then `mcp__simpligen__generate`:

```json
{"mediaType": "video", "backend": "local",
 "packId": "community--minimax-h3-refine-pack",
 "presetId": "community--minimax-h3-refine-pack:minimax-h3-refine-pdd",
 "referenceVideos": ["<handle>"],
 "prompt": "Subject 1: a bald man with a grey goatee, black over-ear headphones, dark navy t-shirt, seated at a podcast desk with a condenser microphone on a boom arm, warm desk lamp, acoustic foam behind him. Target video: realistic cinema. He lifts the headphones onto his ears, glances at the camera and nods. Static camera, medium close-up. Sound: room tone, a soft chair creak, the click of the headphone band.",
 "options": {"aspectRatio": "16:9", "resolution": "768p", "durationSeconds": 5, "seed": 20260907}}
```
If the MCP rejects `referenceVideos`, pass the handle as `video` instead; record which field worked in the pack notes.

Wait with a folder watch:
```bash
d="/f/SimpliGen/output/community--minimax-h3-refine-packminimax-h3-refine-pdd"; until ls "$d"/*.mp4 >/dev/null 2>&1; do sleep 5; done; sleep 3; ls -l "$d"
log=$(ls -t /c/Users/micha/AppData/Roaming/simpligen/logs/session-*.log | head -1)
grep -n "Prompt executed in\|partition check\|heads fused\|MMH3\|Error\|Traceback" "$log" | tail -12
```
Expected: `partition check ok: ref2va file on ref2va model`, `heads fused`, `Prompt executed in N seconds`, no Traceback.

- [ ] **Step 2: Check size, audio and faces**

```bash
v=$(ls /f/SimpliGen/output/community--minimax-h3-refine-packminimax-h3-refine-pdd/*.mp4 | head -1)
ffprobe -v error -show_entries stream=codec_type,width,height,nb_frames -of compact "$v"
ffmpeg -i "$v" -af volumedetect -f null - 2>&1 | grep -o "max_volume: .*"
ffmpeg -v error -y -i "$v" -vf "select='not(mod(n\,20))',scale=432:-1,tile=6x1" -frames:v 1 /c/Users/micha/AppData/Local/Temp/refine_pdd_5s_sheet.jpg
```
Expected: `width=1344|height=768`, `nb_frames=124`, audio stream present, `max_volume` within 3 dB of the source's `-21.8 dB`. Read the sheet with the Read tool and compare to `D:\SimpliGen-Backups\pdd-acc-verify-20260907\pdd_r2v_sheet.jpg`: same man, same headphone lift, sharper. If faces drift, lower `denoise` in `h3_pdd_sigmas` to `0.125` (one block) and re-run once; record which value shipped.

- [ ] **Step 3: 10 s render to exercise two windows**

Upload `F:\SimpliGen\output\chaintest\two_shot_00001_.mp4` (10.3 s) and generate with the same options but `durationSeconds: 10` and this prompt: `Subject 1: a woman with long dark hair in a black leather jacket over a black top, holding a handheld microphone, standing in a server room aisle lined with blue-lit racks. Target video: realistic cinema. She speaks to camera, then the shot cuts to a closer framing and she continues. Static camera. Sound: room tone, server fan hum, her voice.` Expect `nb_frames=243` (247 snapped to the 17k+5 grid, 243) and no visible seam at the window boundary around frame 73 on a 12-frame sheet:
```bash
ffmpeg -v error -y -i "$v10" -vf "select='not(mod(n\,20))',scale=320:-1,tile=13x1" -frames:v 1 /c/Users/micha/AppData/Local/Temp/refine_pdd_10s_sheet.jpg
```

- [ ] **Step 4: Preview, notes, durable copy**

```bash
v=$(ls /f/SimpliGen/output/community--minimax-h3-refine-packminimax-h3-refine-pdd/*.mp4 | head -1)
ffmpeg -v error -y -ss 3.5 -i "$v" -frames:v 1 -q:v 3 packs/minimax-h3-refine/previews/minimax-h3-refine-pdd.jpg
mkdir -p /d/SimpliGen-Backups/video-refine-verify-20260907
cp /f/SimpliGen/output/community--minimax-h3-refine-packminimax-h3-refine-pdd/*.mp4 /c/Users/micha/AppData/Local/Temp/refine_pdd_*_sheet.jpg /d/SimpliGen-Backups/video-refine-verify-20260907/
```
Edit `requirements.notes` in the pack JSON to read (fill the two numbers): `Measured 2026-09-07 on a 12 GB RTX 4070 Ti, engine ComfyUI 0.34.2, Sage attention on: 864x480 -> 1344x768, 5 s in <N5> s, 10 s (two 73-frame windows) in <N10> s. Shares the ref2va base with every R2V pack; new downloads are the 1.37 GB Ref2VA PDD distill and the 0.69 GB LBH upscaler if you lack Two-Stage. Duration follows the source clip up to 15 s. Below ~2 GB free system RAM the decode can fail with 'HostBuffer.read_file_slice failed'.` Replace `see the pack notes for the numbers` in the preset description with `5 s in <N5> s, 10 s in <N10> s`.

- [ ] **Step 5: Commit**

```bash
git add packs/minimax-h3-refine
git commit -m "feat: MiniMax H3 Video Refine pack 1.0.0 - PDD windowed refine, verified in-app

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 4: Pack 2 workflow (LTX 2.5 MSR refine)

**Files:**
- Create: `packs/ltx-2-5-refine/workflows/ltx_2_5_refine_msr.json`

**Interfaces:**
- Consumes: `{{unet}} {{clip}} {{vae}} {{audio_vae}} {{prompt}} {{negative_prompt}} {{width}} {{height}} {{seed}} {{cfg}} {{ref_video_1}} {{ref_video_audio_1}} {{ref_image_1}} {{ref_image_2}} {{ref_image_3}} {{ref_image_4}}`.
- Produces: an MP4 with the source soundtrack at `video/LTX25_refine_msr_*.mp4`.

- [ ] **Step 1: Write the workflow**

The source frames are resized to half the tier (so the 2x upsampler lands exactly on `{{width}}` x `{{height}}`), trimmed to the LTX 8k+1 frame grid, encoded, upsampled, refined with the MSR guide, then decoded. The audio latent is the source audio encoded and masked so the sampler leaves it alone; the mux uses the source audio directly.

```json
{
  "ltx_unet": {"inputs": {"unet_name": "{{unet}}", "weight_dtype": "default"}, "class_type": "UNETLoader", "_meta": {"title": "Load LTX 2.5 distilled (22B INT8 ConvRot)"}},
  "ltx_msr_lora": {"inputs": {"lora_name": "LTX-2.5-Licon-MSR-V1.safetensors", "strength_model": 1, "model": ["ltx_unet", 0]}, "class_type": "ComfyUILTX25MSRICLoRALoader", "_meta": {"title": "Load MSR IC-LoRA"}},
  "ltx_clip": {"inputs": {"clip_name": "{{clip}}", "type": "ltxv", "device": "default"}, "class_type": "CLIPLoader", "_meta": {"title": "Load CLIP - Text Encoder"}},
  "ltx_audio_vae": {"inputs": {"vae_name": "{{audio_vae}}"}, "class_type": "VAELoader", "_meta": {"title": "Load VAE - Audio"}},
  "ltx_video_vae": {"inputs": {"vae_name": "{{vae}}"}, "class_type": "VAELoader", "_meta": {"title": "Load VAE - Video"}},
  "ltx_upscaler": {"inputs": {"model_name": "ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors"}, "class_type": "LatentUpscaleModelLoader", "_meta": {"title": "Load Latent Upscale Model"}},
  "simpligen_lora_1": {"inputs": {"PowerLoraLoaderHeaderWidget": {"type": "PowerLoraLoaderHeaderWidget"}, "➕ Add Lora": "", "model": ["ltx_msr_lora", 0], "clip": ["ltx_clip", 0]}, "class_type": "Power Lora Loader (rgthree)", "_meta": {"title": "SimpliGen User LoRAs"}},

  "ltx_pos": {"inputs": {"text": "{{prompt}}", "clip": ["simpligen_lora_1", 1]}, "class_type": "CLIPTextEncode", "_meta": {"title": "CLIP Text Encode (Positive Prompt)"}},
  "ltx_neg": {"inputs": {"text": "{{negative_prompt}}", "clip": ["simpligen_lora_1", 1]}, "class_type": "CLIPTextEncode", "_meta": {"title": "CLIP Text Encode (Negative Prompt)"}},
  "ltx_cond": {"inputs": {"frame_rate": 24, "positive": ["ltx_pos", 0], "negative": ["ltx_neg", 0]}, "class_type": "LTXVConditioning", "_meta": {"title": "LTXVConditioning"}},

  "sgopt_ref_video_1__load": {"inputs": {"file": "{{ref_video_1}}"}, "class_type": "LoadVideo", "_meta": {"title": "Source clip"}},
  "sgopt_ref_video_1__trim": {"inputs": {"video": ["sgopt_ref_video_1__load", 0], "start_time": 0, "duration": 15, "strict_duration": false}, "class_type": "Video Slice", "_meta": {"title": "Trim source to 15 s"}},
  "sgopt_ref_video_1__components": {"inputs": {"video": ["sgopt_ref_video_1__trim", 0]}, "class_type": "GetVideoComponents", "_meta": {"title": "Source frames + sound"}},
  "sgopt_ref_video_audio_1__load": {"inputs": {"audio": "{{ref_video_audio_1}}"}, "class_type": "LoadAudio", "_meta": {"title": "Source soundtrack"}},

  "refine_half_w": {"inputs": {"expression": "a / 2", "values.a": {{width}}}, "class_type": "ComfyMathExpression", "_meta": {"title": "Half tier width"}},
  "refine_half_h": {"inputs": {"expression": "a / 2", "values.a": {{height}}}, "class_type": "ComfyMathExpression", "_meta": {"title": "Half tier height"}},
  "refine_resize": {"inputs": {"image": ["sgopt_ref_video_1__components", 0], "upscale_method": "lanczos", "width": ["refine_half_w", 1], "height": ["refine_half_h", 1], "crop": "center"}, "class_type": "ImageScale", "_meta": {"title": "Fit source to half the tier"}},
  "refine_count": {"inputs": {"image": ["refine_resize", 0]}, "class_type": "GetImageSizeAndCount", "_meta": {"title": "Frame count"}},
  "refine_len": {"inputs": {"expression": "a - ((a - 1) % 8)", "values.a": ["refine_count", 3]}, "class_type": "ComfyMathExpression", "_meta": {"title": "Snap frame count down to the 8k+1 grid"}},
  "refine_frames": {"inputs": {"image": ["refine_count", 0], "batch_index": 0, "length": ["refine_len", 1]}, "class_type": "ImageFromBatch", "_meta": {"title": "Frames on the LTX grid"}},
  "refine_encode": {"inputs": {"pixels": ["refine_frames", 0], "vae": ["ltx_video_vae", 0]}, "class_type": "VAEEncode", "_meta": {"title": "Encode source video"}},
  "refine_upsample": {"inputs": {"samples": ["refine_encode", 0], "upscale_model": ["ltx_upscaler", 0], "vae": ["ltx_video_vae", 0]}, "class_type": "LTXVLatentUpsampler", "_meta": {"title": "Latent upsample x2"}},

  "sgopt_ref_image_1__load": {"inputs": {"image": "{{ref_image_1}}", "upload": "image"}, "class_type": "LoadImage", "_meta": {"title": "Reference 1 (pic1)"}},
  "sgopt_ref_image_1__resize": {"inputs": {"resize_type": "scale longer dimension", "resize_type.longer_size": 1536, "scale_method": "lanczos", "input": ["sgopt_ref_image_1__load", 0]}, "class_type": "ResizeImageMaskNode", "_meta": {"title": "Resize Reference (pic1)"}},
  "sgopt_ref_image_2__load": {"inputs": {"image": "{{ref_image_2}}", "upload": "image"}, "class_type": "LoadImage", "_meta": {"title": "Reference 2 (pic2)"}},
  "sgopt_ref_image_2__resize": {"inputs": {"resize_type": "scale longer dimension", "resize_type.longer_size": 1536, "scale_method": "lanczos", "input": ["sgopt_ref_image_2__load", 0]}, "class_type": "ResizeImageMaskNode", "_meta": {"title": "Resize Reference (pic2)"}},
  "sgopt_ref_image_3__load": {"inputs": {"image": "{{ref_image_3}}", "upload": "image"}, "class_type": "LoadImage", "_meta": {"title": "Reference 3 (pic3)"}},
  "sgopt_ref_image_3__resize": {"inputs": {"resize_type": "scale longer dimension", "resize_type.longer_size": 1536, "scale_method": "lanczos", "input": ["sgopt_ref_image_3__load", 0]}, "class_type": "ResizeImageMaskNode", "_meta": {"title": "Resize Reference (pic3)"}},
  "sgopt_ref_image_4__load": {"inputs": {"image": "{{ref_image_4}}", "upload": "image"}, "class_type": "LoadImage", "_meta": {"title": "Reference 4 (pic4)"}},
  "sgopt_ref_image_4__resize": {"inputs": {"resize_type": "scale longer dimension", "resize_type.longer_size": 1536, "scale_method": "lanczos", "input": ["sgopt_ref_image_4__load", 0]}, "class_type": "ResizeImageMaskNode", "_meta": {"title": "Resize Reference (pic4)"}},

  "refine_msr": {"inputs": {"strength": 1, "reference_frames": "33", "use_tiled_encode": false, "tile_size": 256, "tile_overlap": 64, "positive": ["ltx_cond", 0], "negative": ["ltx_cond", 1], "vae": ["ltx_video_vae", 0], "latent": ["refine_upsample", 0], "pic1": ["sgopt_ref_image_1__resize", 0], "pic2": ["sgopt_ref_image_2__resize", 0], "pic3": ["sgopt_ref_image_3__resize", 0], "pic4": ["sgopt_ref_image_4__resize", 0], "msr_parameters": ["ltx_msr_lora", 1]}, "class_type": "ComfyUILTX25MSRMultiReferenceGuide", "_meta": {"title": "MSR Multi-Reference Guide (refine)"}},

  "refine_audio_encode": {"inputs": {"audio": ["sgopt_ref_video_audio_1__load", 0], "audio_vae": ["ltx_audio_vae", 0]}, "class_type": "LTXVAudioVAEEncode", "_meta": {"title": "Encode source audio"}},
  "refine_audio_mask": {"inputs": {"value": 0, "width": ["refine_half_w", 1], "height": ["refine_half_h", 1]}, "class_type": "SolidMask", "_meta": {"title": "Preserve the audio latent"}},
  "refine_audio_setmask": {"inputs": {"samples": ["refine_audio_encode", 0], "mask": ["refine_audio_mask", 0]}, "class_type": "SetLatentNoiseMask", "_meta": {"title": "Do not denoise the audio latent"}},
  "refine_av_join": {"inputs": {"video_latent": ["refine_msr", 2], "audio_latent": ["refine_audio_setmask", 0]}, "class_type": "LTXVConcatAVLatent", "_meta": {"title": "Join A/V latent"}},

  "refine_noise": {"inputs": {"noise_seed": "{{seed}}"}, "class_type": "RandomNoise", "_meta": {"title": "RandomNoise"}},
  "refine_sampler": {"inputs": {"sampler_name": "euler"}, "class_type": "KSamplerSelect", "_meta": {"title": "KSamplerSelect"}},
  "refine_sigmas": {"inputs": {"sigmas": "0.85, 0.7250, 0.4219, 0.0"}, "class_type": "ManualSigmas", "_meta": {"title": "Refine schedule (A2V stage-2 tail)"}},
  "refine_guider": {"inputs": {"cfg": "{{cfg}}", "model": ["simpligen_lora_1", 0], "positive": ["refine_msr", 0], "negative": ["refine_msr", 1]}, "class_type": "CFGGuider", "_meta": {"title": "CFG Guider"}},
  "refine_sampling": {"inputs": {"noise": ["refine_noise", 0], "guider": ["refine_guider", 0], "sampler": ["refine_sampler", 0], "sigmas": ["refine_sigmas", 0], "latent_image": ["refine_av_join", 0]}, "class_type": "SamplerCustomAdvanced", "_meta": {"title": "Refine at full size"}},
  "refine_av_split": {"inputs": {"av_latent": ["refine_sampling", 0]}, "class_type": "LTXVSeparateAVLatent", "_meta": {"title": "LTXVSeparateAVLatent"}},
  "refine_crop": {"inputs": {"positive": ["refine_msr", 0], "negative": ["refine_msr", 1], "latent": ["refine_av_split", 0]}, "class_type": "LTXVCropGuides", "_meta": {"title": "Crop Guides (remove reference slots)"}},
  "ltx_decode": {"inputs": {"tile_size": 512, "overlap": 64, "temporal_size": 128, "temporal_overlap": 32, "samples": ["refine_crop", 2], "vae": ["ltx_video_vae", 0]}, "class_type": "VAEDecodeTiled", "_meta": {"title": "VAE Decode (Tiled)"}},
  "ltx_create_video": {"inputs": {"fps": 24, "bit_depth": 8, "images": ["ltx_decode", 0], "audio": ["sgopt_ref_video_audio_1__load", 0]}, "class_type": "CreateVideo", "_meta": {"title": "Create Video (source audio untouched)"}},
  "ltx_save": {"inputs": {"filename_prefix": "video/LTX25_refine_msr", "format": "auto", "codec": "auto", "video": ["ltx_create_video", 0]}, "class_type": "SaveVideo", "_meta": {"title": "Save Video"}}
}
```

- [ ] **Step 2: Validate**

Run the same validator as Task 1 Step 2 against `packs/ltx-2-5-refine/workflows/ltx_2_5_refine_msr.json`, with the bare-width assertion changed to `'"values.a": {{width}}' in raw`.
Expected placeholders: `['audio_vae', 'cfg', 'clip', 'height', 'negative_prompt', 'prompt', 'ref_image_1', 'ref_image_2', 'ref_image_3', 'ref_image_4', 'ref_video_1', 'ref_video_audio_1', 'seed', 'unet', 'vae', 'width']` then `ok`.

- [ ] **Step 3: Commit**

```bash
git add packs/ltx-2-5-refine/workflows/ltx_2_5_refine_msr.json
git commit -m "feat(wip): LTX 2.5 Video Refine (MSR) workflow

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 5: Pack 2 pack JSON and local install

**Files:**
- Create: `packs/ltx-2-5-refine/ltx-2-5-refine-pack.json`
- Create (temporary): `packs/ltx-2-5-refine/previews/ltx-2-5-refine-msr.jpg` (copy of `packs/ltx-2-5-a2v/previews/ltx-2-5-a2v-int8.jpg`, replaced in Task 6)
- Modify: `build-zips.py` `CUSTOM_NODES` (add `ComfyUILTX25MSRICLoRALoader` and `ComfyUILTX25MSRMultiReferenceGuide` if absent)

- [ ] **Step 1: Write the pack JSON**

```json
{
  "id": "ltx-2-5-refine-pack",
  "name": "Community — LTX 2.5 (Video Refine, MSR)",
  "version": "1.0.0",
  "author": "LiconStudio + Lightricks",
  "nsfw": false,
  "description": "Re-render any finished clip (MiniMax H3 or otherwise) at up to 1080p with LTX 2.5, holding the faces with Licon's Multi-Subject-Reference IC-LoRA. Drop the clip in Reference Video 1 and one to four face pictures in the reference slots. The clip is scaled to half the tier, encoded, upsampled 2x by the LTX latent spatial upscaler and refined by the distilled LTX 2.5 with the reference faces prepended, then decoded. The source soundtrack is muxed back untouched. LTX re-renders texture, so expect a crisper, more LTX-looking result than the H3 Video Refine pack; pick this one for sharpness or when a face needs a reference to hold. The prompt must be LTX style, not the H3 brief: one paragraph, '<who> <does what> in <where>, <camera>, <light>'. Requires a HuggingFace API key and one-time acceptance of the LTX 2.5 licence (gated repo); the weights are the same files the LTX 2.5 packs already use.",
  "tags": ["Local", "Video", "V2V", "Upscale", "Refine", "LTX", "MSR", "1080p"],
  "presets": [
    {
      "id": "ltx-2-5-refine-msr",
      "name": "LTX 2.5 Video Refine (Multi-Reference)",
      "icon": "🔍",
      "previewImage": "previews/ltx-2-5-refine-msr.jpg",
      "tagline": "Upscale a clip to 1080p in LTX 2.5, faces held by reference pictures",
      "tags": ["Video", "V2V", "Upscale", "Refine", "MSR", "1080p"],
      "enabled": true,
      "template": "wan-video",
      "description": "Drop a finished clip in Reference Video 1 and at least one face picture in Reference 1 (up to four). Write the prompt LTX style: one paragraph, who, action, place, camera, light. Output is the clip at the chosen tier with its own soundtrack. Measured on a 12 GB RTX 4070 Ti - see the pack notes for the numbers.",
      "video": {
        "supports": ["local"],
        "displayModel": "LTX 2.5 distilled (22B INT8 ConvRot) + latent upsampler + Licon MSR V1",
        "baseModels": ["ltxv-2.5-distilled"],
        "workflow": "workflows/ltx_2_5_refine_msr.json",
        "duration": {"type": "slider", "min": 3, "max": 15, "default": 5, "step": 1, "unit": "seconds", "vramScalesWithDuration": true},
        "acceptsReferenceVideos": {"min": 1, "max": 1, "soundtrack": true},
        "acceptsReferenceImages": {"min": 1, "max": 4, "slotLabels": ["Face 1", "Face 2", "Face 3", "Face 4"]},
        "unet": "ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors",
        "unetUrl": "https://huggingface.co/Lightricks/LTX-2.5/resolve/main/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors",
        "clip": "gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors",
        "clipUrl": "https://huggingface.co/Lightricks/LTX-2.5/resolve/main/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors",
        "vae": "ltx-2.5-video-vae-conv-bf16.safetensors",
        "vaeUrl": "https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-video-vae-conv-bf16.safetensors",
        "spatialUpscaler": "ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors",
        "spatialUpscalerUrl": "https://huggingface.co/Lightricks/LTX-2.5/resolve/main/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors",
        "audio_vae": "ltx-2.5-audio-vae-bf16.safetensors",
        "extraModels": [
          {"dir": "vae", "filename": "ltx-2.5-audio-vae-bf16.safetensors", "url": "https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-audio-vae-bf16.safetensors"},
          {"dir": "loras", "filename": "LTX-2.5-Licon-MSR-V1.safetensors", "url": "https://huggingface.co/LiconStudio/LTX-2.5-MSR/resolve/main/LTX-2.5-Licon-MSR-V1.safetensors"}
        ],
        "extensions": [
          {"name": "rgthree-comfy", "url": "https://github.com/rgthree/rgthree-comfy.git", "pinnedCommit": "d92cad68a6e92a1c5d4032d3ac53f79ea44b08e4", "description": "Power Lora Loader, used by SimpliGen's own LoRA slot. Usually pre-installed by SimpliGen."},
          {"name": "ComfyUI-LTX2.5-MSR", "url": "https://github.com/liconstudio/ComfyUI-LTX2.5-MSR.git", "pinnedCommit": "98941179a82223a0a62219550272b2823b3e3a9c", "description": "Multiple Subject Reference nodes for LTX 2.5. Same pin as SimpliGen's official LTX 2.5 Multi-Reference preset, so usually already installed."},
          {"name": "ComfyUI-KJNodes", "url": "https://github.com/kijai/ComfyUI-KJNodes.git", "pinnedCommit": "3f20054214fec9f9234fd3841ae6f1e4287948f6", "description": "Provides PathchSageAttentionKJ for SimpliGen's Faster Attention injection (supportsSage). Not used by the graph itself."}
        ],
        "cfg": 1,
        "steps": 3,
        "negativePrompt": "",
        "supportsSage": true,
        "vramModel": {"floorGB": 8, "gbPerMpSecond": 0.38},
        "reclaimVramBeforeDecode": true,
        "defaultResolutionTier": 1,
        "resolutionOptions": [
          {"label": "720p", "minVramGB": 8, "aspects": {"1:1": {"width": 960, "height": 960}, "16:9": {"width": 1280, "height": 704}, "9:16": {"width": 704, "height": 1280}, "4:3": {"width": 1024, "height": 768}, "3:4": {"width": 768, "height": 1024}, "21:9": {"width": 1664, "height": 704}}},
          {"label": "1080p", "minVramGB": 12, "aspects": {"1:1": {"width": 1408, "height": 1408}, "16:9": {"width": 1920, "height": 1088}, "9:16": {"width": 1088, "height": 1920}, "4:3": {"width": 1536, "height": 1152}, "3:4": {"width": 1152, "height": 1536}, "21:9": {"width": 2560, "height": 1088}}}
        ],
        "requirements": {"minVramGB": 12, "recommendedVramGB": 16, "minRamGB": 32, "sizeGB": 35, "notes": "FILLED IN TASK 6 FROM THE TEST RENDER"}
      }
    }
  ]
}
```

Verify the MSR LoRA download URL before shipping:
```bash
curl -sIL -m 20 "https://huggingface.co/LiconStudio/LTX-2.5-MSR/resolve/main/LTX-2.5-Licon-MSR-V1.safetensors" | grep -i "^HTTP\|content-length" | tail -2
```
Expected: a `200` and `content-length: 1308840536`. If not, find the URL the official pack uses: `grep -o '"url": "[^"]*Licon-MSR-V1[^"]*"' /f/SimpliGen/presets/ltx-2.5-video-pack.json` and use that.

- [ ] **Step 2: Register the MSR classes in build-zips.py**

Add to `CUSTOM_NODES`:
```python
    'ComfyUILTX25MSRICLoRALoader': {
        'name': 'ComfyUI-LTX2.5-MSR',
        'url': 'https://github.com/liconstudio/ComfyUI-LTX2.5-MSR.git',
        'note': 'Multiple Subject Reference loader + guide for LTX 2.5. Installed by SimpliGen for its official LTX 2.5 Multi-Reference preset; otherwise clone into ComfyUI/custom_nodes.',
    },
    'ComfyUILTX25MSRMultiReferenceGuide': { ...same dict... },
```
Match the field names the other entries use (open one and copy its keys exactly).

- [ ] **Step 3: Placeholder preview, install, restart**

```bash
mkdir -p packs/ltx-2-5-refine/previews
cp packs/ltx-2-5-a2v/previews/ltx-2-5-a2v-int8.jpg packs/ltx-2-5-refine/previews/ltx-2-5-refine-msr.jpg
cp packs/ltx-2-5-refine/ltx-2-5-refine-pack.json /f/SimpliGen/presets/community--ltx-2-5-refine-pack.json
cp packs/ltx-2-5-refine/workflows/ltx_2_5_refine_msr.json /f/SimpliGen/presets/workflows/
cp packs/ltx-2-5-refine/previews/ltx-2-5-refine-msr.jpg /f/SimpliGen/presets/previews/
powershell -NoProfile -Command "Stop-Process -Name SimpliGen -Force -ErrorAction SilentlyContinue; Start-Sleep 3; Start-Process 'C:\Users\micha\AppData\Local\Programs\simpligen\SimpliGen.exe'"
```
Wait ~60 s; `get_status` shows `engineRunning: true`; `list_capabilities` shows `ltx-2-5-refine-msr` with `localReady: true` (else `prepare_preset`).

- [ ] **Step 4: Commit**

```bash
git add packs/ltx-2-5-refine build-zips.py
git commit -m "feat(wip): LTX 2.5 Video Refine pack JSON

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 6: Pack 2 verification render, preview, notes

**Files:**
- Modify: `packs/ltx-2-5-refine/ltx-2-5-refine-pack.json`
- Replace: `packs/ltx-2-5-refine/previews/ltx-2-5-refine-msr.jpg`

- [ ] **Step 1: Render at 1080p with the Ekello sheet as Face 1**

Upload the same 5 s PDD R2V clip and `F:\SimpliGen\output\community--krea2-finetunes-packmuse-krea2-v35-extended\2026-09-07_00001_.png`. Generate:
```json
{"mediaType": "video", "backend": "local",
 "packId": "community--ltx-2-5-refine-pack",
 "presetId": "community--ltx-2-5-refine-pack:ltx-2-5-refine-msr",
 "referenceVideos": ["<clip handle>"], "referenceImages": ["<sheet handle>"],
 "prompt": "A bald man with a grey goatee and black over-ear headphones, in a dark navy t-shirt, sits at a podcast desk in a small studio with a condenser microphone on a boom arm, acoustic foam panels behind him and a warm desk lamp. He lifts the headphones onto his ears, glances at the camera and nods slowly. Static medium close-up, soft warm key light, realistic cinematic footage.",
 "negativePrompt": "",
 "options": {"aspectRatio": "16:9", "resolution": "1080p", "durationSeconds": 5, "seed": 20260907, "cfg": 1}}
```
Watch `/f/SimpliGen/output/community--ltx-2-5-refine-packltx-2-5-refine-msr/` for the MP4 and grep the session log for `Prompt executed in` and `Traceback`.

- [ ] **Step 2: Check size, audio, faces**

Same ffprobe / volumedetect / 6-frame sheet as Task 3 Step 2. Expected `width=1920|height=1088`, `nb_frames=121`, audio peak within 3 dB of `-21.8 dB`. Compare the sheet to the PDD R2V sheet: same man, same action. If the face drifts, change `refine_sigmas` to `"0.7250, 0.4219, 0.0"` and re-run once; record which shipped. If the MSR guide errors on latent shape, set `refine_msr.use_tiled_encode` to `true` and re-run.

- [ ] **Step 3: Preview, notes, durable copy**

```bash
v=$(ls /f/SimpliGen/output/community--ltx-2-5-refine-packltx-2-5-refine-msr/*.mp4 | head -1)
ffmpeg -v error -y -ss 3.5 -i "$v" -frames:v 1 -q:v 3 packs/ltx-2-5-refine/previews/ltx-2-5-refine-msr.jpg
cp "$v" /c/Users/micha/AppData/Local/Temp/refine_msr_5s_sheet.jpg /d/SimpliGen-Backups/video-refine-verify-20260907/
```
Fill `requirements.notes`: `Measured 2026-09-07 on a 12 GB RTX 4070 Ti, engine ComfyUI 0.34.2: 864x480 H3 clip -> 1920x1088 in <N> s for 5 s, one reference face, sigmas <shipped list>. Shares every LTX 2.5 file with the A2V and official LTX packs; the only new download is the 1.3 GB MSR V1 LoRA. Duration follows the source clip up to 15 s. Gated HF repo: needs an API key and licence acceptance.` Replace `see the pack notes for the numbers` in the preset description with `5 s to 1080p in <N> s`.

- [ ] **Step 4: Commit**

```bash
git add packs/ltx-2-5-refine
git commit -m "feat: LTX 2.5 Video Refine (MSR) pack 1.0.0 - verified in-app

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 7: Docs, zips, release, push

**Files:**
- Modify: `README.md` (video packs table, after the `MiniMax H3 (Two-Stage Latent Upscale)` row; hero/catalog counts to 37 packs / 123 presets in `README.md:2`, `README.md:12`, `assets/readme/hero.svg:12`, `assets/readme/section-catalog.svg:3,7`)
- Modify: `CUSTOM-PRESET-AUTHORING-GUIDE.md:304` (two rows after the PDD Acc row)

- [ ] **Step 1: README rows**

Insert after the Two-Stage row:
```markdown
| MiniMax H3 (Video Refine) | 1 | MiniMax H3 (pruned INT8) | **Video in, video out.** Drop a finished H3 clip in Reference Video 1 and paste its brief; it comes back at 672p or 768p with its own soundtrack. LBH-123-AI's 3D latent upscaler, then Alibaba's official PDD 8-step distill at denoise 0.25 in 73-frame windows, so up to 15 s runs in one queue. Same model family, so H3's look and cast survive; it cannot repair a face the source lost. Verified 2026-09-07: 864x480 to 1344x768, 5 s in <N5> s, 10 s in <N10> s on a 4070 Ti. Shares the ref2va base with every R2V pack; adds the 1.37 GB Ref2VA distill |
| LTX 2.5 (Video Refine, MSR) | 1 | LTX 2.5 distilled 22B | **Video in, video out, any source.** Upscales a clip to 720p or 1080p in LTX 2.5 with one to four face pictures held by Licon's Multi-Subject-Reference LoRA. Crisper, more LTX-looking than the H3 refine; prompt must be LTX style. Source audio muxed back untouched. Verified 2026-09-07: 864x480 to 1920x1088, 5 s in <N> s on a 4070 Ti. Reuses the official gated LTX 2.5 weights; adds the 1.3 GB MSR V1 LoRA |
```
Update every `35 packs` to `37 packs` and `121 presets`/`121 ready-to-run presets` to `123` in the files listed above (the catalog SVG's `<desc>` says 120; set it to 123).

- [ ] **Step 2: Authoring guide rows**

After the PDD Acc row at `CUSTOM-PRESET-AUTHORING-GUIDE.md:304` add:
```markdown
| MiniMax H3 Video Refine (V2V) | euler, PDD scheduler denoise 0.25 | 8 grid (2 run) | 1 | Source clip via `{{ref_video_1}}`, H3 VAE encode, LBH 3D latent upscale to the tier, MMH3SplitUpscale 73/22 windows, source audio muxed back |
| LTX 2.5 Video Refine (V2V, MSR) | euler, manual sigmas (A2V stage-2 tail) | 3 | 1 | Source scaled to half tier, LTX VAE encode, 2x latent upsampler, MSR guide (pic1 required), audio latent masked, source audio muxed back |
```

- [ ] **Step 3: Build zips, upload, push**

```bash
uv run python build-zips.py 2>&1 | grep -i "refine\|built\|skipped"
gh auth switch -u michaeldune
gh release upload packs-latest /d/SimpliGen-Backups/zips/community-minimax-h3-refine.zip /d/SimpliGen-Backups/zips/community-ltx-2-5-refine.zip --clobber --repo michaeldune/simpligen-presets
gh release view packs-latest --repo michaeldune/simpligen-presets --json assets -q '.assets[] | select(.name|test("refine")) | "\(.name) \(.size) \(.updatedAt)"'
gh auth switch -u michaelkpate
ssh -T git@github.com-dune 2>&1 | head -1
git add README.md CUSTOM-PRESET-AUTHORING-GUIDE.md assets/readme docs/superpowers
git commit -m "feat: Video Refine packs (H3 PDD + LTX 2.5 MSR) - 37 packs / 123 presets

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push origin master
git log --oneline origin/master -1
```
Expected: `37 zip(s) built, 0 skipped.`, two refine assets dated today, `Hi michaeldune!`, push succeeds.

- [ ] **Step 4: Memory**

Update the `pdd-acc-pack-released` memory file: replace the "Open idea" paragraph with the two pack ids, the verified timings and the shipped sigma/denoise values, and note that Reference Video 1 is passed to the MCP as `referenceVideos` (or `video`, whichever worked in Task 3).
