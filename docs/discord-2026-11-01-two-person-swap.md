**New pack: MiniMax H3 Two-Person Swap - two people in a clip, two characters of your own**
The Character Swap card replaces one person. This one replaces two at once and leaves everyone else in the shot alone. The camera, background, motion, cuts and the clip's own soundtrack stay. The graph is D3voz's, from OpenJutsu: SAM 3.1 tracks the people, a small vision model works out which is which from your two lines, and H3 redraws only those two.

How to use it:
- **Reference Video 1:** the clip. **Character 1 and Character 2:** a picture of each (a full-body picture or a character sheet works).
- **Prompt:** two lines that say how the two people in the clip look. The first line is who Character 1 replaces, the second is who Character 2 replaces. For example:
the man in the mustard jacket
the woman with red hair in the black blazer
- **Describe clothes and hair, not sides.** With "the person on the left" and "the person on the right", the characters landed on the wrong people in 4 of 4 runs. Your two lines only find the people, they are not used to draw anything.

Measured on a 12 GB RTX 4070 Ti with 32 GB of RAM, at 480p:
- About 3.5 minutes for 5 s, 6.5 for 10 s and 10 for 15 s. Peak VRAM was 11.6 GB, and free RAM got down to 1.1 GB on long clips, so close your browsers first.
- With looks in the two lines, the right people were swapped in every test where the shots ran 5 s or longer: 5 s clips, a third person left alone, and 10 s and 15 s clips with hard cuts.

Good to know:
- **Duration is 5 to 15 s**, taken from the start of the clip, and it snaps to fit H3, so 10 s can come back as 9.6 s. A clip shorter than 5 s comes back at its own length or a little under.
- **The output follows your clip's shape.** A vertical clip comes back vertical, so the aspect setting changes nothing.
- **Clips work best with the same two people throughout.** Very quick cuts are the weak spot: with shots of about 2 s, the two characters traded places on one shot in both runs of the one clip we tried.
- **Clothing wider than your character can leave scraps.** A long raincoat left dark shapes beside the legs in 4 of 4 runs.
- **If nobody speaks in the clip, mouths can still move a little** on some seeds (1 of 2 on our test).
- **Small details can cross between the two characters**, such as a backpack strap or a blazer from one picture. Try another seed.
- Things people carry can stay: a shoulder bag or a sword in the hand was kept.
- To replace one person, keep using the Character Swap card.

**Our one change to the code:** on busy streets the vision model sometimes named tiny people in the distance as one of your two, and they came out as white figures, 3 of 3 on our 15 s test clip. The pack installs the swap node from our fork with a small fix, and that clip then came back clean 4 of 4. Everything else in that node is D3voz's.

**8.9 GB** on top of the official MiniMax H3 files. The app installs up to five extensions on first use and restarts the engine. Needs engine v0.43.0 or later.

Thanks to D3voz for the graph and nodes (https://github.com/D3voz/comfyui-h3-oneclick-swap), ZhengmingYu for the DMAD LoRA (https://huggingface.co/ZhengmingYu/DMAD), ethanfel for the Context Loop nodes and Adudeguyman for the Fantastic PromptBuilder nodes. MiniMax H3 Community License (base and DMAD LoRA), SAM License (bars military, weapons and ITAR uses). Use consented references and label output as AI-generated.
