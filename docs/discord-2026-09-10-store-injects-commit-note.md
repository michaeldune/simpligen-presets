# Note draft — Store sync injects `commit` on unpinned extensions (to Sharmystic, 2026-09-10)

Hi Sharmystic, found a small store/app interaction worth a look. Not urgent, I've worked around it on my side.

**What happens**

My Singularity pack listed ComfyUI-KJNodes with just a name and URL, no commit. The copy the store served (`community--minimax-h3-singularity-pack.json`, synced 09-06) had `"commit": "da90cca8..."` on that entry, which is KJNodes' branch head on the sync day. The repo pack never declared it.

In 1.59.2, `extensionPinnedCommit` falls back from `pinnedCommit` to `commit`, and `extensionNeedsWork` enforces that as an exact pin for any non-baseline node. My engine's KJNodes checkout is at 3f20054 (the commit every other H3 pack pins), so readiness reported drift and all three Singularity cards sat on "Install preset locally" even though every weight was on disk. Spectrum matched its pin, the workflow files were fine.

**Why it bites**

Any pack that leaves a node unpinned gets pinned by the store to whatever the branch head was on sync day. From then on it fails readiness for every user whose checkout of that node is at any other commit, which is most of them once a second pack pins the same node. Take the pack update and the next sync can move the target again.

**What I did**

Shipped Singularity 1.0.1 with an explicit `pinnedCommit` for KJNodes (matching the other H3 packs) and scanned my 41 packs: that was the only unpinned non-baseline entry. rgthree is baseline so it's exempt, which is why it never showed up.

**Suggestion**

Either have the sync leave `commit` absent when the author didn't set one (so the app's "track the branch" path applies), or write it as an advisory field the readiness check ignores. If the intent is that every extension must be pinned, a validation error at publish time would be clearer than a silent pin.

Happy to test a fix on my side, I can reproduce it on demand.
