# Ideas to try later

Running backlog. Each entry: what to try, why, rough cost, source. Move an entry to "Done / dropped" with the
result when it is settled.

## Open

### From SatoDive's H3 Latent Continuation (2026-09-19)
Source: https://github.com/SatoDive/Minimax-H3-Latent-Continuation, tutorial https://www.youtube.com/watch?v=KkugNjrpXAc

1. **Lip sync across a Native Guide join.** PARTLY DONE 2026-09-19 (see Done section): speech and picture survive
   the join; lip sync itself could not be measured at 480p and needs Michael to watch
   `D:\SimpliGen-Backups\satodive-continuation-test-20260919\clip2_stitched_00001_.mp4`. If he wants a number,
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
   `D:\SimpliGen-Backups\h3-native-audio-lock-20260920\VERDICT.md`.
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
   `D:\SimpliGen-Backups\h3-latent-mv-chain-20260920\VERDICT.md`.
   `D:\SimpliGen-Backups\h3-native-audio-lock-20260920\VERDICT.md`.
2. **Same test with singing.** DONE 2026-09-19, see Done section. If (1) holds for speech, repeat with a vocal stem + backing at -14 dB. This decides
   whether music-video singing shots can be chained instead of one 345-frame generation.
   **2b REPEAT DONE 2026-09-20:** two more spans (verse 2 with the lead, chorus with the guitarist as a second singer).
   Chain render time = one long generation; every deliverable's audio verified per second. Michael on verse 2: can't
   pick between chain and long, "both are spot on"; chorus/guitarist: "the same, both spot on". 3 of 3 spans now. Caveats: the continuation steps a few luma levels brighter at the
   join, and it inherits the previous clip's drift (the guitarist shot pushed in and brightened in BOTH arms), which
   will compound over more hops: that is what 2c has to measure. The lip metric is blind on continuous singing.
   Details: `D:\SimpliGen-Backups\satodive-singing-test-20260919\VERDICT.md` (REPEAT section).
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
   constant VRAM) ships.

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
    `D:\SimpliGen-Backups\qwen-image-21-test-20260920\`. If it loads on city96, add ONE low-VRAM card to the held
    `feat/qwen-image-21` pack (new card, not a change to the others). Note H3 GGUF presets ran 3-10x slower in our bake-off.
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

## Done / dropped

- **2026-09-19, item 2 (singing):** BITB 9.5-24.58 s, lead close-up, stem + backing -14 dB, join mid-phrase.
  The pack's `digital_human` mode locks the supplied audio (output vs song waveform corr 0.976). Mouth-vs-vocal r:
  fresh clip +0.616, continuation after the join +0.573, single long generation +0.497/+0.340 (framed wider, so
  not a fair win). Chain 460 s = long 460 s; a 2 s context tail fixed the 4x continuation slowdown (item 1b DONE).
  Awaiting Michael's eyes. `D:\SimpliGen-Backups\satodive-singing-test-20260919\VERDICT.md`.

- **2026-09-19, item 1 (first pass) + item 4 (his nodes):** SatoDive pack @4142527 in vanilla ComfyUI, fisherman
  reference, 8 s clip + 10 s continuation. Both lines word-exact across the join, picture join corr 0.997, framing
  and identity carried, latent hand-off +0.3% luma vs -2.2% through pixels. Continuation ~4x slower. His
  `MiniMaxH3TurboLoRA` node did not apply the LoRA on our int8 base; stock loader used. Full write-up:
  `D:\SimpliGen-Backups\satodive-continuation-test-20260919\VERDICT.md`.
