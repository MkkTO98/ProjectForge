# T-20260615 Ecosystem Structure Migration Planning

Date: 2026-06-15
Status: completed
Scope: bounded architecture, naming, ownership, and migration-planning task

## Goal

Review how the physical ecosystem structure should eventually evolve to match project autonomy doctrine, clarify EIP/EII terminology, assess ProjectForge de-hosting, assess MetaHarvest extraction/naming, and preserve ecosystem infrastructure ownership as a future-review question.

## Explicit non-actions

This task did not perform:

- commits;
- staging;
- physical moves;
- directory renames;
- project extraction;
- project creation;
- MacroForge modification;
- ecosystem infrastructure implementation;
- registry implementation;
- contract implementation;
- repository restructuring.

## Outputs

- Review artifact: `artifacts/reports/R-20260615-ecosystem-structure-migration-planning-review.md`
- Future-review note: `artifacts/reports/R-20260615-ecosystem-infrastructure-ownership-future-review-note.md`

## Bounded terminology alignment

Updated active ProjectForge guidance and current ecosystem-reference surfaces only:

- `README.md`
- `CONSTITUTION.md`
- `state/architecture.md`
- `state/project_state.md`
- `workspace/_SUMMARY.md`
- `workspace/projects_registry.yaml`
- `artifacts/reports/R-20260615-ecosystem-infrastructure-future-review-note.md`

Terminology now distinguishes:

- EIP = Economic Intelligence Platform, the future ecosystem as a whole.
- EII = Economic Intelligence Initiative, a possible future user-facing intelligence project.

Historical artifacts were not rewritten.

## Main recommendations

- Neutral EIP root is conceptually aligned but physically premature.
- ProjectForge de-hosting is conceptually aligned but should be future migration work.
- Future project creation should include explicit location selection once purpose/scope are clear.
- MetaHarvest conceptual separation is justified; physical separation is not yet justified.
- MetaHarvest physical rename should wait for path inventory and extraction/hosting decision.
- `No project owns the EIP root` is a high-confidence doctrine candidate, but was not promoted automatically.
- Ecosystem infrastructure ownership remains undetermined.

## Verification

Final verification should include:

- `git diff --check`
- `python3 tools/check_coherence.py --project . --json`
- `python3 tools/architecture_reality_audit.py --project . --json`
