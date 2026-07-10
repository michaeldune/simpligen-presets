# PhotAnima v2.3 Compatibility Update

## Scope

Update the existing `photanima-v22-turbo` preset in the Anima Realism pack to use the locally downloaded PhotAnima v2.3 Turbo UNet.

## Approach

Keep the existing SimpliGen-compatible Anima workflow: Qwen 0.6B text encoder, Qwen-Image VAE, AuraFlow sampling shift 3, ER-SDE/simple sampler, 12 steps, and CFG 1. The v2.3 SafeTensors header confirms the same Anima/Qwen architecture, so no workflow or dependency changes are required.

## Changes

- Rename the preset and its workflow/preview identifiers from `v22` to `v23`.
- Change the UNet filename to `photanima_v23Turbo.safetensors`.
- Change the Civitai download reference to model version `3112450`.
- Copy the supplied model into SimpliGen's `diffusion_models` folder.
- Update the installed pack and workflow together with the source pack.

## Validation

- Confirm JSON is valid UTF-8 without a BOM and all source/installed references resolve.
- Confirm the engine indexes the v2.3 UNet.
- Submit a 1024 by 1024 test generation through the local ComfyUI API and inspect its output.
