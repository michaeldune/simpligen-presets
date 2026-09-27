Discord update note for 2026-09-26: Qwen Image 2.1 1.7.0 (244c9ab), new Head Swap and Outfit Swap cards. Verified in the app on engine 0.37.0 (61 s each). Store synced 1.7.0 at 20:45 on 2026-09-26. 1.7.1 (250d304, promptOptional on 5 packs) adds no new cards; post after it syncs so the version in the heading matches. The packs-latest release zip community-qwen-image-21.zip is still 1.6.0 (2026-09-25) until it is rebuilt and re-uploaded.

---

**Qwen Image 2.1 (1.7.1): new Head Swap and Outfit Swap cards**
Two new cards, about 1 minute each on a 12 GB card, no extra downloads. Both take exactly two pictures: picture 1 is the one being changed, picture 2 is where the new head or outfit comes from. The result keeps picture 1's size and framing, so the aspect ratio setting is ignored.

**Head Swap** puts the face AND hair from picture 2 into picture 1, relit to match it; the body, clothes and background stay. In testing, identity and hair came across every time, even onto a profile shot, a neon-lit night scene and a person of a different age and gender. If the person in picture 1 is looking sharply away, the new head sometimes turns towards the camera; re-roll the seed.

**Outfit Swap** dresses the person in picture 1 in the clothes and shoes from picture 2, which can be a photo of someone wearing them or a flat lay. Face, pose and background stay. Know before you use it:
- Clothes and shoes come across reliably.
- Hats do not change: a hat in picture 2 is left off, and a hat already on the person usually stays.
- Bags and other carried items come across on some seeds and not others, and once in a while nothing changes; re-roll the seed.

The prompt box is only for extra notes. On today's SimpliGen, type a few words such as "head swap" because the app wants some text; from the next app release you can leave it empty on these two cards and on the other built-in-instruction cards (Cutout, Character Sheet, Enhance to 4MP, Outfit Spec Sheet, Viggle Animate, Swap Album Art, VOSR2 Refine). The briefs are adapted from SatoDive's free Qwen 2.1 editing workflow (Apache 2.0). The other cards are unchanged. Non-commercial use only (Qwen Research License).
