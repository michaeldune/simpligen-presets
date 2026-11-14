# Connecting an agent to SimpliGen

Checked 2026-11-13 against SimpliGen 1.83.0, engine 0.45.0 and `@simpligen/mcp` 0.9.1. Official pages: <https://www.simpligen.io/docs/agents> (the whole docs site as plain text: <https://www.simpligen.io/llms-full.txt>).

An agent drives SimpliGen through one MCP server, `@simpligen/mcp`, started as a command. The server forwards each tool call to the app's Control API on the PC where SimpliGen runs.

## What must be true

- SimpliGen is open on its PC. The Control API exists only while the app runs.
- The agent's machine has Node.js, because the server starts with `npx`.
- The agent holds a pairing token (`sg-agent-...`) created in SimpliGen under **Settings -> Connect an agent**. A token is shown once; a lost one is replaced by creating another.
- The server reaches the Control API at `http://127.0.0.1:<port>` **on the machine the server runs on**. The port is 48199 unless that was taken at launch; the live value is in `%APPDATA%\simpligen\agent-api.json` on the SimpliGen PC.

The last point decides which section applies: an agent on the SimpliGen PC follows "Same PC", any other agent follows "Another machine".

## Same PC

1. In SimpliGen, open **Settings -> Connect an agent**.
2. For a client in the grid (Claude Code, Claude Desktop, Cursor, Windsurf, Cline, Gemini CLI, OpenAI Codex, LM Studio Bionic, OpenClaw, Zed): pick it, set a cloud spend cap, select **Install**. SimpliGen writes the server entry and the token into that client's config. Goose and Hermes get numbered steps to paste.
3. For any other client: choose **Manual setup**, copy the token, and add the server yourself.
4. Quit the client fully (tray icon included) and reopen it, so it re-reads its config.
5. Call `get_status`. Done when it returns the engine state and the active project.

JSON clients:

```json
{
  "mcpServers": {
    "simpligen": {
      "command": "npx",
      "args": ["-y", "@simpligen/mcp"],
      "env": { "SIMPLIGEN_TOKEN": "sg-agent-..." }
    }
  }
}
```

TOML clients (OpenAI Codex in `~/.codex/config.toml`; Grok Build in `~/.grok/config.toml`, same table shape, not yet run by us):

```toml
[mcp_servers.simpligen]
command = "npx"
args = ["-y", "@simpligen/mcp"]

[mcp_servers.simpligen.env]
SIMPLIGEN_TOKEN = "sg-agent-..."
```

On Windows a client that cannot start `npx` by name takes the full path to `npx.cmd` as `command`.

Keep the token inside the server's `env` block. A system-wide `SIMPLIGEN_TOKEN` variable overrides later edits and some clients hide it from servers.

## Another machine

The server has no host setting: it always calls `127.0.0.1` on its own machine, and the Control API answers `403 forbidden_host` to any request whose `Host` header is not a loopback address. So the remote machine needs a **forwarder**: something listening on its own `127.0.0.1:48199` that carries traffic to `127.0.0.1:48199` on the SimpliGen PC.

1. Create a token with **Manual setup** and a cloud spend cap.
2. Put a forwarder in place (pick one below).
3. On the remote machine, check it: `GET http://127.0.0.1:48199/health` returns `{"ok":true,"name":"simpligen","version":1}` with no token.
4. Add the server on the remote machine with two variables:

```json
"env": { "SIMPLIGEN_TOKEN": "sg-agent-...", "SIMPLIGEN_API_PORT": "48199" }
```

5. Call `get_status`. Done when it returns the engine state.

Forwarders:

| Forwarder | SimpliGen PC | Remote machine | Status |
|---|---|---|---|
| SSH reverse tunnel | `ssh -N -R 48199:localhost:48199 user@remote` | nothing | The official route (docs: Remote access). Not run by us. |
| Tailscale, plain TCP | `tailscale serve --bg --tcp 48199 tcp://127.0.0.1:48199` (tailnet only; undo with `tailscale serve --tcp=48199 off`) | a TCP forwarder from `127.0.0.1:48199` to `<simpligen-pc>:48199` (socat, or a few lines of Node) | PC side tested 2026-11-13. |
| Tailscale, HTTP only | same `tailscale serve` line | a local HTTP reverse proxy on `127.0.0.1:48199` that forwards to `http://<simpligen-pc>:48199` and sets `Host: 127.0.0.1:48199` | For machines that reach the tailnet only through a web proxy. A request with that header through the Tailscale forward answered 200 in our test. |

A direct request to `http://<simpligen-pc>:48199/health` returns `403 forbidden_host`. That answer proves the link is up; it is the forwarder that makes requests arrive as loopback.

### Hosted assistants (Grok Bot and similar)

A hosted assistant with its own cloud computer connects when it can do three things: run a command server (`npx -y @simpligen/mcp`) on that computer, hold environment variables for it, and reach the owner's tailnet. Grok Bot connected this way on 2026-11-13: Tailscale connector authenticated by the owner, forwarder on its computer, server added with `SIMPLIGEN_TOKEN` and `SIMPLIGEN_API_PORT=48199`, then `get_status` (reported by Grok Bot; which forwarder it chose was not recorded).

What the owner accepts with this setup:

- The assistant's computer joins the tailnet as a device and can reach every host on it unless a Tailscale access rule narrows it.
- Every tailnet device can reach port 48199; the token is the only lock on it.
- The token can spend cloud credits up to its cap, start and stop the engine, and read files on the SimpliGen PC through uploads.

A public HTTPS address in front of the Control API is not needed for any of this, and none of the routes above creates one.

## Working rules once connected

- **Preset ids are `pack:preset`**, for example `community--krea-2-pack:realia-krea2-v10`. Take them from `list_capabilities`; that answer is large (hundreds of KB), so save it and filter it.
- **Say every option the shot needs** (duration, aspect ratio, resolution, steps) in `generate` -> `options`.
- **A wait that times out is still rendering.** Read the job with `get_job` or `list_jobs` before submitting anything again. `wait_for_result` answers within about a minute; video renders take longer.
- **One engine, one queue.** Local jobs run one at a time, shared with the person at the PC and every other connected agent. Check `list_jobs` before a batch.
- **Files live on the SimpliGen PC.** `upload_file` takes a path on that PC, and a finished video comes back as a path on that PC. `get_result_image` returns a picture inline. A remote agent therefore sees images but not videos.
- **Name a project.** Without one, output lands in whichever project is open in the app.
- **Cloud costs credits.** Local generation is free and never counts against the cap; a cap of `0` makes a token local-only. Ask the owner before a cloud run.
- **Films.** Video Studio tools (`create_film`, `update_clip`, `render_clips`, `wait_for_renders`, `export_film`) work on films in the app; create agent films in their own project.

## When it does not connect

| Symptom | Cause | Fix |
|---|---|---|
| Every tool answers `fetch failed` | The server holds a dead port: it reads `agent-api.json` once at start | Confirm `GET /health` on the port in that file, then restart the agent client. Remote: also check the forwarder is running. |
| `401 unauthorized` | Token missing, revoked or mistyped | Create a new token; check that no system-wide `SIMPLIGEN_TOKEN` overrides the config. |
| `403 forbidden_host` | Request arrived with a non-loopback `Host` header | Go through the forwarder, at `127.0.0.1`. |
| Tools missing after install | Client still running with its old config | Quit it fully and reopen. |
| "Value not in list" on a model that is on disk | The app's model list is stale after an engine restart or a new file | Restart SimpliGen. |
| `get_status` shows the engine stopped | Engine still starting, or stopped | Wait and call again, or `start_engine`. |
