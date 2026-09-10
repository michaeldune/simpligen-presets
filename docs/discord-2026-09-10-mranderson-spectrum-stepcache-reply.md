# Reply draft — Mr.Anderson, "Spectrum and step caching OFF for reference shots" (2026-09-10)

Good question, and the wording was sloppier than it should have been. Two answers:

**Which shots.** Any shot that carries a reference image, so R2V and also I2V when you drop a reference picture in. The reason is what Spectrum does: it predicts some transformer steps instead of running them, and the small errors it introduces land hardest on the thing the reference is pinning down, faces and identity. Plain T2V and first-frame I2V with no reference are fine with it on.

**Where step caching is.** It isn't a switch in the 10Eros beta5 packs, so there is nothing to find. The only app-level toggles those packs expose are Faster Attention and Spectrum. Step caching (EasyCache) only exists in packs whose graph has it baked in, the "Sol-Attn + EasyCache" pack and the "Turbo Accelerated" pack. If you're on a beta5 card, turning Spectrum off is the whole instruction. If you're on Sol-Attn + EasyCache or Turbo Accelerated for a reference shot, pick a different card instead, since the cache can't be switched off there.
