# Note to Sharmystic — 0.36 beta soak, 2026-09-16 (to send)

Soak on engine 0.36.0, 4070 Ti, one 5 s / 480p talking-head clip per pack, seed 101:

| pack | result on 0.36 |
|---|---|
| DaSiWa Hybrid v2 | ok (accel=none) |
| H3 Unlocked (1.63 official) | ok (sage + sol-attn) |
| PDD Acc (custom PDD node) | ok, 96 s; its node still fuses heads itself, core's native PDD path untouched |
| TaoMate 3-Step (new) | ok, 50 s |
| FastH3 8-Step V2 (new, held) | ok, ~80 s, VSA node accepted |
| **Turbo Accelerated** | **FAIL** – `FinalLayer.forward() missing 3 required positional arguments: 'sigma', 'sample_sigmas', and 'shifts'` (accel=sage only; the pack bakes SpectrumApplyMiniMaxH3) |
| **10Eros beta5 Turbo** | **FAIL** – same error (accel=sage+spectrum+solAttn, Spectrum app-injected) |

Root cause: the Spectrum node (xmarre/ComfyUI-Spectrum-MiniMax-H3) at the pinned commit 0aeac54 (2026-08-14) calls `inner.final_layer(compact, t_emb, video_seg, audio_seg)`; core 0.36's PDD-aware FinalLayer needs `sigma, sample_sigmas, shifts` too. Upstream fixed it on 2026-08-29 (c7ea4b7 "Fix MiniMax H3 PDD final-layer forecast compatibility", #84) and is at v0.2.27 (120d72e, 2026-09-12). Verified: with the engine checkout at 120d72e and a matching pin, a Spectrum-injected render on 0.36 completes (TaoMate, 48 s, accel=sage+spectrum+solAttn).

So on 0.36 every render that touches Spectrum fails — the user's Spectrum toggle on any pack declaring supportsSpectrum, plus the three cards that bake the node — until the Spectrum checkout moves. And it cannot simply be moved: every pack that lists the extension pins 0aeac54, including the official minimax-h3 / turbo / gguf / unlocked packs. With the checkout at v0.2.27 the app marks all of those cards "not installed locally" (pin mismatch) and a repair would check the broken commit back out. Verified both directions on this machine.

Suggested path: bump the Spectrum pin in the official packs to 120d72e in the same release that takes 0.36 stable, and tell community authors to do the same. I'll bump all eight of mine (10Eros ×3, Singularity, SparseRef15, Zimage Graft, Turbo Accelerated, TaoMate) with version bumps the day 0.36 goes stable — not before, since v0.2.27 has not been tested on 0.34. If you'd rather, an engine-side override that ignores stale Spectrum pins would let both eras coexist.

Also confirmed: the two new packs (TaoMate, FastH3) render on 0.36; FastH3 is committed on a local branch only, per your hold. Krea 2 Finetunes 1.2.0 with the FinalCut Massive Update file is on master and the release.
