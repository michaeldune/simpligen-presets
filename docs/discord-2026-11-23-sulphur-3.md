**New pack: MiniMax H3 (Sulphur 3)**
SulphurAI's Sulphur 3, public since the 21st: an uncensored finetune of MiniMax H3. Three cards, text to video, image to video and reference to video, all in the Video Studio.

**What is different**
The cards load the author's 11.4 GB W4A8 file, the one SulphurAI's own example workflow uses, and run the author's settings: Euler, 20 steps, CFG 1. The model is guidance-distilled, so a negative prompt does nothing. The author writes prompts as JSON captions; a JSON version of our test prompt changed little apart from louder sound, so the usual three-field H3 prompt works. The optional corrector is not included: it needs extra nodes and about 8 GB more video memory.

**Speed** (in the app, 12 GB RTX 4070 Ti, Faster Attention on)
- 5 s at 480p: 147 to 164 s.
- With Faster Attention off the same image-to-video run took 201 s, so leave it on.
- It is slower than the 8-step turbo checkpoints: about 1.8 times as long as 10Eros Max 1.0.

**What we checked**
- On the same picture, prompt and three seeds as 10Eros Max 1.0 and beta7 fix1, it held a locked-off camera best and came out the sharpest of the three.
- The scripted line came out word for word in every clip, and a reference face held in a new scene.
- W4A8 keeps the weights in 4 bits. There is no int8 file of this model yet to compare it with.
- We did not test LoRAs.

In the Preset Store after the next sync. Worth a try when you can wait longer for a steadier, sharper shot.
Thanks to SulphurAI for Sulphur 3.
