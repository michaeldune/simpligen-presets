@echo off
setlocal
set "ENGINE=%APPDATA%\simpligen\engine\models"
set "PRESETS=%APPDATA%\simpligen\presets"
if not exist "%ENGINE%\checkpoints" mkdir "%ENGINE%\checkpoints"
if not exist "%PRESETS%\workflows" mkdir "%PRESETS%\workflows"
if not exist "%PRESETS%\previews"  mkdir "%PRESETS%\previews"
echo Installing MiniMax H3 Turbo Accelerated...
copy /Y "%~dp0minimax-h3-turbo-accelerated-pack.json" "%PRESETS%\minimax-h3-turbo-accelerated-pack.json" >nul || goto :error
copy /Y "%~dp0workflows\*.json" "%PRESETS%\workflows\" >nul || goto :error
copy /Y "%~dp0previews\*.jpg" "%PRESETS%\previews\" >nul || goto :error
powershell -NoProfile -ExecutionPolicy Bypass -Command "$p='%PRESETS%\minimax-h3-turbo-accelerated-pack.json'; $u=New-Object System.Text.UTF8Encoding($false); $j=[IO.File]::ReadAllText($p,$u) | ConvertFrom-Json; foreach($pr in $j.presets){ $leaf=Split-Path ($pr.previewImage -replace 'local-file:///','') -Leaf; $pr.previewImage='local-file:///'+(Join-Path ('%PRESETS%\previews') $leaf).Replace('\','/') }; [IO.File]::WriteAllText($p,($j | ConvertTo-Json -Depth 30),$u)"
echo. & echo Done. Restart SimpliGen. & echo. & echo IMPORTANT: Three custom nodes must be installed first: & echo - ComfyUI-KJNodes (SageAttention) & echo - ComfyUI-Spectrum-MiniMax-H3 (Spectrum) & echo - ComfyUI-SolAttn_triton (Sol-Attn) & echo. & pause
exit /b 0
:error
echo Installation failed. & pause & exit /b 1
