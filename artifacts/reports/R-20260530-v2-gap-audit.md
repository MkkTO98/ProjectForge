# Report: ProjectForge v2 Gap Audit

Date: 2026-05-30

## Findings from v1 inspection

V1 had a useful base scaffold but was incomplete in four areas:

1. The setup interview was hardcoded in `tools/new_project.py` rather than being a reusable questionnaire artifact.
2. There was no explicit sufficiency policy defining when the initializer had asked enough questions.
3. There was no model registry or model-routing layer for assigning agents to local or remote models.
4. Folder-level `_SUMMARY.md` files were not present, despite being important for MacroForge-style context compression.

## Added in v2

- `config/setup_questionnaire.yaml`
- `config/sufficiency_policy.yaml`
- `instructions/`
- `models/`
- folder summaries across core directories
- model selection tool
- folder summary update tool
- updated project initializer that reads the questionnaire schema
- shared project components copied into generated projects

## Remaining intentionally deferred

- Actual Hermes v0.15.1 installation path detection.
- Actual Telegram bot credential setup.
- Real local model inventory detection for the user's machine.
- Full concurrency scheduler for multiple local models.

These are deferred because they depend on the user's machine and Hermes installation, not because they were forgotten.
