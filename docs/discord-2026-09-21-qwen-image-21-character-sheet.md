POSTED by Michael 2026-09-21 ~18:06 on Discord. Update note for the Qwen Image 2.1 pack 1.1.0 (Character Sheet card). RELEASED 2026-09-21 17:55 (master 542b721 pushed, zip on packs-latest). Was: merged locally
Zip built at D:/SimpliGen-Backups/zips/community-qwen-image-21.zip. Example sheets:
D:/SimpliGen-Backups/qwen-image-21-test-20260920/charref-lora-20260921/sheet_D_card_inapp.jpg (the card itself, in-app)

---

:standing_person: **Qwen Image 2.1 pack 1.1.0** - new card: **Character Sheet**

One picture of a person in, a character reference sheet out, on white: a large head in the middle, a headless full-body
front view on the left, a full-body back view on the right, and two small side profiles facing each other underneath.
About 30 seconds on a 12 GB card.

- **Picture 1** = the person. A full-body picture keeps the whole outfit, bag and shoes included. A head-and-shoulders
  portrait works too, but the clothes below the shoulders are then made up and change with the seed.
- **Picture 2 (optional)** = an outfit. Add a picture of clothes and the sheet dresses the person in them (about 60 s).
- **Set the aspect ratio to 3:2.** The sheet layout was trained for that shape.
- The brief is built in; the prompt box is only for extra notes.

The layout comes from the **Portrait2CharRef** LoRA by b675051045971 on Civitai (328 MB, downloads with the card). Without
it the model keeps the front figure's head and draws both profiles facing the same way; with it, all 12 of my test sheets
came out in the right layout with the face intact. Good to know: the large head keeps the angle of your picture, and the
back view sometimes keeps its head.

The other three cards are unchanged. Same licence as the rest of the pack: Qwen Research Licence, **non-commercial use
only**.

:inbox_tray: Zip: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest
