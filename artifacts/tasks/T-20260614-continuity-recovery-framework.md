# Task: Continuity and Recovery Framework

Date: 2026-06-14
Status: Complete
Type: framework implementation and hardening
Scope: ProjectForge root, generated-project inheritance, explicit MacroForge adoption

## Goal

Implement a small file-backed ProjectForge continuity and recovery framework that lets a fresh Hermes session recover current project state, active task, recent decisions, blockers, and next recommended actions without broad repository scanning or cloud-token-heavy context reconstruction.

## Existing mechanisms to extend

- Priority 1 startup files: `state/active_goal.md`, `state/project_state.md`, `state/architecture.md`, and `context/latest_handoff.md`.
- Task artifacts under `artifacts/tasks/` and decision artifacts under `artifacts/decisions/`.
- Folder summaries (`_SUMMARY.md`) and `tools/build_context.py` for explicit context bundles.
- `tools/context_health.py` and coherence checks for token-budget hygiene.
- `context/context_policy.yaml` task completion and context loading hierarchy.
- `recovery/` playbooks and escalation policy.

## Gaps

Initial gaps:
- No single deterministic low-token recovery command existed for root/generated projects.
- Near-quota/compaction shutdown expectations were documented only indirectly through handoff/task-completion policy.
- Generated-project templates did not yet include an explicit continuity framework document or recovery command.
- Existing MacroForge project predated the latest strict ProjectForge startup hierarchy and needed explicit adoption because ProjectForge must not silently mutate instantiated projects.

Final hardening gaps found during validation:
- The continuity framework defined near-quota shutdown but did not explicitly state that the command `Perform standard ProjectForge closeout. Follow the continuity framework. Then stop.` is sufficient.
- Standard closeout behavior existed across `AGENTS.md` and `context/context_policy.yaml`, but the recovery framework document did not yet replace ad hoc user-provided closeout procedures with a single canonical sequence.
- Coherence checked that the recovery helper/framework existed, but did not enforce the presence of standard closeout and fresh-session recovery command contracts.
- `tools/recover_session.py` could treat a referenced `artifacts/tasks/_SUMMARY.md` path as an active task if a handoff/state file mentioned it.

## Implementation plan

1. Add a dependency-free `tools/recover_session.py` that reads only fixed startup files and bounded task/decision/question metadata, then emits Markdown or JSON recovery output.
2. Add `recovery/continuity_framework.md` defining the startup, shutdown, handoff, blocker, and resume procedure without creating parallel governance.
3. Extend `context/context_policy.yaml`, `AGENTS.md`, and generated templates to reference the recovery command and near-quota shutdown priority.
4. Add tests for root usage, generated-project inheritance, and bounded/no-raw-log behavior.
5. Explicitly adopt the same capability in MacroForge by copying the helper/doc/policy/instruction updates and validating from MacroForge.
6. Update task/state/handoff/summaries and run final verification.
7. Final hardening: make the standard closeout and fresh recovery prompts explicit in the framework, context policy, agent instructions, templates, and MacroForge adoption files; enforce their presence in coherence; and validate that recovery skips summary artifacts as active tasks.

## Acceptance criteria

- `python3 tools/recover_session.py --project . --json` works from ProjectForge and from MacroForge.
- A newly generated ProjectForge project contains and passes coherence for the recovery helper and continuity framework.
- Recovery output includes project state, active task/current objective, recent decisions, blockers, next recommended actions, and recommended resume procedure.
- Recovery output excludes raw logs and does not require repository-wide scanning.
- Tests and coherence checks pass after governance/state/summary updates.
- `Perform standard ProjectForge closeout. Follow the continuity framework. Then stop.` is documented as sufficient and maps to an explicit task/state/handoff/summary/verification sequence.
- `Recover project state and continue work.` is documented as sufficient and maps to bounded recovery before editing.
- Coherence blocks missing standard closeout or fresh recovery command contracts in ProjectForge, generated projects, and MacroForge.
- Recovery does not report `_SUMMARY.md` as an active task when summaries are mentioned in state/handoff files.

## Validation notes

Dry-run:
- `simulation/dry_runs/20260614_074352-dry-run.md` was created and validated for the final hardening scope.

Targeted validation already run during hardening:
- `uvx --from pytest --with pyyaml pytest tests/test_session_recovery.py -q` -> 3 passed.
- `python3 tools/check_coherence.py --project . --json` -> no blocks; expected context-health warnings for near-threshold `state/project_state.md` and stale generated `context/active_context.md`.
- `python3 tools/check_coherence.py --project workspace/projects/macroforge --mode generated --json` -> no blocks/warnings.
- `python3 tools/recover_session.py --project . --json` and MacroForge equivalent were machine-checked for required recovery fields, no raw-log reads, no repository-wide scan, active/recent tasks, decisions, blockers, next actions, and resume procedure.
- `uvx --from pytest --with pyyaml pytest tests -q` -> 69 passed.
- `python3 tools/architecture_reality_audit.py --project . --json` -> no blocks/warnings.
- MacroForge `uvx --from pytest --with pyyaml pytest tests -q` -> 68 passed.
- MacroForge `python3 tools/check_coherence.py --project . --mode generated --json` -> no blocks/warnings.
- MacroForge `python3 tools/architecture_reality_audit.py --project . --json` -> no blocks/warnings.

Final post-closeout verification is recorded in `context/latest_handoff.md`.

Additional final verification after resumed closeout:
- ProjectForge `uvx --from pytest --with pyyaml pytest tests/test_session_recovery.py -q` -> 3 passed.
- ProjectForge `python3 tools/check_coherence.py --project . --json` -> no blocks; non-blocking stale generated `context/active_context.md` warning.
- ProjectForge `python3 tools/check_coherence.py --project workspace/projects/macroforge --mode generated --json` -> no blocks/warnings.
- ProjectForge `python3 tools/architecture_reality_audit.py --project . --json` -> no blocks/warnings.
- ProjectForge `uvx --from pytest --with pyyaml pytest tests -q` -> 69 passed.
- MacroForge recovery smoke -> required fields present; `raw_logs_read=false`; `repository_wide_scan=false`.
- MacroForge `uvx --from pytest --with pyyaml pytest tests -q` -> 68 passed.
- MacroForge `python3 tools/architecture_reality_audit.py --project . --json` -> no blocks/warnings.
- Non-destructive generated-project smoke at `/tmp/projectforge-continuity-smoke.YNl7kj/continuity_smoke` -> generated coherence no blocks/warnings and recovery helper inherited with required fields present, `raw_logs_read=false`, and `repository_wide_scan=false`.

## Outcome

Complete. The standard closeout command and fresh recovery command are now explicit framework contracts, inherited by future generated projects, enforced by coherence, and adopted by MacroForge. The implementation extends existing file-backed ProjectForge governance and adds no database, vector store, external service, daemon, autonomous propagation, or parallel state system.

## Commit-sequencing closeout — 2026-06-14T20:53:06Z

Repository hygiene, strict context hierarchy/context health, and Architecture-to-Reality Audit were committed separately before this closeout:

- `add710c` — `chore: ignore local external mirrors and build metadata`
- `c8d1777` — `feat: enforce strict context hierarchy and context health`
- `8a4784c` — `feat: add architecture-to-reality audit`

This Continuity/Recovery task remains complete but uncommitted. Next session should prepare the Continuity/Recovery commit first, before ArchitectureHarvest, because it is the direct remaining deliverable from the original request and is smaller/lower-risk than the ArchitectureHarvest commit.

Boundary notes for that commit:

- Include `tools/recover_session.py`, `recovery/continuity_framework.md`, `tests/test_session_recovery.py`, generated-template recovery inheritance, coherence/scaffold/session-recovery hunks, this task, the continuity decision, and relevant summaries/handoff/state hunks.
- Exclude ArchitectureHarvest, generated-project architecture placeholder hunks, framework notice/doctrine-only follow-ups, `uv.lock`, `external_sources/`, and `projectforge.egg-info/`.
- Use hunk-level staging for mixed files, especially `AGENTS.md`, `context/context_policy.yaml`, `context/latest_handoff.md`, `state/*`, `templates/_shared_project/AGENTS.md`, `templates/_shared_project/context/context_policy.yaml`, `templates/_shared_project/tools/check_coherence.py`, `tools/check_coherence.py`, `tools/new_project.py`, `tests/test_scaffold.py`, and `_SUMMARY.md` files.
