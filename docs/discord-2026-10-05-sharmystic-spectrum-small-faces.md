Something you may want on your radar, from chasing down YaShiRo's distorted-faces report.

The short version: **Faster Attention visibly damages faces narrower than about 80 pixels on H3 i2v, and leaves
larger ones alone.** Three seeds out of three.

Setup: the official `minimax-h3-i2v` card, YaShiRo's own two frames and prompt, 480x864, 8 s, 20 steps, first and
last frame. Toggle-on renders went through the agent route so the graph is whatever the app actually builds, not
something I assembled; I read it back off the engine's `/queue` to be sure. For the record it comes out as

    simpligen_lora_1 -> sage_1 (PathchSageAttentionKJ, "auto")
                     -> simpligen_sigma_shift_1 (MiniMaxH3SigmaShift, shift_video 12, shift_audio 3)
                     -> simpligen_spectrum_1
                     -> simpligen_sol_attn_1

Toggle-off is the shipped template with none of the four, which I ran as the control.

In the 45-80 px band, the toggle-on clips lose face structure on every seed: eye sockets collapse into a dark band,
brows merge into the shadow, beards become a solid mass. The control's faces in the same band stay readable, with
eye, nose and beard edge drawn. Over about 100 px both look fine, which is why this only bites on wide shots with
people at a distance. YaShiRo's faces measure 26-60 px, median 53, so they sit right in it.

One extra data point that narrows it slightly. Before running the real toggle I had hand-built an arm with **only**
Spectrum and Sol-Attn, no Sage and no sigma shift. That arm shows the same damage on the same three seeds. So
Spectrum and Sol-Attn together are sufficient, and Sage and the sigma shift are not required for it. I cannot tell
you which of those two is responsible, since the app always injects them as a pair. Happy to run the single-variable
split if it would help.

Cost on a 4070 Ti was about 220 s with the toggle on and 481 s with it off, so roughly 2x.

I am not suggesting you change the default. The trade is clearly worth it for close-ups and it is a big speed win.
It might be worth a line in the UI or the docs, though, something to the effect that Faster Attention can cost fine
detail on small subjects, since nothing on screen currently connects "my distant faces look melted" to that toggle.
A user hitting this has no way to guess at it.

I have the nine clips and the comparison sheets if you want to look at them.
