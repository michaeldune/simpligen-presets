:scissors: **Also worth a look: OpenShorts (MIT, self-hosted)**
https://github.com/mutonby/openshorts

The opposite end of the pipeline from a generator: feed it a long video (podcast, stream, interview) and it cuts 9:16 shorts. Moment picking by an LLM, scene detection, face-tracked reframing with YOLOv8 + MediaPipe, two-speaker split layout with captions on the seam, faster-whisper word captions, hook text, optional ElevenLabs dubbing. Docker, runs on CPU in 5 to 8 min per 8 min of video, and the LLM step can point at Ollama or LM Studio so it needs no cloud key at all. Has an MCP endpoint, so an agent can drive it.

It also has an "AI Shorts" UGC mode (AI actor + voiceover + lipsync), but that part is fal.ai calls: Flux 2 Pro for the actor, Hailuo 2.3 Fast for the video, Kling avatar for lipsync, roughly $0.65 to $2 a clip. That is exactly what an H3 card does locally in one pass, so the interesting pairing is: generate the talking head in SimpliGen, then hand the long cut to OpenShorts for the shorts.
