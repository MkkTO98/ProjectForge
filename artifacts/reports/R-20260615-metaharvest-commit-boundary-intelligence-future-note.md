# MetaHarvest Commit Boundary Intelligence Future Review Note

Date: 2026-06-15
Status: recorded for future review only
Scope: advisory opportunity; no implementation authorized

## Context

Recent commit-boundary analysis required significant architectural reasoning to identify:

- initiatives;
- overlaps;
- ownership boundaries;
- semantic commit grouping;
- governance-aware commit sequencing;
- historical-coherence risks.

This suggests a possible future MetaHarvest capability: advisory commit-boundary intelligence.

## Potential future capability

MetaHarvest could eventually help preserve semantic repository history by producing advisory analysis such as:

- initiative detection;
- architectural change clustering;
- overlap analysis;
- ownership-boundary detection;
- mixed-file and mixed-hunk warnings;
- commit-boundary recommendations;
- semantic-history preservation guidance;
- governance-aware commit sequencing;
- historical-coherence analysis.

## Rationale

Commit boundaries are not just git mechanics in governance-heavy repositories. They encode historical meaning, ownership, intent, and reviewability.

As ProjectForge, MetaHarvest, and autonomous projects evolve, worktrees may contain overlapping changes across doctrine, templates, state, tooling, generated summaries, and future-review artifacts. Manual grouping by chronology can distort architecture history.

MetaHarvest is a plausible future owner of advisory commit-boundary intelligence because the capability is reusable non-domain knowledge and remains valid across consuming projects.

## Explicit non-goals

This note does not authorize:

- automatic staging;
- automatic commits;
- automatic approval;
- repository mutation;
- branch mutation;
- task creation;
- implementation planning;
- project restructuring;
- governance authority.

The capability would remain advisory only.

## Ownership boundary

MetaHarvest could own reusable commit-boundary reasoning patterns and recommendation generation.

Each consuming project would retain ownership of:

- whether to follow the recommendation;
- what to stage;
- what to commit;
- whether to split or defer work;
- project-local git policy.

## Future review questions

- What minimum inputs are acceptable: git diff, status, governance docs, project registry, session history, or all of them?
- Should output be a recommendation artifact, report, or lightweight review note?
- How should confidence be represented without encouraging blind adoption?
- How should the capability avoid becoming automatic repository mutation?
- How should it handle generated files and summaries?
- Should it identify ownership-by-purpose conflicts explicitly?

## Boundary

This is not a task, implementation plan, schema proposal, or approval to build the capability.
