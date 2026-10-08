:clapper: **New: Agent Skills for Media Creation** - three skills that teach a coding agent to direct AI video

If you use a coding agent (Claude Code, Codex, Gemini CLI and others), a skill is a folder of instructions it loads when the task calls for it. These are our notes from making H3 videos, turned into something your agent can follow.

- **minimax-h3-prompt** - writes MiniMax H3 prompts as structured briefs instead of prose, for the SimpliGen H3 presets, ComfyUI or the API. Covers dialogue and singing shots, keeping a character's look from reference images, and the usual failures: wrong people, a drifting camera, mouths that keep moving after the line ends.
- **ai-filmmaker-director** - plans a shot before any prompt is written: intent, one beat per shot, framing, camera, performance, light, sound and how the shot ends. Works for any model.
- **vrgdg-music-video-builder** - makes or fixes a lip-synced music video with VRGameDevGirl's Music Video Builder and H3, checking every cut against the vocal stem.

Install:
```
npx skills add michaeldune/agent-skills-for-media-creation
```
Repo: https://github.com/michaeldune/agent-skills-for-media-creation

Good to know:
- The first two are instructions only. You still need SimpliGen, ComfyUI or the API to run the model.
- The music video skill needs a plain ComfyUI install with the comfyui-vrgamedevgirl and KJNodes packs, not SimpliGen's engine.
- That skill was written from one full song, then generalised for sharing, and has not been run start to finish since. Tell us where it trips.
- MIT licensed. MiniMax's h3-prompt-writing and the YuE2 authors' yue2-music are not included; the README links to both.

Thanks to Magnavex, whose AI Filmmaker Director document here started the director skill, to Shailesh for the infographic behind it, to Smart Bobo for the character PV method, and to VRGameDevGirl for the Builder.
