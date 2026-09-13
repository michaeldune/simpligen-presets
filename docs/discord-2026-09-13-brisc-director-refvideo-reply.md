# Reply draft — brisc, "Two-Shot Director suddenly needs a reference video" (2026-09-13)

_Posted by Michael 2026-09-13 ~12:00 EDT._

Thanks for the logs, and for the kind words about the Director. Agreed, it deserves more use.

**The "At least 1 Reference videos" block was our mistake.** The Director card's manifest said it needed at least one
reference video. That line was copied from the two Continue Clip cards in the same pack, which really do need a clip,
since they continue from one. For a week it did nothing, because SimpliGen didn't check reference minimums. 1.60.0
started checking them before Generate, and that turned the typo into the block you hit. The Director itself never
needed a video.

Fixed in **Clip Chaining 1.1.1**. Only the manifest changed: the workflow is the same, so your output won't change. I
ran it this morning with one reference image and no video (480p, 2×5 s, Faster Attention on). It finished in about
7 minutes on a 12 GB card, and the join is clean. The store syncs every few hours; once 1.1.1 appears, take the
update and the card works the way it did before. One thing still applies: SimpliGen refuses a run with no reference
at all (an image, clip or sound), because that would quietly become text-to-video. At least one reference image is
enough.

**About the run that stalled with the video attached:** your log shows it at 1344×768, 15 s per segment, 4 references,
with Sage and Sol-Attn both on. It never finished step 1 in the 58 minutes before you cancelled. There's no crash and
no out-of-memory error, just no progress. Two things stand out:

- **Size.** Each segment was 362 frames at 1344×768. That's about 7× the tokens of the test I ran, and attention cost
  grows faster than the token count. So a slow first step is expected at that size. A whole hour with nothing is
  still more than I'd expect from size alone.
- **Memory at submit.** When that job was queued, only 4.9 GB of your 32 GB of VRAM was free: the H3 Image model from
  your earlier edits was still loaded, and auto-unload is off in your settings. The app asks the engine to free the
  old models, but for a job this big, starting from a clean slate helps.

If you have a moment, these would narrow it down:
1. What resolution and duration did your 30-second runs use a few days ago, when it worked?
2. Try the same video-attached job once at 480p with Faster Attention **off**, straight after an app restart.
   If that runs, turn Faster Attention back on at 480p. That separates attention from size.
