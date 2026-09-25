Discord update note for 2026-09-25: Qwen Image 2.1 1.6.0 (367b234), new Fast Edit card. Verified in the app on engine 0.37.0 (one-reference edit 20.7 s, two-reference composite 28.4 s). Release zip community-qwen-image-21.zip re-uploaded to packs-latest 2026-09-25 19:26Z. Post only after the store has synced 1.6.0.

---

**Qwen Image 2.1 (1.6.0): new Fast Edit card**
Picture edits in about 20 seconds instead of about 80, using PrunaAI's 8-step LoRA (336 MB, downloads with the card). Describe the change and refer to your pictures by position, the same as on the Edit card: "Change the dress in <image1> to deep red silk", "Change the price of Lemon Tart to 7".
Tips from testing:
- It is at its best with ONE picture: colour and clothing changes, weather and time of day, and changing a word on a sign all came out right, with faces and the rest of the picture kept.
- It takes up to three pictures, still far faster than the Edit card, but less reliably: small objects can deform or one picture can end up partly hidden. Re-roll the seed, or use the main Edit card for a final multi-picture composite.
- Steps and CFG are fixed by the distillation, so there are no sliders.
The LoRA is PrunaAI's first release (v0.1), so expect an update when they publish a better one. The other eight cards are unchanged. Non-commercial use only (Qwen Research License).
