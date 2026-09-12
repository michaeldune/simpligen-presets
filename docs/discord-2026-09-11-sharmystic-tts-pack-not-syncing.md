# Note draft — store never publishes minimax-h3-tts-lipsync-pack (to Sharmystic, 2026-09-11)

Hi Sharmystic, thanks for 1.60.0, both fixes confirmed on my side (Singularity cards flipped without the 1.0.1 pin, and the pin warning is exactly what I wanted).

One more store question. Of my 43 packs the store lists 42; the only one it has never published is `minimax-h3-tts-lipsync-pack` (MiniMax H3 Emotion TTS Lip-Sync). It has been on master since 09-09, I bumped it to 1.0.1 last night in case the sync keyed on id+version after its 09-05 withdrawal, and the sync that followed picked up three other pack updates but still skipped this one. Nothing in the sync is visible to me, so I'm guessing at the reason.

What's unusual about it: 28 `extraModels` entries whose `dir` values contain dots, e.g. `TTS/IndexTTS-2.5`, `TTS/IndexTTS-2.5/hf_cache/bigvgan`, `TTS/IndexTTS-2.5/qwen0.6bemo4-merge`. That is the IndexTTS 2.5 folder layout the node expects. The app accepts interior dots since 1.59.2 (the `SAFE_DIR_SEGMENT` change), and a fresh install through the app downloads all 26 files fine. My guess is the store still validates `dir` with the pre-1.59.2 rule and drops the pack silently. Other candidates: `sizeGB: 49`, or a per-pack cap on extraModels count.

Could you check what the sync logs for that pack id? If it's the dotted-dir rule, the store validator just needs the same relaxation the app got; I'd rather not rename the folders since the node hard-codes them. And a visible rejection reason in the sync report would save this round trip next time.

---

## Resolved — 2026-09-11, store-side. My guess was wrong.

Not the dotted `extraModels` dirs, and not the id+version keying. Both were my guesses; both were wrong.

**The real gate.** Publishing computes a checksum for *every* model entry in a pack and **fails closed if even
one cannot be pinned**. Hugging Face LFS files pin from their id, so all the multi-gigabyte weights were fine.
The small files are not LFS — HF keeps `config.yaml`, `vocab.json`, `merges.txt`, the tiktoken file and the rest
as plain git blobs, and a git blob id is a hash of the object, not of the content the app verifies. The store
came up empty on **14 of this pack's 26 entries**, so it held the whole pack every night while all 42 others
published normally.

**The fix, deployed by Raynold.** The store now downloads those small files and hashes them itself, matching what
the app verifies against. LFS files still resolve from their id and are never downloaded, so nothing
multi-gigabyte gets pulled at publish time. He verified the previously failing files against the real repo and
they match an independent hash.

**Nothing in this pack needed changing, and the folders must NOT be renamed** — the IndexTTS node hard-codes them.
Pack live 2026-09-11 12:35, 43 of 43.

**Carry forward.** The all-or-nothing pinning rule still applies to any future pack that mixes LFS weights with
small config/tokenizer files; that combination is what to look at first if a pack silently never publishes. And
the process lesson, which Raynold conceded: the reason sat in a column only the store can read, so two days went
into guessing. Visible rejection reasons for pack authors are on his list, along with the warning for nodes the
store had to pin itself. Until that ships, **ask for the rejection reason rather than bumping versions or
renaming folders to work around an invisible gate.**
