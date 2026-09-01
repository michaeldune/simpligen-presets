# Retired: Community — LTX 2.5 MSR (Multi-Subject)

Superseded on 2026-09-01 by **LTX 2.5 Multi-Reference**, an official preset in
SimpliGen's own LTX 2.5 pack (app 1.56.0 or newer). Use that instead.

This pack is kept here for reference. It is no longer built into a zip or
published to the release, because `build-zips.py` only scans `packs/`.

## Why

Both are built on LiconStudio's Multiple-Subject-Reference work, but the
official preset uses the LoRA built for this model generation:

| | this pack | official Multi-Reference |
| --- | --- | --- |
| LoRA | `LTX-2.3-Licon-MSR-V2` on a 2.5 base | `LTX-2.5-Licon-MSR-V1` |
| references | 3 subjects + background | 4 subjects + background |
| clip length | 3–10 s | 3–20 s |
| output | 832×448 (0.37 MP) | 1664×896 (1.49 MP) |
| 12 GB card | 75 s, measured | 231 s, measured |
| per megapixel | 203 s | 155 s |
| extra nodes | pins `ComfyUI-Licon-MSR` | ships its own |

Measured on the same RTX 4070 Ti (12 GB), same three reference plates, on
2026-09-01. The official preset's announcement gives a 16 GB minimum; it ran
here on 12 GB, holding three separate identities, so that floor is
conservative.

The only thing this pack still does better is a fast low-resolution draft. That
is not enough to justify keeping two packs that do the same job, and pointing
people at a previous-generation adapter would not be doing them a favour.
