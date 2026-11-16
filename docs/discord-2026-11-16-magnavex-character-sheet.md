@Magnavex good call, it's in. The MiniMax H3-Image (open weights) pack goes to 1.1.0 with two new cards:

**MiniMax H3-Image Character Sheet**
- One picture of your character in, a reference sheet out at 16 MP on a white background: a front portrait and a side portrait stacked on the left, then the full body from the front, the side and the back.
- It's laid out like ukr8b3g-cmyk's H3 Character Sheet Designer for ComfyUI: the brief and your picture go straight to the model, so no extra node is needed.
- The brief is built in, so the prompt box is just for extra notes. "Draw him in a soft watercolour style" turned a cel-shaded anime character into watercolour across all five views.
- Use a full-body picture so it keeps the whole outfit. With a head-and-shoulders picture the clothes below get invented.
- Set the aspect ratio to 21:9 (6272x2688). 16:9 and 1:1 also gave all five views in our tests, just packed tighter.
- About 75 seconds on a 12 GB card. In our tests (a photo and an anime character, two seeds each) every sheet had all five views, with face, outfit and props carried through: lantern, jacket patches, striped socks.

**MiniMax H3-Image Edit 16 MP**
- The same edit as the Edit card, with the result at about 16 MP in picture 1's shape (a 16:9 picture comes back at 5440x3072).
- About 2 1/2 minutes for a one- or two-picture edit.

Neither card adds a download: they use the files the pack already has. It reaches the Store with the next sync. Update the pack and both cards show up.
