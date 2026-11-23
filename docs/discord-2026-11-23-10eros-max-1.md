**New pack: MiniMax H3 (10Eros Max 1.0)**
TenStrip's 10Eros Max 1.0, released on the 21st: the beta5 and beta7 builds mixed with SulphurAI's Sulphur 3, on a hybrid base with the turbo built in, so there is no LoRA to load. Five cards: text to video, image to video, reference to video, and 768p two-pass text and image to video. The first three are in the Video Studio.

**What is different**
The author made it for explicit animation and suggests plain H3 for anything else. The author says it follows input pictures and poses better than beta7, at the cost of some general knowledge. The cards run the author's sampler (LCM, 8 steps). It is its own 22.9 GB download, separate from the beta5, beta6 and beta7 packs.

**Speed** (in the app, 12 GB RTX 4070 Ti, 5 s clips)
- 480p: 88 to 93 s on the single-pass cards.
- 768p two-pass: about 3 1/2 minutes.

**What we checked**
- On the same picture, prompt and three seeds as beta7 fix1, it held a locked-off camera much better, flickered about half as much and came out sharper. The scripted line came out in every clip.
- The file carries two tensors the engine does not read. The clips look normal without them.
- The author recommends sparse attention, but this checkpoint lacks the layers it needs: it saved about 9% of the time and came out about 30% softer, so the cards leave it off.
- Ordinary high-rank H3 LoRAs work poorly on it, according to the author, who keeps a set of down-ranked ones on Hugging Face (TenStrip/MMH3_Sulphur3Eros_Loras-MLP-energy-patches). We did not test LoRAs.

In the Preset Store after the next sync.
Thanks to TenStrip for 10Eros Max.
