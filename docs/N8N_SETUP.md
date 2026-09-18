# n8n setup

## Compatibility target

The v0.1 workflow templates use a conservative compatibility baseline intended for **n8n 2.30.x and newer**.

The MCP gateway deliberately uses **MCP Server Trigger v2**, not v2.1. n8n added the `n8n OAuth2` authentication option to MCP Server Trigger v2 in n8n 2.27; later MCP-trigger capabilities such as server-level instructions are not required by this release.

The workflow templates use these n8n node families:

- Execute Workflow Trigger;
- Basic LLM Chain;
- Structured Output Parser;
- OpenRouter Chat Model;
- MCP Server Trigger;
- Call n8n Workflow Tool.

The repository validator checks our exported structure, not every future n8n release. Test imports on your own n8n version before production deployment.

## 1. Import sub-workflows

Import:

```text
10-audit-text.json
20-rewrite-text.json
30-validate-text.json
40-compare-versions.json
```

Do not import the gateway first. Its workflow-tool references need the instance-specific IDs assigned to the four imported workflows.

## 2. Configure OpenRouter

Open each **OpenRouter Chat Model** node and select an n8n OpenRouter credential.

No credential ID or API key is stored in the repository JSON.

Select models appropriate for your deployment. The shipped model value exists only as an import-compatible default.

## 3. Test sub-workflows

Test each sub-workflow independently.

Recommended smoke cases:

- a factual paragraph with numbers and one URL;
- an opinion paragraph with no external claims;
- a draft containing an explicit uncertainty marker;
- an original/candidate pair in which the candidate intentionally changes a number.

Verify that the Source Lock distinguishes facts, opinions, experiences, and inferences.

## 4. Wire MCP gateway

Get the workflow IDs from n8n, then run:

```bash
python scripts/wire_router.py \
  --audit-id AUDIT_ID \
  --rewrite-id REWRITE_ID \
  --validate-id VALIDATE_ID \
  --compare-id COMPARE_ID \
  --output workflows/00-authorial-editor-mcp.wired.json
```

Import the generated file.

## 5. Authentication

The reference gateway uses the n8n MCP Server Trigger with `n8nOAuth2` and requires workflow execute permission.

If you intentionally choose another supported authentication mode, document it in your deployment. Do not publish an unauthenticated production endpoint simply because it is quicker.

## 6. Publish

Publish/activate the sub-workflows and gateway as required by your n8n version and deployment mode.

Use the **production** MCP URL from the MCP Server Trigger for external clients.

## 7. Author profiles

For v0.1 the caller can pass `profile_json` as a JSON string.

Do not hard-code a private profile into the public workflow export. A later release will provide a profile-store abstraction.

## Import troubleshooting

### Tool cannot find sub-workflow

The gateway still contains a placeholder ID, or the referenced sub-workflow was not imported/published correctly.

Run:

```bash
grep -R "REPLACE_.*_WORKFLOW_ID" workflows/
```

A wired gateway should contain none of those placeholders.

### OpenRouter node asks for credentials

Expected. Public templates cannot safely ship your n8n credential references.

### Structured parser fails

First inspect the raw model output and reduce model creativity for analysis nodes. The reference analysis nodes use temperature `0`.

### Rewrite changes a fact

Treat the run as invalid. The integrity output is a guardrail, not a permission to publish a known-bad revision.


## Official n8n references

- MCP Server Trigger: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/
- OpenRouter Chat Model: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenrouter/

The workflow JSON in this repository was aligned to the current n8n node structures at the time of the release. Re-run the smoke tests after n8n upgrades.
