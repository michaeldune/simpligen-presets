Sorry for the wait. I went through your 9 Nov zip. It's the same loop as Z-Image: you pressed install on MiniMax H3 Turbo (Fully Accelerated) R2V about 17 times in an hour, and each time the app found the models, restarted the engine and left the button as it was. No render was ever started. Everything else looks fine: every add-on the card needs loads without errors, and the H3 files and both LoRAs are there.

Why it can loop: the installer and the "ready" check don't test the same thing. The installer counts any file with the right name as present, even a 0 KB one, so it never downloads a replacement. The ready check wants a real model file (over 64 KB). An empty file under a model's name passes the first and fails the second, forever.

On symlinks: real symbolic links work. SimpliGen and the engine both read through a link to the file it points at. The catch is that Explorer shows 0 KB for a real link too, so you can't tell from there. Open Command Prompt and run this for each folder you linked into, for example:

`dir /AL "L:\Downloads\Simpligen.ai\models\loras"`

A real link is listed as <SYMLINK> with its target in [brackets]. Any 0 KB file that isn't listed there is just an empty file: delete it. Also make sure every target drive is connected when SimpliGen starts.

You may not need links at all. SimpliGen already reads two more model folders on your machine:
`J:\Wobbly-Life\ComfyUI_windows_portable_nvidia_cu128\ComfyUI_windows_portable\ComfyUI\models`
`L:\Downloads\New I2V Animate\ComfyUI-Easy-Install\ComfyUI-Easy-Install\backup models`
A file in the matching subfolder there (loras, vae, diffusion_models...) with the exact name counts as installed.

Your zip was from app 1.80.0, and 1.82.1 is out, so update too. If it still loops after that, send a fresh diagnostics zip and the dir /AL output, and I'll go through it.
