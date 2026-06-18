# Commit Boundary Intelligence Future Review Note

Date: 2026-06-15
Status: recorded for future review only
Scope: advisory opportunity; no implementation authorized
Origin: ProjectForge commit-boundary analysis and ArchitectureHarvest ownership review

## Purpose

Record a future ArchitectureHarvest opportunity: advisory commit-boundary intelligence for large, mixed, governance-heavy repositories.

As ProjectForge and ecosystem projects grow, commit boundaries become increasingly difficult to identify manually. Recent commit-boundary analysis required architectural reasoning to determine initiative detection, file-to-initiative mapping, overlap detection, semantic commit grouping, governance-aware commit sequencing, and historical-coherence risks.

The opportunity is to preserve this idea for future review without implementing it now.

## Problem

Manual commit-boundary review becomes fragile when a worktree contains overlapping governance, architecture, template, tooling, state, and generated-summary changes.

Risks include:

- misleading historical commits grouped by chronology rather than ownership or purpose;
- whole-file staging of mixed doctrine/state/template files;
- accidental inclusion of unrelated generated artifacts, lockfiles, local caches, or nested-project changes;
- loss of recommendation/adoption lineage;
- difficulty distinguishing ProjectForge framework changes from autonomous-project or ArchitectureHarvest-owned changes;
- repeated rediscovery of commit-boundary heuristics during future mixed-worktree reviews.

## Potential future ArchitectureHarvest capability

ArchitectureHarvest could eventually provide advisory commit-boundary intelligence, including:

- initiative detection;
- repository change clustering;
- file-to-initiative mapping;
- mixed-file overlap analysis;
- semantic commit-boundary recommendations;
- governance-aware commit sequencing;
- historical-coherence analysis;
- warnings for changes that should remain separate by project ownership, purpose, or governance authority.

## Expected benefit

- Improve repository history quality.
- Reduce accidental historical distortion.
- Make large governance/template/tooling work easier to review.
- Preserve project-autonomy boundaries during commit planning.
- Help identify when ownership-by-purpose is a better organizing principle than chronological development history.

## Explicit non-goals

This opportunity does not authorize:

- automatic staging;
- automatic commits;
- automatic repository mutation;
- automatic approval;
- cross-project task creation;
- ArchitectureHarvest governance over target projects;
- repository restructuring;
- splitting ArchitectureHarvest;
- creating a new project.

The capability, if ever approved, must remain advisory only.

## Ownership hypothesis for future review

This capability appears more naturally aligned with ArchitectureHarvest than ProjectForge if its purpose remains valid across multiple consuming projects.

Rationale:

- commit-boundary intelligence is a reusable architectural/repository-history reasoning capability;
- it can consume project-specific governance context without owning that governance;
- it can produce recommendations without staging, committing, or modifying repositories;
- it remains useful if ProjectForge is not the consuming project.

Counterpoint:

ProjectForge may still need local commit hygiene rules for its own repository and generated-project framework work. A future separation should distinguish ArchitectureHarvest-owned advisory reasoning from ProjectForge-owned local git/governance procedures.

## Future review triggers

Revisit this opportunity if one or more occur:

- mixed-worktree commit-boundary reviews become frequent;
- multiple autonomous projects require similar commit-boundary analysis;
- ArchitectureHarvest begins serving multiple consuming projects with repository-history recommendations;
- manual hunk-staging plans repeatedly require architectural ownership analysis;
- repository history quality becomes a measurable bottleneck for long-term maintainability.

## Future review questions

- What minimal artifact schema would capture initiative clusters, ownership, overlaps, exclusions, confidence, and recommended commit sequencing?
- Should commit-boundary recommendations live beside ArchitectureHarvest recommendation records, or in a separate advisory class?
- What inputs are allowed: git status/diff only, governance docs, ArchitectureHarvest records, project registry, or session history?
- How should advisory output preserve lineage without becoming an implementation plan?
- What safeguards prevent advisory recommendations from becoming automatic repository mutation?

## Boundary

This note is not a task, implementation plan, doctrine change, project-creation proposal, or approval to build the capability.

Any future implementation requires explicit human approval, project-local review by the consuming project, and preservation of advisory-only boundaries.
