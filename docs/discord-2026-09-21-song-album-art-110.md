POSTED by Michael 2026-09-21 ~14:43 on Discord. Update note for Song + Album Art 1.1.0. RELEASED 2026-09-21 14:36 (master 2f4ffee pushed, zip on
packs-latest). Example art: D:/SimpliGen-Backups/music3-graphfix-ab-20260921/inapp_110_title_cover.jpg and inapp_110_covers.jpg

---

:musical_note: **Song + Album Art 1.1.0** - better album art, and your song title on it

**Needs engine 0.37.0** (app 1.64.0 first, then the engine update).

- **Album art is now painted by Qwen-Image 2.1.** It follows the scene in your style text much more closely, and it can
  spell.
- **Put your title on the cover.** SimpliGen has no title box, so add one line anywhere in either prompt box:
  `[title] Let It Play`
  It is never sung. The painted art carries it as lettering. No `[title]` line = art with no text, as before.
- **MiniMax Music 3 no longer needs the little fix node.** Engine 0.37.0 has the fix built in. The songs are identical,
  there is just one less thing to install.

Good to know:
- The art model is the same three files as the new Qwen Image 2.1 pack (17.3 GB). If you have that pack, nothing new
  downloads. If not, the update downloads them the next time you prepare a song card.
- For songs over three minutes, turn on Settings > Advanced > Reduce system RAM usage. On my 32 GB machine that was the
  difference between 0.1 GB and 3.6 GB of free RAM at the end of a full-length song.
- :warning: Painted album art is under the Qwen Research Licence: **non-commercial use only**. That now includes the
  MiniMax Music 3 card, whose song is still Apache-2.0. Supply your own art (reference image or a Character) to stay
  clear of it.

:inbox_tray: Zip: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest
