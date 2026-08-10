# PhotAnima v2.3 Compatibility Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace PhotAnima v2.2 Turbo with the supplied v2.3 Turbo Anima UNet while retaining the working SimpliGen workflow.

**Architecture:** Retain the existing Anima workflow: Qwen 0.6B text encoder, Qwen-Image VAE, AuraFlow shift 3, and ER-SDE/simple sampling. Update only versioned asset names and metadata, then mirror the same files into SimpliGen's installed preset folder.

**Tech Stack:** JSON preset packs, ComfyUI API-format workflow JSON, PowerShell validation, SimpliGen local ComfyUI API.

## Global Constraints

- Preserve Qwen 0.6B text encoder, Qwen-Image VAE, AuraFlow shift `3`, ER-SDE/simple, `12` steps, and CFG `1`.
- Use `photanima_v23Turbo.safetensors` from `C:\Users\micha\Downloads` in the `diffusion_models` folder.
- Use Civitai model version `3112450`.
- Write JSON as UTF-8 without a BOM.
- Keep source and installed packs/workflows synchronized.
- Validate with a local 1024 by 1024 generation.

---

### Task 1: Establish and run the preset contract

**Files:**
- Create: `C:\Users\micha\Projects\SimpliGen\tests\photanima-v23-contract.ps1`
- Modify: `C:\Users\micha\Projects\SimpliGen\packs\anima-realism\anima-realism-pack.json`
- Create: `C:\Users\micha\Projects\SimpliGen\packs\anima-realism\workflows\photanima-v23-turbo.json`

**Interfaces:**
- Consumes: the current v2.2 source preset and `C:\Users\micha\Downloads\photanima_v23Turbo.safetensors`.
- Produces: a v2.3 source preset whose model, workflow, and turbo settings are asserted by a repeatable validation script.

- [ ] **Step 1: Write the failing contract test**

```powershell
$ErrorActionPreference = 'Stop'
$repo = 'C:\Users\micha\Projects\SimpliGen'
$pack = Get-Content -Raw "$repo\packs\anima-realism\anima-realism-pack.json" | ConvertFrom-Json
$preset = $pack.presets | Where-Object id -eq 'photanima-v23-turbo'
if ($null -eq $preset) { throw 'PhotAnima v2.3 preset is missing.' }
if ($preset.image.unet -ne 'photanima_v23Turbo.safetensors') { throw 'v2.3 UNet filename is incorrect.' }
if ($preset.image.unetUrl -ne 'https://civitai.com/api/download/models/3112450') { throw 'v2.3 download URL is incorrect.' }
if ($preset.image.steps -ne 12 -or $preset.image.cfg -ne 1) { throw 'Turbo defaults changed.' }
$workflow = Get-Content -Raw (Join-Path "$repo\packs\anima-realism" $preset.image.workflow) | ConvertFrom-Json
if ($workflow.'7'.inputs.sampler_name -ne 'er_sde' -or $workflow.'7'.inputs.scheduler -ne 'simple') { throw 'Sampler contract changed.' }
if ($workflow.'2'.inputs.shift -ne 3) { throw 'AuraFlow shift changed.' }
if ((Get-Item 'C:\Users\micha\Downloads\photanima_v23Turbo.safetensors').Length -lt 4GB) { throw 'Supplied v2.3 model is unexpectedly small.' }
Write-Host 'PhotAnima v2.3 contract is valid.'
```

- [ ] **Step 2: Run it and verify it fails**

Run: `powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\micha\Projects\SimpliGen\tests\photanima-v23-contract.ps1`

Expected: failure with `PhotAnima v2.3 preset is missing.`

- [ ] **Step 3: Apply the minimal source update**

Rename the existing preset ID, name, preview reference, display name, description, workflow reference, and save-image prefix from `v22` to `v23`. Set `image.unet` to `photanima_v23Turbo.safetensors` and `image.unetUrl` to `https://civitai.com/api/download/models/3112450`. Copy the v2.2 workflow and preview under v2.3 names, preserving all node wiring and sampler settings.

- [ ] **Step 4: Run the contract test and verify it passes**

Run: `powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\micha\Projects\SimpliGen\tests\photanima-v23-contract.ps1`

Expected: `PhotAnima v2.3 contract is valid.`

- [ ] **Step 5: Commit the source change**

```powershell
git add tests/photanima-v23-contract.ps1 packs/anima-realism/anima-realism-pack.json packs/anima-realism/workflows/photanima-v23-turbo.json packs/anima-realism/previews/photanima-v23-turbo.jpg
git commit -m "feat: update PhotAnima Turbo preset to v2.3"
```

### Task 2: Install and verify the v2.3 preset

**Files:**
- Modify: `%APPDATA%\simpligen\presets\anima-realism-pack.json`
- Create: `%APPDATA%\simpligen\presets\workflows\photanima-v23-turbo.json`
- Create: `%APPDATA%\simpligen\presets\previews\photanima-v23-turbo.jpg`
- Create: `%APPDATA%\simpligen\engine\models\diffusion_models\photanima_v23Turbo.safetensors`

**Interfaces:**
- Consumes: source assets verified by Task 1.
- Produces: an installed v2.3 preset and one successful 1024 by 1024 local ComfyUI generation.

- [ ] **Step 1: Copy and rewrite installed assets**

Copy the supplied UNet to the installed `diffusion_models` folder. Copy v2.3 workflow and preview to installed folders. Update the installed pack to its v2.3 object and set its preview URL to `local-file:///$env:APPDATA/simpligen/presets/previews/photanima-v23-turbo.jpg`.

- [ ] **Step 2: Validate installed JSON**

Parse both installed JSON files, verify neither begins with `EF BB BF`, verify `photanima-v23-turbo` has the v2.3 UNet filename, and verify its workflow file and preview URL resolve.

- [ ] **Step 3: Generate and inspect an image**

Substitute a non-empty natural-language portrait prompt, empty negative prompt, `1024` width and height, seed `12345`, `12` steps, CFG `1`, and denoise `1` into the installed API workflow. Submit it to `http://127.0.0.1:8199/prompt`, poll its history until completion, and inspect the returned PNG for a complete nonblank image with no node error.

- [ ] **Step 4: Commit any changed verification script**

```powershell
git add tests/photanima-v23-contract.ps1
git commit -m "test: verify PhotAnima v2.3 preset installation"
```
