**Agent route does not fill a two-model `unets` card (Wan 2.2 I2V GGUF)**

App 1.67.2, engine v0.38.0, card `community--wan22-i2v-gguf-pack:wan-22-i2v-gguf-q4` (pack 1.2.2), installed from the store tonight.

**What happens**
The same card, same session, same machine:
- From the UI: works. 5 s at 480p rendered in 159 s (02:59 to 03:02 UTC).
- From an agent (MCP `generate`, backend local, with an uploaded image): rejected by the engine before it runs (03:12 UTC, job 7c7334c6-c55f-4fdb-81ce-ec555200c40c). The app reports "The engine rejected this workflow before it could run. The preset may need updating."

**The engine's reason**
```
Failed to validate prompt for output 108:
* UnetLoaderGGUF 116:96:
  - Value not in list: unet_name: '' not in ['MiniMax-H3-FL2VA-Pruned-Q3_K_M.gguf', 'SeFi-5B-Turbo-Q8_0.gguf', 'Wan2.2-I2V-A14B-HighNoise-Q4_K_M.gguf', 'Wan2.2-I2V-A14B-LowNoise-Q4_K_M.gguf']
* UnetLoaderGGUF 116:95:
  - Value not in list: unet_name: 'sd_xl_base_1.0.safetensors' not in [same list]
```
So on the agent route `{{unet}}` became `sd_xl_base_1.0.safetensors` and `{{unet_low_noise}}` became an empty string. Both GGUF files are on disk and in the engine's list.

**What the card declares**
The video block has no single `unet`. It has a `unets` array with two entries (HighNoise, then LowNoise), and the workflow uses `{{unet}}` and `{{unet_low_noise}}`. The UI path resolves both from the array; the agent path looks like it falls back to a default checkpoint name for `{{unet}}` and leaves the second one blank.

**The call**
```
presetId: community--wan22-i2v-gguf-pack:wan-22-i2v-gguf-q4
mediaType: video
backend: local
image: <upload_file handle>
options: { aspectRatio: "16:9", resolution: "480p", durationSeconds: 5, seed: 101 }
```

**Not checked**
- Whether the built-in `local-core-pack:wan-2.2-i2v` (also two models) has the same problem on the agent route; it is not installed here.
- Which @simpligen/mcp version was running.

Workaround for now: run the card from the UI, or resubmit the UI job's graph straight to the engine.
