# Note draft — "Resolution" in Generation Settings is the request, not the file (to Sharmystic, 2026-09-24) (SENT by Michael 2026-09-24)

Hi Sharmystic, a small display suggestion, off the back of a bug that was entirely mine.

**What happened on my side.** My Qwen Image 2.1 "Enhance to 4MP" card had the 1 MP `resolutionOverrides` map copied
over from the 1 MP cards, so Generation Settings reported **1344 x 768** while every file it produced was
**2752 x 1536**. I noticed because three enhanced pictures looked like they had shrunk, went to the panel, and
believed it over the files. Fixed in 1.5.1, manifest only.

**The part that might interest you.** That card's workflow has no `{{width}}`/`{{height}}` at all: it scales the
reference with `ImageScaleToTotalPixels` at 4 MP and samples that. So the number the panel showed was the canvas the
app computed from the aspect map, which the graph never read. The label says "Resolution", and a user reasonably
reads that as "the size of this picture".

This is not specific to my pack. It applies to any preset that sizes itself from its input - enhance and upscale
shapes generally, including the official ones - and it stays true even with my map corrected: feed my card a 4:3
picture with 16:9 selected and the panel will say 2752 x 1536 while the file is 2400 x 1792, because the output keeps
the source's shape.

**Suggestion, whenever it is cheap:** show the produced size. The app has the finished file, so either
- replace the requested canvas with the real dimensions once the job completes, or
- show both when they differ ("2752 x 1536 requested, 2400 x 1792 produced").

Either one would have caught my bad map before it shipped, and it would make the panel trustworthy for every
self-sizing preset. Low priority - nothing is broken, and the pack fix is already out.

---

**Sharmystic's reply (2026-09-24):** "ahh nice find. ill add it to this hotfix, should be a quick fix" — so the
produced size lands in the same hotfix as the flash-decode driver fallback. Once it ships, re-check the Enhance to 4MP
card with a 4:3 source and 16:9 selected: the panel should stop claiming the picker's canvas.
