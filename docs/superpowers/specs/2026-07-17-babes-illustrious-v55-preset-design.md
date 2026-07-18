# Babes Illustrious v5.5 FP16 Preset Design

## Goal

Add Babes Illustrious by Stable Yogi v5.5 FP16 to the existing `Community — Illustrious Realism` SimpliGen pack. The completed preset must install the local checkpoint, appear with a working preview, load without preset errors, expose SimpliGen user LoRAs, and complete a test generation.

## Source Model

- Source checkpoint: `C:\Users\micha\Downloads\babesIllustriousBy_v55FP16.safetensors`
- Installed checkpoint filename: `babesIllustriousBy_v55FP16.safetensors`
- Architecture: full Illustrious/SDXL checkpoint with baked VAE
- Creator: Stable Yogi
- Variant: v5.5 FP16
- Size: approximately 6.5 GiB
- Published guidance: CLIP skip 2, 18–27 steps, CFG 4–5, DPM++ SDE-family samplers, any SDXL resolution, with 896×1120 recommended for portrait output

The checkpoint header contains SDXL-style `conditioner.embedders.*` keys and `first_stage_model.*` data. Its embedded descriptive metadata is stale and incorrectly labels the model as Z-Image Turbo, so architecture and settings will follow the tensor structure and published v5.5 model documentation rather than that metadata field.

## Pack Integration

Extend `packs/illustrious-realism/illustrious-realism-pack.json` without changing its pack ID or existing presets.

The new preset will use:

- ID: `babes-illustrious-v55-fp16`
- Name: `Babes Illustrious v5.5 FP16`
- Family tags: Illustrious, Realistic, Photoreal, SDXL, Local
- Template: `sdxl`
- Provider: `comfyui`
- Base models: `illustrious`, `sdxl`
- Workflow: `workflows/babes-illustrious-v55-fp16.json`
- Preview: `previews/babes-illustrious-v55-fp16.jpg`
- Default steps: 24
- Default CFG: 4.5
- Denoise: 1

The preset will retain the existing pack’s visible UI fields and use a practical realism negative prompt covering quality defects, anatomy errors, text, signatures, watermarks, and obvious non-photographic rendering.

Resolution overrides will preserve the pack’s standard SDXL buckets. The portrait-oriented entry will include the creator-recommended 896×1120 4:5 resolution while retaining common 1:1, 2:3, 3:2, 3:4, 4:3, 9:16, and 16:9 choices.

## Workflow

Create a flat ComfyUI API-format workflow using only nodes expected in the bundled engine:

1. `CheckpointLoaderSimple` loads `{{checkpoint}}`.
2. `simpligen_lora_1`, class `Power Lora Loader (rgthree)`, receives the checkpoint model and CLIP outputs.
3. `CLIPSetLastLayer` applies CLIP skip 2 (`-2`) to the LoRA-routed CLIP output.
4. Positive and negative `CLIPTextEncode` nodes both use the CLIP-skip output.
5. `EmptyLatentImage` receives runtime width and height placeholders.
6. `KSampler` uses DPM++ 2M SDE with Karras scheduling, runtime seed/steps/CFG/denoise, and the LoRA-routed model.
7. `VAEDecode` uses the baked checkpoint VAE.
8. `SaveImage` uses `babes-illustrious-v55-fp16` as its filename prefix.

The positive prompt will prepend a restrained Illustrious quality prefix: `masterpiece, best quality, amazing quality, ultra detailed, realistic photo`. No external VAE, upscaler, embedding, or custom node beyond the bundled rgthree loader is required.

## Preview

Use a clean, representative v5.5 showcase image with no text, logo, or watermark and the lowest practical content rating. Convert it to a centered 640×640 JPEG at approximately quality 90. Keep the source pack reference relative; the installer will rewrite the installed reference to an absolute `local-file:///` URL.

## Installer

Update `packs/illustrious-realism/install-illustrious-realism.cmd` to remain idempotent and preserve its current restore-all-pack behavior while adding checkpoint installation:

- Read the checkpoint from the user’s Downloads folder.
- Create the checkpoint, workflow, preview, and preset destinations when absent.
- Copy the checkpoint with overwrite enabled.
- Copy the pack JSON, all pack workflows, and all pack previews.
- Rewrite every installed preview path to an absolute local-file URL.
- Write JSON as UTF-8 without BOM.
- Fail with a nonzero exit code when required input is missing or a copy/rewrite operation fails.

Repeated runs will produce the same installed state without duplicate preset entries or renamed model files.

## Validation and Acceptance

Before installation:

- Parse the pack and all workflow JSON files.
- Verify UTF-8 without BOM and intact Unicode keys, including `➕ Add Lora`.
- Verify the preset ID, workflow filename, preview filename, checkpoint filename, installer source, and installer destinations agree exactly.
- Verify every workflow placeholder is either a SimpliGen runtime placeholder or supplied by the pack entry.
- Verify both text encoders route through CLIP skip 2 and the sampler routes through `simpligen_lora_1`.
- Verify the preview is JPEG, 640×640, and reasonably small.

After installation:

- Verify the checkpoint exists under SimpliGen’s checkpoint directory.
- Verify the installed pack, workflow, and preview exist in their expected preset directories.
- Verify the installed pack has an absolute preview URL and no BOM.
- Fully restart SimpliGen so its model and preset caches refresh.
- Inspect the newest session log for successful preset-pack loading and absence of load errors involving the pack or preset.
- Run a test generation and confirm an output image is produced.

Completion may only be reported after the installed preset loads successfully and the test generation succeeds.
