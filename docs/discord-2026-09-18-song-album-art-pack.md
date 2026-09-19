POSTED by Michael 2026-09-18 ~21:15 (announcement + v2 video). The VDOFX thread reply below was SENT by Michael ~21:30 (updated 5-card text). Two drafts: the pack announcement (post with the video) and a reply for VDOFX's "YuE2 Music
Generator?" thread. Video: D:/SimpliGen-Backups/announce-20260918/song-album-art-v2/song-album-art-announcement-v2.mp4 (v2, 5 cards; v1 superseded)

---

:musical_note: **New pack: Song + Album Art** (5 cards) - songs and cover songs in SimpliGen

SimpliGen can't output audio on its own yet, so this pack delivers each song as an MP4: the track playing under its
album art, the way a Sora song ships with its thumbnail. It plays in the gallery, and the MP4 goes anywhere a video goes.

**YuE2 Song + Album Art:** put the style in Subject & Action as short tags, language first ("English, female vocal,
indie pop, warm acoustic guitar, 100 bpm, bright chorus"). Turn on Character Dialogue and write the lyrics there with `[verse]` / `[chorus]` /
`[bridge]` tags. Add a picture for the album art, or pick a Character so your artist is on every song. Leave it empty
and Flux 2 Klein 4B paints art from the style. YuE2 decides the song's length itself, up to the 6-minute cap, and the
video matches the song.

**LoRAs work.** YuE2 style LoRAs load through the usual LoRA picker, for example Atomtan Studio's DreamPop and Old
School Hip-Hop (huggingface.co/atomtanstudio/lora-library). Import them with base model YuE2 and start the style with
the trigger word (`sv_dreampop, dream pop, ...`).

**YuE2 Cover Song + Album Art:** upload a song (MP3/WAV/M4A, or an MP4 and its soundtrack is used). SheetSage2 transcribes its melody and YuE2 sings your lyrics in your style over it: the same tune as a jazz ballad, a punk track, a lullaby. Leave the BPM out of the style: the cover keeps the original tempo.

**YuE2 Faithful Cover + Album Art:** the same idea, but it keeps the original chords too, so it sounds like the same song played by a different band. After the first download of either cover card, restart SimpliGen once so it finds the new model folder.

**Swap Album Art:** put a new picture on a song you already made, without touching the audio. It takes about 10 seconds.

On a 4070 Ti, a 3:04 song took 74 s and a 60 s one took 38 s. The ComfyUI Text to Music (YuE2) settings are used
as-is, int8. About 12 GB to download (YuE2 4 GB, Klein 4B 4 GB, its fp4 text encoder 3.9 GB), plus SheetSage2
(1.4 GB) for the two cover cards. A full-length 4:25 cover took 126 s.

:warning: YuE2 and SheetSage2 are licensed **CC-BY-NC-4.0: non-commercial use only.** Only cover recordings you have the rights to use.

**MiniMax Music 3 Song + Album Art:** MiniMax's own format (Global Metadata / Vocal Details / Arrangement) plus lyrics,
up to 300 s, Apache-2.0. It installs a tiny fix node with it: ComfyUI's Music 3 code replays a freed buffer in its
CUDA graphs, which turns every song into noise inside SimpliGen's engine. Thanks to Sharmystic for pinning down the
exact cause. The node goes away once ComfyUI fixes it upstream.

:inbox_tray: Zip: https://github.com/michaeldune/simpligen-presets/releases/tag/packs-latest

---

**Reply in the "YuE2 Music Generator?" thread (SENT by Michael 2026-09-18 ~21:30; 5-card text):**

It's in the Store now, as a community pack: **Song + Album Art**. Style tags in the prompt, lyrics in Character
Dialogue, and YuE2 gives you back the whole song, up to 6 minutes, as an MP4 with album art (SimpliGen has no audio
output yet). The art is painted for you, or use your own picture. YuE2 style LoRAs work too.

It can also cover a song: upload an MP3 or MP4 and **Cover Song** keeps the tune while singing your lyrics in a new
style, or **Faithful Cover** keeps the chords as well. There's a MiniMax Music 3 card and one that swaps the art on a
song you already made. Details and a short video in the announcement: <link>
