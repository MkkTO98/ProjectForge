# Ecosystem Future Review Note

Date: 2026-06-15
Status: recorded for future review only
Scope: doctrine note; no implementation authorized

## Purpose

Record two bounded future ecosystem review opportunities without implementing either one.

## Future review opportunity 1: ecosystem-level decision registry

A future ecosystem-level decision registry may become useful if multiple autonomous projects begin exchanging recommendations, adoption outcomes, interface contracts, and supersession lineage.

Review trigger examples:

- recommendation history becomes difficult to discover across projects;
- project-local decision records diverge on shared ecosystem interfaces;
- repeated recommendations are rediscovered because rejection/adoption lineage is fragmented;
- registry ownership can be decided without creating a meta-controller.

Boundaries:

- do not implement now;
- do not grant governance authority to ProjectForge, EIP, or any future project by default;
- preserve project-local decision authority;
- treat any registry as descriptive unless a future governance decision explicitly says otherwise.

## Future review opportunity 2: ArchitectureHarvest separation

ArchitectureHarvest is currently hosted within ProjectForge as an advisory subsystem. It is conceptually separable and may warrant future independent operation if its purpose, lifecycle, artifact model, governance, and consumers become distinct enough from ProjectForge.

Review trigger examples:

- ArchitectureHarvest serves multiple autonomous projects with materially different governance needs;
- recommendation persistence, source analysis, and target relevance maps require a lifecycle independent of ProjectForge releases;
- ArchitectureHarvest maintenance burden or scope creates pressure on ProjectForge's framework purpose;
- clear interfaces exist for recommendations, notifications, review outcomes, and adoption outcomes.

Boundaries:

- do not split ArchitectureHarvest now;
- do not create an independent ArchitectureHarvest project now;
- do not add runtime behavior, automation, propagation, or task creation;
- if separation is later proposed, it requires explicit human approval and a separate architecture review.
