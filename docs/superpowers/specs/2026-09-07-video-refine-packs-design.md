# Video Refine packs: MiniMax H3 (PDD) and LTX 2.5 (MSR)

Date: 2026-09-07. Approved by Michael in session.

## Goal

Take a finished MiniMax H3 clip (typically 480p from a Community H3 pack) and
re-render it at a higher tier while keeping its motion, audio and cast. Two
routes, shipped as two packs because the installer downloads every model a
pack declares and the LTX stack is 21.5 GB that H3 users should not be forced
to fetch.

Source of the idea: The Ai Blueprint, "I Combined MiniMax H3 + LTX 2.5 MSR for
INSANE Upscaling" (youtube A1zBGc3oqAY, 2026-09-07), and the
ComfyUI-MiniMax-H3-PDD-Acc `pdd_video_upscale_long.json` example (2026-08-30).

## Pack 1: `minimax-h3-refine` — Community — MiniMax H3 (Video Refine)

One preset: **MiniMax H3 Video Refine (PDD 8-Step)**.

- Input: Reference Video 1 (required, `acceptsReferenceVideos` min 1 max 1,
  soundtrack true). Prompt: the same H3 brief that made the clip.
- Graph: LoadVideo(`{{ref_video_1}}`) -> GetVideoComponents -> H3 video VAE
  encode -> `MinimaxH3LatentUpscaler3D` (target `{{width}}` x `{{height}}`) ->
  `MiniMaxH3PDDAccApply` (Ref2VA distill on the ref2va INT8 base) ->
  `MiniMaxH3PDDAccScheduler` steps 8, denoise 0.25 -> `MMH3SplitUpscale`
  windowed refine (73-frame windows, 22 overlap, from
  `MMH3TemporalSplitParamsV10`) -> VAEDecode -> CreateVideo with the source
  audio (`{{ref_video_audio_1}}`) -> SaveVideo. Frame count comes from the
  clip; the duration slider is not used by the graph.
- Sampler: euler, CFG 1.0, sigma shift 12.0/3.0 (enforced by the node).
- Weights: `minimax_h3_ref2va_pruned_int8_convrot.safetensors` (shared with
  every R2V pack), `MiniMax-H3-Ref2VA-Acc-8Step.safetensors` in `pdd_acc/`
  (1.37 GB), `minimax_h3_latent_upscaler_3d_fp16.safetensors` (shared with
  Two-Stage), H3 video + audio VAEs, Qwen3-VL encoder.
- Extensions: ComfyUI-MiniMax-H3-PDD-Acc pinned at 8335330 (verified
  2026-09-07), Comfyui_Minimax_h3_latent_Upscaler pinned as in Two-Stage,
  ComfyUI-KJNodes, rgthree-comfy.
- Output tiers: 720p and 768p (the Two-Stage table). Inputs are expected at
  480p; a 2x upscaler on a 768p input is out of scope.

## Pack 2: `ltx-2-5-refine` — Community — LTX 2.5 (Video Refine, MSR)

One preset: **LTX 2.5 Video Refine (Multi-Reference)**.

- Input: Reference Video 1 (required). Reference images 1-4 optional, mapped
  to MSR slots pic1..pic4 to hold faces. Prompt is LTX style; the description
  carries a one-line template ("<who> <does what> in <where>, <camera>,
  <light>").
- Graph: LoadVideo -> LTX video VAE encode -> `LTXVLatentUpsampler` 2x
  (`ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors`) ->
  `ComfyUILTX25MSRICLoRALoader` + `ComfyUILTX25MSRMultiReferenceGuide` ->
  `LTXVConcatAVLatent` with the source audio encoded by `LTXVAudioVAEEncode`
  -> SamplerCustomAdvanced on the distilled LTX 2.5 with the A2V pack's
  stage-2 manual sigma tail -> `LTXVSeparateAVLatent` -> `LTXVCropGuides` ->
  VAEDecodeTiled -> CreateVideo with the source audio -> SaveVideo.
- Weights: official gated LTX 2.5 distilled INT8 transformer, Gemma encoder,
  video + audio VAEs (all shared with the A2V pack), the 2.5 latent upsampler,
  `LTX-2.5-Licon-MSR-V1.safetensors`.
- Extensions: ComfyUI-LTX2.5-MSR (the pack the official Multi-Reference
  preset uses), pinned to the installed commit.
- Output tier: 1080p at 1920x1088 (the A2V pack's verified size).

## Verification (both packs, before anything ships)

- Input: the 2026-09-07 PDD R2V clip (864x480 / 5 s, Ekello). Pack 2 also
  gets the Ekello sheet in reference slot 1.
- Run through the SimpliGen MCP, not by direct engine submission.
- Pass: no node error; output is the requested size; audio stream present
  with a peak within 3 dB of the source; face on a 6-frame contact sheet
  matches the source sheet by eye; render time recorded on the 4070 Ti.
- Pack 1 also renders a 10 s clip to exercise more than one window.

## Ships

Pack JSON, workflow, preview from the test render, README catalog rows,
authoring guide rows, zips on `packs-latest`, memory note. Versions 1.0.0.
No shipped preset is modified.

## Out of scope

Upscaling clips that already lost identity (Pack 1 cannot repair a face),
inputs above 480p, clips longer than 15 s, and any change to the PDD Acc pack.
