Thanks RHR, that's a clear request. Feature decisions are Sharmystic's call, so I'll leave that part to him. Here's what you can do today:

**LoRAs: already supported** (see my answer in your other thread). Add them from a Civitai link or a file, set the strength per LoRA on the card, and stack several.

**Reusing your SwarmUI folder: works today, tested on a fresh SwarmUI 0.9.8.** Settings > Storage > **+ Add another folder**, then pick SwarmUI's `Models` folder. SimpliGen reads it in place and copies nothing. One catch: SimpliGen expects ComfyUI's folder names, and SwarmUI's `Lora` and `Stable-Diffusion` aren't found as they are. Add two links so both names work and SwarmUI is left untouched (Command Prompt, your own path):
```
cd /d "D:\SwarmUI\Models"
mklink /J loras Lora
mklink /J checkpoints Stable-Diffusion
```
Restart SimpliGen. Our test LoRAs then showed up in the **+ Add LoRA** list, subfolders included. They arrive with no base model, so they appear on every card until you set one in Manage LoRAs. With hundreds, that takes a while.

**Checkpoints: not yet.** The links above make your checkpoints visible to the engine, but there's no "pick any SDXL checkpoint" card. Each checkpoint runs as its own card, which is why they come in packs. Two routes for now:
- Check the **Preset Store**. It already has a lot of SDXL, Pony and Illustrious checkpoints.
- Build your own pack. One pack can hold as many cards as you like, and an agent following our authoring guide can write one card per checkpoint in your folder: https://github.com/michaeldune/simpligen-presets/blob/master/CUSTOM-PRESET-AUTHORING-GUIDE.md

Picking any checkpoint from the Generate screen is the part that needs Sharmystic.
