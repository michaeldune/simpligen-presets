# Reply draft — .sectorbob DM, "Sulphur 2 I2V as the base of LTX 2.5 Multi Reference?" (2026-09-13)

Hi! Short answer: not the original Sulphur 2. Its LTX 2.5 port does work in that setup, but it keeps faces worse, so I
wouldn't use it for reference shots.

**Sulphur 2 itself is an LTX 2.3 model** (both the Dev and Distilled versions on Civitai are listed as LTXV 2.3). The
SimpliGen Multi-Reference preset is LTX 2.5: the LTX 2.5 distilled transformer, the 2.5 text encoder and VAE, plus the
official LTX-2.5-Licon-MSR LoRA that does the reference binding. A 2.3 checkpoint isn't a drop-in for that stack.

**The LTX 2.5 port of it is REDGraft** ("REDGraft LTX 2.5 Fast 2K | sulphur2 ported" on Civitai), which I package as the
*LTX 2.5 REDgraft Fast 2K* pack in the store. It uses the same encoder and VAE as Multi-Reference, so I tested it: the
exact Multi-Reference graph with only the transformer swapped, same references, prompt and seed, three different
reference sets, at 720p.

- It loads and runs fine with the MSR LoRA, a little faster than the official model.
- Clothes and backgrounds hold just as well.
- **Faces don't.** With one person the two came out even. With two people, REDGraft turned one of them into a
  noticeably different person, and it opened the clip on a shot copied from that person's reference photo. With a
  person plus a background plate, it gave the man a different face and beard. The official model kept all of them.

So for keeping specific people consistent, stick with the official Multi-Reference preset. REDGraft is at its best
in its own T2V and I2V cards.
