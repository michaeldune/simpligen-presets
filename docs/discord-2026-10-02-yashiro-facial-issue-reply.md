Thanks for sending the images, the prompt and your settings. I reproduced it, and I think I can tell you what is
happening and what to do about it.

I rebuilt your job here (your two frames, your prompt, your seed, 480x864, 20 steps, first and last frame; 8 seconds
rather than 15, to keep the test affordable) and ran it twice: once with **Faster Attention on**, exactly as you had
it, and once with it off. Everything else was identical. Then I did the same with two more seeds, so three pairs in
total.

**The faces come apart with Faster Attention on, and hold with it off. Three seeds out of three.**

With it on, every face narrower than about 80 pixels loses its structure: the eye sockets collapse into a dark band,
the brows merge into the shadow, a beard goes to a solid mass. With it off, faces the same size in the same clip stay
readable, with the eye, nose and beard edge all drawn. Faces larger than about 100 pixels were fine either way, which
is why this shows up on a wide room shot and not on a close-up.

In your clip the faces measure between 26 and 60 pixels wide, median 53. That is right in the middle of the band that
breaks.

So, two things to change:

**1. Turn off Settings > Advanced > Faster Attention for shots like this.**
It is the single thing that fixed it in my tests. The cost is real: it roughly doubled my render time (220 seconds
became 481 for an 8-second clip). For a wide shot full of distant people that trade is worth it. For close-ups,
leave it on, it costs you nothing there.

**2. Render the people bigger.**
At 480x864 your movers only ever get ~50 pixels of face, which is very little for H3 to work with even without the
accelerator. Switching to 768p takes the same framing to roughly 85 pixels of face, which is out of the band where I
saw the damage. Pulling the camera in, or framing waist-up instead of the full room, does the same thing for free.

Worth saying as well: an upscaler will not rescue this one. Upscaling makes what is there bigger and cleaner, but it
cannot rebuild an eye that was never drawn in the first place, so a face that came out structurally wrong stays
structurally wrong however far you enlarge it. This has to be fixed at generation time.

Nothing to fix in the preset itself, for what it is worth. It is the official Image to Video card doing what it
should, and the accelerator is an app-level setting that sits on top of it. Your prompt is genuinely good, the
choreography came through cleanly in every single run.
