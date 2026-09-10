# Reply draft — nurul3d, "MiniMax H3 Continue Clip (Motion Context) error" (2026-09-10)

Thanks for the diagnostics zip, that made it a two-minute read.

The job was submitted with a reference **image** and a reference **audio** file, but no video. The engine log says it outright: `No video uploaded (skipping video_file)`, then the two chain nodes fail with `Required input is missing: image`. Those nodes read the last 22 frames of the previous clip, and that clip has to go in the **Reference Video 1** slot. With that slot empty the app drops the video loader and the chain has nothing to continue.

So: put the clip you want to continue into Reference Video 1 (not the image slot, not the audio slot). The preset takes the soundtrack from that video itself, so you don't need to attach the audio separately. Reference images are optional and only for pinning a character.

One thing on our side: the preset already declares that slot as required, but the app let the job through anyway, so you got an engine error instead of a "Reference Video 1 is required" message. I'll flag that to Sharmystic so it gets caught before submission.

If it still fails with the clip in Reference Video 1, send another diagnostics export and I'll look again.
