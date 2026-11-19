Shar, thanks for 1.85.0. I checked all the fixes this morning and they work: the open project, no " high.", To video with H3, the Delete button, the look portrait on agent renders, and the trigger word now reaching the engine at the start.

I also tested whether start or end matters, and moving it to the start was the right call. Krea 2 Turbo, seed 424242, six Krea 2 style LoRAs at strength 1 (Plastic Beads, Floral Splash, Party Animals, Duolingo, Simple and Flat, Pixar 3D), each with the trigger at the start (app-added), at the end (typed), and at both ends. Engine history confirmed the text on every run.

With an illustration prompt:
1. Start: every LoRA showed its style, and no text appeared in any picture.
2. End: Krea 2 drew the trigger as text on 5 of 6, as a signature or label ("partyanimals" bottom right, "saf.", "fsplash", "KR2Pix", and "beaddart" written on the fox's side). Plastic Beads lost its style completely with the word at the end.
3. Both ends: style held, but a signature still appeared on two.

So the old end placement was hurting results locally, and the new behaviour fixes it.

One note for anyone testing: with a photographic prompt ("soft golden light through the pine trees") none of the six changed the picture much wherever the word went, so a photo-style prompt can make a LoRA look broken when it isn't.
