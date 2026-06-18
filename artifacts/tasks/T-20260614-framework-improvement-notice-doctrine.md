# T-20260614-framework-improvement-notice-doctrine

Status: completed
Task type: Framework Improvement Notice Doctrine
Project: ProjectForge
Completed: 2026-06-14T04:51:35Z

## Objective

Define how ProjectForge should communicate framework improvements to instantiated projects while preserving project autonomy and avoiding silent propagation or centralized project control.

## Scope boundaries observed

This was doctrine/design only. No automation, propagation mechanism, migration system, background process, existing-project modification, automatic framework notice implementation, review workflow implementation, template modification, or enforcement system was created.

## Primary deliverable

- `artifacts/reports/R-20260614-framework-improvement-notice-doctrine.md`

## Files changed

- `artifacts/reports/R-20260614-framework-improvement-notice-doctrine.md`
- `artifacts/tasks/T-20260614-framework-improvement-notice-doctrine.md`
- `state/active_goal.md`
- `state/project_state.md`
- `state/recent_changes.md`
- `context/latest_handoff.md`
- `state/_SUMMARY.md`
- `context/_SUMMARY.md`
- `artifacts/reports/_SUMMARY.md`
- `artifacts/tasks/_SUMMARY.md`

## Doctrine proposal summary

The report defines:
- what constitutes a framework improvement;
- which framework changes deserve notices;
- minimal useful notice structure;
- notice lifecycle states;
- project-local review outcomes;
- review-at-relevance doctrine;
- summary/handoff/context interaction rules;
- explicit prohibitions;
- compatibility with current ProjectForge doctrine;
- risks and failure modes;
- recommendation for a future small manual governance convention if separately approved.

## Implementation recommendation

Implementation is justified only as a later small manual governance convention after approval: a file-backed notice location, short README/summary, minimal template, and optional pilot notice. Automation, propagation, scanning, migration, background jobs, enforcement, and existing-project mutation should remain out of scope.

## Remaining risks

- Implementation remains unapproved and should not proceed automatically.
- Broad pre-existing uncommitted ProjectForge/ArchitectureHarvest changes remain in the working tree.
- `state/project_state.md` is approaching the context-health threshold.
- Stale generated `context/active_context.md` remains a non-blocking coherence warning.

## Next recommended task

If approved, implement only a small manual framework notice artifact convention: notice location, README/summary, minimal template, and optional pilot notice. Do not add automation, propagation, migration, scanning, enforcement, or existing-project mutation.

## Verification

After state/handoff/summary updates:
- `uvx --from pytest --with pyyaml pytest tests -q` → 66 passed.
- `python3 tools/check_coherence.py --project . --json` → no blocks; warnings for `state/project_state.md` approaching context-health limit and stale generated `context/active_context.md`.
- `python3 tools/architecture_reality_audit.py --project . --json` → no blocks and no warnings.

## Summary inspection
- Refreshed summaries with `python3 tools/update_context_summaries.py --project . --core-only`.
- Inspected `state/_SUMMARY.md`, `context/_SUMMARY.md`, `artifacts/reports/_SUMMARY.md`, and `artifacts/tasks/_SUMMARY.md`.
- Corrected stale Active Work / Needs Attention notes in `state/_SUMMARY.md`, `context/_SUMMARY.md`, and `artifacts/reports/_SUMMARY.md`.
