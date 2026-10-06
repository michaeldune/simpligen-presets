That is really useful, thank you, and the workflow you attached explains the result exactly: **your OFF test was not
off.** Sol-Attn was still running, and Sol-Attn turns out to be the part that does the damage.

Your `Exact-OFF-workflow.json` still contains `simpligen_sigma_shift_1`, `simpligen_spectrum_1` and
`simpligen_sol_attn_1`, and the two nodes that matter still read from the last of those:

```
"h3_guider": { "inputs": { "model": ["simpligen_sol_attn_1", 0] ... } }
"h3_sigmas": { "inputs": { "model": ["simpligen_sol_attn_1", 0] ... } }
```

Removing the SageAttention node does not take the others out. In the app, the Faster Attention switch controls all
four at once (Sage, a sigma shift, Spectrum and Sol-Attn); editing the JSON by hand only removed the first.

To answer your question directly: **no, Spectrum and Sol-Attn were not both on in my clean runs.** I have since
split them, three seeds each, and it lines up with what you got:

| configuration | faces |
|---|---|
| Spectrum + Sol-Attn, Sage removed  (= your OFF test) | damaged, 3 of 3 |
| everything on | damaged, 3 of 3 |
| Sol-Attn only | damaged |
| **Spectrum only** | **clean, 3 of 3** |
| nothing | clean, 3 of 3 |

I ran your configuration on your seed, 510261, and got the same failure you did, the same dark smear where the eye
sockets should be. So your result reproduces mine rather than contradicting it.

**If you want to fix it in the JSON and keep the speed**, delete `simpligen_sol_attn_1` and point those two inputs
one node earlier:

```
"h3_guider": { "inputs": { "model": ["simpligen_spectrum_1", 0] ... } }
"h3_sigmas": { "inputs": { "model": ["simpligen_spectrum_1", 0] ... } }
```

That keeps Spectrum, which is where nearly all the speed-up comes from, and in my tests it rendered clean faces on
every seed. **To turn everything off**, delete all four SimpliGen nodes and point both inputs at `simpligen_lora_1`
instead, or just use the Settings toggle, which does the same thing. Note that the toggle also removes the sigma
shift, so an app-toggled-off render will differ from your hand-edited one in more than just Sol-Attn.

On the aspect-ratio idea from the LTX thread: I do not think that is your problem here. Your output is 480x864,
which is exactly 9:16, and the workflow centre-crops both reference images to that shape, so nothing is being
squeezed. What matters is how many pixels the faces get. At 480x864 your movers' faces are 26-60 px wide, median 53,
and that is the range where this breaks. 768p (native) is 768x1344, which takes a 53 px face to about 85 px.

One caveat worth stating: your earlier "higher resolution and exact 9:16" tests were presumably still carrying
Sol-Attn, since the workflow you sent does, so those results are confounded. I would re-run one of them with
Sol-Attn removed before concluding anything about resolution or framing.
