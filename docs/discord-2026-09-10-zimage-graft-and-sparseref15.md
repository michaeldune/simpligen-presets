:sparkles: **Two new H3 packs: MiniMax H3 (Z-Image Graft) and MiniMax H3 (SparseRef15)**

Both are drop-in checkpoint swaps on the official 20-step graphs, same speed and VRAM as the stock pruned int8, so if the official H3 pack runs for you these run too.

**Z-Image Graft** (joeygambino) — 3 cards, T2V / I2V / R2V
Stock H3 with Z-Image's attention-normalisation statistics transplanted in. No retraining, same identity and voices, but surfaces render richer: rust bleeds, paint peels, wet concrete carries more light. Measured on a 4070 Ti against the official checkpoint on the same seed and graph: rust-wall crop sharpness 596 vs 411, face crop 353 vs 243, a touch brighter, motion unchanged, same ~200 s per 5 s clip at 480p. Pick it for sets, materials and weathered locations. Two 21 GB files (FL2VA for text/image, ref2va for references); each card downloads only the one it uses.

**SparseRef15** (Aki7777777) — 2 cards, T2V / I2V
FL2VA with a sparse Ref2VA influence through 15 transformer blocks, built for character consistency without losing FL2VA motion. Same measurement: face crop sharpness 396 vs 243, the stillest locked-off shot and the most motion in the tracking shot among the 20-step arms, same ~200 s. One 21 GB file from Civitai (API key may be needed). Text and image cards only for now: it is not a native Ref2VA model, and the author's long-form identity claim is something we have not tested yet, so no reference card until we have.

Both verified in-app before shipping. Keep Spectrum off for any shot that carries a reference image, as with every H3 pack. Store picks them up on its next sync.
