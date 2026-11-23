Bug report from #support (1.92.1, diagnostics zip attached): a user can't install the engine at all and the app gives them no way out.

**What happened:** they once moved to `D:\Simpligen` with "Move the engine too" ticked, so `engine_dir` = `D:\Simpligen\engine`. That folder is gone now (data folder is `H:\simpligen`, engine version `null`). Install and start refuse with `engineLocationMissing`: "The engine is in D:\Simpligen\engine, which is not reachable right now... or move the engine back in Settings > Storage."

**Why they're stuck:**
- `engineLocationProblem()` blocks install while `engine_dir` points at a missing folder, which is right for an unplugged drive.
- Nothing in the app ever clears `engine_dir`. The only write is in the storage move (`if (plan.settings.engine_dir) write(...)`).
- Reset in Storage only resets `data_dir`. They tried it, same error.
- "Move the engine back" can't work: with the engine folder missing, `engineEntries` is empty, so `planStorageMove` returns `nothing_to_move`.

So the error tells them to do something that fails, and the only fixes are recreating the folder on D: or deleting the `engine_dir` row from simpligen.db by hand.

**Suggested fix:** when `engineLocationProblem()` fires, offer "Install the engine in the default folder instead" on that error card (and/or have Storage > Reset clear `engine_dir` when its folder is missing). It would delete `engine_dir`, so `getBasePath()` falls back to `userData/engine`. Maybe keep the warning about a second engine if the old drive comes back.

I've given them the manual workaround for now.
