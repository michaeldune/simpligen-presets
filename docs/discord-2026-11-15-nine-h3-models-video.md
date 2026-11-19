**Video worth a look: 9 MiniMax H3 models side by side, with sound**
https://youtu.be/ZnBxfqNnn3s (Prince does AI, 24 min)

He gives nine H3 models the same 8 prompts (walk, run in the rain, laugh, cup, fast turn, dance, shout, crowd) with one character sheet and one empty scene picture, two seeds, one take each. 9.4 s clips at about 1 MP on an RTX 5090. He picks no winner; you watch and decide.

**The three batches**
- Official: H3 base + turbo LoRA, Pika H3 Flex, HyperFlow H3 Flash
- Speed versions: FastH3 Omni, FastVideo VSA 4-step, 10Eros Max
- Community merges: Singularity v2, Singularity x 10Eros PRISM, PRISM-DMAD-PDMD

**A few things he points out**
- Pika Flex put five copies of the dancer in the loft, on both seeds.
- Several models dress the crowd in her yellow jacket. FastH3 does it to almost everyone.
- Turns and cuts can lose her: some models end on the dog or an empty park.
- PRISM-DMAD-PDMD had the cleanest wave and shout of the three merges, but its background jumped mid-shot in the cup scene and it lost her in the crowd.
- He ran PRISM-DMAD-PDMD on the plain beta scheduler because beta57 isn't installed for him.

**His numbers (per clip, 5090, about 1 MP)**
- FastH3 Omni: 2 min 22 s, the fastest
- HyperFlow: 2 min 34 s
- Pika Flex: 2 min 58 s
- Singularity v2: 3 min 10 s
- H3 base: 3 min 22 s
- PRISM and PRISM-DMAD-PDMD: 3 min 25 s
- 10Eros Max: 3 min 33 s
- FastVideo VSA: 5 min 50 s, the slowest
All nine made 10 of 10 clips. He says times varied from run to run and calls it a small test.

His workflows are free, linked in the video description.
