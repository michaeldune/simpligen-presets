A "harness" is the program wrapped around an AI model that lets it do things instead of just chat. The model only writes text. The harness keeps the conversation, runs the tools the model asks for (read a file, call an API, start a generation), and feeds the results back. Claude Code, Codex, Cursor, OpenCode, Cline and Goose are all harnesses.

**How it connects to SimpliGen: MCP**
MCP (Model Context Protocol) is the standard plug between a harness and an app. SimpliGen ships an MCP server, `@simpligen/mcp`. You add it to your harness once and the model gets SimpliGen tools: list presets, upload a picture, generate, check the job, and so on.
1. In SimpliGen open **Settings -> Connect an agent**.
2. Pick your harness if it's listed, otherwise **Manual setup**, and copy the token (`sg-agent-...`).
3. In the harness's MCP settings, add a server that runs `npx -y @simpligen/mcp` with `SIMPLIGEN_TOKEN` set to that token. You need Node.js installed.

**Why Claude Code or Codex won't do it**
Those are proprietary harnesses tied to their own company's models. The harness is fine, but the model behind it is Claude or GPT, and those are the ones refusing fight and force scenes. You can't swap the model out.

**What you want for Venice**
A harness that lets you choose the provider and model. Venice's API speaks the OpenAI format, so any harness with an "OpenAI-compatible / custom provider" option works:
- **OpenCode**: Venice has an official setup guide for it (docs.venice.ai, Integrations -> OpenCode).
- **Cline** (VS Code extension) or **Goose** (desktop app): add Venice as an OpenAI-compatible provider, base URL `https://api.venice.ai/api/v1`, your Venice API key.

Then add the SimpliGen MCP server to that harness as above and pick a Venice model.

One thing to check: the model has to support tool calls, or it can't use MCP at all. Venice's current list shows `venice-uncensored-1-2` does, as do its GLM and DeepSeek uncensored variants.
