# Note to Sharmystic — what Qwen-Image 2.1 needs to run in SimpliGen, 2026-09-20 (SENT by Michael 2026-09-20)

Qwen-Image 2.1 came out today and Comfy-Org already has the repack up (https://huggingface.co/Comfy-Org/Qwen-Image-2.1). I tested it this morning on stock ComfyUI master, 4070 Ti 12 GB, int8 files, the official template settings (25 steps, euler/simple, cfg 1):

| test | result |
|---|---|
| text-to-image 1024x1024 | 16 s, 2.5 it/s |
| text-to-image 1344x768 | 16 s |
| sign with a 5-word line of text | 16 s, every word correct |
| transparent sticker (RGBA prompt) | 16 s, real alpha, 48% of pixels fully transparent |
| edit, 1 reference (new jacket + new background) | 22 s, face and pose held |
| background removal, 1 reference | 22 s, clean cut-out incl. hair, 0.7% soft-edge pixels |

About 9.4 GB VRAM in use during sampling. One 7B model does t2i, edit (up to 10 refs) and transparency, so it is fast and light enough to be a default-class image model on 12 GB cards.

It cannot run on the current engine, though. What it needs:

1. **Engine past v0.36.0.** Support landed in core last night: `6bfaacc67` "feat: Qwen-image 2.1 support (CORE-423) (#16400)", 2026-09-19. v0.36.0 is an ancestor of master and that commit is 16 commits after the tag, so no tagged release has it yet. It adds `comfy/ldm/qwen_image21/model.py`, a new latent format, a new text encoder (`comfy/text_encoders/qwen_image21.py`), model detection, and two nodes in `comfy_extras/nodes_qwen.py`: `TextEncodeQwenImage21` and `QwenImage21Cache`. Engine 0.36.0 has neither node (checked the engine's ComfyUI tree).
2. **Pin bumps that ride along with master:** comfy-kitchen 0.2.34 -> 0.2.35, comfy-aimdo 0.5.3 -> 0.5.5, frontend 1.52.7 -> 1.53.6. The kitchen bump matters for the `qwen3vl_8b_w4a8` encoder (w4a8 gemv support came in with `9a77c1db9`); I tested the int8_convrot encoder only.
3. **New weights, none shared with Qwen-Image 2512:**
   - `diffusion_models/qwen_image_2.1_int8_convrot.safetensors` 7.26 GB (bf16 is 14.2 GB)
   - `text_encoders/qwen3vl_8b_int8_convrot.safetensors` 9.35 GB (w4a8 6.31 GB, bf16 17.5 GB) — Qwen3-VL 8B, loaded with `CLIPLoader` type `qwen_image`
   - `vae/qwen_image_2.1_vae_bf16.safetensors` 0.68 GB
   All three are LFS files, so store pinning should be fine.
4. **Every output is a 4-channel RGBA PNG**, including fully opaque ones (alpha 250-255 everywhere). The new VAE decodes four channels and SaveImage writes them. Worth a look app-side: gallery thumbnails and the viewer for transparent results (a checkerboard or neutral backing, not black), "use as reference" / send-to-video with an RGBA source, and any place that assumes 3 channels. ComfyUI's own LoadImage splits alpha into a mask, so engine-side reuse is fine; it is the app's own image handling I can't see.
5. **Edit wiring, for information:** `TextEncodeQwenImage21` takes the references as autogrow inputs named `images.image_1` ... `images.image_16` (dotted keys in the API JSON), plus the VAE, and returns positive, negative AND a latent sized to the first reference. The official templates sample on that latent for edits and on an EmptyLatentImage for t2i. Unused reference keys can simply be absent, which should make optional reference slots easier than the ComfySwitchNode pattern the older edit packs need, if the app can drop an input key when a slot is empty.
6. **Licence:** the weights are under the "Qwen Research License", not the Apache 2.0 of the earlier Qwen-Image releases. I have not read it closely; worth checking before anything goes on Cloud.

7. **Cost per reference, for any time estimate the app shows:** one reference 22 s, two 52 s, four 106 s at 25 steps on the 4070 Ti. Each reference is spliced into the sequence, so it is not linear.

On my side: the community pack is built and held on a local branch (Text to Image, Edit with 1-4 references, Cutout to transparent PNG), tested on stock master with the app's placeholder substitution simulated, not in the app. It will be gated with `minComfyuiVersion` on whatever release first contains `6bfaacc67`; I'll run all three cards through the app the day a beta engine has it, and check that the saved PNG keeps its alpha. If you would rather ship it as an official pack, tell me and I will hand over the workflows and test sheets instead of publishing. One finding worth having either way: the model card's background-removal line on its own is fragile (it deleted the subject's jacket and hair on 1 seed in 3 when followed by an empty user prompt); adding a "keep the entire main subject" sentence made it 26 for 26 across people, a product and a dog.

Test scripts and contact sheets: `D:\SimpliGen-Backups\qwen-image-21-test-20260920\`.
