# Context Policy

ProjectForge context is summary-first and budgeted. `_SUMMARY.md` files are folder-local maps. `context/active_context.md` is the selected task bundle. `context/context_audit.md` explains what was included/excluded and why. `state/` contains current project truth. `artifacts/decisions/` contains durable choices and deferred specifications.

Rules:
- Context building should use `tools/build_context.py` for explicit bundles.
- Summary maintenance should use `tools/update_context_summaries.py`.
- Agents must report `Context used:` in every run report.
- Normal task context may include only project summary/current state, active task file, relevant folder summaries, relevant decision records, explicitly retrieved source files, and a short recent handoff.
- Normal task context must not include raw logs, previous full conversations, full session JSONL files, whole-project file dumps, unrelated folders, large tool outputs, or generated artifacts unless explicitly relevant.
- Raw logs may be read only for failure investigation, forensic, or incident work when summaries are insufficient.
- Cloud/Codex escalation requires `context/context_audit.json` / `.md`, estimated token counts, included/excluded file reasons, confirmation that raw logs were excluded, and confirmation that summaries were used.
- Agents must not treat summaries as authoritative when they conflict with decisions or state.
- Cross-module changes must consult `knowledge/dependencies.yaml`.
