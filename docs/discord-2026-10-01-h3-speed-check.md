**MiniMax H3 speed check, one month on**
Same test as September 1st: text to video, 480p (864x480), 5 seconds, same seed, every card at its shipped step count, run through SimpliGen on an RTX 4070 Ti 12 GB. Each time is the render itself, averaged over two prompts (a still portrait and a fast tracking shot). Since then SimpliGen and its engine have both updated, and the community H3 packs moved to the faster int8 video VAE.

```
Card                         Steps   Oct 1   Sep 1
TaoMate 3-Step                  3     39 s     new
10Eros Max beta5 Turbo          8     52 s     new
Turbo LoRA, Fast Motion         4     65 s    75 s
DaSiWa Hybrid                   4     75 s    70 s
Turbo, Fully Accelerated       10     82 s    91 s
Turbo LoRA, larryvrh            6     89 s    93 s
PDD Acc 8-Step                  8     91 s   118 s
DaSiWa Hybrid v2                8     91 s     new
H3 Unlocked (official)          8    100 s     new
10Eros Max beta5               20    102 s     new
Z-Image Graft                  20    103 s     new
FastH3 8-Step V2                8    104 s     new
SparseRef15                    20    107 s     new
Two-Stage Latent Upscale       20    107 s     new
Singularity                    20    107 s     new
H3 stock (official)            20    116 s   202 s
Sol-Attn + EasyCache           20    119 s   116 s
H3 Low VRAM GGUF (official)    20    683 s   605 s
```
Biggest change: the stock official card nearly halved, from 202 s to 116 s. The official H3 Turbo card wasn't in this round because it shows as not installed on the current engine. That's been reported and should come back with its next update.

Fastest overall is TaoMate at about 40 seconds a clip. For detail, Two-Stage still looks best of the 20-step cards at the same speed as the rest of that group.
