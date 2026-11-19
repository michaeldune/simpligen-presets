**Video Studio fix: "Continue from the end of" now works with a cast on the community H3 packs**
Thanks to @KevinLewis for the report.

**What was wrong**
A clip with a cast always renders through the pack's reference-to-video card. The app only hands that card the last frame of the clip before if the card says it can pin a frame. The official H3 cards and Midnight say so. Our community packs didn't, so a cast clip set to continue quietly started fresh from the cast pictures. Clips without a cast were never affected.

**What changed**
The reference card in each of these packs now says it can pin a frame:
- Pika Flex 1.0.8
- PRISM-PIKA 1.0.8
- DaSiWa GXS v5 1.0.4
- Hybrid DMAD PDMD 1.0.4
- Turbo Accelerated 1.7.8
- Heptagram v2 1.0.7
- 10Eros beta7 fix1 1.0.6

Update them in the store. Nothing new downloads; only the card settings changed. Then re-render any clip that should continue.

We filmed it on Pika Flex: before the update the continuing cast clip opened on a different shot, after it the clip opens on the exact last frame.

**Why 8+2 can't do it**
The 8+2 cards render in two passes: eight steps at a small size, an upscale, then the last two steps at full size. The pinned frame is made for the small first pass, the full-size pass doesn't fit it, and the render stopped with a "shape mismatch" error. 8+2 had the change for a few hours today as 1.0.3. If you updated it and a continuing clip failed, update to 1.0.4 (in the store after the next sync, around 7 PM Eastern). On 1.0.4 a cast clip set to continue starts fresh again, so pick another build for that clip.

**Worth knowing**
The last frame decides how the clip opens, not where it goes. Describe the same camera move and the same outfit in the next clip's prompt.
