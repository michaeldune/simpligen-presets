:sparkles: **New pack: MiniMax H3 (10Eros Max beta5)**

The 10Eros Max finetune moved on since we packed it in August. TenStrip's current release is **beta5**, and it is a different animal: one **hybrid** checkpoint that carries both the first-frame and the reference-to-video character, built from seven concept-grouped grafts and consensus merges of 20+ LoRAs instead of direct merges. The author calls beta5 the only functional build; betas 3 and 4 are withdrawn.

We ran it head to head against the pack we ship, same seed, same two prompts (a locked-off portrait and a night tracking shot), same 864x480 / 5 s / 20 steps on a 12 GB 4070 Ti:
• **Cleaner faces.** The mouth smear the original throws on portraits is gone.
• **Real motion.** On the tracking shot it produced motion blur and neon streaks where the original stayed static.
• **Faster.** 202 s against 250 s at the same 20 steps. In-app: 127 s for a 5 s T2V, 139 s R2V, 149 s I2V.
• **R2V on the right base at last.** Because the file is a hybrid, reference-to-video runs on true ref2va character instead of borrowing the first-frame model.

Three cards, all on the unmodified official graphs (res_multistep/simple, 20 steps): **Text to Video**, **Image to Video**, **Reference to Video**. All three verified inside SimpliGen 1.59.1 on fresh prompts, dialogue included.

:warning: Things to know
• Separate **21 GB** download (INT8). The original 10Eros Max packs are unchanged and stay in the store; this does not replace them.
• The author's advice, and ours: keep **Spectrum and step caching OFF for reference shots**, they cost accuracy.
• Licence: MiniMax H3 community licence, plus the LTX 2.3 / Wan 2.2 / Krea 2 community licences for the grafted character.
• Free system RAM matters more than VRAM here. Keep 16 GB+ free.
• No Turbo card yet. The baked-in turbo file matched our Turbo pack's speed in the bake-off but the look needs one more seed before we ship it.

:shopping_cart: Store: `Community — MiniMax H3 (10Eros Max beta5)`, syncs within a few hours.
:inbox_tray: Zip: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest
:books: Catalogue: <https://github.com/michaeldune/simpligen-presets#readme>

Credit to TenStrip for the model and the write-up on the grafting method, which is on the HF page.
