# Contributing

Contributions are welcome, especially around:

- editorial feature definitions;
- factual-integrity evaluation;
- n8n compatibility;
- provider-neutral model adapters;
- reproducible evaluation datasets;
- documentation and tests.

## Ground rules

1. Do not optimize the project for bypassing AI detectors.
2. Do not add fabricated "human-like" mistakes as a rewriting strategy.
3. Do not include copyrighted corpora without a redistribution right.
4. New discourse features must document:
   - what they measure;
   - why they matter editorially;
   - whether they are paper-derived, adapted, or project-native;
   - known limitations.
5. Workflow changes must pass:

```bash
python scripts/validate_workflows.py
```

## Pull requests

Keep workflow JSON exports free of credentials and instance-specific workflow IDs unless the file is clearly an example.
