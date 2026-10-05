Thanks for the details, that was enough to test it properly.

I ran your exact setup here: MiniMax H3 Image to Video (Turbo, Fully Accelerated), 480p, 15 seconds, 10 steps, Faster
Attention on, a first frame and a last frame. The face held all the way through the clip: profile at the start,
three-quarter in the middle, straight to camera at the end, with no melting or warping. So the preset and those
settings on their own don't produce what you are seeing, which means the difference is in what goes into it.

Could you post:

1. **The two images you used** (first frame and last frame), as files rather than screenshots if you can, so I get the
   real resolution.
2. **The exact prompt** you gave it, copied as text.

With those I can run your job here and see the same thing you see, instead of guessing.

Two things I'd look at in the meantime, because they are the usual causes when a face comes apart in the middle of a
clip:

- **How big the face is in frame.** At 480p a person at that distance gets maybe 100 pixels of face, and H3 has very
  little to work with. Jumping to 768p is one click and is the biggest single improvement for faces.
- **How much has to happen between your two frames.** The first and last frames are pinned, and everything between
  them is invented. If the pose, angle or distance changes a lot across 15 seconds, the middle has the furthest to
  travel. Shorter clips, or a last frame closer to the first, give the face an easier job.

If the prompt asks for speech, strong motion, or a camera move, mention that too; all three make faces harder.
