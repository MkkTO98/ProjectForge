# Task: ArchitectureHarvest first analysis batch proposal

Task ID: T-20260606-architectureharvest-initial-analysis-batch
Status: proposed
Created: 2026-06-06
Owner: Hermes / user approval required

## Goal

Analyze the first ArchitectureHarvest source batch after explicit repository approval:

- OpenHands
- LangGraph
- Aider
- SWE-agent
- AutoGen

## Why this batch

These projects are mature or influential examples in agent systems, coding agents, graph/state-machine orchestration, issue-solving loops, and multi-agent coordination. They are likely to contain reusable patterns for ProjectForge and some lightweight relevance for MacroForge.

## Approval boundary

Current status: candidate-only.

Do not clone any repository until the user approves one or more candidates and `ArchitectureHarvest/source_registry.yaml` is updated from `candidate` to `approved` for those sources.

After approval, clones must be placed under:

```text
/home/mkkto/srv/projectforge/external_sources/
```

Do not execute external repository code, install dependencies, run package scripts, run Docker, or run networked build commands without separate approval.

## Proposed analysis sequence

1. Confirm approval scope: all five repositories or a smaller first pair.
2. Update approved sources in `ArchitectureHarvest/source_registry.yaml` with approval date and intended local paths.
3. Clone approved repositories into `/home/mkkto/srv/projectforge/external_sources/`.
4. Record latest seen commit and last cloned commit for each approved source.
5. Inspect repository metadata and license files first.
6. Inspect high-level docs and architecture/design docs before source files.
7. Produce the four required layers for each analyzed source:
   - human summary in `ArchitectureHarvest/projects/`
   - project card in `ArchitectureHarvest/project_cards/`
   - component cards in `ArchitectureHarvest/component_cards/`
   - deep report in `ArchitectureHarvest/reports/`
8. Extract cross-project patterns into `ArchitectureHarvest/pattern_library/` when overlapping solutions are found.
9. Create ProjectForge relevance maps under `ArchitectureHarvest/relevance_maps/projectforge/`.
10. Add lightweight MacroForge relevance maps under `ArchitectureHarvest/relevance_maps/macroforge/` when obvious.
11. Create adoption/simplification/replacement/deletion/rejection candidates as appropriate.
12. Update indexes and source registry statuses/staleness fields.
13. Run ProjectForge coherence checks and YAML parsing verification.

## Initial analysis questions

- Which projects solve problems ProjectForge currently handles with homemade infrastructure?
- Which patterns would simplify ProjectForge rather than expanding it?
- Which patterns should become negative rules because they are too cloud-first, enterprise-heavy, or multi-agent-heavy for the local solo-developer constraints?
- Which patterns are only useful as principles, not dependencies or copied code?
- Which patterns could later help MacroForge without pulling MacroForge into platform overengineering?

## Definition of done for the first approved source

- Source registry updated with approval/cloned/analyzed metadata.
- License captured with reuse classification.
- Human summary written.
- Project card written and valid YAML.
- At least three component cards written unless the repository evidence justifies fewer.
- Deep report written with evidence files and analysis limitations.
- ProjectForge relevance map written.
- MacroForge relevance placeholder written if obvious.
- At least one adoption/rejection/simplification candidate or explicit no-adoption rationale written.
- Indexes updated.
- Coherence and YAML verification pass.
