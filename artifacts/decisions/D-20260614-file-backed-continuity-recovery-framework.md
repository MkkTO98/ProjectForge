# Decision: File-Backed Continuity and Recovery Framework

Date: 2026-06-14
Status: accepted
Related task: `artifacts/tasks/T-20260614-continuity-recovery-framework.md`

## Context

ProjectForge already had concise startup state, task artifacts, decision artifacts, handoffs, folder summaries, context bundles, context-health checks, and generated-project inheritance. Those mechanisms partially solved session continuity, but fresh sessions still lacked a single deterministic low-token recovery command and near-quota shutdown expectations were implicit rather than explicit.

The user requested real implementation for ProjectForge, future generated projects, and explicit adoption by MacroForge without databases, vector stores, embeddings, external services, broad repository scanning, duplicate governance, or parallel state artifacts.

## Decision

ProjectForge accepts a small file-backed continuity and recovery framework that extends the existing state/task/decision/handoff/context-health system.

The framework consists of:

- `tools/recover_session.py`: dependency-free bounded recovery helper.
- `recovery/continuity_framework.md`: recovery contract, standard closeout contract, near-quota shutdown order, resume procedure, and existing-project adoption procedure.
- `context/context_policy.yaml` `continuity_recovery` policy.
- `AGENTS.md` startup and completion instructions.
- generated-project template inheritance through `templates/_shared_project/`.
- coherence requirements for `tools/recover_session.py` and `recovery/continuity_framework.md`.

## Boundaries

- No database, vector store, embeddings, service, daemon, scheduler, autonomous migration, or repo-wide scanner.
- No new state source of truth.
- No replacement of existing task/decision/handoff/state governance.
- Existing projects remain autonomous and adopt through explicit project-local migration or user-approved task. MacroForge adoption is included only because the request explicitly named MacroForge.

## Consequences

- Future generated projects inherit bounded recovery automatically.
- Fresh agents can run `python3 tools/recover_session.py --project . --json` to recover current state, active/recent task, decisions, blockers, next actions, and resume procedure.
- The command `Recover project state and continue work.` is sufficient to trigger bounded recovery before editing.
- The command `Perform standard ProjectForge closeout. Follow the continuity framework. Then stop.` is sufficient to trigger task/state/handoff/summary/verification closeout without a user-provided ad hoc checklist.
- Near quota exhaustion prioritizes task status, blockers/questions, next actions, and latest handoff before optional cleanup.
- Coherence blocks missing continuity framework files and now also blocks missing standard closeout or fresh recovery command contracts.
