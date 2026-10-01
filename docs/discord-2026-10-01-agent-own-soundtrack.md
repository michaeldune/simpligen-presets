Thanks for 1.67.2 and mcp 0.4.0, reference clips over the API work: our new Motion Transfer card received its clip as ref_video_1 and rendered fine.

One gap: `soundtrackMode: "own"` (also the default) never reaches the generation from the agent side.

- In the app, attaching a clip runs `video:extractSoundtrack`, the entry carries `soundtrack: { path: <wav> }`, and the engine uploads it as `ref_video_audio_N`.
- The agent route resolves `referenceVideos` to `{ path, soundtrackMode }` only. No extraction, so the upload loop (`if (!track?.path) continue;`) skips it and the slot stays empty, exactly like `"none"`.

Repro (1.67.2, @simpligen/mcp 0.4.0): `generate` on any card with `acceptsReferenceVideos.soundtrack: true`, `referenceVideos: [{handle, soundtrackMode: "own"}]`, a clip with audio. Session log shows `Uploaded ref_video_1` and no `Uploaded ref_video_audio_1 (own)`; the output carries the card's no-soundtrack audio instead of the clip's.

Suggested fix: in the agent `referenceVideos` resolver, when the mode is `own`, call the same `extractSoundtrack` the UI uses and attach `soundtrack: { path }` (and for `file`, accept a handle for the wav).
