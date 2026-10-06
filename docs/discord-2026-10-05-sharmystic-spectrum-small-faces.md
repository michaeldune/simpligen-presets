Chasing down YaShiRo's distorted-faces report turned into something I think you will want.

Short version: **it is Sol-Attn, not Spectrum, and Spectrum on its own is both clean and nearly as
fast.** Dropping Sol-Attn costs about 5% of the speed-up and fixes the faces.

Setup: the official `minimax-h3-i2v` card, YaShiRo's own two frames and prompt, 480x864, 8 s, 20
steps, first and last frame. Five configurations, three seeds each, fifteen clips. Everything with
an accelerator went through the agent route so the graph is whatever the app actually builds; I read
it back off the engine's `/queue` rather than assembling it myself. For the record, toggle-on is

    simpligen_lora_1 -> sage_1 (PathchSageAttentionKJ "auto")
                     -> simpligen_sigma_shift_1 (MiniMaxH3SigmaShift, shift_video 12, shift_audio 3)
                     -> simpligen_spectrum_1 -> simpligen_sol_attn_1

and the sigma shift is gated on Spectrum, so Spectrum-only keeps it and Sol-Attn-only does not.

| configuration | faces in the 45-80 px band | seconds |
|---|---|---|
| Sage + Sigma + Spectrum + Sol-Attn (toggle on) | damaged, 3 of 3 seeds | ~220 |
| Spectrum + Sol-Attn, no Sage | damaged, 3 of 3 | ~241 |
| Sage + Sol-Attn | damaged, 2 of 3 | ~290 |
| **Sage + Sigma + Spectrum** | **clean, 3 of 3** | **~230** |
| nothing (toggle off) | clean, 3 of 3 | ~481 |

Sol-Attn present, faces damaged. Sol-Attn absent, faces clean. That holds across all fifteen clips.
The one seed where Sol-Attn-only did not clearly show it was under-sampled rather than contradicting
(the detector mostly found trouser legs on that one).

The damage is eye sockets collapsing into a dark band, brows merging into the shadow, beards going to
a solid mass. Faces over about 100 px are fine in every configuration, so it only bites on wide shots
with people at a distance. YaShiRo's faces measure 26-60 px, median 53, right in the middle of it.

There is now an independent confirmation of this from the user's own machine, and it is a useful one. YaShiRo went
off and ran their own "Faster Attention OFF" test, which still came out with faulty faces. The workflow they attached
shows why: they had removed the SageAttention node and left everything else in place, so `h3_guider` and `h3_sigmas`
were both still reading from `simpligen_sol_attn_1`. That is precisely the Spectrum + Sol-Attn configuration from my
second row, on the same seed I used, and it failed the same way, down to the same dark smear across the eye sockets.
Different machine, same result.

Worth noting what they assumed, because I suspect others will assume it too: that turning Faster Attention off means
taking out the Sage node. Nothing told them it also governs a sigma shift, Spectrum and Sol-Attn.

So the thing I would actually suggest: **consider dropping Sol-Attn from the H3 i2v injection**, or
splitting it out of the combined toggle. Spectrum is where essentially all the speed comes from, and
it does not hurt faces. Right now a user cannot make that choice themselves, since `use_sage_attention`
is the only persisted setting and the Advanced panel has one combined switch, so anyone who hits this
has to give up the whole 2.2x to get their faces back.

Happy to be wrong about the mechanism, this is fifteen clips on one prompt. If you want a different
scene or more seeds before changing anything, say the word and I will run it.

I have all fifteen clips and the per-seed comparison sheets if you want to look.
