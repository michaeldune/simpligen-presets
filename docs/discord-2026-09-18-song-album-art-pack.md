HELD - not posted. Two drafts: the pack announcement (post with the video) and a reply for VDOFX's "YuE2 Music
Generator?" thread. Video: D:/SimpliGen-Backups/announce-20260918/song-album-art/song-album-art-announcement.mp4

---

:musical_note: **New pack: Song + Album Art** (2 cards) - songs in SimpliGen

SimpliGen can't output audio on its own yet, so this pack delivers each song as an MP4: the track playing under its
album art, the way a Sora song ships with its thumbnail. It plays in the gallery, and the MP4 goes anywhere a video goes.

**YuE2 Song + Album Art:** put the style in Subject & Action as short tags ("female vocal, indie pop, warm acoustic
guitar, 100 bpm, bright chorus"). Turn on Character Dialogue and write the lyrics there with `[verse]` / `[chorus]` /
`[bridge]` tags. Add a picture for the album art, or pick a Character so your artist is on every song. Leave it empty
and Flux 2 Klein 4B paints art from the style. YuE2 decides the song's length itself, up to the 240 s cap, and the
video matches the song.

**Swap Album Art:** put a new picture on a song you already made, without touching the audio. It takes about 10 seconds.

On a 4070 Ti, a 3:04 song took 74 s and a 60 s one took 38 s. The ComfyUI Text to Music (YuE2) settings are used
as-is, int8. About 16 GB to download (YuE2 4 GB, Klein 4B 4 GB, its Qwen 3 4B encoder 8 GB). If you already have
Z-Image or Klein, that encoder is already on your drive.

:warning: YuE2 is licensed **CC-BY-NC-4.0: non-commercial use only.**

MiniMax Music 3 was supposed to be in here too, but it renders noise in SimpliGen's engine right now (an upstream
ComfyUI bug, already reported). It'll come as an extra card once that's fixed.

:inbox_tray: Zip: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest

---

**Reply in the "YuE2 Music Generator?" thread:**

It's in SimpliGen now, as a community pack: **Song + Album Art**. Style tags in the prompt, lyrics in Character
Dialogue, and you get the song back as an MP4 with album art. The art is either painted for you or your own picture,
since SimpliGen has no audio output yet. There's also a card that puts new art on a song you already made. Details
and a short video in the announcement: <link>
