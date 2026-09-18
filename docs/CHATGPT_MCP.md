# ChatGPT and MCP

Authorial Editor exposes a remote MCP endpoint through n8n.

## Intended connection model

```text
ChatGPT / compatible MCP client
          │
          ▼
HTTPS remote MCP endpoint
          │
          ▼
n8n MCP Server Trigger
          │
          ▼
Authorial Editor tools
```

The deployment must be reachable by the client and use an authentication mode supported by both sides.

## Current ChatGPT status

**Compatibility note dated 2026-09-18:** OpenAI currently documents custom MCP apps as **web-only**. They are not available in ChatGPT mobile apps at this time.

OpenAI also documents that ChatGPT connects to **remote** MCP servers. A server that remains on a private network or developer machine is not connected directly; OpenAI points to Secure MCP Tunnel for supported products when a private MCP server should not be exposed publicly.

Full MCP availability also depends on the ChatGPT plan/workspace and can change while the feature is in beta. Check the current OpenAI documentation before promising support for a specific client or plan.

Official OpenAI references:

- https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt
- https://help.openai.com/en/articles/12515353-build-with-the-apps-sdk
- https://help.openai.com/en/articles/11487775-apps-in-chatgpt

## Why MCP is still the project boundary

The server is intentionally independent from ChatGPT's current client availability. MCP is the integration contract; compatible clients can evolve independently from the n8n workflows.

OpenAI's Apps SDK is built on MCP, so a future ChatGPT-facing app can sit on top of the same backend rather than requiring a second editorial engine.

## Recommended tool instructions

When registering the server, keep the model-facing contract simple:

- use `audit_text` when the user wants diagnosis without rewriting;
- use `rewrite_text` when the user explicitly wants a revised draft;
- use `validate_text` to check a candidate against an original;
- use `compare_versions` for editorial differences;
- never frame outputs as proof of human or AI authorship;
- never use the tools to optimize detector evasion.
