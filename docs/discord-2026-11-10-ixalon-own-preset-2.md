Right, the new one doesn't touch the models folder on purpose: it downloads nothing, it only drops the card's three files into the presets folder. Your sickOllie, Qwen3-VL and VAE files stay where they are in D:\models.

I just installed the same zip here and the pack showed up on the next start, so the files are fine. If the file is in the folder but not in the app, the app hasn't really restarted. SimpliGen reads that folder only when it starts, and the X button can be set to minimise it to the tray instead of quitting. Right-click the SimpliGen icon in the system tray (bottom right, maybe under the ^ arrow), choose Quit, check Task Manager has no SimpliGen.exe left, then open it again.

If it's still missing after that, check the folder is the one the app reads: if you ever moved SimpliGen's data folder, the app reads <that folder>\presets, not %APPDATA%\simpligen\presets. The pack is called "sickOllie Krea 2", it isn't inside the Krea 2 pack.

One more catch: the card's download link (civitai.com/api/download/models/3066243) is the RedCraft Red Mix link, copied from the RedCraft card, not Sick Ollie. If SimpliGen downloaded the model for that card, you have RedCraft saved under the name sickOllie_krea2.safetensors. What's the exact size in bytes of that file? RedCraft fp8 is 13,141,783,440 and Sick Ollie's Krea 2 files are 12,821,587,640 (FP8), 13,148,995,440 (int8) or 25,640,235,408 (BF16).

Easier still: I've added Sick Ollie Krea 2 to our Krea 2 Realism pack, on the author's settings (Euler, Beta, 9 steps, CFG 1). It should show as an update in the store tonight. It uses the int8 ConvRot file; if that's what you have, rename it to sickOllie_krea2_int8_convrot.safetensors and it won't download again. Then you can delete the hand-made pack.
