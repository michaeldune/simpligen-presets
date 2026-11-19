Hey Shar, an engine finding from building a "Motion Transfer + Character" card (pose clip + reference pictures on H3 R2V, for ifOnze's request).

With the Fun pose ControlNet on, H3 ignores the reference pictures. Ref2VA + my character picture + the plain prompt "The woman in <Picture 1> dances on a rooftop...": the moves follow the clip, but none of 6 takes across FL2VA and Ref2VA wore her navy suit (white dresses, black dresses, one beige suit). With strength 0 the picture comes through (and the pose goes, of course). Strength 0.5 and end_percent 0.4 both still lose it.

Cause, I think: in nodes_minimax_h3.py, MiniMaxH3FunControlPatch.after_block adds the control skip to every non-audio row, so the text rows get it too, and that seems to break the "<Picture 1>" binding. I tested on a vanilla ComfyUI on the same commit as the engine (989d93d0, H3 files byte-identical), Spectrum and Sol-Attn off:

```py
skip[args["layout"].audio_pos.to(skip.device)] = 0
img_pos = args["layout"].img_pos.to(skip.device)
img_update = args["layout"].img_update.to(skip.device)
keep = torch.zeros(skip.shape[0], dtype=torch.bool, device=skip.device)
keep[img_pos[img_update]] = True
skip[~keep] = 0
out["img"].add_(skip, alpha=self.strength)
```

Result: the outfit and hair from the picture plus the clip's pose on 3 of 3 seeds (first image). Zeroing only the reference rows (img_pos[~img_update]) did NOT help; the text rows are what matter.

One catch: the same change on the existing pose-only Motion Transfer card lost the clip's spin on the one seed I ran (second image), so the residual on the text rows carries some pose. Maybe apply it only when the layout has reference rows, or make it a node option? Your call, I have not tested beyond this.

The card is on hold until the engine side is sorted. Happy to run more seeds or send the graphs.
