**New pack: MiniMax H3 (HyperFlow 8-Step)**
Video Rebirth's HyperFlow is a new 8-step distill for MiniMax H3. This pack runs it as a plain LoRA on the standard H3 weights, on HyperFlow's own fixed schedule, with no extra nodes to install. Two cards: Text to Video and Image to Video.

How it compares:
- Same cost as the PDD Acc 8-Step pack: about 90-100 s for 5 seconds at 480p on a 12 GB card. It is not a speed upgrade, and TaoMate 3-Step is still about twice as fast.
- What it buys you is steadier shots. On the same three seeds and two prompts, it held a locked-off camera still and kept a tracking shot continuous, where PDD Acc pushed in on the still shot and jumped to a different angle mid-clip on the moving one.
- Image to Video: Reference Image 1 is the first frame, an optional second picture is the last frame.

Good to know:
- The full HyperFlow release also uses a second timing input that the pruned H3 checkpoints don't have, so this runs the LoRA part only. That is what lets it work on the H3 files you already have, with no custom node.
- Steps are fixed at 8. Faster Attention is used when you have it on; Spectrum and Sol-Attn are left off for this schedule.
- No reference-to-video card yet.

If you have any H3 pack installed, only the 316 MB LoRA downloads. About 40 GB if you have no H3 pack yet. MiniMax H3 Community License; the ComfyUI conversion of the LoRA is Apache-2.0.
