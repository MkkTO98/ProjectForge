# Decision: ArchitectureHarvest Decision-Support Layer

Date: 2026-06-06
Status: accepted for file-based v1 implementation

## Context

ArchitectureHarvest already stored project analyses, component analyses, pattern analyses, relevance maps, adoption candidates, and adoption outcomes. That made it useful as a library, but not yet sufficient as a reusable architectural decision-support system.

The new requirement is that Hermes can ask: given a problem, which patterns should ProjectForge consider, why, how strong is the evidence, what tradeoffs exist, and what has historically worked inside this ecosystem?

## Decision

ArchitectureHarvest will use a strictly file-based decision-support layer built from Markdown and YAML:

1. Problem-first retrieval under `ArchitectureHarvest/retrieval/`.
2. Cross-project synthesized pattern records under `ArchitectureHarvest/synthesis/`.
3. Contradiction records under `ArchitectureHarvest/contradictions/`.
4. Outcome weighting models under `ArchitectureHarvest/outcome_models/`.
5. Lifecycle metadata on problems, patterns, relevance records, contradictions, and outcomes.
6. Updated templates requiring maturity, evidence, local-fit, lifecycle, anti-problem, and outcome-weighting fields.

The consultation order is:

1. problem catalog
2. retrieval index
3. synthesized patterns
4. contradiction records
5. adoption outcomes/outcome models
6. target relevance maps
7. project/component/deep reports only if compact records are insufficient

## Rationale

This preserves ArchitectureHarvest's local-first, token-budget-aware design while making it queryable by problem rather than by source project. It avoids databases, embeddings, dashboards, web UIs, agent swarms, autonomous GitHub crawling, and automatic discovery.

The design also prevents false confidence by requiring explicit evidence strength, confidence, evidence quality, limitations, lifecycle status, and separation between generic recommendations and recommendations proven inside the ProjectForge ecosystem.

## Tradeoffs

Benefits:
- Hermes can answer architecture questions from compact indexes before reading large reports.
- Cross-project synthesis reduces pattern duplication.
- Contradiction records preserve tradeoffs without forcing a winner.
- Outcome models create a feedback loop from ProjectForge ecosystem experience.
- Lifecycle metadata helps identify stale, dormant, superseded, and retired recommendations.

Costs:
- More YAML templates must be maintained.
- Seed records are not yet backed by external repository analysis.
- The retrieval layer depends on disciplined updates after future analyses and adoption outcomes.

## Boundaries

No external repositories were approved, cloned, installed, built, or executed by this decision.

ArchitectureHarvest remains advisory only. Implementation work in ProjectForge, MacroForge, or generated projects still requires normal decision, dry-run, test, and coherence gates.

## Verification

- ArchitectureHarvest YAML parse check: `parsed 24 ArchitectureHarvest YAML files`
- Targeted tests: `3 passed in 0.28s`
- Full tests: `66 passed in 5.18s`
