**LoRA trigger words in 1.85.0: why "start of your prompt" matters**

SimpliGen 1.85.0 now puts a LoRA's trigger word at the START of your prompt (the line under the LoRA reads "Added to the start of your prompt"). Locally it used to go at the end. I tested six Krea 2 style LoRAs to see what difference that makes.

Setup: Krea 2 Turbo, same seed for every picture, LoRA strength 1, prompt "An illustration of a red fox sitting in a snowy forest clearing, pine trees behind it, simple stylized artwork." Each LoRA ran with the trigger at the start, at the end, and at both ends.

**1. With the trigger at the start, every LoRA shows its style** (first picture). Same fox, same seed, six different looks.

**2. At the end, Krea 2 tends to write the word into the picture.** 5 of 6 LoRAs put it in as a signature or label: "partyanimals", "saf.", "fsplash", even "beaddart" on the fox's side. Plastic Beads lost its bead look completely (second and third pictures).

**3. A photo-style prompt can make a style LoRA look broken.** With "soft golden light through the pine trees" none of the six changed the picture much, wherever the trigger went. Ask for an illustration, a drawing or a style and the LoRA has room to work (fourth picture).

**Tips**
- Just add the LoRA. On 1.85.0 you don't need to type the trigger word; the app adds it at the start, and won't add it twice if you already typed it.
- If you type it yourself, put it at the start, not the end.
- If a style LoRA seems to do nothing, check your prompt for photo words (lighting, lens, "photo of") before blaming the LoRA.

One seed per test, so treat it as a strong hint rather than a law.
