# Discord update note: Qwen Image 2.1 1.4.0, guided sampling on the 1 MP cards (HELD, 2026-09-22)

**Qwen Image 2.1 (1.4.0): sharper text and detail on the main cards**

Tonight's Reddit thread on a Qwen 2.1 "fix" LoRA got me testing. The LoRA itself didn't help (on its own it made pictures worse, and with the author's settings it made compositions stiff), but his *settings* made a big difference: the model isn't meant to run at CFG 1, which is what the ComfyUI template (and our cards) used.

So **Qwen Image 2.1** and **Qwen Image 2.1 Edit** now run with CFG 3, Adaptive Projected Guidance and FreSca (both built into ComfyUI, nothing extra to download), plus a built-in negative prompt. In testing, signs and menus went from mostly garbled to readable, and colours stay natural.

The cost is time: about 35 seconds per picture instead of 16, and about 1½ minutes for an edit with one picture instead of 20 seconds. Nothing to change on your side; just update the pack.

The other five cards (Cutout, Character Sheet, Enhance to 4MP, 4MP, Edit 4MP) are unchanged. Credit to e-n-v-y for sharing his settings. Non-commercial use only (Qwen Research License).
