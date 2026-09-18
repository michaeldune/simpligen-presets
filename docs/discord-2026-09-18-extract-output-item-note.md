SENT to Sharmystic by Michael, 2026-09-18.

---

Hey Sharmystic, one more from the Song + Album Art pack. I've worked around it on my side, but it's still an app
bug, and it'll hit any preset that loads a video.

**The gallery can pick the input file as the result.** `extractOutputItem` in the local provider returns the first
`images`/`gifs` entry in `Object.keys(outputs)` order, without checking `type`. Core `LoadVideo` posts its input
clip as a preview (`type: "input"`), and it runs before the save node, so its entry comes first.

What that looked like with my Swap Album Art card (loads a song MP4, writes it back with new art):
- `result_url` saved as `local-file:///F:/SimpliGen/output/ref0.mp4`, then `.../output/b514ac85....mp4` on the next
  run. Neither file exists; the real MP4 was in `output/claude/<preset>/`.
- Black gallery tile, the player stuck at `0:00 / 0:00`, and Export offered "ref0.mp4", which the user couldn't find.

**Suggested fix:** skip items whose `type` isn't `"output"`, or prefer the save nodes.

**My workaround:** I gave the save node a numeric id (`"9000"`). JS lists integer-like keys first, so the saved MP4
now comes first. It's verified in the app: the gallery shows the new art and plays the full song. But it only works
because of how JS orders keys, and every other author who loads a video would have to know that trick.

**Related, not a bug, just a request:** the reference-clip windowing (`windowRefVideosToDuration`) cut the song to
the card's duration before the workflow saw it. That's right for H3, but a remux card wants the whole clip. I worked
around it with a fixed 240 s `enum` duration. A per-preset opt-out (something like `acceptsReferenceVideos.window:
false`) would be cleaner if you ever touch that code.
