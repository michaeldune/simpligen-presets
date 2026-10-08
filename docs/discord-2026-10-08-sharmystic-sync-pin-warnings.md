Hey Sharmystic, the new sync message is great, thanks. A question about the two warnings in the 2:01 PM run (repo 271842de): `illustrious-anime-pack` and `pony-realistic-pack` both got "pin resolution failed on re-sync; keeping the previous live version".

Which URL failed for each? I checked everything those two packs point to and it all resolves from here, so I can't tell what to fix:
- All ten Civitai model versions (seven in Illustrious Anime, three in Pony Realistic) are Published and public in the Civitai API, no paid or early access, each with a SHA256 and clean scans.
- The SDXL VAE link on Hugging Face (already pinned to a revision) responds.
- The rgthree commit both packs pin, d92cad68, exists.
- Neither pack has changed in our repo since the 2026-10-03 pinning commit.

Two things I ruled out as the difference, in case it saves you time:
- Some of the Civitai links return 401 without a login, but so do links in `illustrious-realism-pack` and `pony-anime-pack`, which synced without a warning.
- Both packs have a Civitai version with more than one file and no `fileId` in our URL, but about a dozen other live packs do too.

One possible lead: Civitai shows version 2665539 (in Illustrious Anime) as updated yesterday at 16:30 UTC. Nothing in Pony Realistic changed recently, so it doesn't explain both. If this was a temporary Civitai failure or rate limit during the run, that would fit too.

Two requests, if they are cheap:
- Could the warning line name the URL (or the node) that failed and the reason, e.g. HTTP status or hash mismatch?
- If a file's hash changed upstream, is the right fix on our side a version bump, or does the store re-pin on its own?

No rush, both packs are still live. I'll watch the next run and tell you if the same two warn again.
