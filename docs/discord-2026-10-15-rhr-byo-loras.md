Hi RHR! Yes, you can bring your own LoRAs from Civitai and use them with the models you have installed. The screenshot shows a Krea 2 card with six of mine stacked on it.

**Getting them in.** There are two ways:
- **Manage LoRAs** (top right of the LoRA section on a card) > **Add LoRA**. Its **Upload File** tab takes a file from your PC. Its **From URL** tab takes a Civitai download link: right-click the Download button on the LoRA's page and copy the link (it looks like `https://civitai.com/api/download/models/...`). Then give it a display name, pick the **Base Model**, paste the trigger words from the Civitai page (optional), set a default strength, and click **Download & Add**.
- Or drop the `.safetensors` file into the `models\loras` folder of your SimpliGen install. It shows up in your library without registering it, but with no base model. Untagged LoRAs appear on every card, so set the base model in Manage LoRAs to keep it off cards it won't work with.

**Format.** Use `.safetensors`, which is what Civitai serves.

**Using one.** On a card, click **+ Add LoRA**, pick it, and set the strength with the slider or by typing a number. You can stack several. If the LoRA has a trigger word, put it in your prompt.

**Compatibility.** A LoRA only works on the model family it was trained for. The small tag next to each name (`krea2` in the screenshot) is its family, and the **+ Add LoRA** list on a card shows LoRAs tagged for that card's family, plus any tagged "other" or not tagged at all:
- SDXL LoRAs on SDXL cards. Most Pony and Illustrious LoRAs also work on Pony/Illustrious checkpoints, since those are SDXL underneath.
- Flux LoRAs on Flux, Qwen-Image 2.1 LoRAs on Qwen-Image 2.1, Krea 2 LoRAs on Krea 2, and so on.
- An SDXL LoRA will not work on Flux or Qwen, even if it loads. On Civitai, check the "Base Model" field on the LoRA's page before you download it.

Video and music models take LoRAs the same way (MiniMax H3, Wan, YuE2).
