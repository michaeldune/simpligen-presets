@echo off
setlocal
set "PRESETS=%APPDATA%\simpligen\presets"
if not exist "%PRESETS%\workflows" mkdir "%PRESETS%\workflows"
if not exist "%PRESETS%\previews" mkdir "%PRESETS%\previews"
echo Installing Community — Z-Image...
copy /Y "%~dp0z-image-pack.json" "%PRESETS%\z-image-pack.json" >nul
copy /Y "%~dp0workflows\*.json" "%PRESETS%\workflows\" >nul
copy /Y "%~dp0previews\*.*" "%PRESETS%\previews\" >nul
powershell -NoProfile -ExecutionPolicy Bypass -Command "$p='%PRESETS%\z-image-pack.json'; $u=New-Object System.Text.UTF8Encoding($false); $j=[IO.File]::ReadAllText($p,$u) | ConvertFrom-Json; foreach($pr in $j.presets){ $leaf=Split-Path ($pr.previewImage -replace 'local-file:///','') -Leaf; $pr.previewImage='local-file:///'+(Join-Path ('%PRESETS%\previews') $leaf).Replace('\','/') }; [IO.File]::WriteAllText($p,($j | ConvertTo-Json -Depth 30),$u)"
echo. & echo Community — Z-Image restored. Restart SimpliGen. & echo. & pause
