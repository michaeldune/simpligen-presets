# Character PV — prompt template for the MiniMax H3 Character PV preset

This is the brief format the **MiniMax H3 Character PV (DaSiWa Hybrid)** preset expects in its prompt box. Put a character design sheet in the reference slot, set Duration to 15, and paste a brief written to this skeleton. Method reconstructed from Smart Bobo (机智波玩ai), 2026-09.

## The fixed skeleton

| Slot | Time | Type | Content |
|---|---|---|---|
| Shot 1 | (none) | performance | extreme close-up, starts mid-motion, gaze lifts to lock the lens |
| Shot 2 | 00:01.100 | performance | continues Shot 1's movement, a hand interacts with a wardrobe item, the gesture emits a light trail that leads into the cut |
| Shot 3 | 00:02.200 | CARD 1 | bright warm-ivory field, `{CARD_1}` slams in from both sides, circle burst behind; character as ~50% off-centre waist-up crop; gesture triggers a burst that wipes out |
| Shot 4 | 00:03.200 | CARD 2 | pale grey field with horizontal bands, `{CARD_2}` revealed by the main band; character enters as a full-body silhouette; gesture reverses the band, match-cut |
| Shot 5 | 00:04.100 | performance | Whip Pan into the venue wide, character already striding, low Tracking Shot |
| Shot 6 | 00:05.200 | performance | low medium-close, starts on footwear landing, Tilts up the wardrobe, hand touches a wardrobe item, expression shift toward camera |
| Shot 7 | 00:06.200 | CARD 3 | two-tone split field, `{CARD_3A}` drops from above and `{CARD_3B}` rises from below; character as ~55–60% shoulder-and-face crop between them; blink-lock triggers a scan-line wipe |
| Shot 8 | 00:06.900 | performance | low three-quarter, one quick side step, hip pivot, shoulder-led turn, hem and accessories flare, compact fast Arc Shot |
| Shot 9 | 00:07.900 | CARD 4 | warm-ivory field with diagonal planes, `{CARD_4}` arrives along a perspective diagonal, offset then snaps to lock; extreme diagonal eye crop ~45%; gaze crossing the lock line snaps the words, nearest plane rushes past the lens |
| Shot 10 | 00:08.600 | performance | character approaches, passes close beside the lens, half-turn and step-back, camera Trucks back then swings lateral, controlled motion blur |
| Shot 11 | 00:09.600 | CARD 5 | the ONLY deep-black card, two offset lines of `{CARD_5}` crash in from top and bottom, overshoot, rebound, surge at the lens; character tears a coloured brush through the black and reveals a ~55% half-body crop; layers collapse in the stride direction |
| Shot 12 | 00:10.300 | peak | wide hero angle in the venue, everything lit at once, two strides then a planted hero pose, short Pull Out plus subtle Arc, light burst match-cuts into the card |
| Shot 13 | 00:12.300 | identity | clean warm-ivory or silver-white card, `{NAME}` stretches nearly edge to edge and holds one beat, character steps into a full-body hero pose in front of it, `{TITLE}` appears beneath, an emblem derived from the signature accessory contracts behind, near-static camera, one last inertial settle |

Rules the template enforces on every run:

- Shot 1 has no timestamp and begins mid-motion. No establishing shot, no
  neutral pose.
- Every card is entered and exited by a **gesture-triggered wipe**. The
  character's move causes the burst, band reversal, scan or brush that becomes
  the next shot.
- On every card the character is a **large crop with a stated percentage** and
  keeps moving. Typography sits partly behind them; one thin foreground stroke
  (chain, streak, ring) crosses in front.
- Shot 11 is the only black background. Every other card is light.
- The venue wide appears twice: Shot 5 (entry) and Shot 12 (peak).
- Every shot names a camera move from a fixed vocabulary: Arc Shot, Push In,
  Truck, Tilt, Tracking Shot, Whip Pan, Rack Focus, Pull Out, Static. Stay in
  that list.
- Every shot ends with its own sound beat synced to the visible action
  (whoosh, snap, UI tick, chain impact, sub impact, scan buzz, stinger).
- Sections: `subject_definitions`, `summary`, `retention_analysis`,
  `detailed_description`, `overall_soundscape`, `non_diegetic_music`, in that
  order.
- `summary` opens with the literal tag `[reference generation]` and ends by
  naming the `{NAME}` reveal and the `{TITLE}`.
- `retention_analysis` uses the formula
  `<Subject 1> (appears in [Shot 1] through [Shot 13]): fully_preserved -`
  followed by the wardrobe inventory and the closing negative clause: *No
  weapon, armor, supernatural ability, mechanical equipment, alternate costume,
  or second principal character is introduced.*
- `non_diegetic_music` states a BPM (observed 128 to 132), the instrument set,
  a **short three-note motif** tied to the character, a build that does not
  repeat the same hit on every card, the full motif and widest sound field on
  Shot 12, and a final chord plus stinger on Shot 13 instead of a fade.
- `overall_soundscape` ends with the line that no dialogue, narration, lyrics
  or vocal performance is present, unless the user asks for a voice.

## Fill-in fields

| Field | Default | Note |
|---|---|---|
| `{NAME}` | from the sheet title | rendered as display type in Shot 13 |
| `{TITLE}` | e.g. REBEL CHARM | two or three words, all caps |
| `{CARD_1}` | ACTIVE | one word |
| `{CARD_2}` | MODE: ENGAGE | short phrase, may carry a colon |
| `{CARD_3A}` / `{CARD_3B}` | SYSTEM / LINK | two words that read as one line |
| `{CARD_4}` | TARGET LOCK | two words |
| `{CARD_5}` | FULL DRIVE | two words, the climax card |
| `{VENUE}` | concert stage with LED walls | one coherent space with reflective floor, light sources and a runway or path for Shots 5, 10 and 12 |
| `{MOTIF}` | derived from the wardrobe | two or three graphic elements (a pattern, a ring shape, an emblem) that the cards abstract into shapes |

Change the card strings to give each video its own personality. That is the
one edit Bobo tells viewers to make, and it is why they are literal in the
template rather than generated.

## The template

```
You are writing a MiniMax H3 reference-to-video brief. The attached image is
<Picture 1>, a character design sheet. Read it carefully: the name in the title,
the face, hair, proportions, every wardrobe item, and the visual medium (anime
illustration, vinyl toy, photoreal). Output only the brief, in English, using
exactly these six sections in this order with these lowercase headings followed
by a colon: subject_definitions, summary, retention_analysis,
detailed_description, overall_soundscape, non_diegetic_music.

subject_definitions: one paragraph. "<Subject 1> is the character derived from
<Picture 1>, ..." Describe age impression, build, face, eyes, brows, lips, hair,
then the full wardrobe top to bottom naming every graphic, badge, buckle, chain,
ring, strap and hardware item, then "No weapon or functional prop is visible",
then "The original visual medium is ..." naming the medium and its surface
qualities.

summary: one paragraph opening with the literal tag [reference generation]. A
15-second, 13-shot premium character-reveal video presents <Subject 1> as
{attitude} inside {VENUE}. Her/his visual motif is derived from {MOTIF}. The
sequence begins directly in expressive motion, develops through attitude-driven
gestures, movement through the venue, beat-based turns and five gesture-
triggered kinetic typography cards, and culminates in a confident full-body
reveal of "{NAME}" with the title "{TITLE}".

retention_analysis: "<Subject 1> (appears in [Shot 1] through [Shot 13]):
fully_preserved - " then list facial identity, complexion, eyes, hair,
proportions, every wardrobe item, the palette and the rendering medium as
"remain unchanged". End with: "No weapon, armor, supernatural ability,
mechanical equipment, alternate costume, or second principal character is
introduced."

detailed_description: one opening paragraph stating that the video preserves
the sheet's medium while adding {VENUE} lighting, fabric and hardware motion,
and bold editorial motion graphics; name the palette and say which motif shapes
define the motion language and fast-cut rhythm. Then exactly thirteen shots
following this skeleton. [Shot 1] has no timestamp; every later shot begins
"[Shot N] At MM:SS.mmm," with these times: 00:01.100, 00:02.200, 00:03.200,
00:04.100, 00:05.200, 00:06.200, 00:06.900, 00:07.900, 00:08.600, 00:09.600,
00:10.300, 00:12.300.

  Shot 1 extreme close-up, mid-motion, a hand touches hair or a face-adjacent
  accessory, small fast Arc Shot with Push In, eyes lift and lock the lens, a
  light sweep crosses the face. Sound: fabric or hair friction, a light tap, a
  short whoosh.
  Shot 2 continues the same movement; a hand hooks or flicks a wardrobe item;
  the gesture emits a thin coloured light curve with motif echoes that travel
  and contract toward one side; camera Trucks with the hand and Tilts back to
  the face; a half-smile; everything peaks together and hard-cuts. Sound: the
  item's impact and one clean snap.
  Shot 3 CARD. Hard cut to a bright warm-ivory field; giant ultra-bold condensed
  "{CARD_1}" slams in from both sides and tightens to fill about ninety percent
  of the width; a large motif-coloured circle expands behind it while fine
  rings counter-rotate; <Subject 1> as a large off-centre waist-up crop
  occupying about fifty percent of frame pushes in from the left continuing the
  arm gesture; part of the word stays behind her while one thin foreground
  stroke crosses in front; the gesture triggers a second circle burst that
  expands full-screen and wipes into Shot 4. Sound: UI tick, air-cut whoosh,
  light metal ring.
  Shot 4 CARD. Pale grey field with several horizontal bands in the motif
  colours rolling at different speeds; the dominant band reveals one complete
  giant "{CARD_2}" while secondary bands carry fragmented letterforms and speed
  streaks; <Subject 1> enters as a moving full-body silhouette, one step on the
  beat and an arm swing that flings the accessories out; the gesture reverses
  the main band, which match-cuts into Shot 5. Sound: footstep, fabric snap, two
  UI ticks.
  Shot 5 the band becomes a fast Whip Pan into the {VENUE} wide; describe the
  floor, the walls, the light sources and the path; <Subject 1> is already
  striding along the path with relaxed confidence, hem and accessories reacting
  with delayed inertia, hair lifting; camera settles into a low Tracking Shot.
  Sound: live footsteps, sole friction, accessory swing, light-rig switching.
  Shot 6 low medium-close beginning on the footwear landing and Tilting upward
  across every wardrobe item to the face; <Subject 1> catches a wardrobe item
  with two fingers, releases it, then redirects her gaze to camera with an
  expression change (cool confidence to a raised-brow, mildly disdainful look);
  a blurred venue element crosses the foreground; optional Rack Focus from
  accessory to eyes. Sound: a small metal click, fabric and breath briefly
  amplified.
  Shot 7 CARD. Hard cut to a two-tone split field; "{CARD_3A}" drops from above
  and "{CARD_3B}" rises from below as two enormous ultra-bold layers locking
  with a narrow centre gap and a slight opposing drift; <Subject 1> as a huge
  shoulder-and-face crop occupying nearly sixty percent of the screen fills the
  gap, turns from profile to camera, blinks once, then sends her gaze sharply
  sideways; hair and neck accessory intersect the gap; a bright scan line
  sweeps across the eyes; the gaze triggers a brief positive/negative split and
  the scan wipes along the eye-line into Shot 8. Sound: scan buzz, UI tick,
  short snap.
  Shot 8 low three-quarter perspective; one quick side step, a hip pivot, a
  sharp shoulder-led turn; hem flares and accessories swing late; compact fast
  Arc Shot around her while venue lights crisscross; finishes head turned back
  to camera with a playful controlled defiant expression. Sound: footfalls,
  accessory impacts, a rising whoosh.
  Shot 9 CARD. Warm-ivory field cut by two giant diagonal planes in the motif
  colours; ultra-bold "{CARD_4}" moves from distant depth toward camera along a
  perspective-shortened diagonal, front and rear sections offset before the
  final lock; an extreme diagonal crop of <Subject 1>'s eye, hair fringe, neck
  accessory and chest graphic occupies about forty-five percent of frame; pupils
  track the incoming type; the moment the gaze crosses the locking line the
  words snap into alignment with a brief camera jolt; the nearest plane rushes
  past the lens and becomes Shot 10. Sound: sharp UI lock, snap, fast whoosh.
  Shot 10 the passing plane becomes a glowing edge along the venue path;
  <Subject 1> approaches, passes close beside the lens, then changes direction
  with a smooth half-turn and a confident step-back; camera Trucks backward then
  swings laterally; face and body stay sharp while the venue gets controlled
  lateral motion blur; hair and accessories sweep the foreground. Sound: air
  displacement, successive sole impacts.
  Shot 11 CARD. Cut to the only deep-black card; two gigantic offset lines of
  "{CARD_5}" crash inward from top and bottom, overshoot, rebound into
  alignment, then surge toward the lens at different depths; <Subject 1> steps
  out of a narrow light slit at the centre or swings a forearm across the torso
  and steps forward, tearing a broad motif-coloured brush through the black and
  revealing a dynamic half-body crop of about fifty-five percent; the principal
  type stays behind her while letter edges, motif lines and brush remnants race
  in front; expression firm and fully focused; all layers collapse at speed in
  her stride direction into Shot 12. Sound: heavy sub impact, fabric snap,
  accessory impact, low-frequency whoosh.
  Shot 12 the visual peak in the {VENUE}: everything lights at once, follow-
  spots converge; wide hero angle; <Subject 1> takes two confident strides,
  pivots a hip and shoulder, plants one foot and settles into a powerful
  asymmetric hero pose, one hand lifted near the collar line, the other relaxed;
  short Pull Out combined with a subtle Arc, then a sudden hold at the peak; the
  motif shapes form a giant emblem behind her; a light burst produces one
  bright-frame trail that match-cuts into the identity card. Sound: footfall,
  accessory swing-back, light ignition and one wide sub impact land together
  as the film's maximum hit.
  Shot 13 hard cut to a clean warm-ivory identity layout; the giant display
  name "{NAME}" stretches almost edge to edge and stays fully readable for one
  beat; <Subject 1> takes one short step into a complete full-body hero position
  in front of part of the name while the smaller title "{TITLE}" appears
  beneath; behind her a huge translucent motif circle, thin technical arcs,
  sparse nodes and a dark circular emblem derived from the signature accessory
  create layered depth, then contract into one clean emblem; camera nearly
  Static; one restrained blink; hair, hem and accessories complete one last
  inertial settle. Sound: one last light metal ring, a UI register, a clean
  stinger.

overall_soundscape: one paragraph. Venue ambience and reflections, footwear
impacts, fabric movement, every accessory's own sound, light-rig mechanics,
air displacement from turns and close passes; cards use typography impacts,
scan sweeps, snap locks, depth passes and brush tears synced to the visible
motion; Shot 12 is the maximum spatial impact and Shot 13 contracts to a clean
metal tail and identity-register sound. End with: "No dialogue, narration,
lyrics, or vocal performance is present."

non_diegetic_music: one paragraph. A character-specific {genre} score at about
{BPM} BPM; name the drums, bass, synth and percussion; a short three-note motif
that reflects the character's personality; the opening presents the motif
sparsely, the middle expands the groove, stereo width and syncopation, the
build after Shot 8 grows drum density and harmonic tension without repeating
the same hit on every card, Shot 12 carries the fullest drum attack, biggest
low end, widest field and complete motif statement, and Shot 13 cuts the drive
and resolves with one bold final chord, a bell-like answer to the motif and a
short energised tail instead of a generic fade.

Fields:
NAME = {from the sheet unless overridden}
TITLE = {TITLE}
CARD_1 = {ACTIVE}   CARD_2 = {MODE: ENGAGE}   CARD_3A/3B = {SYSTEM} / {LINK}
CARD_4 = {TARGET LOCK}   CARD_5 = {FULL DRIVE}
VENUE = {concert stage with glossy black floor, LED walls, moving spotlights,
laser lines, elevated platforms and a short runway}
MOTIF = {derive from the wardrobe: a pattern, a ring shape, an emblem}
Extra instructions: {optional}
```

## Verified run (2026-09-06)

First attempt, vanilla ComfyUI on the 4070 Ti 12 GB: DaSiWa Hybrid 4Turbo
ref2va, 4 steps euler simple, shift 12/3, 864x480, 362 frames (15 s), one
reference (a Qwen-Image-Edit design sheet of a photoreal woman in a leather
jacket), seed 20260906. **316 s wall**, audio present (mean -14 dB, peak
-0.4 dB). Every one of the 13 shots landed on its timestamp: all five cards
rendered with legible type ("ACTIVE", "MODE: ENGAGE", "SYSTEM / LINK",
"TARGET LOCK", "FULL DRIVE"), the black card at Shot 11, the venue wide at
Shots 5 and 12, and the identity card with "MARA" and "NIGHT SIGNAL" both
readable. Identity and wardrobe held throughout; the photoreal medium of the
sheet carried into the video. Only weak spots: the eye crop in Shot 9 lost its
type layer, and Shot 8's turn was mostly a silhouette pass. Artifacts at
`D:\SimpliGen-Backups\character-pv-20260906\` (graph, prompt, sheet, video,
contact sheet).

Sheet-step note: Qwen Image Edit produced a usable sheet in 37 s but ignored
the 16:9 request (came back 1:1), garbled the small labels and drew the
expression heads as cartoons. It was still a sufficient reference. GPT Image 2
and Nano Banana 2 presets exist in SimpliGen but are API-backed and cannot be
driven from the MCP.

## Worked example

Bobo's own output for the punk girl "looova" is embedded verbatim as the
prompt in the RunningHub workflow `MiniMax H3 Epic Character PV Creation`
(post 2095032985100173313 on runninghub.ai, node 217 in the API export). It is
the canonical instance of this skeleton with the default field values and a
concert-stage venue. A second run of the same template placed her in an
"underground music-and-arcade complex" with chrome railings and red panels and
changed nothing else in the structure.
