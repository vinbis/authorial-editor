# Security policy

## Supported versions

Only the latest tagged/alpha release is supported while the project is pre-1.0.

## Secrets

Never commit:

- n8n credential exports;
- API keys or bearer tokens;
- private author corpora;
- unpublished source documents;
- private author profiles containing sensitive information.

The public n8n workflow templates intentionally contain no credential IDs or API keys.

## MCP exposure

An MCP endpoint can cause model-initiated workflow execution. Treat it as an application endpoint, not a decorative webhook.

For production deployments:

- use authentication;
- restrict n8n project/workflow permissions;
- expose only the tools needed;
- keep write-capable unrelated workflows out of the MCP gateway;
- inspect execution logs;
- rotate credentials after any accidental exposure.

## Reporting

Please report security issues privately to the repository owner rather than opening a public issue containing secrets or exploit details.
