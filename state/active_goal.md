# Active Goal

Current objective:
- Rebuild MacroForge as a fresh ProjectForge-managed project from the completed reconstruction report, using current ProjectForge templates and compact curated context before any major implementation.

Immediate next action:
- Start a fresh Hermes session from `/home/mkkto/srv/projectforge`, read `context/latest_handoff.md` and `workspace/macroforge-reconstruction-report-20260602.md`, then initialize MacroForge at `workspace/projects/macroforge` with the `python_data_project` template.

Definition of done for ProjectForge v1:
- Can initialize a new project from templates.
- Stores setup decisions in `artifacts/decisions/`.
- Supports deferred specifications.
- Provides layered command permissions.
- Provides always-on logging.
- Provides MacroForge-like state files.
- Provides agent and skill instructions usable by Hermes or other agent frameworks.

Current constraints:
- Framework-adjacent by default.
- Do not rely on hidden chat memory.
- All durable assumptions must be file-backed.
