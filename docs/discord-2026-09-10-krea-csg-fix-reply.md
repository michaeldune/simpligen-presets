# Reply draft — Issue Report – Krea 2 CSG Foundation (Magnavex, 2026-09-10)

Thanks Magnavex, and thanks Sharmystic for the diagnosis — that was exactly it.

The Krea 2 CSG Foundation workflow hardcodes the Flux text encoders (clip_l_hidream + t5xxl_fp8_e4m3fn_scaled) but the pack only declared the GGUF + VAE, so SimpliGen never downloaded them. It worked on my PC only because the HiDream pack had left both files behind.

**Fixed in Krea Flux 1.1.1** (pushed to the repo; the store picks it up on its next sync, within ~6 h). Take the pack update in the Store, then Prepare/Generate once and it will download the two encoders (~5.4 GB, from Comfy-Org / comfyanonymous on Hugging Face). Total install is ~12 GB, so it needs that much free in your models folder.

The requirements note also wrongly said "Qwen3VL encoder"; corrected. Same workflow, same output, nothing to re-tune.

I also added a repo check so a workflow can't ship a weight the manifest doesn't declare — the other 40 packs are clean.
