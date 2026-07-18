@echo off
setlocal
set "SOURCE=%USERPROFILE%\Downloads\babesIllustriousBy_v55FP16.safetensors"
set "ENGINE=%APPDATA%\simpligen\engine\models"
set "PRESETS=%APPDATA%\simpligen\presets"
if not exist "%SOURCE%" goto :missing
if not exist "%ENGINE%\checkpoints" mkdir "%ENGINE%\checkpoints" || goto :error
if not exist "%PRESETS%\workflows" mkdir "%PRESETS%\workflows" || goto :error
if not exist "%PRESETS%\previews" mkdir "%PRESETS%\previews" || goto :error
echo Installing Community - Illustrious Realism...
copy /Y "%SOURCE%" "%ENGINE%\checkpoints\babesIllustriousBy_v55FP16.safetensors" >nul || goto :error
copy /Y "%~dp0illustrious-realism-pack.json" "%PRESETS%\illustrious-realism-pack.json" >nul || goto :error
copy /Y "%~dp0workflows\*.json" "%PRESETS%\workflows\" >nul || goto :error
copy /Y "%~dp0previews\*.*" "%PRESETS%\previews\" >nul || goto :error
powershell -NoProfile -ExecutionPolicy Bypass -Command "$p='%PRESETS%\illustrious-realism-pack.json'; $u=New-Object System.Text.UTF8Encoding($false); $j=[IO.File]::ReadAllText($p,$u) | ConvertFrom-Json; foreach($pr in $j.presets){ $leaf=Split-Path ($pr.previewImage -replace 'local-file:///','') -Leaf; $pr.previewImage='local-file:///'+(Join-Path ('%PRESETS%\previews') $leaf).Replace('\','/') }; [IO.File]::WriteAllText($p,($j | ConvertTo-Json -Depth 30),$u)"
if errorlevel 1 goto :error
echo.
echo Community - Illustrious Realism restored. Restart SimpliGen.
echo.
pause
exit /b 0

:missing
echo Checkpoint not found: %SOURCE%
pause
exit /b 1

:error
echo Installation failed.
pause
exit /b 1
