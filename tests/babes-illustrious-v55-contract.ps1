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
