:eyes: **Worth a look: Hypit (open source, out today)**
https://github.com/hypit-ai/hypit

Not a preset and nothing to install in SimpliGen, but it sits right above what we do. You hand a coding agent (Claude Code, Codex) a short-form video and it rebuilds the whole edit as a markup file: A-roll clips, word-aligned captions from WhisperX, B-roll, stickers, ranking boards, music, rendered in headless Chrome. Then you swap the host, the product or the language and re-render 100 variants.

The catch: every generation step goes through their paid gateway (Seedance 2/2.5, GPT Image 2, Seedream, Nano Banana, Grok Imagine, MiniMax H3 via API, ElevenLabs/Fish TTS). No ComfyUI anywhere in the tree. Their demo clips cost about a dollar each. Licence is Apache with no-resell / no-hosting conditions, fine for your own use.

Why it is interesting for us: the provider layer is a small documented SDK, and its three H3 modes map straight onto our t2v / i2v / r2v cards. A local provider that routes H3 to SimpliGen while Hypit does captions and layout looks feasible; untested. Also its prompt playbooks direct H3 dialogue the same way we have been recommending here: attitude toward the listener first, then two or three physical beats, let the model fill the rest.
