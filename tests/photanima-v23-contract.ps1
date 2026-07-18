$ErrorActionPreference = 'Stop'

$repo = Split-Path -Parent $PSScriptRoot
$packPath = Join-Path $repo 'packs\anima-realism\anima-realism-pack.json'
$pack = Get-Content -Raw $packPath | ConvertFrom-Json
$preset = $pack.presets | Where-Object id -eq 'photanima-v23-turbo'

if ($null -eq $preset) { throw 'PhotAnima v2.3 preset is missing.' }
if ($preset.image.unet -ne 'photanima_v23Turbo.safetensors') { throw 'v2.3 UNet filename is incorrect.' }
if ($preset.image.unetUrl -ne 'https://civitai.com/api/download/models/3112450') { throw 'v2.3 download URL is incorrect.' }
if ($preset.image.steps -ne 12 -or $preset.image.cfg -ne 1) { throw 'Turbo defaults changed.' }

$workflowPath = Join-Path (Join-Path $repo 'packs\anima-realism') $preset.image.workflow
if (-not (Test-Path $workflowPath)) { throw 'v2.3 workflow is missing.' }

$workflow = Get-Content -Raw $workflowPath | ConvertFrom-Json
if ($workflow.'7'.inputs.sampler_name -ne 'er_sde' -or $workflow.'7'.inputs.scheduler -ne 'simple') { throw 'Sampler contract changed.' }
if ($workflow.'2'.inputs.shift -ne 3) { throw 'AuraFlow shift changed.' }

$modelPath = 'C:\Users\micha\Downloads\photanima_v23Turbo.safetensors'
if (-not (Test-Path $modelPath)) { throw 'Supplied v2.3 model is missing.' }
if ((Get-Item $modelPath).Length -lt 3.8GB) { throw 'Supplied v2.3 model is unexpectedly small.' }

Write-Host 'PhotAnima v2.3 contract is valid.'
