# Project State

ProjectForge is a reusable, Hermes-native project initializer for agent-assisted projects. It is a file-first project operating system: Markdown for human-readable policy, YAML for machine-readable configuration, JSONL for events/metrics, and explicit artifacts for decisions, tasks, reports, and handoffs.

## Stable defaults
- AI-first but human-designed through initial questioning.
- Hermes is the primary operator and adaptive interviewer.
- `config/setup_questionnaire.yaml` is a coverage map, not a rigid user-facing terminal script.
- `tools/new_project.py` is the deterministic scaffold renderer and manual fallback.
- Balanced-to-aggressive local autonomy with permission and dry-run constraints.
- Standard logging by default; no SQLite index by default.
- Auto-commit after tests may be allowed; remote push requires human approval.
- Specialized agents require a request and explanation before generation.
- Context budgeting uses auto-maintained folder summaries as inputs.
- Capability failures escalate current Hermes session -> stronger local model if configured -> Codex/premium model -> human.

## Current v6 additions
- Root ProjectForge `AGENTS.md` for Hermes/local agent startup instructions.
- Generated-project `AGENTS.md` in `templates/_shared_project/`.
- Local Hermes skill `projectforge` installed under `~/.hermes/skills/software-development/projectforge/`.
- Hermes-led project creation flow documented in README and operator manual.
- Model registry/routing YAML repaired and reframed as advisory to Hermes.
- Test coverage now verifies Hermes-native entrypoints and generated-project `AGENTS.md`.

## Current hardening additions
- Root and generated-project coherence contracts are split with `tools/check_coherence.py --mode root|generated|auto`.
- Project scaffolding validates must-pause sufficiency items, derives paths from the active ProjectForge root, and avoids registering noncanonical temp outputs by default.
- Generated projects receive setup-answer-derived state files and no longer receive the factory-only `tools/new_project.py`.
- Workspace registry schema is clean YAML with no `raw` fallback or pytest temp entries.
- Context summary refreshes are deterministic and avoid volatile timestamps/ignored dry-run report listings.
- Tests now exercise registry side effects, generated coherence, runner behavior, stale questionnaire language, and non-mutating verification behavior.

## Earlier additions preserved
- Workspace layer for multi-project coordination.
- Confidence policy for explicit uncertainty handling.
- Memory retention policy for long-term hygiene.
- Invariant tests for ProjectForge's own rules.
- Simplified knowledge graph to reduce maintenance burden.
