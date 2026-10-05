Got it on all three: GGUF cards stay in `krea-2`, I'll take minAppVersion out or leave it in according to what you confirm before switch day, and I won't touch the engine's loader.

On Krea Flux: there is no non-GGUF original. The Civitai page (model 1962590) has a single version and its only files are `kreaCSG_foundation.gguf` and the VAE, so the GGUF is the only form this finetune was published in.

I built the next best thing and the answer is clear: **the fork is the correct one, city96 is the outlier.**

What I did:
- Decoded the file with both loaders on CPU and compared every tensor. All 780 come out bit-identical between city96 `6ea2651` and molbal `48de657`, and they match the `gguf` library's own decoder (F32 and BF16 exact, Q5_K within 0.002). So neither loader reads the file wrong.
- Wrote those decoded weights to a plain safetensors (23.8 GB, fp16) and rendered it with the stock UNETLoader, no GGUF code involved. Same graph, seed 101, same two prompts, plain ComfyUI v0.37.2.

Against that reference:
- portrait: city96 23.8 dB (36% of pixels differ by more than 8/255), fork 32.2 dB (5%)
- street: city96 20.5 dB (52%), fork 28.9 dB (11%)

By eye the fork render and the reference are the same picture (same signage, same cart, same background figures); city96 is a different take on the same composition. Since the weights are equal, the difference is in how city96 runs the model, not in how it reads the file. I have not tracked down where.

So I take back what I said earlier about the fork being the odd one out. After the switch, Krea Flux users get what the model produces in stock ComfyUI. Old seeds will still change, but toward the correct result.

Caveat: the reference is the decoded GGUF, not the creator's weights from before quantization, since those were never released. It tells you which loader is faithful to the file, which I think is the question.

Standing by for the date.
