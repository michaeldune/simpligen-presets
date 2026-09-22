# Discord update note: combined 2026-09-22 (replaces the two held notes of the same day; POSTED by Michael 2026-09-22 14:40)

**Today's pack updates**

**Qwen Image 2.1 (1.2.0): two new 4-megapixel cards**
Someone asked whether our Qwen pack is a cut-down model. It isn't: same full model, but the cards ran it at 1 MP to stay quick on 12 GB. Now there are two more:
- **Qwen Image 2.1 4MP**: text to image at the size Qwen publishes for the model (2048 x 2048 square, 2752 x 1536 wide). Much finer skin, hair and fabric. About 1.5 minutes on a 12 GB card; for signs and small lettering, raise the steps to 40.
- **Qwen Image 2.1 Enhance to 4MP**: give it any picture and get the same picture back at about 4 MP with real added detail. Faces, lettering and layout are kept. About 2 minutes. Uses the Detail Enhancer LoRA by Elusarca (76 MB, downloads with the card).
- **Qwen Image 2.1 Edit** now works with the new cast picker in SimpliGen 1.65.0: pick up to 4 characters and refer to them as @name in the prompt.
Why not more than 4 references on the Edit card? The model accepts up to 10, but in our test it started dropping people after about 5. The earlier cards are otherwise unchanged. Non-commercial use only (Qwen Research License).

**MiniMax H3 Music Video Chain (1.0.2)**
- Fixed: a `[Shot 1]` mention anywhere in your shared description used to cut the description off at that point. A `[Shot N]` marker now only counts when it starts its own line.
- New tip on every card: if the camera slowly creeps in over the clips, generate again with a new seed. In testing about one seed in three drifted, and wording in the prompt did not stop it.

**Behind the scenes**: 25 packs now declare every custom node they use (the rgthree LoRA loader, and ComfyUI-GGUF for Krea CSG Foundation), so cards no longer depend on another pack having installed them first. H3 Refine and H3 Two-Stage point at the upscaler's new download location.
