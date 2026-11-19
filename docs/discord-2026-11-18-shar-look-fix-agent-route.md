Shar, I reran the Lori clip on H3 Reference to Video (Studio 1.5.0, app 1.84.0, engine v0.45.0, 480p, local). The fix works from the Studio's Render button, but not when an agent renders the same clip.

1. Agent route: MCP render_clips on Clip 1 (job 9f2bf747-a118-4c63-aed2-403fdf27985d). The new wording is there ("wearing an outfit described as: This blue mini dress has..."), but Picture 1 is still Lori's base portrait. The reference file is byte-identical to her base.png (sweater and jeans), same as the old take c091aa3a.
2. Render button in the Studio, same clip, a few minutes later (job d48fba6e-80d3-44e7-b878-c64db2815b41). Picture 1 is the Mini Dress look portrait (look-466dda82-portrait-front.png). It shows in the clip too: she now wears the look's gold necklace and the shorter dress, which neither base-picture take has.
3. Clip 2, which continues from Clip 1, rendered after it from the button (b201f339-6487-46b0-b04c-8440e67b6db9) and got last frame + look portrait + location, so continue works too.

So render_clips seems to build the references the old way while the editor builds them the new way. Both runs happened after the Studio update had loaded: the What's New dialog was up and both clips already showed as edited before the agent render.

Expected: an agent render of a clip sends the same pictures as the Render button.
