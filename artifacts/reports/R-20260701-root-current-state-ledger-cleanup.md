# Root Current-State Ledger Cleanup Report

Date: 2026-07-01
Type: Closeout cleanup / state hygiene
Status: Completed

## Purpose

ProjectForge's root `state/project_state.md` had drifted toward a historical ledger and triggered root context-health/coherence warning. This cleanup preserves useful provenance in a durable report and restores root current-state files to concise pointers.

## Scope

Reviewed and cleaned only ProjectForge root current-state and recovery files:

- `state/project_state.md`
- `state/architecture.md`
- `state/recent_changes.md`
- `context/latest_handoff.md`
- `artifacts/reports/_SUMMARY.md`

No generated templates were modified for this cleanup.
No historical reports were rewritten.
No new architectural subsystem was introduced.

## Content condensed from current state

The following historical/provenance material was removed or condensed from root current-state files and preserved here as durable provenance:

### Prior recent changes ledger

- 2026-06-18: Completed ProjectForge architecture-boundary cleanup for EIP sibling projects. Removed embedded MetaHarvest and obsolete nested MacroForge archive from ProjectForge, retained external MetaHarvest provider at `/home/mkkto/srv/EIP/projects/MetaHarvest`, and updated active config/docs/tests/state so ProjectForge no longer falls back to a hosted MetaHarvest tree.
- 2026-06-15: Implemented bounded ecosystem-autonomy doctrine/schema alignment. Added project autonomy, ownership, anti-monolith/scope extraction, project-creation threshold, recommendation persistence, descriptive registry, future ecosystem context, interface, and infrastructure-as-means doctrine; described the then-current ArchitectureHarvest advisory boundary and candidate task proposals only; added recommendation schema v2 template and future-review note for ecosystem decision registry/ArchitectureHarvest separation. No restructuring, new projects, ArchitectureHarvest split, MacroForge mutation, automation, cross-project task creation, governance authority, or future-project functionality was implemented.
- 2026-06-14: Proposed Framework Improvement Notice Doctrine in `artifacts/reports/R-20260614-framework-improvement-notice-doctrine.md`. The proposal defines significant framework improvements, minimal notice fields, lifecycle states, review-at-relevance expectations, project-local outcomes, summary/handoff/context interaction, explicit prohibitions, risks, and a recommendation for only a future small manual notice artifact convention if separately approved. No automation, propagation, migration, existing-project modification, template change, or enforcement system was created.
- 2026-06-14: Implemented ProjectForge doctrine alignment with the approved constitutional direction. Updated constitution, root agent instructions, README, general/self-management instructions, architecture description, and ArchitectureHarvest constitution to clarify ProjectForge as reusable framework rather than project manager/meta-controller; generated-project autonomy; no silent project mutation; project-local adoption; improvement-flow doctrine; question classes; automation/automation-theater doctrine; framework-change recognition; and ArchitectureHarvest as librarian/reference/evidence/advisory system. Verification before closeout passed with full tests, coherence, and Architecture-to-Reality audit JSON; coherence still reported only the then-existing stale generated `context/active_context.md` warning.
- 2026-06-14: Recorded `AH-FUTURE-001` as a deferred ArchitectureHarvest Evidence Propagation Layer adoption candidate and updated closeout state/handoff/summaries. The candidate was notification-only, must not create tasks/implementation/architecture changes automatically, and remained deferred until MacroForge canonicalization lifecycle was proven. Verification passed with YAML parsing, full tests, coherence, and Architecture-to-Reality audit JSON; coherence still reported only the then-existing stale generated `context/active_context.md` warning.
- 2026-06-05: Added recurring Architecture-to-Reality Audit governance for root and generated projects: dedicated audit tooling, generated-project inheritance, automation cadence/triggers, coherence/context-health integration, permission allowlist updates, docs/instructions/template updates, and tests. Final verification passed with context health, coherence, architecture-reality audit, and full pytest suite.
- 2026-06-01: Made ProjectForge Hermes-native: added root/template `AGENTS.md`, created a local Hermes `projectforge` skill, reframed project creation as Hermes-led adaptive interrogation followed by noninteractive scaffold rendering, fixed model registry/routing YAML, updated tests, and recorded the decision in `artifacts/decisions/D-20260601-hermes-native-project-creation.md`.
- 2026-05-31: v4 added workspace layer, confidence scoring, memory retention, invariant tests, and simplified knowledge graph scope.
- v4 preserved manual GitHub push default, JSONL-first metrics, risk-scaled dry-run, and request-before-generation for specialized agents.

### Condensed root current-state doctrine

Before cleanup, `state/project_state.md` included long current and historical sections for continuity/recovery, context and verification systems, governance permission framework, MetaHarvest provider, ecosystem autonomy, and MetaHarvest boundary. These were condensed into concise current pointers. Stable doctrine remains owned by root architecture/governance documents, templates, and prior reports.

### Architecture state wording

`state/architecture.md` was refreshed from older layer language to the now-complete five-system operating architecture:

1. Project Identity
2. Context and Continuity
3. Governance and Decision
4. Work Execution Methodology
5. Validation and Evidence

This was a closeout alignment of current-state wording, not a redesign.

## Preservation locations

- Historical recent-change ledger: preserved in this report.
- Relocation provenance: remains in `artifacts/reports/R-20260618-eip-relocation-retrospective.md`.
- Framework improvement notice doctrine: remains in `artifacts/reports/R-20260614-framework-improvement-notice-doctrine.md`.
- Hermes-native project creation decision: remains in `artifacts/decisions/D-20260601-hermes-native-project-creation.md`.
- Architecture-to-Reality Audit process evidence: remains in existing architecture audit reports.

## Verification

Verification was run after the cleanup and before final report delivery:

- ProjectForge coherence: passed with no blocks and no warnings.
- ProjectForge context health: passed with no blocks and no warnings.
- ProjectForge architecture reality audit: passed with no blocks and no warnings.
- Full ProjectForge test suite: passed.

## Result

ProjectForge root current-state files now behave like concise current-state pointers instead of historical ledgers. Historical provenance remains durable in reports and decisions.
