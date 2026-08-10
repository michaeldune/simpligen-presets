# Babes Illustrious v5.5 FP16 Preset Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add, install, and successfully load a complete Babes Illustrious v5.5 FP16 preset in the existing Community — Illustrious Realism pack.

**Architecture:** Extend the existing pack with one new declarative preset, a flat ComfyUI API workflow, and a repository contract test. Reuse the pack installer while adding an idempotent checkpoint copy, then validate the installed state and use SimpliGen itself for the final load and generation checks.

**Tech Stack:** JSON, ComfyUI API workflow nodes, Windows batch, PowerShell 7/5.1-compatible validation, JPEG preview assets, SimpliGen/ComfyUI.

## Global Constraints

- Work only inside `C:\Users\micha\Projects\dune\simpligen-presets` except for reading the supplied checkpoint and installing into SimpliGen's `%APPDATA%` directories.
- Preserve the pack ID `illustrious-realism-pack` and all existing presets.
- Use preset ID `babes-illustrious-v55-fp16` and checkpoint filename `babesIllustriousBy_v55FP16.safetensors` consistently.
- Use CLIP skip 2 and the exact node ID `simpligen_lora_1` with class `Power Lora Loader (rgthree)` and title `SimpliGen User LoRAs`.
- Store JSON as UTF-8 without BOM and preserve the exact Unicode key `➕ Add Lora`.
- Use a 640×640 JPEG preview without text, logos, or watermarks.
- Do not report completion until the installed preset loads successfully and a test generation produces an image.

---

### Task 1: Add the preset contract test

**Files:**
- Create: `tests/babes-illustrious-v55-contract.ps1`

**Interfaces:**
- Consumes: the existing pack path and the agreed preset/workflow/preview/checkpoint identifiers.
- Produces: an executable repository contract that exits zero only when source artifacts, encoding, wiring, placeholders, and cross-references are valid.

- [ ] **Step 1: Write the failing contract test**

Create a PowerShell test that:

```powershell
$ErrorActionPreference = 'Stop'
$repo = Split-Path $PSScriptRoot -Parent
$packPath = Join-Path $repo 'packs\illustrious-realism\illustrious-realism-pack.json'
$packBytes = [IO.File]::ReadAllBytes($packPath)
if ($packBytes.Length -ge 3 -and $packBytes[0] -eq 0xEF -and $packBytes[1] -eq 0xBB -and $packBytes[2] -eq 0xBF) { throw 'Pack JSON has a UTF-8 BOM.' }
$pack = [Text.Encoding]::UTF8.GetString($packBytes) | ConvertFrom-Json
$preset = @($pack.presets | Where-Object id -eq 'babes-illustrious-v55-fp16')
if ($preset.Count -ne 1) { throw 'Expected exactly one Babes Illustrious v5.5 preset.' }
$preset = $preset[0]
if ($preset.image.checkpoint -ne 'babesIllustriousBy_v55FP16.safetensors') { throw 'Checkpoint filename mismatch.' }
if ($preset.image.workflow -ne 'workflows/babes-illustrious-v55-fp16.json') { throw 'Workflow reference mismatch.' }
if ($preset.previewImage -ne 'previews/babes-illustrious-v55-fp16.jpg') { throw 'Preview reference mismatch.' }
if ($preset.image.steps -ne 24 -or $preset.image.cfg -ne 4.5) { throw 'Preset defaults mismatch.' }
if ($preset.image.resolutionOverrides.'4:5'.width -ne 896 -or $preset.image.resolutionOverrides.'4:5'.height -ne 1120) { throw 'Native portrait resolution mismatch.' }

$workflowPath = Join-Path (Join-Path $repo 'packs\illustrious-realism') $preset.image.workflow
$workflowBytes = [IO.File]::ReadAllBytes($workflowPath)
if ($workflowBytes.Length -ge 3 -and $workflowBytes[0] -eq 0xEF -and $workflowBytes[1] -eq 0xBB -and $workflowBytes[2] -eq 0xBF) { throw 'Workflow JSON has a UTF-8 BOM.' }
$workflowText = [Text.Encoding]::UTF8.GetString($workflowBytes)
$workflow = $workflowText | ConvertFrom-Json
$lora = $workflow.'simpligen_lora_1'
if ($lora.class_type -ne 'Power Lora Loader (rgthree)' -or $lora._meta.title -ne 'SimpliGen User LoRAs') { throw 'LoRA marker contract mismatch.' }
if ($lora.inputs.'➕ Add Lora' -ne '') { throw 'Unicode LoRA key is missing or changed.' }
if ($workflow.'10'.inputs.stop_at_clip_layer -ne -2) { throw 'CLIP skip must be 2.' }
if ($workflow.'6'.inputs.clip[0] -ne '10' -or $workflow.'7'.inputs.clip[0] -ne '10') { throw 'Both encoders must use CLIP skip.' }
if ($workflow.'3'.inputs.model[0] -ne 'simpligen_lora_1') { throw 'Sampler must use the LoRA-routed model.' }
if ($workflow.'3'.inputs.sampler_name -ne 'dpmpp_2m_sde' -or $workflow.'3'.inputs.scheduler -ne 'karras') { throw 'Sampler contract mismatch.' }

$previewPath = Join-Path (Join-Path $repo 'packs\illustrious-realism') $preset.previewImage
if (-not (Test-Path -LiteralPath $previewPath)) { throw 'Preview is missing.' }
Add-Type -AssemblyName System.Drawing
$image = [Drawing.Image]::FromFile($previewPath)
try { if ($image.Width -ne 640 -or $image.Height -ne 640) { throw 'Preview must be 640x640.' } } finally { $image.Dispose() }

$allowed = @('checkpoint','prompt','negative_prompt','width','height','seed','steps','cfg','denoise')
$matches = [regex]::Matches($workflowText, '\{\{([a-z_]+)\}\}')
$unknown = @($matches | ForEach-Object { $_.Groups[1].Value } | Sort-Object -Unique | Where-Object { $_ -notin $allowed })
if ($unknown.Count -gt 0) { throw "Unknown workflow placeholders: $($unknown -join ', ')" }

$installer = Get-Content -Raw (Join-Path $repo 'packs\illustrious-realism\install-illustrious-realism.cmd')
if ($installer -notmatch [regex]::Escape('babesIllustriousBy_v55FP16.safetensors')) { throw 'Installer does not reference the checkpoint.' }
Write-Host 'Babes Illustrious v5.5 source contract passed.'
```

- [ ] **Step 2: Run the contract and confirm it fails**

Run: `pwsh -NoProfile -File tests/babes-illustrious-v55-contract.ps1`

Expected: nonzero exit with `Expected exactly one Babes Illustrious v5.5 preset.`

- [ ] **Step 3: Commit the failing test**

Run:

```powershell
git add tests/babes-illustrious-v55-contract.ps1
git commit -m "test: define Babes Illustrious preset contract"
```

Expected: one commit containing only the new contract test.

---

### Task 2: Add the pack entry and API workflow

**Files:**
- Modify: `packs/illustrious-realism/illustrious-realism-pack.json`
- Create: `packs/illustrious-realism/workflows/babes-illustrious-v55-fp16.json`

**Interfaces:**
- Consumes: identifiers and settings enforced by `tests/babes-illustrious-v55-contract.ps1`.
- Produces: a SimpliGen preset entry and workflow whose paths and runtime placeholders agree exactly.

- [ ] **Step 1: Append the preset entry**

Add exactly one preset with these required values:

```json
{
  "id": "babes-illustrious-v55-fp16",
  "name": "Babes Illustrious v5.5 FP16",
  "tagline": "Natural portrait realism with flexible LoRA blending",
  "icon": "📷",
  "previewImage": "previews/babes-illustrious-v55-fp16.jpg",
  "description": "Stable Yogi's Illustrious v5.5 FP16 checkpoint, tuned for realistic skin, diverse faces, stronger anatomy, and controlled portrait lighting.",
  "tags": ["Illustrious", "Realistic", "Photoreal", "SDXL", "Local"],
  "enabled": true,
  "template": "sdxl",
  "ui": { "visibleFields": ["content", "aspectRatio", "shotType", "environment", "lightingSource", "atmosphere"] },
  "image": {
    "supports": ["local"],
    "provider": "comfyui",
    "displayModel": "Babes Illustrious v5.5 FP16",
    "baseModels": ["illustrious", "sdxl"],
    "workflow": "workflows/babes-illustrious-v55-fp16.json",
    "checkpoint": "babesIllustriousBy_v55FP16.safetensors",
    "steps": 24,
    "cfg": 4.5,
    "denoise": 1,
    "negativePrompt": "lowres, worst quality, low quality, bad anatomy, bad hands, missing fingers, extra fingers, extra digits, fewer digits, malformed limbs, deformed, disfigured, blurry, jpeg artifacts, signature, watermark, username, text, logo, cartoon, illustration, 3d render",
    "resolutionOverrides": {
      "1:1": {"width": 1024, "height": 1024},
      "2:3": {"width": 832, "height": 1216},
      "3:2": {"width": 1216, "height": 832},
      "3:4": {"width": 896, "height": 1152},
      "4:3": {"width": 1152, "height": 896},
      "4:5": {"width": 896, "height": 1120},
      "9:16": {"width": 768, "height": 1344},
      "16:9": {"width": 1344, "height": 768}
    },
    "controls": {
      "steps": {"min": 18, "max": 27, "step": 1},
      "cfg": {"min": 4, "max": 5, "step": 0.1}
    },
    "requirements": {
      "minVramGB": 8,
      "recommendedVramGB": 12,
      "minRamGB": 16,
      "sizeGB": 6.5,
      "notes": "Illustrious/SDXL full checkpoint with baked VAE, CLIP Skip 2, and DPM++ 2M SDE / Karras defaults."
    }
  }
}
```

- [ ] **Step 2: Create the flat API workflow**

Create nodes `4`, `10`, `simpligen_lora_1`, `5`, `6`, `7`, `3`, `8`, and `9`. Route checkpoint model/CLIP into the LoRA marker, LoRA CLIP into node `10` with `stop_at_clip_layer: -2`, both encoders into node `10`, sampler model into the LoRA marker, and VAE decode into checkpoint output 2. Use `dpmpp_2m_sde`/`karras` and the runtime placeholders specified in the global constraints.

- [ ] **Step 3: Run syntax and partial contract checks**

Run:

```powershell
Get-Content -Raw packs/illustrious-realism/illustrious-realism-pack.json | ConvertFrom-Json | Out-Null
Get-Content -Raw packs/illustrious-realism/workflows/babes-illustrious-v55-fp16.json | ConvertFrom-Json | Out-Null
pwsh -NoProfile -File tests/babes-illustrious-v55-contract.ps1
```

Expected: both JSON parses succeed; the contract advances past preset/workflow assertions and fails only because the preview or installer update is not present yet.

- [ ] **Step 4: Commit pack and workflow**

Run:

```powershell
git add packs/illustrious-realism/illustrious-realism-pack.json packs/illustrious-realism/workflows/babes-illustrious-v55-fp16.json
git commit -m "feat: add Babes Illustrious v5.5 preset"
```

---

### Task 3: Add the preview image

**Files:**
- Create: `packs/illustrious-realism/previews/babes-illustrious-v55-fp16.jpg`

**Interfaces:**
- Consumes: a clean representative model showcase image and the preview path from the pack entry.
- Produces: a 640×640 JPEG card asset.

- [ ] **Step 1: Select and inspect a clean showcase**

Choose a representative v5.5 image from the creator/model listing with no visible text, watermark, or logo and the lowest practical content rating. Inspect the downloaded source visually before processing it.

- [ ] **Step 2: Center-crop and encode the preview**

Use `System.Drawing` with a `MemoryStream` to center-crop the source to a square, resize to 640×640, and save JPEG at quality 90 to the exact path above. Do not retain the full-size source in the repository.

- [ ] **Step 3: Verify dimensions and source contract progression**

Run: `pwsh -NoProfile -File tests/babes-illustrious-v55-contract.ps1`

Expected: the preview assertions pass; the test fails only on the installer checkpoint reference.

- [ ] **Step 4: Commit the preview**

Run:

```powershell
git add packs/illustrious-realism/previews/babes-illustrious-v55-fp16.jpg
git commit -m "assets: add Babes Illustrious preview"
```

---

### Task 4: Make the installer copy and validate the checkpoint

**Files:**
- Modify: `packs/illustrious-realism/install-illustrious-realism.cmd`

**Interfaces:**
- Consumes: the source checkpoint in `%USERPROFILE%\Downloads`, and all pack-local JSON/JPEG artifacts.
- Produces: repeatable installed files under `%APPDATA%\simpligen\engine\models\checkpoints` and `%APPDATA%\simpligen\presets`.

- [ ] **Step 1: Add checkpoint variables and preflight**

Define:

```bat
set "SOURCE=%USERPROFILE%\Downloads\babesIllustriousBy_v55FP16.safetensors"
set "ENGINE=%APPDATA%\simpligen\engine\models"
set "PRESETS=%APPDATA%\simpligen\presets"
if not exist "%SOURCE%" goto :missing
```

- [ ] **Step 2: Add idempotent directory creation and guarded copies**

Ensure `checkpoints`, `workflows`, and `previews` exist. Copy the checkpoint, pack JSON, all workflows, and all previews with `/Y`, and append `|| goto :error` to every copy. Preserve the BOM-free preview rewrite, then check its exit status with `if errorlevel 1 goto :error`.

- [ ] **Step 3: Add explicit success and failure exits**

The success path must print that the pack was restored and request a SimpliGen restart, then `exit /b 0`. `:missing` and `:error` must print actionable messages and `exit /b 1` after any pause.

- [ ] **Step 4: Run the complete source contract**

Run: `pwsh -NoProfile -File tests/babes-illustrious-v55-contract.ps1`

Expected: `Babes Illustrious v5.5 source contract passed.` and exit code 0.

- [ ] **Step 5: Commit installer changes**

Run:

```powershell
git add packs/illustrious-realism/install-illustrious-realism.cmd
git commit -m "feat: install Babes Illustrious checkpoint"
```

---

### Task 5: Install and validate installed artifacts

**Files:**
- Installed output: `%APPDATA%\simpligen\presets\illustrious-realism-pack.json`
- Installed output: `%APPDATA%\simpligen\presets\workflows\babes-illustrious-v55-fp16.json`
- Installed output: `%APPDATA%\simpligen\presets\previews\babes-illustrious-v55-fp16.jpg`
- Installed output: `%APPDATA%\simpligen\engine\models\checkpoints\babesIllustriousBy_v55FP16.safetensors`

**Interfaces:**
- Consumes: the completed source pack and installer.
- Produces: the exact installed state consumed by SimpliGen.

- [ ] **Step 1: Run the installer non-interactively**

Invoke `packs\illustrious-realism\install-illustrious-realism.cmd` with input redirected so its pause does not block automation. Immediately check the native process exit code.

Expected: exit code 0 and the pack-restored message.

- [ ] **Step 2: Validate installed files and encodings**

Verify all four installed paths exist and are non-empty. Parse installed pack/workflow JSON; reject a leading `EF BB BF`; confirm exactly one matching preset; confirm the preview URL equals `local-file:///` plus the normalized absolute installed preview path; and confirm installed checkpoint length equals the source length.

- [ ] **Step 3: Run the installer a second time**

Expected: exit code 0, unchanged preset count, same checkpoint filename and length, and no duplicate artifacts.

---

### Task 6: Restart SimpliGen and prove runtime success

**Files:**
- Inspect: newest `%APPDATA%\simpligen\logs\session-*.log`
- Inspect: generated output image path reported by SimpliGen/ComfyUI

**Interfaces:**
- Consumes: installed preset artifacts and the fully restarted SimpliGen application.
- Produces: evidence that SimpliGen loaded the pack and the workflow generated an image.

- [ ] **Step 1: Fully restart SimpliGen**

Close the running SimpliGen process cleanly and relaunch it so the model and preset caches refresh. Do not terminate unrelated processes.

- [ ] **Step 2: Inspect the new session log**

Confirm the newest log was created after restart, contains a successful preset-pack load count, and contains no `Failed to load preset pack`, JSON parse error, missing checkpoint, missing node, or unresolved-placeholder error involving `illustrious-realism-pack` or `babes-illustrious-v55-fp16`.

- [ ] **Step 3: Run a test generation**

Select `Babes Illustrious v5.5 FP16`, use a benign adult portrait prompt, the default 896×1120 portrait setting, 24 steps, and CFG 4.5. Submit one image with no user LoRA selected.

Expected: the job completes and produces a readable, non-empty image file.

- [ ] **Step 4: Record final verification evidence**

Record the relevant log filename/time, successful pack-load evidence, generated image path/dimensions, and final source contract result. Report any failure plainly and continue diagnosis rather than claiming completion.
