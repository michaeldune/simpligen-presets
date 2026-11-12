**New pack: MiniMax H3 Perfect Looper**
Seamless looping video with sound, after CoolBreeze_'s Perfect Looper workflow on Civitai. Six cards: text, image and reference to video, each on the official H3 base and on Singularity v2 (darker).

**How it works**
- Each card makes a short anchor clip, then a second clip that starts on the anchor's last frames and ends on its first ones, held in place by seitanism's Masked AV Bridge node. The end of the result runs straight back into its start, picture and sound.
- Larryvrh's Turbo LoRA, 6 steps. About 3 minutes for a 7 s loop at 480p on a 12 GB card.
- The loop comes out a little shorter than the duration you pick: 7 s gives 6.4 s.

**What to write**
- One shot. Start it with: No video cuts. Looping video. Movement loops in the end.
- Pick motion that can repeat: something on the spot, a there-and-back move, a full camera orbit that ends where it began. Say the camera stays still or ends where it started.
- Leave music out. A beat will not line up across the join; add a track afterwards.
- Image to video: your picture is the start of the loop, centre-cropped to the shape you choose.
- Reference to video: up to nine pictures; name each one as you would on the other H3 reference cards.

**One thing to know**
The join itself was clean in every test. In about 2 loops in 5, though, the picture drifts during the loop (often a slow push-in) and snaps back into place in the last few frames. If that happens, run it again with another seed.

**Download**
Uses the same weights as the official H3 pack and the Singularity v2 pack, plus the 744 MB Turbo LoRA. 32 GB of system RAM recommended.

Measured on a 12 GB RTX 4070 Ti.
Thanks to CoolBreeze_ for the workflow, seitanism for the bridge node and Larryvrh for the Turbo LoRA.
