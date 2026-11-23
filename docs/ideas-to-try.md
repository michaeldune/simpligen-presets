# Ideas to try later

Running backlog. Each entry: what to try, why, rough cost, source. Move an entry to "Done / dropped" with the
result when it is settled.

## Open

### MiniMax H3 video pixel head (2026-11-23)
Source: https://huggingface.co/pocis/MiniMax-H3-Video-PixelHead (same author as the Qwen-Image 2.1 head; a
Krea-2-PixelHead also exists). The Qwen-Image 2.1 head was tested 2026-11-23 and not adopted: about 0.6 s saved per
image, visibly softer, worst on Turbo (`F:\Claude-Work\pixelhead-qwen21-20261123\VERDICT.md`). For H3, the VAE decode
is a much bigger share of each render, so the speed case may be different. To try: read its node and training range
first (check the last sigma of our 8-step H3 graphs against it), then run an A/B on vanilla ComfyUI the same way.
Michael said "not now" on 2026-11-23.

### Ray Krea2 x Mid Aesthetic card, after 2026-11-03 (2026-10-24)
Source: RHR's Nov/Dec Discord wishlist, https://civitai.com/models/3009760/ray-krea2-x-mid-aesthetic?modelVersionId=3415465.
Ray3780's Krea 2 checkpoint rebuilt from several of OnlyLemon's LoRAs (a moody, Niji / Midjourney-style gothic look).
Only build: version 3415465 'turbo v1 INT8ConvRot', file 3308391 `rayKrea2XMid_turboV1Int8convrot.safetensors`,
12,821,825,036 B, SHA256 554b9d48b93c7d4db698ba7f35cee3dc79e34b521557cbfea1f03ddbe84bd999. Author settings: er_sde /
simple, 8-12 steps (version page: 12), CFG 1. Not run: the download is Civitai Early Access (403 "Early Access",
paid with Buzz) until **2026-11-03 10:02 UTC**; Michael has told the user. Then: add an arm to
`F:\Claude-Work\krea2-wishlist-20261024\run.py` (same prompts, seeds and controls, so the stock-Turbo, FinalCut, Moody,
CyberRealistic and Nippon images there are reusable), compare against Moody especially, and if it earns a card it likely
goes in Krea 2 Art & Styles. Licence flags: Image, RentCivit, Rent.

### Motion speed slider LoRAs for H3 (2026-10-22)
Source: Beyond Frame AI, https://www.youtube.com/watch?v=hHoMM2NSF1Y (0:12-1:30; transcript at
`F:\Claude-Work\watch-hHoMM2NSF1Y-20261022\transcript-clean.txt`). Three LoRAs, all from the video description:
https://civitai.com/models/2951265/motion-speed-slider-for-h3-minimax-by-fos,
https://civitai.com/models/2985458/motion-speed-mmh3-slider (a second slider), and
https://civitai.com/models/2994324/progressive-acceleration-mmh3-slider-smoothly-accelerates-the-speed-of-any-action-or-motion-over-time.
Claim: the strength value is signed, so it reads as a direction rather than an amount - positive speeds motion up,
negative (he shows -4) slows it to full slow-mo on the same prompt and seed; the acceleration one ramps over the clip
instead of holding one speed (car launching, sprint, a punch that lands harder). Plain LoRA loader, stackable, toggled
per shot. Also claimed to clean up smearing on fast action. Not run. Why: a signed strength maps straight onto a card
slider, we ship nothing that controls motion speed, and it would give MV Chain shots a speed ramp without an editor.

Corrections after reading the Civitai metadata (2026-10-22, same day):
- **The usable range is +/-8, not +/-4.** The v1.1 author's note says min -8, max 8, default 4, and that a strength
  **below 4 largely keeps the no-LoRA content** - so the -4/-2/0/+2/+4 sweep this entry first proposed would have
  measured almost nothing. Sweep 0 / +/-4 / +/-8 instead.
- **It is two different sliders, not one.** Under the same model page, `motion_speed_slider_mmh3_v1.1` (0.18 MB) is
  *spatial displacement* (sprinting, dashing across the scene), and a newer `action_speed_slider_mmh3_v1` (4.11 MB,
  2026-10-16, not in the video's links) is *limb cadence* (punch flurries, sword swings, instrument playing, fast
  chopping) and claims to hold face, clothing and background stable. The author recommends stacking both at +1.5 for
  rapid strikes while sprinting. Two axes, so a single "motion speed" card slider may be the wrong shape.
- **The fos slider is paywalled.** `civitai.com/models/2951265` (the one the video demos first, and the only one with
  trigger words - `slow` / `fast`) returns `403 {"error":"Early Access"}` and needs Buzz. Not a token problem; the
  other three download fine with `CIVITAI_TOKEN`.
- Downloaded to `D:\SimpliGen-Models\loras\`: `motion_speed_slider_mmh3_v1.1` (8 tensors),
  `action_speed_slider_mmh3_v1` (184), `progressive_acceleration_slider_v1.0` (416).

**TESTED 2026-10-22, stage 1** (`F:\Claude-Work\h3-speed-loras-20261022\VERDICT.md`, 10 renders on vanilla 8188:
official ref2va pruned int8, 864x480, 124 frames, 20 steps, seed 101, one locked-camera prompt of a sprinter crossing
frame; control run twice). **The dial direction is real but these are not retiming controls - not a card slider.**

- **Every arm regenerated the scene.** Mean abs difference of frame 0 against the control's frame 0, before the runner
  enters: the second control scores 2.4 (same-seed rerun noise), every LoRA arm 11.5-35.4 - different stadium, trees,
  floodlights and lane geometry, confirmed on the contact sheet. The v1.1 note claims it "minimized the LoRA's impact
  on the overall framing and composition"; at the author's own recommended strengths it does not hold. A user nudging
  this slider gets a different shot, not a faster one. That alone rules out the card.
- **Signed direction holds, strongly.** Both controls crossed the frame in exactly 60 frames (noise floor 0), against
  Motion Speed -4 = 87 (1.45x slower), -8 = 79, +4 = 43 (1.4x faster); Action Speed -4 = 73, +4 = 37 (1.6x faster).
  Magnitude is NOT monotonic (-8 less slow than -4) and cannot be separated from scene geometry on one seed.
- **Motion Speed +8 overrode an explicit camera instruction**: the prompt said the frame never moves, no pan, no
  reframing; frames 0-40 are a locked wide and from frame 60 the camera tracks her with the background sweeping
  (`dense_ms_p8.jpg`). Picture quality fine - a direction failure, not corruption.
- **Progressive Acceleration did the opposite of its claim.** The plain shot already accelerates (2nd-half speed
  2.63x the 1st, identical on both controls); with the LoRA that drops to 1.14 at +4 and 1.08 at +8, i.e. it flattened
  the acceleration and made her slower overall. Caveat: apparent acceleration is perspective-driven and every arm has
  different perspective, so direction-opposite-to-claim is suggestive, not proven.
- Costs at the extremes: -8 is 19% darker with 26% less contrast; Progressive +8 picks up a green cast (green-minus-red
  +1.3 vs the control's -11.3).

Untested, so the verdict covers only the above: one prompt, one seed, 20 steps, 480p, no dialogue. Not covered -
whether any of this survives a 4-step distill; whether they cost dialogue or lip sync (the real card blocker); Action
Speed on a strike-in-place prompt, which is its actual use case and which a running prompt cannot separate from
displacement; stacking Motion + Action at +1.5 each as the author suggests; and the paywalled fos slider. Worth
keeping as a hand tool for ComfyUI iteration where re-rolling the scene is acceptable. Unrelated tip from the same
video section, worth keeping: the info icon beside a LoRA in ComfyUI's loader shows the author's own example clips, so
a strength can be picked without burning test renders.

### MiniMax H3 Singularity v2 vs the v1.3 we ship (2026-10-22)
Source: same video (5:43-end), weights https://huggingface.co/WarmBloodAban/Minimax-h3_Singularity/tree/main.
**Not a new model to us.** We already ship `minimax-h3-singularity-pack` 1.1.1 (t2v/i2v/r2v) on
`Minimax-h3_Singularity_ref2va_Pruned_v1.3_int8` (19.53 GB), and the README row already carries a three-seed verdict
against the official checkpoint: close-up faces ~30% sharper and distant faces readable in action, but ~20 points
darker, lower contrast and a quarter to a third less motion - "a look, not a free upgrade". The video is a tutorial
for the pack we have; the only new thing is **v2** (repo last modified 2026-10-21).

So the question is v2 vs v1.3, and it is a narrow one. V2's release notes claim expanded action coverage and "more
varied motion sequences", stronger prompt adherence (recommends prompts under ~5,000 characters), an audio-reference
conditioning fix, and stronger style rendering with explicit style keywords (photorealistic / East Asian realism /
3D CG / cinematic CG). The claimed motion gain is exactly the fault we measured in v1.3. It claims **nothing** about
the darkness or the contrast, which were the other two.

Blocker on shipping it, independent of quality: **v2 is 31.67 GB unpruned int8 and there is no pruned v2.** Our pack
ships the pruned v1.3 for exactly that reason. 31.67 GB exceeds this machine's total 31.2 GB of RAM, so it may not
load here at all, and it would be out of reach for the 12 GB users the pack is for even if it wins. Downloaded and
verified anyway (1,035 tensors, I8/U8/BF16/F32, header consistent with the byte count) at
`D:\SimpliGen-Models\diffusion_models\Minimax-h3_Singularity_ref2va_v2_int8.safetensors`.

Cost: first one prompt, one seed, just to see whether it loads and how long a step takes. Only if that is viable,
3 prompts x 3 seeds x {v2, v1.3 pruned, Midnight} scored on the same axes as the original verdict - mean brightness,
contrast, optical-flow magnitude, and face sharpness on native-pixel crops. Note the comparison confounds version
with pruning (v2 full vs v1.3 pruned); HF has a full v1.3 int8 if that needs isolating later.

### Three conventions worth stealing from Pixelle-Video (2026-10-22)
Source: https://github.com/ATH-MaaS/Pixelle-Video (Apache-2.0, Pixelle.AI / AIDC-AI, read at `848b054e`; 29.3k stars
but dormant — last push 2026-06-14, and third-party trackers show it "updated today" only because `updated_at` moves
on every star). A topic-to-short-video orchestrator: LLM script -> one image or clip per narration line -> TTS -> HTML
frame templates screenshotted with Playwright -> moviepy stitch. Nothing in its output beats our H3 work and it is not
worth installing (reviewed, not run). Three structural ideas are worth lifting:

1. **Late binding by role, for Recipes.** Its pipelines never name a model, only a capability: `self.media`,
   `self.tts`, `self.video`. `utils/workflow_util.py` is the whole mechanism — `workflows/{source}/{service}.json`,
   where `source` is `selfhost` or `runninghub`, so switching a step from the local GPU to a cloud renderer is one
   path segment, and config names only a default per capability (`comfyui.image.default_workflow` etc.). Try: a
   recipe that declares roles (still / motion / voice) and resolves each to a preset id at run time, with a default
   and a one-field override, instead of baking preset ids into the flow steps. Makes "same flow, DaSiWa instead of
   Midnight" a launch parameter rather than an edit.
2. **A layout declares its own required inputs.** Template filenames carry a prefix the pipeline reads before it
   generates anything: `static_*` needs no generated media, `image_*` needs a still per line, `video_*` needs a clip
   per line (`templates/1080x1920/`, `1080x1080/`, `1920x1080/`). Cheap contract for recipe blocks and HyperFrames
   compositions: the layout states what it consumes, so an impossible pairing is refused up front instead of failing
   three steps in.
3. **Per-capability prompt prefix as a style lock.** `comfyui.image.prompt_prefix` / `video.prompt_prefix` are
   prepended to every generated shot in a run (theirs is a matchstick-figure style string). That is exactly the
   consistency problem a multi-step recipe has; one style string applied to every generative step in a flow.

Not worth copying: their parameter contract lives *inside* the graph, as node titles like `$prompt.text`,
`$width.value`, `$height.value` (comfykit convention, same trick Pixelle-MCP uses to expose workflows as MCP tools).
Self-describing and import-friendly, but it can only say "string" or "int" — it cannot express sliders with mins,
grouped reference-image rules, shot modes, engine-version gates or declared weights, which is what our manifests are
for. Mentioned here only because it is the design you would pick if workflow import ever mattered, which SimpliGen
deliberately does not support. Their renderer is also strictly worse than HyperFrames (screenshot per frame,
moviepy 1.0.3, no audio-accurate timing) — it is the thirty-layout style shelf organised by aspect ratio that is
interesting, not the renderer.

### H3 face-only swap LoRA (2026-10-19)
Source: AI Late to Class, https://www.youtube.com/watch?v=SzqMV4S1908 (0:30-4:15). LoRA:
https://huggingface.co/UntMods/FaceSwap_MiniMaxH3_REF2VA (from the video description; the CRT-Nodes author, Apache-2.0,
Ref2VA base, trigger word "Faceswap" at strength 1, pruned, 187 likes on 2026-10-19). He ran it on Ref2VA + Ref2V
turbo LoRA, 8 steps, prompt just "face swap". Why: our Character Swap card (akatz V1.5) replaces the whole person (face,
hair, clothes); a face-only swap would keep hair, outfit and accessories, which suits continuity across shots and
putting a recurring character's face on stock footage. His caveat: it still swapped the hair and added earrings, so
"face only" is the claim to test. **TESTED 2026-10-19** (`F:\Claude-Work\h3-faceonly-swap-20261019\VERDICT.md`,
14 renders): with our four-view sheet as reference it did not swap at all (talk/sea/geisha), went for the man on the
cafe shot and broke one seed (white patch + glasses); with a head-and-shoulders crop it swapped and picked the right
person, but copied hair and the sweater visible in the crop, so "keeps the original hair and outfit" did not hold.
Not worth a card now. If revisited: a tight face crop (little hair, no clothes), and the author's CRT sampler.
Also from the video, for a Discord example with our
existing card: edit the clip's first frame (e.g. blood on the face with Qwen Image) and use it as the Character
picture to carry an effect through the whole clip.

### DaSiWa H3 v4 + the smaller quants (2026-10-17)
Source: https://civitai.com/models/2877206 (Hybrid v4 3391862, Hybrid v4 Turbo 3392061, published 2026-10-09).
v4 Turbo is a 4-step distill (our v3 pack is 8-step). Its int8 file is structurally identical to v3's (drop-in). New:
engine 0.41.1 reads DaSiWa's W4A8 (12.5 GB) and W6A8 (16.8 GB) layouts natively (`comfy/ops.py` loads `weight_s_rel`
/ `weight_s_channel` / `weight_codebook`), so the earlier "engine cannot read W4A8" note is stale - not yet run.
**BAKED 2026-10-17** (`F:\Claude-Work\dasiwa-v4-20261017\VERDICT.md`, 48 clips): v4 Turbo at 4 steps is ~40%
faster than v3 at 8 (42-54 s vs 63-81 s), dialogue 11/12 word-exact, identity held. More contrast; lit a "dim studio"
backdrop. Defect: 1 of 3 seeds opened r2v set C with 1.7 s of the person reference photo, then hard-cut (v3 0/3).
w6a8 = int8 pictures, 4 GB smaller; w4a8 drifts. Michael watched all 48 clips: "everythings good". Next: a v4 pack
if he wants one.

### From SatoDive's H3 Latent Continuation (2026-09-19)
Source: https://github.com/SatoDive/Minimax-H3-Latent-Continuation, tutorial https://www.youtube.com/watch?v=KkugNjrpXAc

1. **Lip sync across a Native Guide join.** PARTLY DONE 2026-09-19 (see Done section): speech and picture survive
   the join; lip sync itself could not be measured at 480p and needs Michael to watch
   `F:\Claude-Work\satodive-continuation-test-20260919\clip2_stitched_00001_.mp4`. If he wants a number,
   re-run at 768p with a tight face so the mouth is big enough to score.
1b. **Make the continuation cheaper.** It took 780 s vs 200 s for a fresh clip because the 8 s `seed_ref_video` is
   encoded as a reference. Try a 2 s tail, or no `seed_ref_video` when the framing does not change.
2a. **Audio-locked H3 lip sync as a SimpliGen card.** The singing test (Done section) showed the SatoDive pack's
   `digital_human` mode locks the real song into the audio latent instead of using it as a guide. Check whether
   our shipped H3 lip-sync presets can do the same with native nodes (set the audio latent + a zero audio noise
   mask) - it would give frame-true song audio in the output and make chained singing shots safe.
   **TESTED 2026-09-20: yes, with three core nodes already in engine 0.36.0** (`VAEEncodeAudio` ->
   `SetLatentNoiseMask` with a zero `SolidMask` -> `LTXVConcatAVLatent` onto the H3 AV latent). No gain on a single
   clip (the shipped card already carries a trimmed track: waveform corr 0.943 vs 0.951 locked, same lip sync). In a
   one-hop continuation the guide's audio falls to 0.827 while the lock holds 0.952; sync equal at one hop. So the
   card worth building is a locked-track CHAIN card, and 2c decides how much it matters. One seed, one span.
   `F:\Claude-Work\h3-native-audio-lock-20260920\VERDICT.md`.
2b. **Repeat the singing chain on two more song spans and a second singer** before trusting it (one-clip rule).
2c. **3-hop singing chain** (A + B + C) to see whether sync or brightness degrades with depth.
   **DONE 2026-09-20 on our native graph, guide vs lock:** audio does NOT compound on the guide path once the 22
   overlap frames are trimmed (0.94/0.90/0.92 vs 0.95/0.90/0.93 locked), so the audio lock buys nothing; the PICTURE
   compounds in both arms (sharpness x3 by hop 3, contrast +15%, crunchy skin) because the tail goes through pixels at
   every hop. Next idea worth testing: **2d. a LATENT tail hand-off with native nodes** (save the AV latent, feed its
   last latent frames as the next clip's prefix at noise-mask 0, no decode/re-encode) and re-run this 3-hop chain.
   Lossless-tail split run the same day: a lossless WebP tail instead of MP4 frames did NOT help (sharpening compounds
   faster, background still crushes), so the codec is ruled out and SaveVideo bitrate is not worth touching. 2d is
   now the only test that separates "VAE round trip" from "H3 over-commits to guide detail". First step can be
   SatoDive's relay over 3 hops in vanilla (already installed), before building anything native.
   **SatoDive relay x3 DONE 2026-09-20: it does NOT degrade** (sharpness 98 -> 128 vs 132 -> 406 on the pixel chain,
   background steady, join 0.997 at every hop, brightness steps +2 once and stays). So the pixel hand-off is the cause.
   **2d is now: a multi-hop LATENT chain as ONE workflow** (the app cannot pass a latent between jobs; SatoDive's
   save/load nodes are not packable). Starting point: our Director pack's `MiniMaxH3GeneratedAVMaskedContext`, which
   already hands the AV latent over inside one job; extend from 2 segments to N with a driving track per segment.
   **2d FIRST RUN 2026-09-20:** it already exists - seitanism's `MiniMaxH3SongMaskedAVContext` (in the engine, pinned by
   our chain pack) locks the master song and hands the latent tail over, N clips in one workflow. Ran 4 clips in vanilla:
   joins 0.998+, soundtrack perfect (one master-song slice), BUT on our ref2va + turbo v4 recipe clip 2 pushed in to an
   extreme close-up and brightened, and clips 3-4 still darkened and sharpened. So the hand-off is not the whole cause;
   SatoDive's clean relay also used another base/LoRA/sampler and a previous-clip reference video. **Next: the same
   4-clip graph on SatoDive's recipe (fl2va + fl2v turbo v1.2, res_multistep, 7 steps), then add a reference video.**
   **RECIPE SWAP DONE same day: the recipe was the difference.** Same graph on fl2va int8 + fl2v turbo v1.2 (euler then
   res_multistep, 7 steps): brightness 34-35 for all 27 s, no sharpening, joins 0.9988, audio 0.99 at zero lag, lip sync
   positive on all four clips, no reference video needed; softer and calmer than ref2va + turbo v4. Open: which of
   base / LoRA / sampler / steps carries it; whether the pixel-tail chain is also fine on this recipe; a second shot.
   **2e (card): "H3 Music Video Chain" - N clips in one workflow, master song in, `[Shot N]` prompt split, native
   assembly (no VHS), fl2va recipe.** Everything it needs is already in the engine.
   `F:\Claude-Work\h3-latent-mv-chain-20260920\VERDICT.md`.
   `F:\Claude-Work\h3-native-audio-lock-20260920\VERDICT.md`.
2. **Same test with singing.** DONE 2026-09-19, see Done section. If (1) holds for speech, repeat with a vocal stem + backing at -14 dB. This decides
   whether music-video singing shots can be chained instead of one 345-frame generation.
   **2b REPEAT DONE 2026-09-20:** two more spans (verse 2 with the lead, chorus with the guitarist as a second singer).
   Chain render time = one long generation; every deliverable's audio verified per second. Michael on verse 2: can't
   pick between chain and long, "both are spot on"; chorus/guitarist: "the same, both spot on". 3 of 3 spans now. Caveats: the continuation steps a few luma levels brighter at the
   join, and it inherits the previous clip's drift (the guitarist shot pushed in and brightened in BOTH arms), which
   will compound over more hops: that is what 2c has to measure. The lip metric is blind on continuous singing.
   Details: `F:\Claude-Work\satodive-singing-test-20260919\VERDICT.md` (REPEAT section).
3. **Separate context reference from the handoff clip.** Continue from a close-up while feeding an earlier wide
   master as `<Video 1>`, then ask for a wide. Check the room layout holds. Could fix cuts in the Clip Chaining
   and Two-Shot Director cards.
4. **Measure the pixel round-trip darkening on OUR Clip Chaining pack.** Confirmed on his nodes 2026-09-19 (-2.2%
   mean luma through pixels vs +0.3% through the latent, same seed). Still to do: 3 hops on our own pack; if it
   compounds, that is the argument for a latent hand-off there.
5. **New characters first in the prompt.** He says subjects listed first get more weight. A/B the same seed with
   the new character listed first vs last in a 3-subject r2v shot.
6. **Lower reference strength for returning characters.** Check whether our H3 conditioning nodes expose a
   per-reference strength, and whether dropping it for recurring subjects helps a newly introduced one.
7. **Phonetic respelling for words H3 mispronounces.** He wrote "coughs" for "cuffs". Try on any line that
   garbles; if it works, add it to the minimax-h3-prompt skill.
8. **res_multistep + simple on continuation clips.** His preferred sampler pair for continuations. Compare against
   our current continuation sampler on one join.
9. **Fixed-count latent relay as a pack.** His save/load-from-disk nodes are not packable (folder-scanned
   dropdown, JS UI). A fixed 2- or 3-segment in-graph chain is. Revisit when his v2 (one master prompt, 6+ clips,
   constant VRAM) ships. CHECKED 2026-09-26: v2 not out; main still 4142527 (09-18, what vanilla has). A side branch
   `claude/comfyui-lora-merge-nodes-owkv88` (9562b4e, 09-25, unmerged) adds an unrelated "LoRA Merge Studio" node pack
   with example workflows for Klein 9B, Krea 2, Qwen 2.1 Edit and Z-Image Turbo.

### From thedotmack/claude-mem (2026-09-19)
Source: https://github.com/thedotmack/claude-mem (README only, not installed). Verdict: covered by our agentmemory
setup; do NOT install it alongside (two hook sets capturing the same sessions, and its installer defaults to a
hosted account). Ideas worth borrowing for our own bridge:

10. **Compact-index injection instead of raw blobs.** Our agentmemory hook injects truncated JSON of old tool
    inputs (`{"file_path":...,"new_string":...`), which is mostly noise. claude-mem injects a one-line-per-item
    index with IDs (~50-100 tokens each) and fetches full detail only on request. Change the bridge/shim to inject
    titles + IDs and let the agent pull detail with `memory_recall`. Cost: an afternoon on bridge.mjs.
11. **Relevance gate on PreToolUse recall.** Today a Write to the ideas file recalled a GPU note and an
    agent-toolkit clone. Add a minimum-score cutoff, or inject only at SessionStart/UserPromptSubmit.
12. **`<private>` tag convention.** Text wrapped in `<private>` is never stored. Cheap to add to the bridge; useful
    for tokens and held Discord drafts.
13. **Typed observations.** claude-mem tags each as decision / bugfix / etc. and filters search by type. Check
    whether `memory_facet_tag` already gives us this before building anything.

### Memory-store audit findings (2026-09-19)
14. **agentmemory observations are raw tool records titled "Write"/"Edit".** 847 observations over 659 sessions
    (532 sessions hold zero); a search for "H3 latent chaining lip sync" returned five items all titled "Write"
    with scores under 0.02. Compact search mode already exists server-side, so idea 10 is mainly a TITLE problem:
    have the bridge send a meaningful title (file name + first line) or turn on server-side compression.
15. **Close sessions.** 539 of 659 sessions are still "active"; 533 diagnose warnings are all abandoned sessions.
    The Stop/SessionEnd hook is not ending them. Only 134 sessions have summaries.
16. **Run the project backfill** the diagnose asks for (`POST /agentmemory/migrate {"step":"infer-memory-projects"}`);
    20 of 20 memories have no project scope. Also project = last cwd segment, so scratch dirs become "projects".
17. **Make the OB1 daily digest say what was done, not just counts.** (OB1 itself: RESOLVED 2026-09-19, Supabase
    had suspended it for inactivity; ZCode restored it and HermesAgent now posts a daily digest from agentmemory.)
    The digest currently lists sessions/observations per project + cwd. Feed it agentmemory's session summaries
    (134 exist) so it carries one line of substance per project. Also dedupe: day one left 3 near-identical
    digests, a "failed to build a summary" entry and a connectivity-test thought. ZCode's lane.
18. **Viggle Meridian: re-camera an existing H3 shot (or a still).** https://huggingface.co/Viggle/Meridian, read
    2026-09-20 (card only, nothing run). Two 1.88 GB LoRAs (`comfyui/meridian_teacher_lora` + `meridian_turbo_lora`,
    load BOTH at 1.0, teacher first, never merge) on the H3 **fl2va** base (not ref2va), conditioned on two reference
    videos: the source clip and a point-cloud render of it along an authored camera path (grey holes where unseen).
    Orbit / slide / push, freeze-frame bullet time, play-hold-resume; 73-243 frames at 24 fps, 768-class. Turbo grid in
    ComfyUI: `MiniMaxH3SigmaShift` 3.0, steps 3, euler/simple, cfg 1; teacher alone shift 12, steps 49. Needs their two
    nodes (`meridian_embed.py` Frozen Prompt, `meridian_geometry.py`) and **VGGT-Omega**, which is gated + FAIR-NC
    (noncommercial) and runs in its own Python via subprocess: Michael has to request access himself. Vanilla only,
    NOT packable (gated model + subprocess; the no-geometry graph wants two pre-rendered videos). Open questions for
    a first test: (a) does it run at all on the 4070 Ti through ComfyUI's H3 path with our int8 convrot fl2va base
    (their numbers are 88-113 GiB on a B200, no offload support); (b) does the turbo LoRA survive an int8 base, given
    its delta is ~100x below bf16 rounding (if not, teacher-only at 49 steps is the fallback and will be slow);
    (c) cheapest first step needs no VGGT: their `meridian_workflow.json` + a `cond_source.mp4`/`cond_render.mp4`
    pair, if one can be had from their examples. Use: music-video orbit around a frozen beat of an existing shot,
    or a camera move from one still. Input must be one continuous take at constant 24 fps.
19. **Low-VRAM GGUF card for the Qwen Image 2.1 pack (8 GB cards).** https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF,
    read 2026-09-20 (card + file list only, nothing downloaded). NOT a different model: GGUF quants (Q4_0 4.05 GB ...
    Q8_0 7.59 GB, Q4_K_M 4.6 GB recommended) of the SAME base weights as Comfy-Org's int8; "Uncensored" = no safety
    checker in the release, which is true of our int8 pack too (no abliteration, LoRA or retraining claimed). Its text
    encoder and VAE are byte-identical to Comfy-Org's (same sha256 as our manifest pins). Same Qwen Research licence
    (non-commercial). Only gain: VRAM, so a card for 8 GB GPUs with the encoder in system RAM; nothing for 12 GB (int8
    already runs in ~9.4 GB at 16 s). Blockers: (a) the card says it needs **leejet/ComfyUI-GGUF** (7-star fork, pushed
    the same day) while SimpliGen's engine has **city96/ComfyUI-GGUF** @6ea2651 (Jan 2026) - same node names, cannot
    coexist, and our shipped H3 GGUF pack depends on city96's; city96's loader does list a `qwen_image` arch, so the
    files MIGHT load unpatched - unknown until one is downloaded; (b) needs the 0.37 engine like the rest of 2.1;
    (c) a day-old personal upload (Comfy-Org-first rule). WHEN: after a 0.37 engine exists. Test in vanilla: download
    Q4_K_M, does city96's loader take it, speed vs the 16 s int8, quality at Q4 on the text-sign and edit prompts from
    `F:\Claude-Work\qwen-image-21-test-20260920\`. If it loads on city96, add ONE low-VRAM card to the held
    `feat/qwen-image-21` pack (new card, not a change to the others). Note H3 GGUF presets ran 3-10x slower in our bake-off.
    **Four sources compared 2026-09-21 (metadata + hashes only, nothing downloaded or run):**
    (1) `realrebelai/Qwen-Image-2.1_GGUFs` - Q2..Q8 "HQv3" MIXED precision (attention + img_mlp.out kept at Q8, so Q4 is
    5.96 GB), converted from the Comfy-Org BF16 with native Comfy tensor names, author A/B'd against Comfy INT8; model only;
    no licence field on the card. FIRST CHOICE to test. (2) `abenzerps/Qwen-Image-2.1-GGUF` - plain Q4_0..Q8_0 (Q4_K_M
    4.60 GB), 33k downloads; ALSO hosts the encoder + VAE, byte-identical (sha256) to the Comfy-Org files we already pin.
    It is the SAME repo as yesterday's `...-Uncensored-GGUF` link (renamed; both URLs resolve to it) and its card says
    "original upstream base weights ... uncensored version in development": nothing about it is uncensored. Its card now
    links `leejet/ComfyUI-GGUF`, a 3-week-old 22-star fork. (3) `0xSojalSec/Qwen-Image-2.1-Uncensored-GGUF` - a day-old
    COPY of (2) under the old name: 4 of 5 files same sha256, the Q8_0 is the pre-re-upload one, card still points at
    abenzerps. Skip. (4) Civitai 2952547 (molbal) - Q4_0 4.10 GB, Q8_0 7.51 GB and an "int8" GGUF 7.09 GB + two workflows;
    recommends his own loader fork `molbal/ComfyUI-GGUF` ("reboot"). Open question for ALL of them: SimpliGen's engine has
    city96/ComfyUI-GGUF @6ea2651 (2026-01-12, lists arch `qwen_image`); two of four authors point at forks, which hints the
    stock loader may not take 2.1. Test the loader first. Saving is small: our INT8 is 7.26 GB, the 9.35 GB encoder dominates.
    **RUN 2026-09-21 17:10 in SimpliGen's engine (0.37.0), same graph/prompts/seeds, files sha256-verified then deleted:**
    realrebelai Q4 LOADS on the stock loader and matches INT8 on composition, lettering and a nude prompt, but takes
    35-38 s vs 12-13 s warm at the same ~10.5-11 GB peak VRAM. abenzerps Q4_K_M does NOT load ("Unknown model
    architecture", 7 of 7). Verdict: no GGUF card on a 12 GB card's account; only an 8 GB-GPU request would justify one, with
    realrebelai's file, after an edit-with-references test. Write-up: `F:\Claude-Work\qwen-image-21-test-20260920\gguf_ab\VERDICT.md`.
20. **Calliope (story-to-video studio) - LOW PRIORITY, no follow-up planned** (Michael 2026-09-20: "I don't know that we
    will follow up anytime soon"). https://github.com/benjiyaya/Calliope, MIT, 178 stars, 1.5.4 on 2026-09-18; read the
    README + example workflows only, nothing run. A standalone app (FastAPI + SvelteKit + an OpenAI-compatible LLM) that
    drives YOUR ComfyUI: idea -> beats/characters/locations -> per-scene script -> shot clips -> reference images ->
    one video per clip -> ffmpeg film export. NOT packable: it is an orchestrator, not a model or workflow; inside
    SimpliGen the nearest things are the UGC/Product studios and Recipes, and a full pipeline is an app feature for
    Sharmystic. Came up as a Discord request; close in spirit to aurangcool's "Music Video Studio" thread (his is
    song-driven, this is story-driven). Against SimpliGen's engine (node types only): the two Krea 2 workflows need
    nothing extra; the five H3 r2v examples miss only `VHS_VideoCombine`; the extend workflow also needs kat3ri's
    H3-Extend nodes; model filenames/folders differ (`minimax-h3\...`, an uncensored text encoder). Do NOT point it at
    SimpliGen's engine (bypasses the app, second client on one 31 GB machine); vanilla only if ever. Worth borrowing if
    we come back: its role-tag convention for discovering workflow inputs (`(Input:prompt)`, `(Output:video)`) and its
    LLM rewrite of a scene into the H3 six-section format with `<Subject N>` numbering tied to reference order.
21. **Music-video direction tools found on GitHub (Michael's search, checked 2026-09-20).** All six exist; three are live.
    - `guigulaoshi/music-video-director-skill` (53 stars, MIT, last push 2026-07): agent skill + `mvd` CLI that CUTS EXISTING
      FOOTAGE to a song (whisper/librosa/scenedetect -> edit decision list -> ffmpeg). Not installed: its setup edits the
      shell profile, pip-installs --user, assumes macOS/Linux paths, works in /tmp and burns a watermark into every
      render. Its ~220-line editorial knowledge base was the useful part: **DONE - adapted to generated shots in
      `C:\Users\micha\.agents\references\music-video-direction.md`** (section strategy, arc, lyric-to-image matching,
      shot grammar, beat-snapped cuts, colour, plus our own model/shot rules and a shot-list template).
    - `Blizaine/Maestro` (570 stars, active, **WanGP Non-Commercial licence**, installs via Pinokio): a full local studio
      on WanGP with a Director mode whose "Music Video" path analyses BPM/sections/energy, transcribes and diarises the
      vocal, plans shots on downbeats, makes consistent start frames and renders natively on MiniMax H3 (clips to 14.4 s),
      also LTX 2.5, Wan, YuE2. The closest existing thing to aurangcool's "Music Video Studio" request. Not installed: a
      second whole generation stack on a 12 GB / 31 GB machine. TRY LATER, only if we want to see how its planner
      decides shots; worth mentioning to people who ask for an automated studio.
    - `nebrass/hve-video-director` (105 stars, MIT, active): product/explainer videos as HyperFrames motion graphics for
      Claude Code, six human-approved phases. Not music video; overlaps the HyperFrames skills already installed.
    - Skip: `seme-org/open-director` (quiet since 2026-05), `sheagryphon/Gemini-Music-Video-Director-AI` (no licence,
      two days in 2025), `fresh-creations/tammy` (dead since 2023).
    NEXT, if we make another music video: fill the reference's shot-list template BEFORE rendering, and try the 2-second
    energy map (librosa) alongside the existing demucs + whisperx lyric timing.
22. **Music Video Chain: how often does a SEED push in?** (Michael 2026-09-21: "a little later".) On 2026-09-20 one of three
    same-seed 4-clip renders drifted into an extreme face close-up; on 2026-09-21 (engine 0.37.0, Reduce system RAM usage
    on) two same-seed renders were bit-identical and held their framing, so repeats are now pointless. Run 3-5 DIFFERENT
    seeds of the 4-clip card (13 min each, `pushin-check-20260921/run3.py` with the clip seeds changed), judge framing from
    a frame strip (the head-width proxy misreads the bobbed-hair singer). If some seeds drift: test a framing lock in the
    prompt, and say "re-roll the seed" in the card text. Also unresolved: which change made renders reproducible.
    **RUN 2026-09-21 22:20:** seeds 101/202/303/404 on the original 4-clip graph (`seed-test-20260921/seeds.py`,
    `strips_all.jpg`): seed 101 pushes in (head-and-shoulders -> face fills the frame by 26.5 s, gradual over clips
    3-4); 202, 303 and 404 hold. Counting yesterday's drifting control, 2 of 6 distinct seeds drift: about one in three.
    DONE (a) 22:42: a camera_lock paragraph in the header did NOT stop seed 101 - same creep, frame for frame. The drift is in
    the seed, not the wording. Remaining: (b) card text "if the shot creeps in, generate again with a new seed", and fix the
    prompt-split regex that cuts the header at any "[Shot 1]" mention (see memory), both in a 1.0.2. Was: (a) test a framing lock ("the camera does not move; the framing stays exactly as in the first
    second") on seed 101; (b) add "if the shot creeps in, re-roll the seed" to the three cards' text (1.0.2, text only).
23. **H3 Planner node suite (AI Jigyasa, YouTube PwV9Hvtr7EA, watched as transcript 2026-09-26).** 12 nodes on the Comfy
    registry ("H3 Planner", free; the ready workflow is a paid $4 extra). For LONG MULTI-CUT music videos on 8-12 GB cards:
    an LLM (Ollama Qwen3-VL 8B or an API) or a no-LLM slicer splits one long H3 prompt / an idea into ~6 s segments that all
    repeat the same subject definitions; librosa beat map puts cuts on the beat; per-segment slices of the song; draft pass
    (~0.5 MP) then final (latent upscale + refine); a "vault" tracks pending/done/locked segments with auto-advance, redo and
    range runs; ffmpeg stitches with the song or the clips' own audio. Segments are HARD CUTS, not continuations (no tail or
    latent hand-off), so it is the opposite trade to our Clip Chaining / MV Chain (one continuous take). Tested up to 3-4 min
    by the author. Not packable as a SimpliGen card (interactive timeline/vault UI, LLM step). Nearest SimpliGen equivalent
    would be a Recipe that fans one brief out into N card jobs. Only try if Michael wants long multi-cut videos.
    Side find: he runs a ~12 GB "W4A8 mixed" pruned H3 ref2va (vs our 21 GB int8). Not a Comfy-Org file; community builds
    exist (HF `koongrizzly/MiniMax_H3_int4_W4A8_ConvRot_Pruned`, `AX1Y2JP/MiniMax-H3-W4A8-ConvRot`,
    `cicalooo/MiniMax-H3-hybrid-b45-49-rtx3090-w4a8-int8`). Unchecked: licence, loader support in engine 0.37, quality and
    speed vs int8. Could ease the 31 GB RAM pressure behind the checkpoint-swap stalls.
24. **Songssx/ComfyUI-MiniMaxH3-TimelineDirector - HIGH PRIORITY to test (found 2026-09-26).** GitHub, GPL-3.0, 486 stars,
    main @ a81f13b (2026-09-22, v0.7+). Demo video: Smart Bobo, YouTube 0h1BK0h3NQY (35 s single-take shots, 8 min at
    1280x720 / ~10 min at ~1 MP on a 4090 24 GB, int8 + one accel LoRA, 8 steps). What it does in ONE execution:
    N overlapping segments of one continuous take, each started from the previous segment's AV-LATENT tail (no VAE round
    trip), "Drift-Control" masking (re-noises only the disposable prefix; adapted from ethanfel/ComfyUI-MiniMaxH3-Contex-Loop,
    GPL-3.0), "Soft AV" audio overlap, overlap trim + final AV assembly; per-segment prompts and per-segment reference
    images; "Locked Original Audio" slices an uploaded song/voice onto the timeline through the native AV mask/sigma path
    (lip sync stays audio-driven, the soundtrack is the untouched original); bundled SelfLift two-stage sampling (e.g. 6
    low-res steps + H3 latent upscaler + 2 high-res steps). Overlaps align down to H3's grid (24 -> 22, 48 -> 39), so the
    finished video is shorter than the sum of segments (4 x 10 s -> 35 s); write prompts knowing the overlap repeats.
    WHY IT MATTERS: it is ideas 2d (multi-hop latent chain in ONE workflow) and 2a (audio-locked singing/lip sync) already
    built, plus a drift fix we never had. It could supersede the MV Chain pack and extend Clip Chaining past 2 segments.
    OPEN QUESTIONS before any card: (1) the Material Planner is an interactive timeline widget whose state is saved in the
    workflow JSON; can a card drive a FIXED plan with {{placeholders}} for media/prompts, or via the split native-loop nodes
    (Initialize/Select/Plan Encoder/Prepare/Accumulate/Finish)? (2) two-stage needs an H3 latent-upscaler checkpoint; the
    LBH-123-AI upscaler we have in vanilla has NO LICENCE (not shippable), so a card would use one-stage unless a licensed
    upscaler exists; (3) VRAM/RAM on 12 GB / 31 GB at 480p. First test: vanilla ComfyUI, one-stage, 3 x 8 s at 480p with one
    reference image, then locked-song singing; compare the joins and drift with MV Chain on the same song.
    **TESTED 2026-09-26 (vanilla, one-stage, 864x480, 8-step ref2v turbo): it works on 12 GB.** 3x8 s take 680 s, joins
    invisible; 4x8 s locked-song singing 27.1 s in ~14-15 min, soundtrack = the original song (0.994). Reference pictures
    are centre-cropped to the output shape by the planner (portrait in 16:9 -> eyes cut off): pad them. Lip metric falls
    per segment in both runs (0.77->0.46 / 0.44->0.28), confounded with song content. Next: (a) Michael watches
    `F:\Claude-Work\timelinedirector-test-20260926\B2_sing_4x8_locked_169ref.mp4`; (b) control for the lip decline;
    (c) fair A/B vs MV Chain with the same singer; (d) card design (JSON plan from placeholders + auto-padding).
    **(a) DONE 23:49: Michael watched B2 - "the lipsync was perfect, I didn't notice any joins".** The metric's per-segment
    decline is not visible; (b) is dropped unless a later render shows a problem. Card design (d) is the next step.
    Details: that folder's VERDICT.md.

### From Michael's Recall saves (triaged 2026-10-02)
Source: app.recall.it/items, read through webcmd. Only H3 / Qwen-Image 2.1 / current-pipeline items that were not
already in TOOLING-STATE, memory or this file; older or off-topic saves (TTS lists, Wan 1.3B, FLUX/SDXL LoRAs) left out.
Titles are as saved; open the Recall item for the link.

25. **HyperFlow 8-step H3 LoRA (Video Rebirth).** GitHub `Video-Rebirth/hyperflow`, HF `videorebirth/hyperflow`; built
    for the diffusers Modular Pipeline, so first check whether the LoRA loads in ComfyUI core. If it does, bake it against
    DaSiWa and TaoMate on 3 seeds x 2 prompts (sampler time, not wall clock). Highest-value H3 item here.
    **TESTED 2026-10-02 (vanilla, t2v, pruned fl2va int8, 480p 5 s, seeds 4242/5151/6262 x bake prompts).** Not a plain
    LoRA (two-time embedder our pruned bases lack); tried the plain-LoRA conversion (core nodes + ManualSigmas) and the
    Adudeguyman node with curve refit. Same cost as PDD Acc (~102-106 s vs 107 s; TaoMate 51 s), so no speed win. On
    frames, both held "camera locked off" 3/3 and tracked coherently 3/3, where PDD pushed in 3/3 and jumped 2/3. The node
    route crashes when run right after a PDD render (PDD's leftover final-layer patch); the plain-LoRA route does not.
    Michael watched pdd vs hfA (p2motion 5151): "pretty much the same except the pdd one had the turn in the middle".
    IN THE APP (test pack hyperflow-test-pack, same day): t2v 3 seeds 90-96 s (PDD Acc in-app 91 s), all coherent;
    i2v works (picture via referenceImages). Audio not listened to. Next: decide the card's home (new card beside PDD
    Acc), r2v on the ref2va base, then remove the test pack.
    Possible outcome: a core-nodes-only "HyperFlow 8-Step" card as a steadier alternative to PDD Acc.
    `F:\Claude-Work\hyperflow-test-20261002\VERDICT.md`.
26. **Qwen 2.1 Frame-Lock LoRA** (Wildminder tweet): pins edits to the original frame so nothing shifts. Directly targets
    the edit drift we fought on Ming mask-back; A/B on our Edit / Fast Edit cards with the same inputs.
    **TESTED 2026-10-02:** it is ausboss/Qwen-Image-2.1-Consistency-LoRA (step 1500, 159 MB, Qwen Research License).
    Shipped Edit card, 3 sources x 7 edits x 2 seeds: restyle drift median 44 px -> 5 px, local and head-turn edits
    pixel-locked (0.1 px), look unchanged, +32% time; it still turned the head. 2- and 4-picture edits also passed
    (all pictures placed, no extra time). SHIPPED as the "Qwen Image 2.1 Edit (Steady Frame)" card, Qwen pack 1.8.0.
    `F:\Claude-Work\qwen-drift-test-20261002\VERDICT.md`.
27. **AnyAngle LoRA for Qwen-Image 2.1** (R@aiaicreate tweet): changes the camera angle while keeping the style. Possible
    new Qwen card; compare with the Character Sheet card's head angles.
    **READ 2026-10-02, PARKED:** lilylilith/QI_2.1_AnyAngle needs a coarse render from the target angle as picture 2,
    made via a Gaussian splat / 3D model + Blender. Untested shortcut: an H3 orbit-clip frame as that render.
28. **Qwen 2.1 pixel-drift fix nodes** (R@aiaicreate tweet): two ComfyUI nodes, a plain re-alignment and one with colour
    correction + mask. Same problem as 26; check whether they are core-node-only or need a custom pack.
    **TESTED 2026-10-02 (AusBoss Realign to Source, MIT, no deps):** lines a drifted edit back up, but big restyle drifts
    leave stretched edge strips (up to 7%). The LoRA (26) avoids the drift instead; Realign stays a fallback.
29. **Qwen-Image 2.1 PE "Pocket" 2B and 0.8B** (HF `ML-Intern-lab/Qwen-Image-2.1-PE-T2I-Pocket-2B` / `-0.8B`): small
    versions of the official prompt enhancer. Changes the 2026-10-02 verdict on the PE (9B was too slow at 12 GB); a 2B
    in core Generate Text might be fast enough for a "write the prompt for me" Qwen card. Needs a with/without-PE image A/B.
30. **ComfyUI-SongLRC** (GitHub `TheAwaken1/ComfyUI-SongLRC`): timed .lrc lyrics from YuE2 / MiniMax Music 3 output.
    Compare with our demucs + whisperx lyric timing (lyric-video pipeline); could replace that step or become a card output.
31. **Other Qwen 2.1 add-ons:** Outpaint LoRA (Linoy Tsaban tweet), Relight Space (`linoyts`), Felldude `QWEN_2.1_HDR_VAE`,
    Ollin Boer Bohan's two Qwen 2.1 autoencoder variants (tweet; likely a tiny preview VAE), anime2real-2511 Qwen LoRA +
    the civitai "Anime to Real: 10 workflows compared" guide, NSFW Qwen 2.1 LoRA (civitai), uncensored Qwen 2.1 roundups
    (AI少年, Md Ismail tweets) plus the Heretic creator's PSA against heretic models as text encoders (Reddit; read before
    trying any). Index: GitHub `wildminder/awesome-qwen-image`.
32. **Other H3 add-ons:** BUNNY Motion Repair LoRA V2 (Stable Diffusion Tutorials tweet), "best H3 LoRA for high-action
    scenes" (AI Search tweet), AI Search's roundup (upscaler, head swap, style transfer), Ai-Hakase's "H3 as uncensored
    image editor" workflow, astropuzzo `ComfyUI-MiniMax-H3-Image-Studio`, Simply Advanced H3 workflows v1.5.3 (civitai).
    Index: GitHub `wildminder/awesome-minimax-H3`.
33. **H3 prompting reading** (feeds the minimax-h3-prompt skill, not cards): PromptSama "MiniMax H3 Prompting Field
    Guide", instasd "MiniMax H3 Claude Skill" and "H3 Text Encoders in ComfyUI: Files, VRAM, Myths", "How I write motion
    graphics prompts for MiniMax H3 Max", Reddit "Most important tip I've learned so far with MiniMax-H3", Reddit
    "turbo / fast / sla attention - best current method".
34. **Unread link-only saves:** toyxyz tweet, two R@aiaicreate tweets that are only a t.co link, a Matt Jaynes reply to
    @blizaine, an "Untitled" X post, a bare Reddit link, "You no longer need Grok Imagine" (Reddit). Open and sort.
35. **ethanfel/ComfyUI-MiniMaxH3-Context-Loop - check for usable updates** (Michael, 2026-10-02). GPL-3.0; the
    TimelineDirector node (item 24) adapted its "Drift-Control" masking from it. When there is time: read its commits
    since 2026-09-22 and see whether anything (drift control, loop/continuation nodes) improves Clip Chaining, MV Chain
    or a future TimelineDirector card. Not cloned yet.

### From the H3 preset test session (2026-10-09)

36. **10Eros + Semantic Bridge + Ultimate Upscale two-stage workflow** (Michael, 2026-10-09). A text/image-to-video
    graph by Wilderness_19 (v1.0, 2026-09-07) aimed at 8 GB cards. Stage 1: 10Eros TURBO-hybrid at 0.3-0.4 MP,
    6 steps, euler/simple, no extra speed LoRA. Semantic Bridge: an ~11 MB conditioning adapter blended into the H3
    text conditioning (alpha 0.10, per_token), claimed to tighten prompt structure. Stage 2: MMH3 Ultimate Upscale
    with the official H3 3D latent upscaler, tiled, denoise 0.18, to about 0.9 MP.
    Why: two questions from today's test. (a) Does the Semantic Bridge improve prompt-following on prose the way
    the structured rewrite did (same seed, 480p, 15 s snow-globe prompt, results in
    `F:\Claude-Work\h3-preset-test-20261009\`)? (b) Does low-res-then-latent-upscale get a 15 s clip to 768p-class
    output on the 12 GB card without the RAM stall the 1344x768 15 s Midnight run hit? Compare with our own
    Two-Stage Latent Upscale card before assuming it is new.
    Cost: two third-party custom nodes, neither reviewed: `bbaudio-2025/Comfyui-MMH3-UltimateUpscale` (GitHub) and
    the Semantic Bridge node, which ships as a zip on Hugging Face (`speach1sdef178/MiniMax-H3-Semantic-Bridge`,
    not in ComfyUI-Manager). Small weights (bridge ~11 MB, latent upscaler from `LBH-123-AI/Minimax_h3_latent_Upscaler`);
    the workflow names a 10Eros beta3 skip-edges INT8 file we do not have, so try our beta5 TURBO first. Vanilla
    ComfyUI only, not SimpliGen's engine. Nothing downloaded or installed yet.
    Source: https://civitai.com/models/2920367 (Michael's link was the civitai.red mirror of the same page).

### From foxydits' H3 Seed Hunter workflow (2026-10-10)
Source: https://www.youtube.com/watch?v=H8JSzhkOmXA, https://civitai.com/models/2881362 (v2.5.1). Same latent
upscaler node and weights as our Two-Stage and Refine packs (checked 2026-10-10); only the recipe around it differs.

37. **Pick-a-preview before the upscale ("seed hunting").** The workflow renders up to three small first-pass clips,
    the user picks one, and only that one goes through the latent upscale. A SimpliGen card cannot pause for a
    choice, so the in-app version is two cards: a "Two-Stage Preview" card that runs ONLY stage 1 of the Two-Stage
    graph (same model, steps, sampler and small size) and decodes it, then the existing Two-Stage card run with the
    seed of the preview the user liked. Same seed + same stage-1 settings should rebuild the same small clip, so the
    upscale lands on the clip that was picked.
    Why: on Two-Stage a bad seed costs the whole run (248-351 s at 768p, measured 2026-09-02). A preview costs only
    stage 1 plus a small decode.
    What decides whether it is worth building (measure FIRST, no build needed, read the two sampler times from one
    Two-Stage log): the share of the run that stage 1 takes. Stage 1 is paid again on the final run, so with three
    previews the cost is 4x stage 1 + 1x stage 2, against 3x (stage 1 + stage 2) for three full runs. If stage 1 is
    a quarter of the run this saves about a third; if stage 1 is half or more it saves little or nothing, and the
    answer is "just run Two-Stage three times".
    Second check: that the same seed really reproduces stage 1 across the two cards (3 seeds, compare the preview
    with a stage-1 decode from the full card; image-to-video and reference cards included, attention options equal).
    Not the route: Preview -> Refine card. Refine starts from the decoded video file, not the kept latent, so it is a
    different (already shipped) thing. A Recipe/flow has the same limit, it passes files between presets.
    Cost: one new workflow per mode (the Two-Stage graph cut after stage 1), no new weights or nodes. Half a day
    with the 3-seed in-app check. Lower-cost variant if it measures well: text-to-video only.

### T3-Video: native 4K text-to-video on Wan (watch, 2026-10-12)
Source: https://huggingface.co/APRIL-AIGC/T3-Video, code https://github.com/zhangzjn/T3-Video, paper
https://arxiv.org/abs/2512.13492 (ICML 2026). Read only on 2026-10-12; nothing downloaded or run.

38. **Watch for a ComfyUI port, then test whether 4K (or a smaller size) runs on 12 GB.** T3-Video retrains a Wan
    model with a changed attention pattern (multi-scale window attention) so it generates 3840x2176 directly; the
    paper claims more than 10x faster 4K generation than full attention. Two Apache-2.0 text-to-video weights, not
    gated: `T3-Video-Wan2.1-T2V-1.3B.safetensors` (2.8 GB) and `T3-Video-Wan2.2-T2V-5B.safetensors` (10.0 GB), HF
    commit b38f51b5. 81 frames, 50 steps, no audio.
    Why it is parked: the speed-up lives in the authors' modified DiffSynth-Studio code, so the weights alone in a
    stock Wan graph would not reproduce it; there is no ComfyUI node (repo issue #4 "ComfyUI native implementation?"
    is open and unanswered); the only inference script is `infer_multi_gpu.py` and the README gives no VRAM or
    timing figures; training code is not released; no image-to-video weights despite the tag.
    Trigger to pick it up: a ComfyUI port, or a reply on issue #4. First test then: the 1.3B file at a reduced size
    in the isolated `Projects\ComfyUI-v0.39`, VRAM and time measured, before attempting 4K (the 4K VAE decode alone
    may not fit 12 GB; that is an estimate, not a measurement).
    Cost now: none. Cost to try the authors' script directly: a separate environment plus the Wan base weights, with
    a real chance of ending at out-of-memory.

### MOSS-Image SFT (OpenMOSS text-to-image, TESTED in vanilla 2026-10-17)
Sources Michael sent: https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT,
https://huggingface.co/Abiray/MOSS-Image-SFT-INT8-convrot, https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd.
- What it is: 5B DiT, Qwen3.5 9B text encoder, FLUX.2 VAE (same file as our `flux2-vae.safetensors`). Apache-2.0.
  Strengths claimed: rendered text (English and Chinese), tag or prose prompts, and JSON layout prompts with bounding
  boxes. Stock settings 50 steps, CFG 3, shift 5, Euler/sgm_uniform, SLG on the negative branch at layer 22.
- Weights: use **Comfy-Org/MOSS-Image** (per the Comfy-Org-first rule): `moss_image_sft_int8_convrot` 5.41 GB +
  `qwen3.5_9b_int8_convrot` 9.75 GB (or `w4a8_gptq` 7.34 GB). Abiray's int8 files are the same idea, third party.
- ComfyUI: core support merged on master 2026-10-16 (Comfy-Org/ComfyUI#17095, e087d8f6, + #17099), NOT in any release
  yet (v0.41.0 predates it; SimpliGen engine is 0.41.1). The `moss-image` registry node CANNOT load the Comfy-Org
  files (it expects separate q/k/v, Comfy-Org fuses them), so a store card waits for a ComfyUI release with native
  support, or Sharmystic may take the stock model as official (as with Klein).
- 8-step DMD (lodestones): WIP, update 2600 of 12000, author says "probably overcooked, lower the lora weights". Also
  new: toxicdog SFT-Turbo int8, darask0 4-step adapter LoRA, Kijai SFT-as-LoRA extracts (untested).
- **Result 2026-10-17** (vanilla master 5cc4b870, 4 prompts x 3 seeds, 1024², judged by Claude only):
  stock 50 steps 28.5 s; Kijai's 25-step graph (er_sde, CFG 2.5, SLG to 50%) 15.5 s with stock-level skin; DMD LoRA
  1.0 at 8 steps 4.9 s and 0.7 at 12 steps 5.7 s, composition and text hold but skin is smoothed (matches REBEL AI's
  video). Chinese handwriting exact on every MOSS arm incl. 8-step; Klein garbled it. Graph gotcha: no
  ModelSamplingSD3 (multiplier 1000 gives pure noise). Untested: layout/bbox prompts, anime, other sizes, w4a8 TE.
  Card idea when the engine supports it: a 25-step quality card plus a DMD fast card; text-heavy and Chinese text
  are its edge over Klein. `F:\Claude-Work\moss-image-test-20261016\VERDICT.md`.
- **ENGINE 2026-10-18**: the app's beta engine (ComfyUI master c06bf5f5) has native MOSS; the vanilla graphs give
  pixel-identical images there (36/36). Engine adds ~5 s per changed prompt (9.3 GB TE and DiT evict each other on
  12 GB; same prompt + new seed = 2.7 s): try the `qwen3.5_9b_w4a8_gptq` TE before building a card. lodestones' Base
  8-step DMD LoRA (update 12000, also the Civitai "Moss Image Turbo LoRAs" Base file, same sha256) on MOSS Base int8
  is WORSE than SFT + SFT LoRA (flat hazy light, red lighthouse came out white 3/3); on SFT it looks the same as the
  2600 LoRA. Keep SFT + SFT LoRA. `F:\Claude-Work\moss-image-engine-20261018\VERDICT.md`.
- **LOCAL TEST CARDS 2026-10-18** (`test-moss-image-pack`, not in the repo): Fast (DMD LoRA, 8 steps) and 25-step (Kijai
  SLG graph), both on the w4a8 TE (cuts the changed-prompt reload from ~10 to ~6 s on the engine, text holds). App route
  pixel-identical to the engine; ~9.5 s per new prompt in-app; Japanese menu text exact. Open: `supportsLoras` false,
  3:2/2:3 sizes just added. Civitai has a burst of MOSS LoRAs (styles, DeBand banding fix, DaSkin skin) to try on it.
  `F:\Claude-Work\moss-image-card-20261018\VERDICT.md`.
- **DeBand / DaSkin 2026-10-18**: MatlowAI's DeBand Main (.diff, SFT layers 37-41 -> Base, core LoraLoaderModelOnly,
  no time cost) only fades the faint vertical stripes on the 25-step card and does nothing visible on the Fast card;
  on our prompts the stripes show only with colour x5, so not added. Retest with both fixes (Quality+) on wide sky
  pictures. DaSkin is Civitai paid access (403), untested. `F:\Claude-Work\moss-deband-20261018\VERDICT.md`.

### FLUX 3 Image Klein variants (stock model goes official via Sharmystic; we wait for fine-tunes, 2026-10-15)
Sources: https://blog.comfy.org/p/flux-3-image-klein-in-comfyui-56b, weights
https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy (HF commit 8c99a01a), code
https://github.com/black-forest-labs/flux-3-image-klein. Read only on 2026-10-15; nothing downloaded or run.

39. **Community pack for FLUX 3 Image Klein: text-to-image plus editing with up to 10 references.** 5.6B DiT,
    Qwen3-VL-4B text encoder, the Flux 2 VAE. Two models: Klein (distilled, 16 steps, no CFG, the one to ship) and
    Klein Base (50 steps, guidance 3.5, for training). Comfy files: `flux3_image_klein_sd_int8_convrot` (5.83 GB,
    distilled) and `flux3_image_klein_int8_convrot` (5.81 GB, base), bf16 (~11.1 GB) and NVFP4 (~5.3 GB) of each,
    `qwen3vl_4b_int8_convrot` (4.86 GB) or bf16 (8.88 GB), `flux2-vae` (0.34 GB), optional prompt upsampler
    `qwen3.5_9b_flux3_prompt_upsampler_int8_convrot` (9.75 GB). Four official workflows in the repo's `workflows/`
    (t2i and image edit, base and distilled). BFL says the int8 files run on 8 GB GPUs; Comfy's blog quotes under
    9 s at 1024x1024 on an RTX 4070 for int8 + distilled. Also does bounding boxes in the prompt (JSON list of
    `{"id", "desc", "bbox": [x0, y0, x1, y1]}` on a 0-1 scale; edits use `from`/`src_bbox`/`tgt_bbox`) and native 4K.
    Why it is parked: ComfyUI added support on master on 2026-10-15 (commit 20b46065, "Support Flux3-image"), after
    the v0.40.0 release; the SimpliGen engine is on 0.38.0 and has no Flux 3 code. BFL's own CLI needs 25-31 GB of
    VRAM, so it is not a 12 GB route. Michael said not to update vanilla ComfyUI for this.
    Also: the HF repo is gated (users need an HF token in Settings after accepting the licence, see
    gated-hf-download memory) and the weights are under the FLUX Kommunity License (non-commercial, with a
    commercial-output exception for Qualifying Users); say both on the card.
    Trigger to pick it up: an engine release that contains commit 20b46065. Asked Sharmystic on 2026-10-15
    (`F:\Claude-Work\flux3-klein-20261015\sharmystic-flux3-engine.md`). Check first whether the official store
    already carries it, so the community pack does not duplicate an official one.
    First test then: distilled int8 + qwen3vl int8 t2i and one 2-reference edit in the app, 3 seeds each; check
    whether our Krea 2 `qwen3vl_4b_fp8_scaled` encoder is the same model (it would save a 4.9 GB download).
    UPDATE 2026-10-15, vanilla test (ComfyUI master 29e28e2b, 4070 Ti, `--lowvram`): distilled int8 + qwen3vl int8
    runs at 3.8-5.2 s per 1024x1024 and ~21 s at 2048x2048 (clean at native pixels). Lettering exact on 2 of 2
    seeds; a sign-text edit and a night-plus-scarf edit kept everything else; a 2-reference composite kept the
    character but not the requested style on the background. The `flux2-vae.safetensors` SimpliGen already ships
    gives pixel-identical output to BFL's, so the pack reuses it. Edit graph = `ReferenceMultiLatent` (resize to
    1 MP) feeding the KSampler's positive, negative and latent. Scripts and images:
    `F:\Claude-Work\flux3-klein-20261015\`. Still untested: bounding boxes, the prompt upsampler, the base model.
    DECISION 2026-10-15 (Michael): Sharmystic is updating the engine and has an OFFICIAL Flux 3 Klein pack ready,
    so we do NOT build a community pack of the stock model. Our job is the variants: community fine-tunes and
    LoRAs of Flux 3 Klein as they appear on Civitai/HF, built on top of the official pack's stack once it ships
    (check its file names and workflow first, and reuse its encoder/VAE ids so users download nothing twice).
    RENAMED UPSTREAM 2026-10-17 (HF main feef60b0, with ComfyUI v0.41.3's reworked templates): the old
    `flux3_image_klein_sd_*` (distilled) is now `flux3-image-klein-*`, and the old `flux3_image_klein_*` (BASE) is now
    `flux3-image-klein-base-*`. TRAP: old base `flux3_image_klein_int8_convrot` looks like new DISTILLED
    `flux3-image-klein-int8-convrot`; never map by name. Old names are gone from main, so URLs must stay pinned to
    8c99a01a (official pack 1.9.0 and our test outpaint card both are). New upstream defaults: distilled 16 steps,
    base 50 steps (pack 1.9.0: 15/16 and 25), prompt upsampler on in every template, now also a w4a8 file
    (`qwen3.5_9b_flux3_prompt_upsampler_w4a8`, ~7 GB). Upsampler on 12 GB and its effect on anatomy still untested;
    the official pack's steps and upsampler are Sharmystic's call. When he renames, re-point variant cards to his ids.
    OFFICIAL UPDATE 2026-10-18 (Sharmystic's @everyone): distilled 16 steps, Base 50, BFL's prompt upsampler built in
    (6.7 GB, runs before every image, reads edit references; no off switch yet), the model's own reference timestep
    shift instead of a resolution-derived one, and the 2 MP / 4 MP / 4K size picker is back (the duplicated anatomy was
    the old step counts + no upsampler, not the resolution). CONSEQUENCES FOR US: every Klein result in this file and
    in the MOSS poster comparison ("Klein garbled the Chinese") was made on the OLD settings; re-test before quoting it.
    Our test outpaint card and the 4-step LoRA idea need re-checking on the new graph (shift + upsampler), and check
    whether the update moved to BFL's renamed files before reusing his ids.
    OFFICIAL PACK 1.8.0 (2026-10-16, with app 1.75.0): the edit cards now size the output themselves. The latent is
    `EmptyFlux2LatentImage({{width}}, {{height}})`, and Flux2Scheduler uses the same size. Before, the latent was
    ReferenceMultiLatent's empty_latent, so the output followed the reference. References are resized on their own
    by `ReferenceMultiLatent` "resize" at `{{reference_megapixels}}` (image default 1, control 0.5-2 step 0.25).
    Sizes come from `image.resolutionOptions`: three tiers, 1 MP (minVramGB 8), 2 MP (12) and 4 MP (16), each with
    1:1, 16:9, 9:16, 4:3, 3:4 and 21:9 sizes (2 MP 1:1 = 1440x1440, 4 MP 16:9 = 2720x1536), with
    `defaultResolutionTier: 0`. Other controls: steps 8-20, cfg 1-2. Same weights and encoder/VAE ids as 1.7.0, and
    the t2i workflow is unchanged. Variant edit cards should copy this block and wiring. An outpaint card is the
    exception: its latent must match the padded canvas ("keep resolution" empty_latent), so it does not use the
    size tiers.
    APP TEST of the 1.8.0 Klein Edit card, 2026-10-16 (SimpliGen MCP, app 1.75.0, 4070 Ti 12 GB; images in
    `F:\SimpliGen\output\claude\flux3-klein-packflux3-klein-edit\`, sheet in `F:\Claude-Work\flux3-klein-edit-180-20261016\`).
    The agent route takes `options.resolution` = the tier label ("1 MP (native)", "2 MP", "4 MP") plus `aspectRatio`.
    Every output came back at exactly the chosen tier and aspect, confirmed in the engine graph: 1024x1024,
    1344x768, 1664x1248, 2720x1536. Job times: 16-18 s at 1 MP with one reference, 21 s at 1 MP 16:9 with two, 21 s
    at 2 MP, 51 s at 4 MP. The 4 MP tier says minVramGB 16, but it was accepted and finished cleanly on 12 GB (native crop sharp).
    Sign edit "SALT & CINDER" exact with the rest kept on 2 of 2 seeds. Two references into 16:9 (the anime girl in
    front of the bakery) worked on 2 of 2, but she stays anime in the photo, as in 1.7.0. Watch out: a shape
    different from the reference (1:1 anime picture -> 2 MP 4:3) makes the edit RECOMPOSE the scene (closer
    framing). Night + beanie were applied, but the falling snow was lost despite "everything else unchanged". For a
    faithful edit, keep the reference's own shape. One seed for the 2 MP and 4 MP runs.
    CANDIDATE 2026-10-16: https://huggingface.co/Muinez/flux3-klein-distil-4step (HF commit 56905ed), a 169 MB
    4-step distill LoRA for Klein BASE, not for the distilled Klein. Read only; nothing downloaded or run. The
    author calls it experimental and briefly trained. Settings from the card: 4 steps (2-3 also work), CFG 1, no
    negative prompt, euler/simple, LoRA 1.0 via LoraLoaderModelOnly, ModelSamplingFlux with max_shift = base_shift
    = 1.0986 (ln 3, so resolution stops mattering), trained at 1024x1024. FLUX Kommunity License like the base.
    Why it matters: stock distilled Klein already does 16 steps in ~4-5 s here, so speed alone is a small gain.
    The use is base-model fine-tunes and LoRAs trained on Klein Base: stacked with this LoRA they could run at 4
    steps instead of base's 50 with guidance 3.5. First test once the official pack ships: base int8 + this LoRA
    vs stock distilled, same 3 seeds and prompts (lettering, a face, a busy scene), then the same with one
    base-trained style LoRA stacked on top to see whether the two LoRAs fight.
    TESTED 2026-10-16 on the SimpliGen engine (8199, direct graphs, official pack 1.7.0 int8 weights), 1024x1024,
    4 prompts (fox, bakery sign, anime girl, Michael's castle) x 3 seeds x 6 arms, judged by Claude from sheets plus
    one native-pixel image. Median execution times: Klein card (15 steps) 3.9 s, Base card (25 steps, CFG 3.5)
    11.3 s, Base + LoRA 4 steps 1.6 s, Klein 4 steps with or without LoRA 1.4 s.
    - Base + LoRA works: clean on 12 of 12, lettering exact on 3 of 3 sign seeds ("FLOUR & EMBER", "Fresh sourdough
      7am"), anime linework clean, about 7x faster than the Base card. It looks more saturated and contrasty than
      the Base card, and seed variety is lower (the three fox seeds are near-identical poses; castles all frontal
      and symmetric).
    - Base at 4 steps WITHOUT the LoRA is grey fog on 12 of 12, so the LoRA is doing the work.
    - The LoRA on the DISTILLED Klein overcooks: gritty, over-busy, double signs and a stray glyph in the sign
      ("FLOUR&EMBER|"). Do not use it there. Plain Klein at 4 steps with the LoRA's shift-ln3 schedule is already
      usable (slightly softer than its 15-step card), which is the cheaper speed route for the stock model.
    - The castle seed 3 drew a fake signature/logo bottom-left on BOTH Base arms (card and LoRA), so that comes
      from the base model, not the LoRA.
    - Untested: the app route, stacking a base-trained style LoRA on top, edit cards. A card cannot use it through
      the app's LoRA slot alone: it needs its own workflow (ModelSamplingFlux 1.0986/1.0986 + BasicScheduler
      simple, 4 steps, CFG 1). Files: `F:\Claude-Work\flux3-klein-4step-lora-20261016\` (run.py, sheet.py, sheets);
      the LoRA is in `F:\SimpliGen\models\loras\`.
    CANDIDATE + TESTED 2026-10-16: ausboss Outpaint LoRA, https://huggingface.co/ausboss/FLUX-3-Image-Klein-Outpaint-LoRA
    (161 MB, rank 32, trained on Base, used on the distilled Klein at strength 1.5, FLUX Kommunity License). Pad the
    picture with flat #808080, give the padded canvas as the reference (ReferenceMultiLatent, keep resolution, no
    noise mask), 16 steps CFG 1 euler/simple, ConditioningZeroOut negative, then paste the original back. Prompt
    trigger first: "Outpaint the image: replace the solid gray areas with a seamless continuation of the scene,
    keeping the existing picture unchanged." then optional " Scene: <description of the picture>".
    The author's workflow needs AusBoss nodes (2.13.0+: Crop+Rotate+Pad, Crop for Inpaint, Stitch Inpaint with tone
    match, plus UI helpers). The SimpliGen engine has NO AusBoss nodes (vanilla has an old 2.5.2 copy), and nothing
    was installed. The sampling half is all core nodes; I did the padding, hand-written caption and a feathered
    paste-back in Python. Core ImagePadForOutpaint (0.5 grey fill + mask) and ImageCompositeMasked could probably
    replace the AusBoss pad/stitch in a card, untested; no tone match then.
    Test (bare engine 8199, distilled int8, 1024x1024, `F:\Claude-Work\flux3-outpaint-lora-20261016\`): 3 Klein
    renders with known continuations, greyed on the right 31% (castle), top+left 25% (bakery), both sides 19%
    (anime), LoRA 0 / 1.0 / 1.5 x seeds 3/1015/77. "Moved" = the kept part shifted or rescaled in the raw output
    (phase-correlation shift and kept-region PSNR under 20 dB). No LoRA moved on 3 of 9 (bakery 2, anime 1),
    1.0 on 2 of 9, 1.5 on 0 of 9. The castle (one-side pad) never moved, even without the LoRA, so the author's 36
    of 40 failure rate without it did not show on simple pads here. Continuations looked right at native pixels
    (platform roof posts, scarf ends, cliffs and waterfalls), seams invisible after the paste-back. ~8.5 s per
    image (the reference doubles the tokens) vs ~4 s for plain t2i.
    Gotcha: the bakery sign was half in the grey, and every arm rewrote it as gibberish ("FLOOR CF RIIO"), because
    my Scene caption did not give the words. Put any lettering that crosses the grey into the Scene text.
    Not tested: rotated pictures with grey corners, pads over 50%, real photos, the app route. A card would need
    pad controls (sides/amount or a target aspect); check whether the app has any outpaint/canvas input first.
    ALL-CORE-NODE GRAPH TESTED 2026-10-16 (`run_core.py`, same folder): LoadImage -> ImagePadForOutpaint (0.5
    grey, feathering 24) -> ReferenceMultiLatent -> KSampler (LoRA 1.5) -> VAEDecode -> ImageCompositeMasked
    (source = padded picture, mask = InvertMask(pad mask)). Runs on the engine as it is, no custom nodes. The 3
    repeat pads gave the same numbers as the Python pipeline (0 of 9 moved), and the in-graph paste-back left the
    kept pixels exactly as they were (max difference 0 away from the feather). With the words in the Scene text,
    the bakery sign came back as "FLOUR & EMBER". True extensions to 1536x1024 (castle +512 right, anime +256
    each side): 5 of 6 clean at about 15 s. FAIL on castle seed 3: the model re-centred the castle (212 px slide)
    instead of extending, and the paste-back then shows a hard seam with the castle drawn twice, the failure the
    author describes ("run it again with another seed"). A card has no way to retry by itself, so its description
    must say to change the seed when a seam or a double appears. Still untested: the app route.
    TILTED TESTED 2026-10-16 (`run_tilt.py`, `out_tilt\`): castle turned 8 deg, bakery -6, anime -11 on the same
    1024 canvas, grey corners, LoRA 0 vs 1.5 x 3 seeds. Core has no any-angle rotate node, so the turn was made in
    Python and saved as RGBA (alpha 0 over the grey, 16 px soft ramp); core LoadImage then hands the paste-back mask
    straight to ImageCompositeMasked. Moved (raw output): no LoRA 7 of 9, LoRA 1.5 2 of 9, both on the -6 deg bakery
    (seeds 3 and 77 reframed the shop). The castle and anime held on 6 of 6 with the LoRA. Those bakery corners are thin
    (about 50 px), so after the paste-back both moved runs still look clean at native pixels. Without the LoRA the
    big -11 deg corners show it: anime seed 3 has a diagonal seam where the rails break and do not line up; with the
    LoRA the rails run through. Fill time is the same as for pads (~8.5 s). A card that turns the picture itself
    would need a rotate node (AusBoss Crop+Rotate+Pad or another pack); a card that takes an already-turned RGBA
    picture would not.
    VERTICAL TESTED 2026-10-16 (`run_vert.py`, `out_vert\`, core graph, LoRA 1.5): anime 1024 +256 top +256 bottom
    and castle +512 bottom, both to 1024x1536, 3 seeds each. Held in place 6 of 6, and the seams are invisible at
    native pixels. Above the girl it adds the platform roof and lamp; below, her coat and scarf. Under the castle it
    continues the cliffs and waterfalls into cloud, but the bottom third gets darker and emptier than the picture
    (plausible, dull). ~15 s. The author's two documented misses (a big pad on top; 40% added under a seated person,
    who was redrawn lower with her knees twice) did not come up; no seated person was tested.
    TEST CARD BUILT 2026-10-16 (`F:\Claude-Work\flux3-outpaint-card-20261016\`: build_card.py, install_test_pack.py,
    engine_test.py; installed locally as pack `test-flux3-outpaint-pack`, card `test-flux3-klein-outpaint`, NOT in the
    repo). Michael's idea: an ANCHOR 1-9 laid out like a keypad (where the picture sits; 5 = centre) plus ZOOM OUT
    1.0-1.4, with the app's shape pill (1 MP sizes) as the canvas. The graph does the padding maths in
    ComfyMathExpression (fit, zoom out, floor at 45% coverage = the LoRA's training floor, multiples of 8, then
    ImageScale -> ImagePadForOutpaint), all core nodes plus the user LoRA slot. Gotcha: ComfyMathExpression's
    autogrow inputs must be named a, b, c... in order, or the graph fails validation ("values.a missing").
    Results: the placement maths is right for all 9 anchors (bare engine). Through the app (after a restart to load
    the pack), all placeholders were filled, including the slider defaults (5, 1.2) when they were left out, and the
    output was the canvas size, 15-20 s. 3 of 4 app results clean. On the 1:1 default the fill drew a wall where the
    picture shows a tree, and the 24 px feather left a ghost strip at native pixels.
    BIG LIMIT: adding space ABOVE a person draws a second head: 10 of 12 (anchors 7/8/9 and a 9:16 canvas, anime
    girl, seeds 3/1015/77) when the prompt only describes the picture. LoRA 1.0 instead of 1.5: still 3 of 3
    doubled. A prompt that says what fills the new space ("Only one person ... above her head there is only the
    roof, wires and sky; nothing else") cut it to 2 of 9. The card description tells users to write it that way,
    but it is not solved. Before any release: real photos, a person extended downward (seated), a fix for the
    top-extension doubling, and a look by Michael. Note to Sharmystic asking for a 3x3 anchor-picker control is
    drafted, unsent: `F:\Claude-Work\flux3-outpaint-card-20261016\sharmystic-anchor-grid-control.md`.
    DOUBLING FIXES TESTED 2026-10-16 (`doubling.py`, `engine_out\doubling\`, bare engine, card template): case A =
    9:16 anchor 8 (576 px on top), case B = 1:1 anchor 7 zoom 1.3, seeds 3/1015/77. Heads drawn twice, out of 6:
    plain caption (describes the girl) 6; plain + fixed guard sentence ("Every person appears exactly once... no
    extra people, heads or faces") 4; two passes of half the pad each, 1 head, but pass 2 drew the roof twice
    (offset) or left a dark band at the join on 2 of 3 in A; TRIGGER ONLY (empty Scene text) 1, with no new faults.
    So naming the person in the prompt is what makes the model draw them again. The card now says: leave the
    prompt empty, or describe only the surroundings, never the people. Feathering was not tested because it
    cannot help: ImagePadForOutpaint fills and places the picture the same way at any feather; feather only shapes
    the paste-back mask. Not yet tested: a surroundings-only prompt that does not name the person (the 7 of 9
    "guidance" caption still named her), and the 1 trigger-only miss (A seed 3, a partial head).
    REAL PHOTOS TESTED 2026-10-16 through the app (test card, EMPTY prompt, zoom 1.0, seeds 3/1015/77; Michael's
    own family scans in `C:\Users\micha\Pictures\real photos`, private, not to be committed; results in
    `F:\SimpliGen\output\claude\test-flux3-outpaint-packtest-flux3-klein-outpaint\` 00005-00019, sheets in
    `F:\Claude-Work\flux3-outpaint-real-20261016\`). Five photos: B&W woman and car -> 16:9 anchor 5; mother and boys
    SITTING on a rock -> 1:1 anchor 2 (adds below); three people cut at the waist -> 3:4 anchor 2 (adds legs); a
    couple cut at the knees -> 9:16 anchor 5 (adds 352 px above AND below); a porch group -> 1:1 anchor 5.
    13 of 15 usable, 0 doubled heads (including the 9:16 with space above two people), 0 double knees on the
    seated photo, and the waist seam is invisible at native pixels. The look matches old film: grain, fading, the
    colour cast. Faults: B&W seed 3 painted a blurred ghost figure and a bent arch on the left; couple seed 77 gave
    the woman stiff, mannequin-like legs and blob shoes. Minor: a pinker bottom on the rock photo seed 1015, and the
    scan's rounded white corners are kept as part of the picture. Legs, feet and clothes below the frame are
    invented and change per seed (trousers on one seed, a skirt on another), so the card should say so.

## Done / dropped

- **2026-10-01, LongLive-Plug 4-step LoRA for H3 (NVIDIA Efficient-Large-Model, Kijai conversion):** needs the lcm
  sampler (their scheduler re-noises with fresh noise each step) and sigmas 1.0, 0.973, 0.9231, 0.8, 0.0. Best of the
  four distills on seed 11, but over seeds 22/33/44 DaSiWa was sharper on every fisherman and better on one
  skateboarder, and TaoMate matched it ~12 s faster. DROPPED: no slot. Kit: F:\Claude-Work\pdmd-ab-20261001\.

- **2026-10-01, FlashGen 4-step LoRA for H3 (Beidouqixing, Kijai rank-13 conversion):** its model-card schedule
  [1.0, 0.7, 0.4, 0.15, 0.0] must be shift-12 converted for ComfyUI (1.0, 0.9655, 0.8889, 0.6792, 0.0) or the video
  smears. Clean once fixed; ~45 s sampling like PDMD, no ollie on the skateboarder, softer than DaSiWa, speech tied
  (Michael listened). DROPPED: no niche. Kit: F:\Claude-Work\pdmd-ab-20261001\.

- **2026-10-01, PDMD 4-step LoRA for H3 (pdmd2026, Kijai rank-57 conversion):** loads clean on the pruned fl2va base;
  T2V 1 seed x 3 prompts vs TaoMate 3-step and DaSiWa v1 4-step. Speech tied on all three (Michael listened), PDMD
  ~48 s sampling vs TaoMate ~36 s and DaSiWa ~60 s, weakest motion (no clear ollie) and less detail than DaSiWa.
  DROPPED: no niche. Kit: F:\Claude-Work\pdmd-ab-20261001\.

- **2026-09-22/23, M3_Unlocked_V2 LoRA on every H3 model (Shar's "Unlocked" cards):** same SFW prompt and seed, 480p,
  no LoRA vs 0.5, 11 models. Only Turbo Accelerated showed a real, pleasant variation at no time cost; it SHIPPED as an
  unlock slider (1.5.0, default 0, pixel-identical at 0). DaSiWa v1 reshuffled the scene and sexualised a background
  painting. SolAttn, Z-Image graft, SparseRef15, FastH3, 10Eros v1/beta5/beta5 Turbo, DaSiWa v2 and Singularity: near
  no-op (at most a changed painting, +0-16 s). Decision: add it nowhere else. Shar's sharper look was mostly his 768p
  default; at matched 768p DaSiWa won on hair. Untested: NSFW prompts, more seeds.
  `F:\Claude-Work\unlocked-lora-dasiwa-20260922\`.

- **2026-09-19, item 2 (singing):** BITB 9.5-24.58 s, lead close-up, stem + backing -14 dB, join mid-phrase.
  The pack's `digital_human` mode locks the supplied audio (output vs song waveform corr 0.976). Mouth-vs-vocal r:
  fresh clip +0.616, continuation after the join +0.573, single long generation +0.497/+0.340 (framed wider, so
  not a fair win). Chain 460 s = long 460 s; a 2 s context tail fixed the 4x continuation slowdown (item 1b DONE).
  Awaiting Michael's eyes. `F:\Claude-Work\satodive-singing-test-20260919\VERDICT.md`.

- **2026-09-19, item 1 (first pass) + item 4 (his nodes):** SatoDive pack @4142527 in vanilla ComfyUI, fisherman
  reference, 8 s clip + 10 s continuation. Both lines word-exact across the join, picture join corr 0.997, framing
  and identity carried, latent hand-off +0.3% luma vs -2.2% through pixels. Continuation ~4x slower. His
  `MiniMaxH3TurboLoRA` node did not apply the LoRA on our int8 base; stock loader used. Full write-up:
  `F:\Claude-Work\satodive-continuation-test-20260919\VERDICT.md`.

- **Qwen 2.1 Enhance to 4MP: note on textured backgrounds** (2026-09-24). In-app test on 1.65.1 (1344x768 edit output -> 2720x1536, info panel showed produced + requested sizes correctly) flattened the source's mottled paper grain to near-flat red while faces/armour improved. A one-line description warning ("smooths textured or grainy backgrounds") is a description-only 1.5.2 patch; deliberately NOT shipped unless a user reports it, to avoid an update badge for one sentence. Batch with the next Qwen 2.1 housekeeping if any.

- **Kandinsky 6 Lite distill: lip-sync to an existing song** (2026-10-06). K6 has no audio-input mode; it generates picture and sound together. Its image-to-video node already holds one stream fixed with a mask (the reference frame), and the audio mask is all ones. Idea: encode a real vocal with the MMAudio VAE (the extension loads it with `need_vae_encoder=False`, so that flag has to flip), put it in the audio half of the joint latent with mask 0, and let the sampler denoise only the video. Unknown whether the distilled PiFlow sampler honours an audio mask. Baseline facts: speech is reliable, generated singing is not (last sung word wrong on 4 of 4 clips), ~3 min per 5 s 480p clip in `Projects\ComfyUI-v0.39`. Details in TOOLING-STATE clones.md, kandinsky-6.

- **H3 Anti-Burn LoRA for long chains** (TESTED 2026-10-20, not shipped). Imagineer13/H3-Anti-Burn-LoRA
  (`h3_antiburn_universal_v1`, @b98eb1d3, rank 32, 310 MB, MiniMax H3 Community License) keeps continuation clips from
  getting crunchier; the card measures +44-61% face burn by clip 10 cut to about 0. On our 4-clip MV Chain card
  (engine-direct, same seed, LoRA on clips 2-4 only, base -> LoRA -> turbo_next): skin texture +11% by clip 4 without
  it, +3% at 0.5, +1% at 0.7, a little softer as strength rises, same render time. It does NOT fix our real chain
  drift: each continuation gets brighter and less saturated (luma 92 -> 111-115) with or without it. Four clips are
  too short for burn to matter; revisit if a chain of 6+ clips ships. Our continuations run on fl2va; the LoRA was
  trained on ref2va. `F:\Claude-Work\h3-antiburn-20261020\VERDICT.md`.

- **TurboDiffusion I2V (anveshane/Comfyui_turbodiffusion): TESTED 2026-10-22, DEAD END.** rCM-distilled Wan 2.2
  I2V-A14B at 4 steps with SLA attention; node @`ccf900c7` (last commit 2026-02-10), weights 2x 14.53 GB int8 `.pth`.
  Produced **zero frames in three attempts** on vanilla ComfyUI (torch 2.11, 4070 Ti 12 GB). (1) The compiled
  `turbo_diffusion_ops` CUDA kernels do not exist and the repo ships no build script, so the PyTorch int8 fallback
  runs; (2) that fallback dies at sampling step 0 with `mat1 and mat2 must have the same dtype, Float vs BFloat16`
  in `wan2pt2.py:660` — upstream issue #53, open since 2026-10-03, unanswered; (3) the default `comfy_native` offload
  mode segfaults the whole ComfyUI process inside `ops/core.py:501`. Separately, `layerwise_gpu` does not stream: it
  put 13.56 GB on a 12 GB card (`-1.60GB free`) at 640x640/65 frames. Also no `requirements.txt`, no LoRA support
  (#29), and its logger's `✓` raises `UnicodeEncodeError` through ComfyUI's cp1252 log handler and wedges the job
  silently. Same-seed control on our shipped `wan-22-i2v-gguf-q4` card: clean 65-frame clip, **127 s**, 11.58 GB peak,
  loaded partially (5.2 GB resident / 4.1 GB offloaded), 10 GB less download. Revisit only if #53 closes AND a build
  path for the CUDA ops ships AND real layer streaming lands. `F:\Claude-Work\turbodiffusion-test-20261022\VERDICT.md`.
