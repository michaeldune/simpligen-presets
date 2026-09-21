POSTED by Michael 2026-09-21 ~14:49 on Discord. Reply to the Discord question "What are the differences between MiniMax H3 10Eros Turbo and 10Eros beta5
besides the steps?" (2026-09-21). Facts from the pack manifests and the 2026-09-09 bake-off
(D:/SimpliGen-Backups/10eros-beta5-bake-20260909/VERDICT.md).

---

They are different checkpoints, not the same model at different step counts.

**10Eros Max, Turbo** (the older pack)
- TenStrip's ORIGINAL 10Eros Max: a finetune of the H3 first/last-frame base, in DmitryDB's INT8 quant.
- Speed comes from a separate Turbo LoRA (larryvrh v4) loaded on top, 6 steps.
- Because it is built on the first/last-frame base, its reference-to-video card is that base doing a job it was not
  trained for. It works, but characters hold less well.

**10Eros Max beta5** (the newer packs)
- TenStrip's current release, and the only one he now calls functional. It is a rebuild, not a small update: a hybrid
  base with concept grafts and a merge of 20+ LoRAs on top. It is a separate 21 GB download.
- It is a true hybrid, so text-, image- AND reference-to-video all run on weights made for them. Reference-to-video is
  where you will notice it most.
- In my side-by-side (same prompts, same seed): cleaner faces (the original had a mouth artefact that beta5 does not),
  real motion blur on fast subjects, and the 20-step version rendered about 20% faster than the original at 20 steps.
- Two packs: **beta5** = 20 steps, no LoRA, the full look. **beta5 Turbo** = 8 steps on a file with the turbo already
  fused into the weights, so there is no Turbo LoRA to download or mismatch. On image-to-video the 8-step Turbo came out
  sharper than the 20-step at about half the time.

Which one: beta5 Turbo for everyday use, beta5 (20 steps) when you want the most natural motion and do not mind waiting.
I would only keep the original Turbo pack if you like its particular look, since it is a different finetune and does
render differently. All of them produce audio.
