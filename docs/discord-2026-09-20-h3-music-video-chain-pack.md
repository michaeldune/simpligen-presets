POSTED by Michael 2026-09-20 ~19:12 as a SCHEDULED Discord post (delayed a few hours so the store sync can catch up), with the announcement video. Announcement for the MiniMax H3 Music Video Chain pack. Pack RELEASED 2026-09-20 19:08 (master 52a416f pushed, zip on packs-latest). Was: merged on master locally
(52a416f). Announcement video APPROVED by Michael 19:04: D:/SimpliGen-Backups/announce-20260920/mv-chain/h3-mv-chain-announcement.mp4 Sample renders (in-app): D:/SimpliGen-Backups/h3-mv-chain-card-20260920/
app_2clips_off9.mp4, app_3clips.mp4, app_4clips.mp4.

---

:microphone: **New pack: MiniMax H3 Music Video Chain** (3 cards) - long single-take singing shots to your own song

Upload a song, pick where it starts, add a picture of your singer, and get one continuous performance shot: **14, 21 or
27 seconds** from 2, 3 or 4 H3 clips chained in a single job.

**Your song is the soundtrack.** Each clip gets its slice of your track locked in, and the finished video carries the
original song, not a re-generated one. The singer's mouth follows the song: leave the start offset at 0 on a track with
an intro and she waits, then comes in on the first lyric.

**No visible cuts.** Every clip continues from the previous clip's latent, not from saved frames, so brightness, framing
and sharpness stay put from the first second to the last. On my test renders every cut sat inside normal frame-to-frame
motion.

**How to prompt it:** write what stays the same first (who is in the picture, the look, the room), then one block per
clip starting with `[Shot 1]`, `[Shot 2]`, ... with the lines sung in that clip. Without `[Shot]` markers every clip
gets the whole prompt. 1 to 4 reference pictures.

On a 4070 Ti at 480p: 2 clips 6 min, 3 clips 9 min, 4 clips 12 min. 480p only for now, because the 4-clip card needs
most of 32 GB RAM; close other apps. Your song has to be at least as long as the video from the start offset.

Good to know: this recipe is steady rather than lively, and a little soft. It is made for a performer singing to the
camera, not for action shots.

It reuses the H3 fl2va weights, the H3 VAEs and the node pack the Clip Chaining pack already installs. New download:
one 2 GB LoRA (lightx2v fl2v Turbo v1.2, Apache-2.0). Thanks to seitanism for the Song Audio + Masked Video Context
node, and to SatoDive, whose continuation pack showed the recipe that holds still.

:inbox_tray: Zip: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest
