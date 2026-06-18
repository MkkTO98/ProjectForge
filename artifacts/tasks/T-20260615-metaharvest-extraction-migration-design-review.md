# T-20260615 MetaHarvest Extraction-Migration Design Review

Date: 2026-06-15
Status: completed
Scope: migration-design and extraction-readiness planning only
Permission level: L4 foundational design; no extraction or implementation

## Goal

Design how a later MetaHarvest/ArchitectureHarvest extraction should be performed if explicit extraction approval is granted, without performing extraction, renaming, compatibility implementation, template/tooling/test modification, ecosystem infrastructure work, or repository restructuring.

## Explicit non-actions

- No commit.
- No staging.
- No directory move.
- No directory rename.
- No MetaHarvest extraction.
- No MacroForge modification.
- No EII modification.
- No compatibility-layer implementation.
- No aliases implemented.
- No template modification.
- No tooling modification.
- No test modification.
- No ecosystem infrastructure implementation.
- No repository restructuring.

## Deliverable

Produced:

- `artifacts/reports/R-20260615-metaharvest-extraction-migration-design-review.md`

## Key conclusions

- Recommended naming strategy: Option A — extract first, rename later.
- First extraction should preserve the physical/name identity `ArchitectureHarvest` to reduce compatibility and historical-reference churn.
- `MetaHarvest` should remain the conceptual broader purpose and possible later rename until a separate rename migration is approved.
- Historical artifacts should preserve ArchitectureHarvest terminology and remain immutable by default.
- Future generated projects should keep `architecture/architectureharvest/` for first extraction; provider-neutral paths such as `architecture/advisory/` should be reviewed later.
- ProjectForge tooling/tests should eventually validate ProjectForge integration promises, not MetaHarvest internals.
- Minimum shim set should be a notice/glossary/path mapping, not a duplicate tree or sync layer.
- Preferred interim extraction location, if later approved: `/home/mkkto/srv/architectureharvest` as a sibling beside ProjectForge.
- Extraction remains blocked until compatibility, verification, rollback, evidence-reference, and exact implementation plans are approved.

## Validation performed

- Context inspected:
  - `CONSTITUTION.md`
  - `state/project_state.md`
  - prior extraction-independence review report
  - prior doctrine-finalization/inventory report
- Coherence validation: completed after artifact creation.
- Doctrine consistency validation: completed after artifact creation.
- Staging check: completed after artifact creation.

## Follow-up recommendation

If the next step is approved, perform a design-to-implementation dry-run only. That dry-run should enumerate exact path moves, shim files, docs/tool/test/template diffs, validation commands, and rollback commands, but still should not execute extraction until a separate L4 approval checkpoint.
