No huge differences. They're close cousins: both run the stock H3 model with a speed-up LoRA, plus the same M3 Unlocked LoRA by The Midnight Lab on an "unlock" slider. What actually differs:

- **Speed-up LoRA:** Midnight uses the official 8-step turbo LoRA. Turbo Accelerated uses the turbo v4 LoRA at 10 steps by default.
- **Video VAE:** Turbo Accelerated decodes with the smaller int8 VAE; Midnight uses the fp16 one. That's the most likely source of the small speed edge you saw, even with two extra steps.
- **Unlock strength:** Midnight starts at 0.5. On Turbo Accelerated it starts at **0** (off), so to compare like for like, set it to 0.5 there. It costs no extra time.
- **Resolution, the big one:** Midnight opens at **768p**, while Turbo Accelerated (and TaoMate) open at **480p**. Left on their defaults, Midnight renders about 2.5x the pixels, which explains a lot of both the extra time and the extra quality. Match the resolution before comparing.

Even at a matched 480p, though, Midnight is the best-looking of the bunch. It's the most photographic: natural light, soft background blur, calmer faces, better camera moves.

**What about TaoMate 3-Step + the Midnight (unlock) LoRA?** We tested it: 27 clips at 480p, 5 s, the same 3 seeds on a talking head, a dog running on a beach, and an explicit scene, comparing Midnight, TaoMate, and TaoMate with the unlock LoRA at 0.5.
- TaoMate is about 3x faster than Midnight (30-35 s a clip vs 95-100 s), and the unlock LoRA adds no time.
- The unlock LoRA didn't make TaoMate look more like Midnight. It mostly changed the person and the room and softened the picture a little. No visible gain on any of the 9 pairs.
- TaoMate already handles explicit prompts fully without it.
- TaoMate is crisper but glossier, with bigger expressions and weaker camera motion than Midnight.

So: Midnight when you want the best result, TaoMate when you want speed, and skip the unlock LoRA on TaoMate. If you want to try it anyway, the TaoMate card has a LoRA slot.

Caveats: we judged from still frames at 480p and didn't judge the audio or lip sync.
