POSTED by Michael 2026-09-23 18:52 in #preset-news (pasted from the rendered chat, so bold headings and tip bullets were lost). Discord update note for 2026-09-23: Qwen Image 2.1 1.5.0 (869a3da), Viggle Animate for H3 1.0.0 (deead5a),
LTX 2.5 Stubelius Remix 1.0.0 (4347ed7), Flux 2 Klein 1.2.2 (aba7fc1). All cards verified in the app on engine 0.37.0. Post only
after the store has synced the new versions.

---

**Today's pack updates**

**Qwen Image 2.1 (1.5.0): new Fast Drafts card**
Text to image in 5 steps instead of 20, using Viggle's turbo LoRA (1.36 GB, downloads with the card). About 11 seconds a picture on a 12 GB card instead of about 40, so it's the card for trying ideas and seeds; move a keeper to the main card for the final picture. Photos, portraits and poster headlines hold up well; small or long lettering garbles more often, and now and then an object comes out doubled, so re-roll the seed. Steps and CFG are fixed, so there are no sliders. The other seven cards are unchanged. Non-commercial use only (Qwen Research License).

**New pack: Viggle Animate for H3 (Character Swap)**
Put your own character into an existing video. Drop a clip in Reference Video 1 and one picture of your character (a front view or a character sheet) in the Character slot. Flux 2 Klein repaints the clip's first frame with your character in the same pose and light, then Viggle-Animate carries them through the clip's motion and camera, keeping the background and the clip's own soundtrack. You get the first 5.2 seconds at 480p in the clip's own shape, in about 3 minutes on a 12 GB card.
Tips from testing:
- Use the prompt box to name anything the original person holds or wears that should go ("Remove the sword and the long kimono train; her hands are empty"). Without that, the repaint keeps it and the video carries it through.
- Pick clips where the person is large in frame and has an outline like your character's (loose hair, no long costume). Faces follow the frame size: a full-body shot gives a small, soft face; a medium close-up looks like your character.
- Made for 24 fps clips such as H3's.
45.6 GB from scratch, about 22 GB new if you already have the Flux 2 Klein pack and an H3 pack. The custom node's original GitHub account was deleted today, so the pack installs it from a copy we host.
:warning: Non-commercial use only (MiniMax H3 Community License + FLUX Non-Commercial). Viggle's terms: only use pictures of people who have agreed to it, and label the result as AI-generated.

**New pack: LTX 2.5 Stubelius Remix (Anime)** :underage: NSFW
Stubelius's LTX 2.5 checkpoint that carries the 10Eros / Sulphur 2 stylised look onto LTX 2.5: text to video and image to video, on the same graphs as REDgraft. Anime, 2.5D and stylised characters stay stylised where REDgraft drifts toward semi-real. Side by side with REDgraft it missed staging beats more often (a turn to camera, a second person arriving) and takes about twice as long (80-95 s for 5 s at 480p). It sexualises clothed women even when the prompt asks for modest clothing, so treat it as an NSFW model only. 21.5 GB new if you have REDgraft; like REDgraft it needs a HuggingFace key and the LTX 2.5 licence accepted.

**Flux 2 Klein (1.2.2): download fix**
The 9B card's text encoder moved to a new HuggingFace address. Every download in the pack is now pinned to a fixed version, so new installs keep working. Nothing changes if you already have it.
