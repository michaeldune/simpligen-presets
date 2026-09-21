HELD, not sent. Update note for Outfit Spec Sheet 1.1.0. Merged on master LOCALLY 2026-09-21 (not pushed); zip built at
D:/SimpliGen-Backups/zips/community-outfit-spec-sheet.zip (not uploaded). Example boards:
D:/SimpliGen-Backups/outfit-qwen21-test-20260921/sheet_2passB_p2.jpg and sheet_inapp_card.jpg

---

:thread: **Outfit Spec Sheet 1.1.0** - a second card on Qwen-Image 2.1

**Needs engine 0.37.0** (app 1.64.0 first, then the engine update). The original card is unchanged and still there.

New card: **Outfit Spec Sheet (Qwen 2.1)**. Same idea, one outfit photo in, one specification board out, but done in two
passes inside one job: first the outfit is lifted off the person as a ghost-mannequin shot, then the board is built
around it. What that buys you:
- the person is removed every time
- hats, bags, scarves and shoes stay with the outfit (the original card tends to drop them)
- a proper heading, OUTFIT SPECIFICATION, spelled right
- four colour swatches taken from the real colours of the outfit

Straight talk: it is not reliable on every try. On my test set the whole outfit survived on 6 of 9 boards. A coat, or the
shirt and tie under a jacket, can go missing, and once it added a hat nobody was wearing. When that happens, generate
again with a new seed. Small text (garment labels, colour names) still comes out as gibberish, so the card does not ask
for any. About a minute per board on a 12 GB card; made for the 3:4 shape.

:warning: **Licence:** the new card runs on Qwen-Image 2.1, Qwen Research Licence, **non-commercial use only**. For
commercial work keep using the original card (Apache-2.0 weights). The new card uses the same three files as the Qwen
Image 2.1 pack, so nothing new downloads if you have that.

:inbox_tray: Zip: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest
