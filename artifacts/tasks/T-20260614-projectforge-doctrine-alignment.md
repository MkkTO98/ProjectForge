# T-20260614-projectforge-doctrine-alignment

Status: completed
Task type: Doctrine Implementation Only
Project: ProjectForge
Completed: 2026-06-14T04:36:31Z

## Objective
Bring ProjectForge governing doctrine into alignment with the approved constitutional direction without structural redesign, template redesign, generated-project migration, ArchitectureHarvest redesign, worker-system redesign, or code-first implementation.

## Scope constraints observed
Permitted doctrine-only edits were made. No template restructuring, generated-project layout changes, inheritance changes, worker creation/removal, framework notice implementation, code changes, ArchitectureHarvest structural changes, migration mechanisms, or new subsystems were performed.

## Files changed
- `CONSTITUTION.md`
- `AGENTS.md`
- `README.md`
- `instructions/GENERAL_INSTRUCTIONS.md`
- `instructions/PROJECTFORGE_SELF_MANAGEMENT.md`
- `state/architecture.md`
- `ArchitectureHarvest/CONSTITUTION.md`
- `artifacts/tasks/T-20260614-projectforge-doctrine-alignment.md`
- closeout state/handoff/summary files

## Doctrine changes made
- Reframed ProjectForge as a reusable framework that improves itself and future inheritance, not an active project manager, meta-controller, or owner of instantiated projects.
- Added explicit generated-project autonomy and no-silent-mutation doctrine.
- Added framework boundary doctrine distinguishing ProjectForge-owned reusable concerns from project-owned goals, architecture, implementation, task execution, and adoption decisions.
- Added improvement/adoption flow doctrine: ProjectForge improvement → improvement notice/recommendation → project review → project decision → optional adoption.
- Added questioning doctrine recognizing FOUNDATIONAL, ARCHITECTURAL, IMPLEMENTATION, and PREFERENCE questions while preserving the questionnaire as a coverage map.
- Added automation doctrine distinguishing useful automation from automation theater and preserving correctness-over-automation.
- Added framework-change doctrine requiring explicit user awareness when changes affect framework-level behavior.
- Clarified ArchitectureHarvest as librarian/reference/evidence/advisory system, not a controller, while preserving strong recommendations and project-local adoption.
- Added doctrine that framework improvements should answer the recurring problem, future beneficiaries, and why the behavior belongs in ProjectForge rather than a single project.

## Tests and checks run before closeout updates
- `uvx --from pytest --with pyyaml pytest tests -q` → 66 passed.
- `python3 tools/check_coherence.py --project . --json` → no blocks; warning only for stale generated `context/active_context.md`.
- `python3 tools/architecture_reality_audit.py --project . --json` → no blocks and no warnings.

## Summary inspection
- Refreshed summaries with `python3 tools/update_context_summaries.py --project . --core-only`.
- Inspected `_SUMMARY.md`, `state/_SUMMARY.md`, `context/_SUMMARY.md`, `artifacts/tasks/_SUMMARY.md`, `ArchitectureHarvest/_SUMMARY.md`, and `ArchitectureHarvest/adoption_candidates/_SUMMARY.md`.
- Corrected stale Active Work / Needs Attention notes in `state/_SUMMARY.md`, `context/_SUMMARY.md`, and `ArchitectureHarvest/_SUMMARY.md`.

## Remaining risks
- Broad pre-existing uncommitted ProjectForge/ArchitectureHarvest changes remain in the working tree; this task did not attempt to separate or commit them.
- The existing stale generated `context/active_context.md` coherence warning remains non-blocking; regenerate a task-specific context bundle before future context/model-routing work.
- Framework notice implementation remains deliberately unimplemented; later work should decide artifact shape and review workflow before adding mechanics.
- ArchitectureHarvest new-project consultation is now doctrine-lightened for simple projects; if this conflicts with desired strict mandatory consultation, make that a follow-up constitutional decision.

## Next recommended task
Define a doctrine-to-governance follow-up for optional framework improvement notices: artifact shape, review states, and summary/handoff expectations only. Do not implement propagation or migration until that notice doctrine is separately approved.
