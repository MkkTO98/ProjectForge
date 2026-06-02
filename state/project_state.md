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

## Current local-execution/cloud-governance hardening
- `tools/build_context.py` builds summary-first bundles, estimates tokens, excludes raw logs/session transcripts from normal context, writes `context/context_audit.json` and `context/context_audit.md`, and supports three modes: normal, compact governance, and justified `project_wide_review`.
- `tools/select_model.py` routes implementation/refactoring/testing/debugging/summarization/retrieval toward local tools/models and requires an allowed governance/escalation reason plus a passing context audit before returning a cloud/Codex model.
- Project-wide architecture audits, redesigns, strategic planning, gap analysis, and consistency review remain possible under a larger configurable review budget when a review justification is recorded.
- `tools/log_run.py` preserves raw JSONL audit records while also maintaining compact derived session summaries, `context/latest_handoff.md`, and `context/project_summary.md`.
- `context/context_policy.yaml`, model routing/selection policies, logging policy, AGENTS/CONSTITUTION/README/instructions, and generated-project templates state the local-execution/cloud-governance split and raw-log exclusion requirements.

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
- Context summary refreshes are deterministic, preserve curated Purpose/Active Work/Needs Attention sections, and avoid volatile timestamps/ignored dry-run report listings.
- Tests now exercise registry side effects, generated coherence, generated wrapper behavior across all templates, runtime-cache filtering, stale questionnaire language, uv-first install guidance, and non-mutating verification behavior.
- Generated templates use uv/venv-first setup guidance on this PEP 668/no-pip host.
- Generated agent prompts now tell Hermes sessions to use Hermes tools directly and reserve `tools/run.py` for manual or explicitly audited wrapper use.

## Earlier additions preserved
- Workspace layer for multi-project coordination.
- Confidence policy for explicit uncertainty handling.
- Memory retention policy for long-term hygiene.
- Invariant tests for ProjectForge's own rules.
- Simplified knowledge graph to reduce maintenance burden.
