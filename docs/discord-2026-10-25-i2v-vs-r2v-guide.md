## Image to Video vs Reference to Video — which card do you want?

Three questions this week all turned out to be the same thing, so here's the distinction in one place.

**The rule, in one line:**

- **Image to Video (i2v)** — your picture *becomes a frame of the video*.
- **Reference to Video (r2v)** — your picture *describes something that should appear in* the video.

Every MiniMax H3 pack has both, and they take different slots:

| Card | Picture slots | Video slots |
|---|---|---|
| Text to Video | none | none |
| **Image to Video** | **First frame**, Last frame (optional) | none |
| **Reference to Video** | **Reference 1 … Reference 9** | up to 3 |

Read the slot labels — they're telling you exactly what the picture is for.

### "My reference picture flashes on screen at the start, then it cuts"

You're on Image to Video. The first slot is called **First frame** and it means it: your picture *is*
frame 1 of the clip.

It looks like a glitch when the picture doesn't match the scene — a studio portrait on a white
background followed by a prompt about a forest path. There's no way to move continuously from one to
the other, so the model abandons the portrait after a couple of frames and starts the real shot. You
see a hard cut.

If you want the character but not the picture on screen, that's **Reference to Video**.

If you genuinely want Image to Video, give it a first frame that is *already the scene* — your
character standing on that path, not a portrait. A good trick: run the same prompt through an image
card first and use that picture as the first frame.

### "Can I add a face photo to keep the character consistent?"

Yes — on **Reference to Video**, which takes up to **nine** reference pictures.

Not on Image to Video. Its second slot is the **Last frame**, so a face photo dropped there tells the
clip to *end* on that photo.

With more than one reference, name them in the prompt so the model knows which is which:

```
<Subject 1> is the woman in <Picture 1> and <Picture 2>, with long dark hair and a grey wool coat.
```

References are numbered **in the order you attach them**, so attach them in the order you name them.
Citing two pictures of the same person is the intended usage, not a hack — one reference gives the
model less to hold and identity softens as the camera moves.

### "I gave it a dance clip and the result came back in slow motion"

Reference to Video takes **video** references too, but the word reference is doing real work: the
model *draws motion and camera work from* the clip. It does not copy it frame by frame.

Which means the length of your result comes from the **duration slider**, not from your clip. Put in a
five-second dance, ask for eleven seconds of video, and the same movement gets spread across twice the
time. That's your slow motion. Match the duration to the clip and it comes back roughly right.

For an exact copy of the movement, you want a card built to drive from the source instead:

- **Character Swap** — replaces one person in your clip with your character, leaving the rest alone.
  Because it edits the existing clip, the timing is the original timing.
- **Viggle Animate (H3)** — driving clip plus a character picture (5 seconds).
- **Motion Transfer** — a movement clip drives a brand-new scene you describe in the prompt.

### Quick guide

- The picture should be the **opening shot** → Image to Video
- You have a start *and* an end picture → Image to Video, both slots, it runs first to last
- The picture is **a character, an outfit, a place or a style** that should appear → Reference to Video
- You want **several** things kept consistent → Reference to Video, one picture each, named in the
  prompt
- You want a clip's **exact movement** copied → Character Swap, Viggle Animate or Motion Transfer

One last thing that catches people out on both cards: the camera. If you don't say what the camera
does, H3 drifts and reframes on its own. For a locked shot, write that the frame never moves and say
what must not happen — no pan, no push-in, no reframing.
