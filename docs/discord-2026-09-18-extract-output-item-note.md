HELD - not sent. Draft for Sharmystic (2026-09-18).

---

Hey Sharmystic, one more from the same Song + Album Art pack. Small one, and I've already worked around it on my side.

**The gallery can pick the input file as the result.** `extractOutputItem` in the local provider returns the first
`images`/`gifs` entry in `Object.keys(outputs)` order, without checking `type`. Core `LoadVideo` posts its input
clip as a preview (`type: "input"`), and it runs before the save node, so its entry comes first.

What that looked like with my Swap Album Art card (loads a song MP4, writes it back with new art):
- `result_url` saved as `local-file:///F:/SimpliGen/output/ref0.mp4`, then `.../output/b514ac85....mp4` on the next
  run. Neither file exists; the real MP4 was in `output/claude/<preset>/`.
- Black gallery tile, the player stuck at `0:00 / 0:00`, and Export offered "ref0.mp4", which the user couldn't find.

Any preset that loads a video with core `LoadVideo` will hit this. Possible fix: skip items whose `type` isn't
`"output"`, or prefer the save nodes.

My workaround: I gave the save node a numeric id (`"9000"`). JS lists integer-like keys first, so the saved MP4 now
comes first. I checked it by running your `extractOutputItem` logic on the engine's real history for that job; it
now picks the saved MP4.

**Related, not a bug, just a request:** the reference-clip windowing (`windowRefVideosToDuration`) cut the song to
the card's duration before the workflow saw it. That's right for H3, but a remux card wants the whole clip. I worked
around it with a fixed 240 s `enum` duration. A per-preset opt-out (something like `acceptsReferenceVideos.window:
false`) would be cleaner if you ever touch that code.
