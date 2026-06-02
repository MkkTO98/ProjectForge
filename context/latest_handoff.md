# Latest Handoff

Updated: 2026-06-02T20:02:22.481463+00:00
Agent: hermes
Status: completed
Run ID: 6855d9fb-667f-4022-a7e4-37db09f6c51c

## Goal
Transform ProjectForge into local-execution/cloud-governance system

## Files changed or touched
- `tools/build_context.py`
- `tools/select_model.py`
- `context/context_policy.yaml`
- `models/routing.yaml`
- `models/selection_policy.yaml`
- `AGENTS.md`
- `CONSTITUTION.md`
- `README.md`
- `instructions/CONTEXT_POLICY.md`
- `templates/_shared_project`
- `tests/test_context_governance_mode.py`
- `tests/test_context_policy_strict.py`
- `state/project_state.md`

## Compact notes
Adjusted previous strict cloud-minimization policy into a leverage-per-token architecture: local execution for implementation/routine work, cloud governance for architecture/audit/strategy/gap/redesign work, and justified project-wide review mode with larger budget.

## Context rule
Future agents should read this handoff, project/folder summaries, active task files, and relevant decisions first. Raw logs remain available for audit/debugging but must not be loaded into normal task context.
