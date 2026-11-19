You're not missing a step. A card only shows up in the Studio when its pack sets a Studio flag, and that flag only exists for plain shot cards (text, image or reference to video), because the Studio builds each shot itself. Our singing cards (H3 Lip-Sync, Music Video Chain, the TTS lip-sync cards, LTX Lip-Sync) are a different shape, so they stay in regular SimpliGen. You don't need them there: the Studio does lip sync itself with the H3 models that are in it.

How to make a singing video in the Studio:

1. Put the song on the timeline as an audio track and set its kind to Singing. Better still, split the song first (UVR, demucs or similar) and add two tracks: the vocals as Singing and the rest as Music.
2. Add your singer as a character and cast them in the clips.
3. In each clip where they sing, give the shot the lyric line and set the singer as the speaker.
4. Make the sung clips hear only the vocals track (and clips without singing hear nothing). H3 then lip-syncs to the voice alone, so the drums and bass don't throw the mouth off.
5. Use a MiniMax H3 model for the film, R2V for the sung clips. Cut the clips on the lyric lines.

The final film plays the full song over everything, so each clip only needs to get the mouth right.

Earth Boy, the one I posted today, was made exactly this way, all in the Studio, if you want to see what it gives you.
