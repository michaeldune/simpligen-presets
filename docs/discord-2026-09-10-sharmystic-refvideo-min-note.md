# Note draft — app does not enforce `acceptsReferenceVideos.min` (to Sharmystic, 2026-09-10)

Small one from nurul3d's "Continue Clip (Motion Context)" thread. The preset declares `acceptsReferenceVideos: {min: 1, max: 3}`, the user submitted with a reference image and a reference audio but no video, and the app sent the job anyway. The engine then rejected the graph (`No video uploaded (skipping video_file)`, then `Required input is missing: image` on the chain nodes), which surfaces as "The preset may need updating" — misleading, the preset is fine.

`acceptsReferenceImages.min` seems to gate the Generate button; `acceptsReferenceVideos.min` (and probably `acceptsReferenceAudios.min`) does not. A pre-submit check with a "Reference Video 1 is required for this preset" message would have saved the round trip. Diagnostics zip is in the thread if you want the log.
