# Ecosystem Infrastructure Future Review Note

Date: 2026-06-15
Status: recorded for future review only
Scope: question preservation; no implementation authorized

## Observation

The ProjectForge ecosystem is beginning to expose responsibilities that are neither ordinary project-local knowledge nor MetaHarvest-owned reusable non-domain knowledge.

Emerging responsibilities include:

- project registries;
- recommendation registries;
- active interface contracts;
- ecosystem lineage;
- ecosystem-level decisions;
- project relationship metadata;
- cross-project recommendation status;
- shared compatibility/versioning expectations.

These responsibilities may eventually form an ecosystem infrastructure layer.

## Current conclusion

This does not yet justify a project.

ProjectForge may continue hosting limited descriptive registry and ecosystem-context responsibilities as a framework convenience while the ecosystem remains small and while no dedicated ecosystem-level owner has been approved.

This note does not assign future ownership to EII, MetaHarvest, ProjectForge, or any other project. EIP means the ecosystem, not a project owner.

## Future review question

Should ecosystem infrastructure remain shared infrastructure, or eventually require a dedicated owner?

Subquestions:

- Which responsibilities are live ecosystem state rather than reusable knowledge?
- Which responsibilities require governance authority, and therefore cannot belong to an advisory-only system?
- Which responsibilities are merely descriptive registries versus active contracts?
- At what scale does ProjectForge-hosted descriptive infrastructure become inappropriate?
- Would a dedicated owner improve coherence, or create unnecessary project fragmentation?

## Boundary distinctions

MetaHarvest may preserve reusable patterns about ecosystem infrastructure.

MetaHarvest should not automatically own active ecosystem infrastructure such as live registries, active interface contracts, ecosystem decisions, or compatibility commitments.

ProjectForge may host descriptive registry duties temporarily, but hosting does not imply permanent ownership or authority over registered projects.

EII, if ever created, is provisionally a consumer/synthesizer/recommender, not a governor of ecosystem infrastructure by default. EIP means the ecosystem as a whole.

## Explicit non-goals

This note does not authorize:

- project creation;
- interface implementation;
- registry implementation;
- schema creation;
- infrastructure automation;
- ecosystem governance changes;
- assignment of ownership;
- repository restructuring.

## Future review triggers

Revisit if:

- multiple autonomous projects depend on shared active contracts;
- registry updates become frequent or safety-critical;
- recommendation lineage spans several projects;
- compatibility/versioning expectations need enforcement or arbitration;
- ProjectForge-hosted descriptive infrastructure begins to look like governance authority;
- ecosystem infrastructure becomes a bottleneck to maintainability.
