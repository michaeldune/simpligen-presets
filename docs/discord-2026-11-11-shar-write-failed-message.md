Small one from amanwithanewplan's report this morning (MiniMax H3 update, app 1.81.2). The pack update fails with "Could not download 3 workflow files ... write verify failed: UNKNOWN: unknown error, open 'D:\Simpligen Output\presets\workflows\video_minimax_h3_t2v.json.tmp' ... Check your connection and try again."

The download was fine. Windows refused to create the .tmp in their custom data folder (the same UNKNOWN shows up on reads and on the preview save in their log, so it's their D: drive). But the message tells them to check their connection, which sends them the wrong way.

The downloader already knows the difference: `fetchValidatedWorkflow` returns `reason: 'write-failed'` for this case. It gets lost on the way up (line numbers from the 1.81.1 asar):
- `presetCatalog.js` ~323 pushes only `${filename} (${result.error})` into `workflowFailures`, dropping `result.reason`
- ~366 always appends "Check your connection and try again."

Suggestion: when any failure has reason `write-failed`, say something like "SimpliGen couldn't save files to <folder>. Check that the drive is connected and has free space, and that antivirus or Controlled folder access isn't blocking it." Keep the connection wording for `unreachable`.

Minor, same path: a `write-failed` result is retried with backoff like a network error, but on a volume that refuses the open it fails the same way every time, so it only adds a few seconds before the error.
