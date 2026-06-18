# Active Goal

Project: MacroForge

## Current milestone

Milestone 3 — second-source PostgreSQL promotion through deterministic canonicalization proposal workflow and bounded WDI unit metadata enrichment are complete.

## Purpose

MacroForge exists to progressively reduce the recurring effort required to build, maintain, validate, canonicalize, and use trusted macroeconomic data for investment-relevant research.

Trusted macroeconomic databases and datasets are outputs of MacroForge. The project itself is the effort-reduction machine that makes such data increasingly cheaper, safer, clearer, and more reproducible to produce and use.

## Current objective

TASK-038 is complete and the session wrap-up selected the highest-leverage next task. Await user approval to create a bounded artifact/report task that persists TASK-038 deferred mapping advancement requirements: rationale, missing evidence, semantic blocker, minimum advancement condition, and evidence/replay pointers. Do not implement metadata enrichment, lifecycle redesign, model assistance, conversion/aggregation, report integration, or new canonicalization logic unless separately approved.

## V1 success

MacroForge v1 succeeds when one World Bank WDI vertical slice proves raw evidence, checksum, staging transform, idempotent PostgreSQL load, metadata, lineage, quality checks, validation, and an inspectable report.

## Current defaults

- Evaluate future work by asking which recurring effort it reduces: source onboarding, source maintenance, validation, canonical mapping, schema evolution, downstream analysis, or future agent recovery/context effort.
- Recreate schema/WDI/OECD/Eurostat cleanly from decisions, tasks, and tests.
- Use isolated temporary PostgreSQL databases for smoke verification unless a fresh dry-run and explicit approval allow otherwise.
- Keep source-specific loaders and metadata work bounded until accepted decisions justify broader abstractions; abstraction must be earned by repeated non-semantic duplication.
- Preserve canonical-domain identities: structured periods, ISO3 country identity, explicit territory types for aggregates, and provider period/territory codes as mappings/metadata rather than curated identities.
- Treat PostgreSQL as the accepted analytical store, not proof of truth by itself.
- Treat confidence scores as review-routing metadata, not truth.
- Use `artifacts/manifests/canonical_assets.json` as the minimal file-backed pointer registry for existing accepted/provisional canonicalization artifacts.
- TASK-034 proved the deterministic loop: provider evidence -> proposal generation -> review routing -> mapping update proposal -> audit report.
- DEC-021 selected bounded WDI unit metadata enrichment as the next uncertainty-reduction step because TASK-034 exposed `unknown_unit_metadata` as the sharpest blocker.
- TASK-037 enriched only existing WDI GDP unit metadata evidence with fixture-backed metadata, marking it as source metadata evidence rather than canonical truth and preserving no-unit-conversion/no-auto-apply boundaries.
- TASK-038 validated the proposal -> review -> accepted/provisional lifecycle in bounded file-backed form using existing WDI/OECD/Eurostat GDP evidence. It produced explicit review decisions, check gates, state deltas, manifest deltas, lineage, and replay evidence. WDI reached a governed provisional outcome; OECD and Eurostat were deferred because unresolved basis/frequency/currency caveats remain material.

## Completed TASK-037 evidence

- Task: `artifacts/tasks/TASK-037-implement-bounded-wdi-unit-metadata-enrichment-for-canonicalization-evidence.md`
- Dry-run: `simulation/dry_runs/20260613_172928-task-037-wdi-unit-metadata-enrichment.md`
- Audit artifact: `artifacts/reports/canonicalization-wdi-unit-metadata-enrichment-20260613.json`
- Implementation: `src/macroforge/canonicalization_state.py`
- Tests: `tests/test_canonicalization_proposal_workflow.py`

## Completed TASK-038 evidence

- Task: `artifacts/tasks/TASK-038-simulate-bounded-canonicalization-review-lifecycle.md`
- Dry-run: `simulation/dry_runs/20260614_151206-task-038-review-lifecycle-validation.md`
- Lifecycle JSON: `artifacts/reports/canonicalization-review-lifecycle-20260614.json`
- Lifecycle report: `artifacts/reports/canonicalization-review-lifecycle-20260614.md`

## Preserved boundaries

TASK-037 and TASK-038 did not call models, live-fetch data, add sources, add migrations, write to live/default `macro`, implement unit conversion, aggregate frequencies, integrate GDP reports, extract generalized metadata/source frameworks, add provider-specific fact columns, auto-apply accepted mappings, or push to git. TASK-038 also did not change code, tests, schemas, workers, pipelines, the canonical asset manifest base file, or accepted mapping base state.
