**Tested: the Molmo2-8B text encoder for MiniMax H3 - the 8+2 card stays on Qwen**
A few of you saw Ok Todd's video on Alissonerdx's Molmo2-8B encoder, which swaps H3's 32B Qwen text encoder for a much smaller one and promises faster renders. We baked it against the Qwen encoder the 8+2 card ships with: same graph, same DenoMix checkpoint, four shots (close-up dialogue, two-person dialogue, a wide shot, a sword fight), three seeds each, 40 renders at 1344x768 on a 12 GB RTX 4070 Ti with 32 GB of RAM.

What we found:
- **No speed gain.** 136 s per render with Molmo, 139-141 s with Qwen. That gap is within normal run-to-run noise. The text encoder takes about 6 s either way; nearly all the time goes to the video model.
- **More system RAM, not less.** Molmo left 3 GB free where Qwen left 8 GB. It keeps its model in RAM even after ComfyUI frees memory, so you get it back only by restarting.
- **Dialogue:** in text-only mode, which is what Todd's workflow uses, every line came out word for word. In the mode where Molmo also looks at your reference pictures, it cut the last word ("...I had no choice, Dad") on all three seeds.
- **Camera:** on a shot written "the frame never moves", both Molmo modes pushed in or reframed anyway. Qwen held the frame.
- **Picture quality:** about the same. Molmo looks a touch brighter. Changing the encoder gives you a different take on the same seed, so don't expect your favourite seed to come back.

So for now there's nothing to gain from switching. The 8+2 card keeps the Qwen encoder. We only tested one checkpoint, in English, on this one machine, so cards with less VRAM may see something different. If a later Molmo release fixes the RAM use, we'll test it again.

Thanks to Alissonerdx for releasing it (https://huggingface.co/Alissonerdx/Molmo2-8B-Minimax-H3). Experiments like this are how the faster encoders will eventually turn up.
