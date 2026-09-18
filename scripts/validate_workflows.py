#!/usr/bin/env python3
"""Static validation for version-controlled Authorial Editor n8n workflow exports."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "workflows"

EXPECTED = {
    "00-authorial-editor-mcp.json": "Authorial Editor - MCP Gateway",
    "10-audit-text.json": "Authorial Editor - audit_text",
    "20-rewrite-text.json": "Authorial Editor - rewrite_text",
    "30-validate-text.json": "Authorial Editor - validate_text",
    "40-compare-versions.json": "Authorial Editor - compare_versions",
}

SECRET_PATTERNS = [
    re.compile(r"\bsk-[A-Za-z0-9_-]{12,}"),
    re.compile(r"api[_-]?key\s*[:=]\s*[A-Za-z0-9_-]{12,}", re.I),
    re.compile(r"authorization\s*[:=]\s*bearer\s+", re.I),
]

errors: list[str] = []

def check_no_credentials(value, path="root"):
    if isinstance(value, dict):
        if "credentials" in value and value["credentials"]:
            errors.append(f"{path}: contains non-empty credentials")
        for k, v in value.items():
            check_no_credentials(v, f"{path}.{k}")
    elif isinstance(value, list):
        for i, v in enumerate(value):
            check_no_credentials(v, f"{path}[{i}]")

for filename, expected_name in EXPECTED.items():
    path = WORKFLOWS / filename
    if not path.exists():
        errors.append(f"missing {filename}")
        continue

    raw = path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        errors.append(f"{filename}: invalid JSON: {exc}")
        continue

    if data.get("name") != expected_name:
        errors.append(f"{filename}: unexpected workflow name {data.get('name')!r}")

    if data.get("active") is not False:
        errors.append(f"{filename}: public template must ship inactive")

    check_no_credentials(data, filename)

    for pattern in SECRET_PATTERNS:
        if pattern.search(raw):
            errors.append(f"{filename}: possible secret matched {pattern.pattern!r}")

gateway_path = WORKFLOWS / "00-authorial-editor-mcp.json"
if gateway_path.exists():
    gateway = json.loads(gateway_path.read_text(encoding="utf-8"))
    mcp = [n for n in gateway.get("nodes", []) if n.get("type") == "@n8n/n8n-nodes-langchain.mcpTrigger"]
    if len(mcp) != 1:
        errors.append(f"gateway: expected exactly one MCP Server Trigger, found {len(mcp)}")
    else:
        params = mcp[0].get("parameters", {})
        if mcp[0].get("typeVersion") != 2:
            errors.append("gateway: MCP Server Trigger must use typeVersion 2 for the v0.1 compatibility baseline")
        if params.get("authentication") != "n8nOAuth2":
            errors.append("gateway: expected n8nOAuth2 authentication")
        if params.get("requireExecuteAccess") is not True:
            errors.append("gateway: requireExecuteAccess must be true")
        if "instructions" in params or "includeUserInOutput" in params:
            errors.append("gateway: v2.1-only MCP parameters found in v0.1 compatibility template")

    tool_names = {
        n.get("name")
        for n in gateway.get("nodes", [])
        if n.get("type") == "@n8n/n8n-nodes-langchain.toolWorkflow"
    }
    expected_tools = {"audit_text", "rewrite_text", "validate_text", "compare_versions"}
    if tool_names != expected_tools:
        errors.append(f"gateway: tool set mismatch: {tool_names!r}")

if errors:
    print("FAIL")
    for err in errors:
        print(f"- {err}")
    raise SystemExit(1)

print("PASS: workflow templates are structurally valid and contain no stored credentials.")
