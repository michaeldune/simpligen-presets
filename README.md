<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="SimpliGen Community Preset Packs: 171 ready-to-run presets in 51 packs. One zip, one click, models auto-downloaded into SimpliGen.">
</p>

Custom local preset packs for [SimpliGen](https://www.simpligen.io/), covering image models across SDXL, Pony, Illustrious, SD 1.5, Anima, Krea 2, Flux (1 & 2), Z-Image and SeFi — plus video: MiniMax H3 packs (text/image/reference-to-video with synchronized audio), LTX 2.5 image-to-video and lip-sync packs, a Wan 2.2 image-to-video pack, and music: YuE2 and MiniMax Music 3 songs, plus YuE2 cover songs, with album art.

**Getting a pack takes three steps:** download the pack zip from the [Releases page](https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest), unzip it, and run `install.cmd`. The installer downloads the models for you, verifies them, and the pack appears in SimpliGen's preset picker under `Community — `.

> This repo is the source of truth the zips are built from — and now the distribution point too. The `packs-latest` release is rolling: its assets get replaced each time `build-zips.py` runs, so the same link always has the current set. End users never need to clone it.

<p align="center">
  <img src="./assets/readme/section-catalog.svg" width="100%" alt="01 — Pack catalog: 51 packs, 171 presets.">
</p>

**Image packs**

| Pack | Presets | Architecture | Notes |
|---|---|---|---|
| SDXL Realism | 5 | SDXL 1.0 | Photoreal, baked VAE, no CLIP skip |
| SDXL Art & Anime | 5 | SDXL 1.0 | Stylized/anime |
| Pony Anime | 4 | Pony (SDXL) | CLIP Skip 2, score tags |
| Pony Realistic | 3 | Pony (SDXL) | Photoreal/semi-real |
| Illustrious Realism | 6 | Illustrious (SDXL) | Photoreal & semi-real |
| Illustrious Anime | 8 | Illustrious (SDXL) | Anime, incl. V-Pred models |
| SD 1.5 Anime | 3 | SD 1.5 | External kl-f8-anime2 VAE, 512-base |
| DucHaiten | 9 | SD 1.5 ×5, SDXL ×1, NoobAI ×2, Pony ×1 | DucHaiten's checkpoint family: GoldenLife, Retro, Real3D-NSFW, StyleLikeMe and ThiccBoi on SD 1.5 (512-base, CLIP Skip 2); GoldenAge on SDXL; NoobAI-Cinematic plain and Snapvu hires; GameArt UnrealEngine on Pony. ThiccBoi also lives in SD 1.5 Anime, same checkpoint |
| Reij's Merges | 6 | Illustrious (SDXL) | reijlita merge family |
| Anima Anime | 5 | Anima (Cosmos) | UNet + Qwen encoder + Qwen-Image VAE |
| Anima Realism | 3 | Anima (Cosmos) | Same stack, photoreal |
| Krea 2 Identity Edit | 2 | Krea 2 Turbo + Identity Edit LoRA v1.2 | **Image editing.** Hand it a photo and an instruction in plain English. Identity Edit changes one thing and leaves the rest alone; Identity Lock holds a face while you re-stage a character sheet into a new scene, transfer a face between two images, or do virtual try-on. Takes one or two reference images — image 1 is the scene, image 2 is the subject. Shares the Krea 2 checkpoint, encoder and VAE with the Krea 2 pack, so the only new download is a 1.83 GB LoRA. No masked inpainting: SimpliGen presets cannot pass a mask |
| Outfit Spec Sheet | 2 | Qwen Image Edit 2511 + Lightning 4-step; Qwen-Image 2.1 (two-pass) | **Image editing, fixed brief.** One photo of an outfit in, one fashion-house specification board out. **Original card** (Apache-2.0): the garments and accessories lifted onto a mannequin against warm ivory, three close-up detail crops, deliberately no text; same weights as SimpliGen's own Image Edit pack, so nothing new downloads if that is installed. **Qwen 2.1 card** (added in 1.1.0): two passes in one job, first the outfit is lifted off the person as a ghost-mannequin shot, then the board is built around it with the heading OUTFIT SPECIFICATION, three detail crops and four colour swatches taken from the real colours. It removes the person every time and keeps hats, bags and shoes the original drops, but it is not reliable on every try: the whole outfit survived on 6 of 9 test boards, so re-roll the seed when a coat or a shirt goes missing. About a minute per board; same weights as the Qwen Image 2.1 pack. **Qwen Research Licence, non-commercial use only** - for commercial work use the original card. Since 1.1.0 the pack needs SimpliGen engine 0.37.0. The prompt box is optional extra notes |
| Qwen Image 2.1 | 7 | Qwen-Image 2.1 7B (INT8) + Qwen3-VL 8B encoder | **One model, seven cards:** text to image (renders legible signs and captions), editing with 1–4 reference images in plain English, a Cutout card that removes the background and saves a real transparent PNG at the source size, and (since 1.1.0) a **Character Sheet** card: one picture of a person in, a sheet out with a large head, a headless full-body front view, a back view and two mirrored profiles on white; an optional second picture dresses the person in that outfit. The sheet layout comes from the Portrait2CharRef LoRA by b675051045971 (328 MB, built in); set the aspect ratio to 3:2. Since 1.2.0, two **4MP** cards: text to image at the model's full ~4-megapixel size (about 1.5 min on 12 GB), and **Enhance to 4MP**, which adds real detail to any picture while keeping faces and lettering (Detail Enhancer LoRA by Elusarca, 76 MB, built in). Since 1.3.0, **Edit 4MP**: the Edit card with 1-4 pictures and 4MP output (about 2 min with one picture, under 4 with four on 12 GB). About 20 s per image on a 4070 Ti, under a minute for a two-reference edit. **Needs SimpliGen engine 0.37.0 or newer.** 17.3 GB download. **Licence: Qwen Research Licence, non-commercial use only** |
| Krea 2 | 6 | Krea 2 DiT | Uncensored mixes, 8–10 step distilled. Renders at native ~2 MP (1408×1408 and equivalents) plus an Upscale slider with a gated 4-step refine pass; 2 MP costs ~5 s more than 1 MP on a 4070 Ti |
| Krea 2 Finetunes | 4 | Krea 2 DiT | Trained checkpoints, not merges: Muse v3.5 Extended (clean SFW editorial, real 8–20 step / CFG 1–3 range, ships 12 steps / CFG 1.5), FinalCut Massive Update (matte skin instead of Krea gloss, native up to 2432×1920, NSFW-capable), Binyuan Portrait v3.2 (East Asian portrait realism, trained on ~1,000 unedited photos) and Kreamania V8 (Adel_AI's refinement of Krea 2: volumetric light, matte skin, NSFW intact, 10 steps / CFG 1). Same 2 MP + gated Upscale as the Krea 2 pack; shares its encoder and VAE Renders at native ~2 MP (1408×1408 and equivalents) plus an Upscale slider with a 4-step refine pass, matching the official Krea 2 Turbo preset; 2 MP costs ~5 s more than 1 MP on a 4070 Ti |
| Krea Flux | 1 | Flux.1 Krea (GGUF) | CSG Foundation, low-VRAM |
| Flux 2 Klein | 2 | Flux 2 | 9B + 4B, 4-step distilled — **non-commercial license (BFL)**. A third preset, MiracleIn NSFW, was retired 2026-08-30 when Civitai's author put paid access on every version of that checkpoint; it is kept in `packs/flux2-klein/retired/` for manual install |
| Ideogram 4 | 2 | Ideogram 4 (INT8) | Best-in-class text rendering; UltraReal photo + Graphic/Poster tiers — **requires engine 0.28+** |
| SeFi-Image | 2 | SeFi 5B (Q8) | Turbo, 4- and 8-step tiers |
| Moody Models | 5 | Z-Image / Flux | NSFW-biased/uncensored |
| Z-Image | 1 | Z-Image | Semi-real/anime |
| Hentai Mixes | 8 | SD 1.5 ×6, SDXL ×2 | Civitai anime/hentai checkpoints. SD 1.5 tier runs 512–768 with CLIP Skip 2; the SDXL pair run native 1024, one of them Pony-based (wants `score_9, score_8_up, score_7_up`) |

**Video packs**

All the MiniMax H3 packs generate video *with synchronized stereo audio*. The first four ship text-to-video, image-to-video, and reference-to-video presets off the same base weights — so adding one costs only its LoRA, not another 40 GB. **10Eros Max is the exception**: it is a different base checkpoint (a separate 20.94 GiB download), and it ships as two packs - plain and Turbo - each with text-, image- and reference-to-video. **10Eros Max beta5** is TenStrip's current release of that finetune on its own 21 GB hybrid file, a third separate download, and **beta5 Turbo** is a fourth: the same beta5 with the turbo delta fused into the weights, so it needs no Turbo LoRA.

| Pack | Presets | Architecture | Notes |
|---|---|---|---|
| MiniMax H3 (Turbo LoRA, larryvrh) | 5 | MiniMax H3 (pruned INT8) | The default: 6–8 steps, best for static/small motion. Named for the LoRA author to stay clear of SimpliGen's own official H3 Turbo pack. v1.4.0 adds two I2V cards: the Turbo recipe with Comfy Kitchen attention (about 25% faster, same look) and a lightx2v 4-step card (about 40% faster sampling, a little less fine detail) |
| MiniMax H3 (Turbo, Fast Motion) | 3 | MiniMax H3 (pruned INT8) | 4-step tier tuned for heavy/fast motion |
| MiniMax H3 (Sol-Attn + EasyCache) | 3 | MiniMax H3 (pruned INT8) | Sparse attention + step caching at the full 20 steps. **Not a speed pick** since 1.50.0 — pick it for the no-LoRA path, and for the R2V preset, which is the crash-free route for reference *video*. Needs Faster Attention ON |
| MiniMax H3 (Two-Stage Latent Upscale) | 3 | MiniMax H3 (pruned INT8) | Full 20 base steps at 0.6x size (~0.36 MP), trained latent upscaler, 4-step Turbo refine at your chosen size. Stock non-distilled look at 768p in 248-351 s on 12 GB where a direct full-steps render took 882 s. A smaller first pass wrinkles close-up faces, so 0.6x is the floor. Verified at 768p / 5 s only |
| MiniMax H3 (Video Refine) | 1 | MiniMax H3 (pruned INT8) | **Video in, video out.** Drop a finished H3 clip in Reference Video 1 and paste its brief; it comes back at 672p or 768p with its own soundtrack. LBH-123-AI's 3D latent upscaler, then Alibaba's official PDD 8-step distill at denoise 0.25 in 73-frame windows, so up to 15 s runs in one queue. Same model family, so H3's look and cast survive; it cannot repair a face the source lost. Verified 2026-09-07 on a 4070 Ti: 864x480 to 1344x768, 5 s in 162 s, 10 s in 297 s with the clip's hard cut preserved. Resolves mesh, lines and beard hair a Lanczos upscale smears. Shares the ref2va base with every R2V pack; adds the 1.37 GB Ref2VA distill |
| LTX 2.5 (Video Refine, MSR) | 1 | LTX 2.5 distilled 22B | **Video in, video out, any source.** Upscales a clip to 720p or 1080p in LTX 2.5 with one to four face pictures plus an optional background plate, held by Licon's Multi-Subject-Reference LoRA. Crisper and more LTX-looking than the H3 refine; the prompt must be LTX style. Source audio muxed back untouched. Verified 2026-09-07 on a 4070 Ti: 864x480 to 1920x1088, 5 s in 155 s, face held from one design sheet. Reuses the official gated LTX 2.5 weights; adds the 1.3 GB MSR V1 LoRA |
| VOSR 2.0 (Video Refine) | 1 | VOSR 2.0 one-step SR (1.4B) | **Video in, exactly 2x out, no prompt.** Per-frame one-step super-resolution with the source soundtrack muxed back. Sharpest of the three refine packs on a same-clip bake-off (sharpness 88 vs 51 H3 / 46 LTX, face held) but the slowest, 274 s for 5 s of 480p on a 4070 Ti, and per-frame so it can shimmer on fast motion; pick it for static shots. **First render downloads 7 GB** into the engine with no progress bar. Declares no model files by design: the node reads only its own engine folder and converts the DINOv2 encoder itself |
| MiniMax H3 (Clip Chaining) | 3 | MiniMax H3 (pruned INT8) | Continue an existing H3 clip: drop it in Reference Video 1, describe what happens next, and the new clip picks up its last 22 frames with motion and timing carried across the cut. Motion Context preset continues the soundtrack (corr 0.95, 0 ms lag); Add Guide preset uses ComfyUI's stock guide and imitates it (-8 ms). Two-Shot Director preset renders both segments in one file via AIMixer's Director, prompt split on H3's own `[Shot 2]` tag (join ratio 1.9, colour drift under 1/255). All visually seamless on static-camera shots (hard cut = 16). Fast action across the cut untested |
| MiniMax H3 (Turbo, Fully Accelerated) | 3 | MiniMax H3 (pruned INT8) | Every technique stacked — Turbo + SageAttention + Sigma Shift + Spectrum + Sol-Attn. 10 steps for roughly what 6 used to cost |
| MiniMax H3 (PDD Acc 8-Step) | 3 | MiniMax H3 (pruned INT8) | Alibaba's **official** 8-step distill (Parallel Decoding Distillation), loaded through its own node pack because a plain LoRA loader silently drops it. Euler only, CFG 1, 8 steps fixed and enforced; multistep samplers flicker with this and any turbo distill. T2V + I2V + R2V on the FL2VA weights, All three cards verified in-app 2026-09-07 at 864x480 / 5 s on a 4070 Ti: T2V 106 s, I2V 113 s, R2V 117 s, with the R2V run holding identity from one design sheet through a headphone lift. Same speed as Fully Accelerated; pick this one for a single official component instead of a stacked chain. Do not stack with Turbo, lightx2v, Spectrum or EasyCache |
| MiniMax H3 (Singularity) | 3 | MiniMax H3 Singularity v1.3 ref2va (pruned INT8) | WarmBloodAban's HDR merge-and-finetune, one 21 GB checkpoint for T2V, I2V and R2V on the official 20-step graphs. Measured over three seeds against the official checkpoint: close-up faces ~30% sharper and distant faces readable in action, but ~20 points darker, lower contrast and a quarter to a third less motion. A look, not a free upgrade. Card claims Apache-2.0; it is an H3 derivative, so the H3 Community License applies |
| MiniMax H3 (Z-Image Graft) | 3 | MiniMax H3 x Z-Image zs05 (pruned INT8, FL2VA + ref2va) | joeygambino's spatial detail graft: stock H3 with Z-Image's attention-normalisation statistics transplanted, so surfaces render richer at the same identity, speed and VRAM. Measured against the official pruned int8 on the same seed and graph: rust-wall crop sharpness 596 vs 411, face crop 353 vs 243, a touch brighter, motion unchanged, same ~200 s per clip. The pick for sets, materials and weathered surfaces |
| MiniMax H3 (SparseRef15) | 2 | SparseRef15 Hybrid v1.0 (pruned partial-INT8) | Aki7777777's FL2VA-based hybrid with a sparse Ref2VA influence in 15 blocks. Measured the same way: face crop sharpness 396 vs 243, the stillest locked-off shot and the most motion in the tracking shot of the 20-step arms, same ~200 s. Text and image to video only: the author's long-form identity claim is untested on our side, so no reference card yet. Use FL2VA LoRAs |
| MiniMax H3 (10Eros Max) | 3 | MiniMax H3 (**non-pruned** INT8) | Different base — a separate 20.94 GiB download. Plain 20-step, T2V + I2V + R2V |
| MiniMax H3 (10Eros Max + Turbo) | 3 | MiniMax H3 (**non-pruned** INT8) | The same base at 6 steps — the fastest preset here. Shares the 20.94 GiB download with the pack above |
| MiniMax H3 (10Eros Max beta5) | 3 | 10Eros Max beta5 hybrid (INT8) | TenStrip's current beta5, one 21 GB **hybrid** file so R2V runs on true reference character. Same-seed bake-off vs the original: cleaner faces, real motion, ~20% faster at 20 steps (202 vs 250 s vanilla; 127 s for 5 s at 480p in-app). Separate download; the original packs are unchanged |
| MiniMax H3 (10Eros Max beta5, Turbo) | 3 | 10Eros Max beta5 TURBO-hybrid (INT8) | beta5 with the turbo **baked into the checkpoint**: 8 steps, res_multistep/simple, no LoRA. ~105 s for 5 s at 480p on vanilla, same wall as the larryvrh Turbo at 6; on a face-visible I2V it was sharper than 20-step beta5 at half the time. Its own 21 GB file, so pick this or the plain beta5 unless you want both |
| MiniMax H3 (TaoMate 3-Step) | 2 | MiniMax H3 FL2VA (INT8) + LoRA | Alibaba TaoLive's three-step distill LoRA (Kijai rank-19 conversion, 173 MB) on the standard FL2VA weights: 3 steps, no CFG, Euler. T2V and I2V only, the LoRA ignores references. Bake vs Turbo Accelerated at 10 steps, same seeds: talking head 50 s vs 83 s and sharper (Laplacian 46 vs 29); product a draw; beach run softer (58 vs 102) with less motion. Dialogue and static shots, not action |
| MiniMax H3 (FastH3 8-Step V2) | 2 | FastVideo FastH3 V2 (INT8) | FastVideo's DMD2 distill with VSA block-sparse attention, Comfy-Org repack (20.6 GB, its own checkpoint), official template graph: 8 steps, no CFG, sigma shift 10/3, VSA keep 10%. **Needs engine 0.36+ (beta channel as of 2026-09-16)**, store-gated with minComfyuiVersion. Bake vs TaoMate and Turbo Accelerated, same seeds: sharper on every scene (talk 68 vs 46 vs 29, product 257 vs 111 vs 121, run 138 vs 58 vs 102) with motion kept (6.7 vs the turbo's 7.2); ~80 s per 5 s at 480p. T2V + I2V, no R2V |
| Wan 2.2 I2V (GGUF) | 1 | Wan 2.2 14B | Image-to-video, Q4 GGUF, 12 GB-friendly |
| LTX 2.5 Lip-Sync (A2V) | 1 | LTX 2.5 distilled 22B | Drive a shot with your own audio. Two-pass to 1080p; 165 s for 5 s at 1920x1088. Reuses the official LTX 2.5 weights |
| LTX 2.5 REDgraft Fast 2K (T2V + I2V) | 2 | LTX 2.5 REDgraft (INT8) | Text-to-video with generated audio or image-to-video from a source image. Separate NSFW finetune; reuses the official LTX 2.5 companion stack |
| MiniMax H3 (DaSiWa Hybrid) | 4 | MiniMax H3 (int8 + ConvRot) | **The fast one.** Darksidewalker's finetune with the distillation baked in: 4 steps, no Turbo LoRA, nothing extra to install. ONE checkpoint covers T2V + I2V + R2V where every other H3 pack needs two, so it is ~19.5 GB lighter. Roughly 70-140 s per 5 s shot against ~180. Reads brighter and wider than stock — pick another H3 pack for the darker look. Needs a Civitai API key (free model, sign-in required). 1.1.0 adds **Character PV**: one design sheet in, a 15 s 13-shot reveal trailer with five typography cards and a name/title card out (316 s at 480p on a 4070 Ti). How-to with both prompt templates: [docs/character-pv-guide.md](docs/character-pv-guide.md) |
| MiniMax H3 (DaSiWa Hybrid v2) | 3 | DaSiWa Hybrid Turbo v2 (int8 + ConvRot) | **The natural-skin one.** Darksidewalker's v2 Turbo (2026-09-11): FL2VA weights with a baked REF2VA delta, one 19.5 GB checkpoint for T2V + I2V + R2V, distillation baked in, nothing to install. Measured 2026-09-13 against the v1 pack on the same seed and prompts: at 4 steps it is softer than v1, at **8 steps** (default, ~100 s per 5 s shot at 480p) it gives the cleanest skin of every H3 turbo we ship - no oily sheen, no blown key light - where v1 reads bright and crunchy. Keep v1 for speed, use this for faces. Identity held on every reference test. Needs a Civitai API key (free model, sign-in required). |
| MiniMax H3 Lip-Sync | 1 | MiniMax H3 (pruned INT8) | Audio-driven lip sync with up to 9 reference images, so a whole band stays recognisable in a wide. Trims your track to the shot automatically; 10 s default. Reuses the H3 Turbo weights |
| MiniMax H3 Emotion TTS Lip-Sync | 1 | IndexTTS 2.5 + MiniMax H3 (pruned INT8) | Type the line in quotes, add an optional [emotion: ...] tag, supply a voice sample in the audio slot: IndexTTS 2.5 clones the voice and speaks the line with that emotion, H3 lip-syncs your reference character to it, all in one generation. Adds 7.7 GB of TTS weights and a node that downgrades the engine's transformers (allowed, persistent). English lines only. Requires SimpliGen 1.59.2 or newer (older apps skip the dotted TTS model folders) |
| MiniMax H3 Music Video Chain | 3 | MiniMax H3 fl2va (pruned INT8) + lightx2v fl2v Turbo v1.2 | A long single-take singing shot to YOUR song: 14, 21 or 27 s from 2, 3 or 4 H3 clips chained in one job. The song is locked into every clip and the finished file carries the original track (0.98-0.99 against the source, zero lag); each clip continues from the previous clip's latent, not from saved frames, so exposure, framing and sharpness stay flat and the cuts sit inside normal motion. Prompt: shared text first, then one `[Shot N]` block per clip. 480p; about 3 min per clip on a 4070 Ti. Steady rather than lively: for a performer singing to camera, not action |

**Music packs**

SimpliGen has no audio-only output yet, so these deliver each song as an MP4: the track plus its album art held on screen, the way a Sora song ships with a thumbnail.

| Pack | Presets | Architecture | Notes |
|---|---|---|---|
| Song + Album Art | 5 | YuE2 3B (INT8) + SheetSage2 + MiniMax Music 3 (INT8) + Qwen-Image 2.1 | **YuE2 Song + Album Art:** style tags in Subject & Action, lyrics in Character Dialogue with `[verse]`/`[chorus]` tags (any case), optional album art or a Character; leave it empty and Qwen-Image 2.1 paints art from the style. The song decides its own length up to the 6-minute cap: a 3:04 song rendered in 74 s on a 4070 Ti, 60 s in 38 s. YuE2 style LoRAs work (e.g. Atomtan Studio's DreamPop). **YuE2 Cover Song + Album Art:** upload a song (MP3/WAV/M4A, or an MP4's soundtrack), SheetSage2 transcribes its melody and YuE2 sings your lyrics in your style over it (paste the original lyrics to keep the words; leave them out and YuE2 writes new ones to the same tune); a full-length 4:25 cover took 126 s. Leave the BPM out of a cover's style: the tempo comes from the transcribed score. **YuE2 Faithful Cover + Album Art:** the same, but SheetSage2 also transcribes the chords and YuE2 follows them (full mode), so the cover keeps the original harmony as well as the tune (a 60 s test score carried 37 chord symbols against 0 in melody mode). First use needs one SimpliGen restart after the download (new audio_encoders folder). **Swap Album Art:** new picture on a finished song, audio untouched, about 10 s. YuE2 and SheetSage2 are CC-BY-NC-4.0 (non-commercial). **MiniMax Music 3 Song + Album Art:** MiniMax's structured caption (Global Metadata / Vocal Details / Arrangement) plus lyrics, up to 300 s, Apache-2.0; 61 s in 114 s. **Since 1.1.0 the pack needs SimpliGen engine 0.37.0**, which carries the upstream fix for the Music 3 noise bug, so the one-node GraphFix extension of 1.0.0 is gone. Album art is painted by Qwen-Image 2.1 (the same three files as the Qwen Image 2.1 pack, so nothing new downloads if that is installed): **Qwen Research Licence, non-commercial use only** - supply your own art to stay clear of it. For songs over three minutes turn on Settings > Advanced > Reduce system RAM usage |

Measured on a 12 GB RTX 4070 Ti — T2V, 5 s at 480p (864×480), one prompt and one seed across all seven, each preset at its own default step count. **SimpliGen 1.50.0, engine v0.33.1**, ~19 GB system RAM free at the start of each run:

| Preset | Steps | Time | Per step | vs. official |
|---|---|---|---|---|
| **10Eros Max + Turbo** | **6** | **67.9 s** | 5.16 s | **1.82×** |
| Turbo, Fast Motion | 4 | 80.9 s | 11.14 s | 1.53× |
| Fully Accelerated | 10 | 87.4 s | 4.86 s | 1.41× |
| Turbo | 6 | 102.7 s | 10.71 s | 1.20× |
| 10Eros Max | 20 | 119.1 s | 3.60 s | 1.04× |
| Official MiniMax H3 | 20 | 123.5 s | 3.01 s | — |
| Sol-Attn + EasyCache | 20 | 127.7 s | 4.18 s | 0.97× |

**SimpliGen 1.50.0 changed the baseline, not these packs.** 1.50.0 frees VRAM before decoding and unloads the text encoder before sampling. That took the *official* preset from 170.7 s to 123.5 s — a 28% gain — while every community pack here landed within a few percent of its pre-1.50.0 time. Nothing regressed; the thing they are measured against simply got much faster, so every ratio in this table is smaller than the one it replaces.

Two consequences worth stating rather than burying. **Sol-Attn + EasyCache is no longer a speed win** — at 0.97× it is marginally slower than the official preset, where it used to be 1.32× faster; its case now rests on output at the full 20 steps, not throughput. And the **Turbo-family gains are roughly half what they were**: Fast Motion was 2.15×, it is now 1.53×. Still a real saving, just an honest one.

Earlier figures for reference, measured on engine v0.31.0 / SimpliGen 1.46.0: official 170.7 s, Sol-Attn 129.5 s, Turbo 103.8 s, Fully Accelerated 84.1 s, Fast Motion 79.5 s.

Engine v0.31.0 took 8–18% off every one of these versus v0.30.1, and not evenly: the two 20-step presets gained most and the low-step Turbo presets least, which is what you would expect if the work landed in per-step execution rather than fixed overhead. Treat these as one run each — a repeat of the Sol-Attn row landed within 2%, but reference-to-video conditioning has shown far wider spread, so the I2V and R2V figures quoted in individual packs are less firm than these.

**A note on 10Eros and quantisation, because the earlier version of this README got it wrong.** On pre-1.50.0 builds 10Eros beat the pruned base by 22%, and that was attributed to it skipping per-step dequantisation on the 30 layers the pruned weights store as int8. The 1.50.0 numbers show that explanation was backwards: 10Eros is *slower* per step (3.60 s vs 3.01 s), and its advantage is lower fixed overhead, not cheaper compute. The old 22% was a VRAM-pressure artifact — while the run was memory-bound, streaming behaviour dominated and masked the per-step cost. Free the memory and the pruned base's smaller footprint wins on compute, leaving 10Eros ahead by only ~4%.

Two caveats worth stating plainly. These are single runs. And **free system RAM moves these numbers more than any preset choice does** — the same preset and seed measured 47.7 s with ~20 GB free and 78.6 s with ~2.8 GB free, a 65% swing. Quote your own free RAM alongside any timing, or the comparison means very little.

Every pack is self-contained: a `readme.html` with model download links and destination folders, a one-click `install.cmd` (full pack or single preset), the pack JSON, ComfyUI workflows, and preview thumbnails.

<p align="center">
  <img src="./assets/readme/section-pipeline.svg" width="100%" alt="02 — From repo to installed preset.">
</p>

<p align="center">
  <img src="./assets/readme/workflow.svg" width="100%" alt="Pipeline: pack sources in packs/ are built by build-zips.py into zips with readme.html and install.cmd, distributed via a rolling GitHub Release, installed by install.cmd which auto-downloads and verifies models, and appear in SimpliGen's picker under the Community prefix.">
</p>

```
python build-zips.py
```

Generates `community-<slug>.zip` per pack into `D:\SimpliGen-Backups\zips\` (readme.html + install.cmd/ps1 + pack JSON + workflows + previews). Both image and video packs are built. Any preset relying on a custom ComfyUI node gets that node's repo and install caveat written into its `readme.html` automatically, from the `CUSTOM_NODES` registry at the top of the script — add an entry there when you introduce a new one.

The installer prompts for a **Civitai API token** (required by Civitai for downloads) and a **HuggingFace token** where needed, verifies downloads, and reports failures honestly.

<p align="center">
  <img src="./assets/readme/section-authoring.svg" width="100%" alt="03 — Authoring your own pack.">
</p>

Each pack lives under `packs/<slug>/`:

```
packs/<slug>/
├── <slug>-pack.json     ← pack manifest (relative previews/ paths)
├── workflows/*.json     ← ComfyUI API-format workflows with {{placeholders}}
└── previews/*.jpg       ← 640×640 thumbnails
```

See [`CUSTOM-PRESET-AUTHORING-GUIDE.md`](./CUSTOM-PRESET-AUTHORING-GUIDE.md) — architecture detection, workflow families, the `simpligen_lora_1` LoRA marker, pack schema, thumbnails, installer conventions, and validation.

Key conventions:
- Models install to `%APPDATA%\simpligen\engine\models\<subfolder>\` — checkpoints→`checkpoints\`, UNet/GGUF→`diffusion_models\`, **CLIP/text encoders→`clip\`**, VAE→`vae\`.
- Pack names carry the `Community — ` prefix so they group together in SimpliGen's picker.
- JSON is UTF-8 **without BOM**; installed `previewImage` uses absolute `local-file:///` URIs, source uses relative paths.

<p align="center">
  <a href="https://github.com/oil-oil/beautify-github-readme"><img src="./assets/readme/made-with-beautify.svg" width="300" alt="README made with beautify-github-readme"></a>
</p>
