# Architecture

Version: `0.1.0-alpha.2`

## Design goals

Authorial Editor separates four concerns that are often collapsed into one "humanize this" prompt:

1. evidence and claim preservation;
2. discourse-level analysis;
3. controlled rewriting;
4. integrity validation.

The MCP layer is intentionally thin. n8n is the initial orchestration runtime. The v0.1 gateway uses the MCP Server Trigger v2 compatibility baseline so it does not depend on later v2.1-only fields.

## Runtime topology

```text
MCP client
   │
   ▼
n8n MCP Server Trigger
   │
   ├── audit_text ─────────► 10-audit-text
   ├── rewrite_text ───────► 20-rewrite-text
   ├── validate_text ──────► 30-validate-text
   └── compare_versions ───► 40-compare-versions
```

Each public MCP tool delegates to a dedicated sub-workflow. This keeps schemas inspectable and lets individual stages evolve without turning the MCP gateway into a single untestable graph.

## Why n8n

The v0.1 architecture uses n8n for:

- MCP transport;
- authentication;
- tool registration;
- LLM-provider configuration;
- workflow orchestration;
- execution logging;
- future human-in-the-loop gates.

The editorial method itself is represented through version-controlled schemas, taxonomy, prompts, and workflow JSON rather than hidden in one model prompt.

## Private author data

The engine and author data are separate layers:

```text
PUBLIC
  engine + schemas + taxonomy + example profile

PRIVATE
  verified corpus
  author profile
  unpublished drafts
  private evals
```

The MCP tools accept an optional serialized `profile_json`. v0.2 is expected to add a profile builder rather than hard-coding a single author's voice into the public engine.

## Model roles

v0.1 distinguishes:

- **analysis model**: low-temperature source locking, discourse audit, integrity validation;
- **rewrite model**: controlled structural and surface revision.

Both are OpenRouter nodes in the reference workflows so deployments can choose an underlying provider/model without redesigning the graph.

## Failure philosophy

Integrity beats stylistic improvement.

If a rewrite introduces a new claim, changes a source, turns uncertainty into certainty, or invents experience, the validator should return `warn` or `fail`. The current alpha reports the problem rather than silently performing recursive repair. Automated repair is deferred until the validation/eval layer is stable.
