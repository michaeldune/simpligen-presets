Hey Sharmystic, the official MiniMax H3 Turbo pack is showing as not installed here, and I think it's a stale Spectrum pin.

- Pack: minimax-h3-turbo-pack 1.0.16 (all three cards: t2v, i2v, r2v)
- Its ComfyUI-Spectrum-MiniMax-H3 extension is pinned to 0aeac5434db6743b7201226f8c484c0bf795710d
- The engine checkout is on v0.2.27 (120d72e2f48b781235b34149e39bbdf0f1317d82), the version the other H3 packs pin now, including the official GGUF pack 1.3.1
- Agent generate on minimax-h3-turbo-t2v returns: preset_not_installed: MiniMax H3 Text to Video is not installed locally. Use backend "cloud" or install it first.

It's the only manifest in my presets folder that still pins 0aeac54. Moving the pin to 120d72e should bring it back. The old commit also breaks Spectrum renders on engine 0.36+ (FinalLayer.forward signature), so rolling the checkout back isn't an option. This is the installed 1.0.16; I can't tell whether the store already has a newer version.
