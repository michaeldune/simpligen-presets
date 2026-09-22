# Discord update note: Qwen Image 2.1 1.2.0, two 4MP cards (HELD, 2026-09-22)

**Qwen Image 2.1: two new 4-megapixel cards**

Someone asked whether our Qwen pack is a cut-down model. It isn't: same full model, but the cards ran it at 1 MP to stay quick on 12 GB. Now there are two more:

- **Qwen Image 2.1 4MP**: text to image at the size Qwen publishes for the model (2048 x 2048 square, 2752 x 1536 wide). Much finer skin, hair and fabric. About 1.5 minutes on a 12 GB card; for signs and small lettering, raise the steps to 40.
- **Qwen Image 2.1 Enhance to 4MP**: give it any picture and get the same picture back at about 4 MP with real added detail. Faces, lettering and layout are kept. About 2 minutes. Uses the Detail Enhancer LoRA by Elusarca (76 MB, downloads with the card).

Why not more than 4 references on the Edit card? The model accepts up to 10, but in our test it started dropping people after about 5.

The earlier cards are unchanged. Non-commercial use only (Qwen Research License).
