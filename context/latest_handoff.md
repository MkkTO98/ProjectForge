# Latest Handoff

Updated: 2026-06-02T19:47:56.018331+00:00
Agent: hermes
Status: completed
Run ID: 4ebf51ed-cdd3-4d61-9eab-73c85d0c48d1

## Goal
Implement strict ProjectForge context/token architecture

## Files changed or touched
- `tools/build_context.py`
- `tools/select_model.py`
- `tools/log_run.py`
- `context/context_policy.yaml`
- `models/routing.yaml`
- `models/selection_policy.yaml`
- `logs/logging_policy.yaml`
- `AGENTS.md`
- `CONSTITUTION.md`
- `README.md`
- `instructions/CONTEXT_POLICY.md`
- `templates/_shared_project`
- `tests/test_context_policy_strict.py`
- `state/project_state.md`

## Compact notes
Strict summary-first context policy implemented. Raw logs remain stored but are excluded from normal context. Cloud/Codex routing now requires allowed escalation reason and context audit under budget. Tests and coherence passed.

## Context rule
Future agents should read this handoff, project/folder summaries, active task files, and relevant decisions first. Raw logs remain available for audit/debugging but must not be loaded into normal task context.
