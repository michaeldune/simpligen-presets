Understood on all of it: we hold ours, push in your window, and set minAppVersion to the release you name.

Krea Flux repeat test is done, and it's the fork, not noise.

Same setup as before (plain ComfyUI v0.37.2, our krea-flux graph, `kreaCSG_foundation.gguf`, 1024x1024, 35 steps, seed 101, two prompts). Three runs per loader, with models and the execution cache freed between runs so nothing came back cached:

- **city96 `6ea2651`:** all three runs byte-identical, both prompts. Also identical to the render from before a ComfyUI restart.
- **molbal `48de657`:** all three runs byte-identical, both prompts.
- **fork vs city96:** 23.8 dB on the portrait, 21.0 dB on the street scene; 36% and 51% of pixels differ by more than 8/255. Same composition, different details (signage, small objects).

So each loader repeats itself exactly and they disagree with each other. Wan 2.2 Q4_K_M is still bit-identical between them.

One possible lead, not verified: the Krea Flux file contains Q5_K (38 tensors) and BF16 (10) alongside Q4_K and F32. The Wan file has Q4_K, Q6_K, F16 and F32 only. Q5_K and BF16 are the types that appear only in the file that differs.

What it means for our Krea Flux card: after the switch, the same seed gives a different picture. The fork's output looks just as good to me, so I'd treat it as acceptable, but it is a visible change for anyone re-running an old seed.
