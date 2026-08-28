@echo off
setlocal
set "ENGINE=%APPDATA%\simpligen\engine\models"
set "PRESETS=%APPDATA%\simpligen\presets"
if not exist "%ENGINE%\pdd_acc"     mkdir "%ENGINE%\pdd_acc"
if not exist "%PRESETS%\workflows" mkdir "%PRESETS%\workflows"
if not exist "%PRESETS%\previews"  mkdir "%PRESETS%\previews"
echo Installing MiniMax H3 PDD Acc 8-Step...
copy /Y "%~dp0minimax-h3-pdd-acc-pack.json" "%PRESETS%\minimax-h3-pdd-acc-pack.json" >nul || goto :error
copy /Y "%~dp0workflows\*.json" "%PRESETS%\workflows\" >nul || goto :error
copy /Y "%~dp0previews\*.jpg" "%PRESETS%\previews\" >nul || goto :error
powershell -NoProfile -ExecutionPolicy Bypass -Command "$p='%PRESETS%\minimax-h3-pdd-acc-pack.json'; $u=New-Object System.Text.UTF8Encoding($false); $j=[IO.File]::ReadAllText($p,$u) | ConvertFrom-Json; foreach($pr in $j.presets){ $leaf=Split-Path ($pr.previewImage -replace 'local-file:///','') -Leaf; $pr.previewImage='local-file:///'+(Join-Path ('%PRESETS%\previews') $leaf).Replace('\','/') }; [IO.File]::WriteAllText($p,($j | ConvertTo-Json -Depth 30),$u)"
echo. & echo Done. Restart SimpliGen. & echo. & echo IMPORTANT: two custom nodes must be installed first: & echo - ComfyUI-MiniMax-H3-PDD-Acc (loads the PDD distill) & echo - ComfyUI-KJNodes (SimpliGen injects its SageAttention node) & echo. & echo The PDD file goes in models\pdd_acc\ - the app downloads it, but the & echo folder only registers once ComfyUI-MiniMax-H3-PDD-Acc has loaded once. & echo. & echo Needs ComfyUI v0.33.0 or newer. Do NOT combine with a Turbo/lightx2v & echo LoRA or a step-caching pack - distills do not stack. & echo. & pause
exit /b 0
:error
echo Installation failed. & pause & exit /b 1
