_Posted by Michael 2026-09-26 ~22:44 EDT (all three messages)._

Discord guides for the three cards in Community — MiniMax H3 (Clip Chaining) 1.1.1, 2026-09-26. One message per card, each under
Discord's 2,000-character limit. Facts from the pack manifest, the workflows (Continue Clip trims the pinned 22 frames and outputs the
NEW part only; the clip tail is centre-cropped to the chosen width/height; the Director splits on [Shot 2] and carries segment 1's tail
into segment 2) and the 2026-09-10 / 09-13 support replies. Example prompts follow the minimax-h3-prompt skill (camera stated, <d>
tags, lip closure as an event, the leftover time claimed). ALL THREE EXAMPLE PROMPTS RENDERED 2026-09-26 (480p, 16:9, 5 s, seed 2026) and
checked: see D:\SimpliGen-Backups\clip-chaining-guides-20260926\VERDICT.md. Examples 2 and 3 were revised after their first render.

=== MESSAGE 1 ===

**How to use: MiniMax H3 Continue Clip (Motion Context)**
Makes an H3 clip longer. Give it a clip you already made, describe what happens next, and it renders the next part starting exactly where your clip ends: same shot, same motion, and the SOUND CARRIES ON (music, singing and speech continue instead of restarting). Use this one for anything with dialogue, singing or a beat.

**Setup**
1. **Reference Video 1** = the clip to continue (any H3 clip from SimpliGen). It must go in Reference Video 1, not the image or audio slots.
2. **Aspect ratio and resolution** = the same as that clip. Its last frames are centre-cropped to what you pick.
3. **Prompt** = only what happens next. Describe the people, place and voice the same way as in the first clip, and say what the camera does.
4. **Duration** = length of the NEW part (5-15 s).
5. Optional: character pictures in Reference 1-9 keep faces steady.

**What you get**
Only the new part, starting right after your clip's last frame. Put the two files end to end in any editor. For a third part, drop the new clip into Reference Video 1 and go again.

**Example prompt** (continuing a clip of a woman at a cafe window):
`The woman keeps looking out of the window, then turns to face the camera and smiles. The camera pushes in slowly. She says: <d>[English] I think it's going to rain.</d> The instant that sentence ends, her lips close completely and all speaking motion stops; for the rest of the shot she stays silent, watching the window.`

**Tips**
- End the first clip on movement; a join in the middle of a still pose is where the eye catches it.
- Colour warms a little with each link. After 3-4 links, start fresh at a natural cut.
- Allow about 5 words per second of speech, and describe the lips closing afterwards, or H3 invents extra words.
- Fast action across the join (someone running) hasn't been tested yet.

=== MESSAGE 2 ===

**How to use: MiniMax H3 Continue Clip (Add Guide)**
The twin of Continue Clip (Motion Context): same inputs, same result on the PICTURE, but the SOUND is a sound-alike instead of a true continuation. The join in the audio can shift slightly in timing and level. Picture continuity measured as good or slightly better than Motion Context.

**Which one do I pick?**
- Dialogue, singing, music with a beat: **Motion Context**.
- You'll replace the audio in your editor anyway (your own music or voiceover), or the scene is just ambience: **Add Guide** is fine.
- Not sure: Motion Context.

**Setup** (identical to Motion Context)
1. **Reference Video 1** = the clip to continue (any H3 clip from SimpliGen). Not the image or audio slots.
2. **Aspect ratio and resolution** = the same as that clip. Its last frames are centre-cropped to what you pick.
3. **Prompt** = only what happens next, with the same people and place, and what the camera does.
4. **Duration** = length of the NEW part (5-15 s).
5. Optional: character pictures in Reference 1-9.

**What you get**
Only the new part, starting right after your clip's last frame. Join the files in any editor; for another link, drop the new clip into Reference Video 1.

**Example prompt** (continuing a drone shot over a coastline):
`The camera keeps gliding forward along the cliffs at the same height and speed, then banks left out over the cliff edge and tilts down until the frame is filled with waves breaking on the dark rocks below. No people. Wind and surf only.`

**Tips**
- End the first clip on movement; a seam inside a still hold is where the eye lands.
- Colour warms a little with each link; restart after 3-4 links at a natural cut.
- Needs the Motion Context node pack too (for its Trim node). SimpliGen installs it with the pack.

=== MESSAGE 3 ===

**How to use: MiniMax H3 Two-Shot Director (one render)**
Makes two connected shots in ONE render and ONE file. No clip to feed back in: the end of shot 1 is carried into shot 2 for you, so the join is already made. If shot 2 keeps the same view, it flows on as one take; ask for a very different view (his face after his back) and H3 makes a clean cut to it.

**Setup**
1. **At least one reference.** A picture of your character in Reference 1 is enough. SimpliGen won't run with no reference at all. Reference videos are optional (since 1.1.1).
2. **Prompt in two parts:** start with `[Shot 1]` and what happens first, then `[Shot 2]` and what happens next. Everything before [Shot 2] is shot 1. No [Shot 2] = the same prompt runs over both.
3. **Duration = length of EACH shot.** 5 s gives a 10 s video.
4. **Dialogue:** write it inside the shot where it's spoken, with `<d>[English] ...</d>` tags. The Dialogue field is added to the end of the prompt, so it only ever lands in shot 2.
5. References are used by both shots.

**Example prompt** (Reference 1 = a picture of the man):
`[Shot 1] The man in <Picture 1> walks along a rainy harbour at dusk in a grey coat. The camera tracks beside him at walking speed. He stops at the railing and looks out at the boats. [Shot 2] The camera arcs slowly around to the front of him and ends on a close-up of his face, rain on his glasses, his eyes still on the water. He says: <d>[English] She's not coming back.</d> The instant that sentence ends, his lips close completely and all speaking motion stops; for the rest of the shot he stays silent, rain on his face, eyes on the water.`

**Speed**
About 7 minutes for 2 x 5 s at 480p on a 12 GB card. Big sizes get slow fast: 1344x768 with 15 s shots can take hours. Start at 480p and 5 s, then scale up.

**Tips**
- Colour stays steadier than chaining clips by hand (the hand-off happens inside the model).
- Fixed at two shots; for longer, continue the result with a Continue Clip card.
