One from a user report, confirmed here: on the MiniMax H3 cards, picking **3:2 (Photo)** or **2:3** in the Generate screen ignores the resolution tier and renders at 1152x768 (768x1152).

Why: every H3 tier's `aspects` map has 1:1, 16:9, 9:16, 4:3, 3:4 and 21:9, but the video ratio picker also offers 3:2 and 2:3. The tier map is merged over the built-in default table, so a ratio the tier doesn't define keeps the default `'3:2': { width: 1152, height: 768 }` whatever tier is selected.

Two runs on my machine, `minimax-h3-gguf-pack:minimax-h3-gguf-t2v` 1.3.2, 3:2, 5 s, 20 steps, from the Generate screen:
- tier=4 (768p): output 1152x768, sampling 5 min 12 s
- tier=0 (480p): output 1152x768, sampling 5 min 15 s

So 480p costs the same as 768p at that ratio, about double what the user gets at 480p on any other ratio (16:9 is 864x480). The Run log line also has no WxH for these jobs, only `ar=3:2 | tier=0`.

The agent route already handles it: `generate` with aspectRatio 3:2 on `minimax-h3-pack:minimax-h3-t2v` returns "Unsupported aspectRatio "3:2" ... Supported: 1:1, 16:9, 9:16, 4:3, 3:4, 21:9". It's only the Generate screen that lets it through.

It's not specific to your packs: all 469 H3 tiers installed here (yours and mine) have the same six ratios, and the LTX 2.5 packs I checked do too. I'd guess the clean fix is app-side, either hiding ratios the selected tier doesn't define or scaling the default to the tier, since that covers every pack at once. If you'd rather have 3:2 and 2:3 added to the tier maps, tell me the sizes you want per tier and I'll add them to mine to match.
