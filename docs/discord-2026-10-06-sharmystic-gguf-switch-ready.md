Great, and nice bonus on the LTX speech.

All three are ready and held, nothing pushed:
- `krea-flux` 1.2.0 and `wan22-i2v-gguf` 1.3.0: ComfyUI-GGUF url `https://github.com/molbal/ComfyUI-GGUF.git`, pinnedCommit `48de657b3aa830ae6981960e928b31cb51fd16aa`, no minAppVersion.
- `krea-2` 1.7.0: the two new Dark Beast GGUF cards (Q8 and Q4) with the same url and pin, no minAppVersion.

I'm available all afternoon and evening today (it's noon here, US Eastern), so ping me when your side is checked and we push together.

One thing about order: the Dark Beast cards have only run on plain ComfyUI with the fork, never in the app, because the old loader can't read Krea 2 files. So my plan for the window is: push `krea-flux` and `wan22-i2v-gguf` with you, let the app move the loader, run the Dark Beast cards once in the app, then push `krea-2` a few minutes later. `krea-2` has no GGUF pin today, so holding it back those few minutes can't cause any flipping. If you'd rather have all three in one sync, say so and I'll push them together and test right after.
