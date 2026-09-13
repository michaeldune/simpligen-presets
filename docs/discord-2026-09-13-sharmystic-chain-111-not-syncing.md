# Note draft — Clip Chaining 1.1.1 not picked up by the store (to Sharmystic, 2026-09-13)

_NOT SENT: 1.1.1 synced; Michael installed it 2026-09-13 14:19 EDT (~4 h after the push). The store expanded both short pins to full SHAs itself, so they were not a blocker. Kept for the licence-badge question only._

Hi Sharmystic, could you check whether the store rejected a pack update?

**Pack:** `minimax-h3-chain-pack` (MiniMax H3 Clip Chaining), repo `michaeldune/simpligen-presets`.
**Change:** 1.1.0 -> 1.1.1, pushed 2026-09-13 10:21 EDT (commit 60c542e). It's a manifest-only fix: the Two-Shot Director
card had a copy-pasted `acceptsReferenceVideos.min: 1`, and 1.60's reference-minimum gate started blocking it for users.
No models, workflows or extensions changed.
**What I see:** the store modal still shows v1.1.0 at 13:40 EDT.

If the sync held it, what was the reason? The only thing I can see that's unique to this pack: it's the one pack in my
repo whose extensions declare **abbreviated** `pinnedCommit` values:

- `seitanism/ComfyUI-H3-Motion-Context-MultiRef` -> `a823ca7`
- `AIMixer/ComfyUI_MiniMaxH3_Director` -> `e00b408` (resolves to e00b4089c5a34cb13eb7ca1d12fbcc3df86d6a34)

Every other pack uses full 40-character SHAs. 1.1.0 synced on 09-05, before the pin-enforcement changes, so if the new
rules want a full SHA, that would explain it. That's a guess, though. I haven't changed anything, and I'll expand them to
full SHAs if that's the cause.

Also, all three cards show "Licence unverified" in the store modal. Is that computed store-side from the model repos and
node licences? If there's a manifest field I should fill in, point me at it.
