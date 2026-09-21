POSTED by Michael 2026-09-21 on Discord. Announcement for the Qwen Image 2.1 pack. RELEASED 2026-09-21 12:11 (master 7617e7a pushed, zip on packs-latest). Zip built at
D:/SimpliGen-Backups/zips/community-qwen-image-21.zip. All 3 cards verified in-app on engine 0.37.0 /
app 1.64.0. Sample outputs: F:/SimpliGen/output/claude/qwen-image-21-pack*/2026-09-21_00001_.png

---

:frame_photo: **New pack: Qwen Image 2.1** (3 cards) - one model for text to image, editing and transparent cutouts

**Needs engine 0.37.0** (update the app to 1.64.0 first, then take the engine update).

- **Qwen Image 2.1** - text to image. It can spell: signs, labels and captions come out readable. About 20 s per image
  on a 4070 Ti.
- **Qwen Image 2.1 Edit** - 1 to 4 reference pictures plus an instruction in plain English ("the woman from image 2
  stands beside the man from image 1 on the same street"). Pick the output shape with the aspect selector. About a
  minute with two references.
- **Qwen Image 2.1 Cutout** - one picture in, the background removed, saved as a real transparent PNG at the size of
  your picture. The prompt is optional: use it to say what the subject is when the picture is busy.

Good to know:
- Every result from these cards is a PNG with an alpha channel, even when nothing is transparent.
- Editing gets slower with each extra reference (about 20 s, 50 s and 105 s for 1, 2 and 4).
- 17.3 GB download (int8 model, Qwen3-VL 8B encoder, VAE), all from Comfy-Org's repack.

:warning: **Licence: Qwen Research Licence, non-commercial use only.** Fine for personal work and experiments, not for
paid client work or anything you sell.

:inbox_tray: Zip: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest
