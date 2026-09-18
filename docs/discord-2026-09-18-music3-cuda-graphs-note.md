SENT to Sharmystic by Michael, 2026-09-18.

---

Hey Sharmystic, heads-up: MiniMax Music 3 produces noise in SimpliGen's engine on every render, and there's no
error. It's a known upstream ComfyUI bug, but SimpliGen's `--disable-cuda-malloc` launch flag makes it hit every
time.

**Upstream:** Comfy-Org/ComfyUI#16002 (comment by woshilhz001, 2026-09-09) and #16222. Commit 804eb551 (Comfy
Compiler) replaced the fixed-address buffers that `Llama2_.forward` used for CUDA-graph capture with `x = x.clone()`,
so graph replays in the AR text encoder read stale, freed memory. The result is garbage audio codes and noise, with
no error. That comment includes a patch to `comfy/text_encoders/llama.py`, reported as verified at full graph
speed. Both issues are still open.

**Why SimpliGen hits it every time:** with cudaMallocAsync on, the freed memory often survives by luck. With
`--disable-cuda-malloc` it gets reused. My repro on vanilla ComfyUI 1a14b82e (5 commits behind v0.36.0), with the
official Music 3 template, its example prompt and seeds, the Comfy-Org int8 files, 30 s, RTX 4070 Ti, torch
2.11.0+cu130:

| launch flags | result |
|---|---|
| (none) | clean lo-fi track (listened) |
| `--disable-cuda-malloc` (SimpliGen's flag) | NaN audio, same as the engine |
| `--disable-cuda-malloc --disable-cuda-graphs` | bit-identical to the clean track (72 s vs 44 s) |

In SimpliGen the NaN makes an MP4 save fail with `avcodec_send_frame() returned 22`; an audio-only save gives noise.
YuE2 is NOT affected: the same test graph gives bit-identical output in the engine and in vanilla, and it's real
music.

**Options:** add `--disable-cuda-graphs` until upstream merges a fix (costs Music 3 ~40% speed; other models that
use graphs would slow down too), carry the #16002 patch in the engine, or wait for upstream. Happy to test any
build.

I have a "Song + Album Art" pack ready (a song plus album art, delivered as an MP4, since there's no audio output
type yet). Its YuE2 card works now; the Music 3 card is held until this is fixed.

