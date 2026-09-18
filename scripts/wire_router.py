#!/usr/bin/env python3
"""Replace instance-specific n8n sub-workflow IDs in the Authorial Editor MCP gateway."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

PLACEHOLDERS = {
    "REPLACE_AUDIT_WORKFLOW_ID": "audit_id",
    "REPLACE_REWRITE_WORKFLOW_ID": "rewrite_id",
    "REPLACE_VALIDATE_WORKFLOW_ID": "validate_id",
    "REPLACE_COMPARE_WORKFLOW_ID": "compare_id",
}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-id", required=True)
    parser.add_argument("--rewrite-id", required=True)
    parser.add_argument("--validate-id", required=True)
    parser.add_argument("--compare-id", required=True)
    parser.add_argument(
        "--template",
        default=str(Path(__file__).resolve().parents[1] / "workflows" / "00-authorial-editor-mcp.json"),
    )
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    template = Path(args.template)
    output = Path(args.output)
    data = json.loads(template.read_text(encoding="utf-8"))

    values = {key: getattr(args, attr) for key, attr in PLACEHOLDERS.items()}
    replacements = 0
    for node in data.get("nodes", []):
        workflow_id = node.get("parameters", {}).get("workflowId")
        if not isinstance(workflow_id, dict):
            continue
        value = workflow_id.get("value")
        if value in values:
            workflow_id["value"] = values[value]
            replacements += 1

    if replacements != 4:
        raise SystemExit(f"Expected 4 workflow ID replacements, made {replacements}")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote wired gateway to {output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
