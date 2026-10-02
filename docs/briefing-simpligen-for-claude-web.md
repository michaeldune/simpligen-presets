# Background: SimpliGen, YuE2, and my Community Preset Packs

You won't have heard of most of this, so here is the context. Treat it as accurate as of October 2026.

## What SimpliGen is

SimpliGen (simpligen.io) is a Windows desktop app for local AI generation: images, video and now music, all on your own GPU. Under the hood it runs a bundled ComfyUI engine, but the user never touches a node graph. Every workflow is packaged as a **preset**, which shows up as a **card** with a fixed set of input boxes. Presets come in **packs**. Packs install from SimpliGen's built-in **Store**, which downloads the model weights for you. Some presets can also run on SimpliGen Cloud.

The input boxes are the same on every card, and each card's description says how it uses them:

- **Subject & Action**: the main prompt
- **Character Dialogue**: a toggle-on text box. Video cards use it for spoken lines; music cards use it for lyrics.
- **Duration**, **Aspect ratio**, **Resolution**, plus an **Advanced Settings** panel (steps, CFG, seed, sliders)
- **Reference Image / Reference Video / Reference Audio** slots
- **Characters**: saved people or artists you can drop into a card in place of a reference image
- A **LoRA picker**, on cards that support LoRAs

Packs come in two kinds. **Official** packs are made by SimpliGen. **Community** packs are made by other people and show in the app under a "Community —" prefix.

## Who I am in this

I write community packs for SimpliGen. My repo is github.com/michaeldune/simpligen-presets, and my packs reach users through the SimpliGen Store (and as zips on that repo's Releases page). Right now it's about 55 packs and 184 presets. I test on an RTX 4070 Ti (12 GB VRAM) with 31 GB of system RAM, so every speed figure below is from that machine.

## The music pack: "Song + Album Art" (version 1.2.1)

SimpliGen can't output audio on its own yet. So each card delivers its song as an **MP4**: the full track, with album art held on screen for its whole length (the way a Sora song comes with a thumbnail). For the album art you can supply your own picture or use a Character. Leave it empty and Qwen-Image 2.1 paints the art from the style. To get the song title lettered on the painted art, add a line `[title] Song Name` anywhere in the text. It is never sung.

The pack needs SimpliGen engine 0.37.0 or newer. It has five cards:

1. **YuE2 Song + Album Art.** YuE2 is an open 3B song model from m-a-p (the YuE team), run here at INT8. It writes a full song, vocals and backing, from a style plus lyrics.
   - *Subject & Action* = short comma-separated style tags, language first: language, voice, genre, instruments, mood, tempo. Example: `English, female vocal, indie pop, warm acoustic guitar, soft drums, 100 bpm, intimate, bright chorus`
   - *Character Dialogue* = the lyrics, one sung line per line. Section tags such as `[verse]`, `[chorus]`, `[bridge]`, `[outro]` go on their own lines, with a blank line between sections.
   - *Duration* is a ceiling of up to 6 minutes. YuE2 often ends the song earlier on its own. A 3:04 song took 74 s to render; a 60 s song took 38 s.
   - YuE2 style LoRAs work, for example Atomtan Studio's DreamPop and Old School Hip-Hop. Put the LoRA's trigger word first in the style.
2. **YuE2 Cover Song + Album Art.** You upload a song (MP3/WAV/M4A, or an MP4's soundtrack). SheetSage2 transcribes its melody into a score, and YuE2 sings your lyrics in your style to that tune. The arrangement is free to change. Paste the original lyrics to keep the words, or leave the lyrics out and YuE2 writes new words to the same tune. **Leave BPM out of the style**, because the tempo comes from the transcribed score. A full 4:25 cover took 126 s.
3. **YuE2 Faithful Cover + Album Art.** The same as the Cover card, except SheetSage2 also transcribes the chords and YuE2 follows them. The result keeps the original harmony as well as the tune, so it sounds more like the same song played by a different band. Transcription errors, especially wrong chords, carry into the cover. The first time you use either cover card, restart SimpliGen once after the models download.
4. **MiniMax Music 3 Song + Album Art.** MiniMax's open Music 3 model, run here at INT8. It works best with MiniMax's own structured caption, written in English:
   `Global Metadata: lo-fi hip-hop, 78 BPM, D flat major, laid-back and dreamy. Vocal Details: soft female vocal, half-sung. Arrangement: dusty boom-bap drums, Rhodes, vinyl crackle.`
   A longer description of how the song builds section by section also helps. If you add an `Application Scenarios & Imagery:` line, the painted album art shows that scene. Lyric tags here are `[Intro] [Verse] [Pre-Chorus] [Chorus] [Post-Chorus] [Bridge] [Instrumental] [Solo] [Outro]`. For an instrumental, turn the lyrics off and also say "instrumental, no vocals" in the description. Songs can run up to 300 s, and the lyrics decide the length. A 61 s song took 114 s.
5. **Swap Album Art.** Puts a new picture on a song MP4 you already made. The audio is copied untouched, and it takes about 10 seconds.

Licences: YuE2 and SheetSage2 are CC-BY-NC-4.0, so non-commercial only. Music 3 is Apache-2.0. Qwen-Image 2.1, which paints the album art, is under the Qwen Research Licence (non-commercial), so supply your own art if you need commercial clearance. For songs over three minutes, turn on Settings > Advanced > Reduce system RAM usage.

## The other community packs, in brief

**Image packs.** These cover SDXL, Pony, Illustrious and SD 1.5 checkpoint collections, plus Anima, Krea 2 and Krea 2 finetunes, Flux 1 Krea, Flux 2 Klein, Z-Image, SeFi and Ideogram 4 (strong text rendering). Specialist packs:
- **Qwen-Image 2.1**: text-to-image, plain-English edits with 1–4 reference images, a background-removal Cutout card, a Character Sheet card, 4 MP cards and Fast Drafts
- **Ming Image Design**: app screens, posters, menus and infographics with correctly spelled text
- **Krea 2 Identity Edit**: change one thing and keep the face
- **Outfit Spec Sheet**: a photo of an outfit in, a fashion specification board out

**Video packs.** Most are built on **MiniMax H3**, an open video model that generates video *with synchronized audio* (speech, sound and music) from text, an image, or reference pictures (text-, image- and reference-to-video). Mine are variants of it:
- **Speed**: Turbo LoRAs, step distills, accelerated attention stacks, DaSiWa Hybrid
- **Look**: Singularity, Z-Image Graft, SparseRef15, 10Eros Max
- **Video in, video out**: Motion Transfer (copies a dance or movement onto a new person and setting), Viggle Animate (character swap), Video Refine upscalers, and Clip Chaining (continue an existing clip)
- **Audio-driven**: Lip-Sync (your audio, up to 9 reference faces), Emotion TTS Lip-Sync (type a line and it is spoken in a cloned voice with an emotion, then lip-synced), and **Music Video Chain** (a 14–27 s single-take singing shot to your own song, built from 2–4 chained H3 clips)

There are also LTX 2.5 packs (lip-sync, anime and NSFW finetunes, an upscaler) and a Wan 2.2 image-to-video pack.

Speed is set by H3's clip length. A 5-second H3 clip at 480p typically takes 1–4 minutes on my card, and 768p takes several times longer. Only one H3 job fits in my RAM at a time.

## How you can help me

You can't run any of this. What you can do is help me write inputs and text:

- YuE2 style tags and properly tagged lyrics
- MiniMax Music 3 structured captions
- H3 video prompts
- descriptions and Discord announcements for packs

When you write lyrics or prompts for me to paste into a card, **give the complete text, word for word**. Don't use shorthand like "(repeat chorus)", because the model will sing that literally.
