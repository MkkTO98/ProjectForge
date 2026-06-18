# Decision: Integrate ArchitectureHarvest as architectural advisory service

Date: 2026-06-06
Status: accepted

## Context

ArchitectureHarvest was scaffolded as a file-based subsystem. To avoid becoming a passive research repository, it needs explicit ProjectForge lifecycle integration and a feedback loop from target projects.

## Decision

ArchitectureHarvest is now a first-class ProjectForge architectural advisory service and feedback repository.

ProjectForge and generated projects consult ArchitectureHarvest at architectural decision points: project creation, architecture definition, major architecture changes, new subsystems, new agent roles, memory/context/orchestration/permission/workflow design, scheduled reviews, repeated failures, and user-requested scans.

Generated projects receive lightweight local architecture and ArchitectureHarvest placeholders under `architecture/`.

ArchitectureHarvest adoption outcomes are recorded locally by target projects and mirrored to `ArchitectureHarvest/adoption_log/` when generally useful.

## Non-goals

- No mandatory participation in ordinary implementation tasks.
- No autonomous refactoring campaigns.
- No bypassing project decisions, dry-runs, approvals, tests, or coherence.
- No database, vector store, dashboard, UI, or continuous scanner.
- No MacroForge implementation changes.

## Consequences

Project creation, architecture reviews, and major governance work now have a standard ArchitectureHarvest consultation point. Individual projects remain responsible for operational and implementation decisions.
