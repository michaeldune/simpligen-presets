**How to: blend a pasted subject into a background with Qwen-Image 2.1 Edit**
RunningHub published a small LoRA that takes a rough cut-and-paste composite and makes the subject sit in the scene. It needs no special preset: it works on the standard **Qwen-Image 2.1 Edit** card.

What you need:
- The LoRA (160 MB): https://huggingface.co/RunningHubAI/rh-qwen-image-2.1v2.0-lora/tree/main
- The Qwen-Image 2.1 community pack from the Store.

Steps:
1. Download the `.safetensors` file from the link and add it to your LoRAs in SimpliGen with the base model set to Qwen-Image 2.1.
2. In any image editor, paste the cut-out subject onto the background where you want it. Rough is fine, no shadow needed.
3. Open **Qwen-Image 2.1 Edit**, load the composite as the reference image, and pick the LoRA in the LoRA picker at strength 1.
4. Use the author's prompt:
```
pysj666, keep the subject position and size unchanged, adjust the background perspective angle to align with the subject's vanishing point. seamless blending between subject and background.
```
5. Generate. Leave the seed unlocked and roll a few.

What we measured (one test composite, three seeds, with and without the LoRA):
- With the LoRA the subject stayed in place at 94 to 102% of its original size on all three seeds. Without it the card shrank the subject to 40 to 59% and moved it every time.
- The LoRA added a ground shadow under the subject and matched the light on all three.
- It did not fix a badly mismatched camera angle. Our test was extreme (an eye-level figure on a view looking straight down) and the scene stayed top-down. Pick a background shot from roughly the same height as your subject.

Good to know:
- `pysj666` is the author's trigger word. We did not compare with and without it.
- The model card carries no licence of its own, and Qwen-Image 2.1 itself is under the non-commercial Qwen Research License.

Thanks to 浩的AI日常 and RunningHub for the LoRA.
