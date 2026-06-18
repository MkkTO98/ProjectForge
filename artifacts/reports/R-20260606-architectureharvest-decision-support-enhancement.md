# ArchitectureHarvest Decision-Support Enhancement Report

Date: 2026-06-06
Dry-run: `simulation/dry_runs/20260606_113938-dry-run.md`

## Summary

ArchitectureHarvest was enhanced from a library of analyses into a file-based architectural decision-support system. The new layer lets Hermes start from a problem and traverse to patterns, synthesized records, contradictions, outcomes, relevance maps, and finally deeper source evidence only when needed.

## Files and structures added

### Retrieval layer

- `ArchitectureHarvest/retrieval/problem_catalog.yaml`
- `ArchitectureHarvest/retrieval/retrieval_index.yaml`
- `ArchitectureHarvest/retrieval/recommendation_rules.yaml`
- `ArchitectureHarvest/retrieval/retrieval_policy.md`

These define the query path:

`Problem -> Relevant Patterns -> Relevant Components -> Relevant Projects -> Prior Adoption Outcomes -> Recommendation`

### Problem-first indexing

Added problem-first records for:

- `long_running_agent_state`
- `architecture_decision_reuse`

These are seed entries. Candidate-source links are explicitly marked pending analysis, not evidence claims.

### Pattern maturity framework

Updated templates require:

- `evidence_strength`
- `adoption_count`
- `projects_observed`
- `confidence`
- `maintenance_cost`
- `local_fit`
- `recommendation_strength`
- explanations and limitations

### Contradiction framework

Added:

- `ArchitectureHarvest/contradictions/README.md`
- `ArchitectureHarvest/contradictions/event-sourcing-vs-snapshot-persistence.example.yaml`
- `ArchitectureHarvest/templates/contradiction_record.template.yaml`

Contradiction records capture competing approaches, assumptions, where each wins or loses, and guidance without forcing a winner.

### Outcome weighting framework

Added:

- `ArchitectureHarvest/outcome_models/README.md`
- `ArchitectureHarvest/outcome_models/ecosystem_outcome_model.yaml`
- `ArchitectureHarvest/outcome_models/outcome_weighting.template.yaml`

Outcome weighting separates generic recommendations from recommendations proven successful or unsuccessful inside the ProjectForge ecosystem.

### Lifecycle tracking

Added lifecycle metadata template and lifecycle fields in updated templates:

- `ArchitectureHarvest/templates/lifecycle_metadata.template.yaml`

Tracked fields include `first_seen`, `last_reviewed`, `last_referenced`, `last_adoption`, `adoption_frequency`, and statuses `active`, `dormant`, `stale`, `superseded`, `retired`.

### Cross-project synthesis

Added:

- `ArchitectureHarvest/synthesis/README.md`
- `ArchitectureHarvest/synthesis/checkpointing.example.yaml`
- `ArchitectureHarvest/synthesis/problem-first-decision-support.example.yaml`
- `ArchitectureHarvest/templates/synthesized_pattern.template.yaml`

Synthesized records are now the preferred recommendation source when multiple projects independently converge on a pattern.

### Updated templates

Updated or added:

- `ArchitectureHarvest/templates/pattern_card.template.yaml`
- `ArchitectureHarvest/templates/component_card.template.yaml`
- `ArchitectureHarvest/templates/adoption_candidate.template.yaml`
- `ArchitectureHarvest/templates/adoption_outcome.template.yaml`
- `ArchitectureHarvest/templates/audit_record.template.yaml`
- `ArchitectureHarvest/templates/relevance_map.template.yaml`
- `ArchitectureHarvest/templates/problem_record.template.yaml`
- `ArchitectureHarvest/templates/retrieval_query.template.yaml`
- `ArchitectureHarvest/templates/contradiction_record.template.yaml`
- `ArchitectureHarvest/templates/synthesized_pattern.template.yaml`
- `ArchitectureHarvest/templates/lifecycle_metadata.template.yaml`

### Updated governance and integration documents

- `ArchitectureHarvest/README.md`
- `ArchitectureHarvest/CONSTITUTION.md`
- `ArchitectureHarvest/INTEGRATION.md`
- `CONSTITUTION.md`
- `AGENTS.md`
- `context/context_policy.yaml`

### Tests

Updated:

- `tests/test_architectureharvest_integration.py`

The tests now validate the decision-support structures, YAML parseability, retrieval order, recommendation scales, maturity fields, generated-project ArchitectureHarvest placeholders, and generated-project coherence.

## Design choices

1. File-only retrieval instead of a database/vector store.
   - Reason: matches ArchitectureHarvest v1 constraints, keeps context inspectable, and avoids overengineering.

2. Problem-first retrieval before project reports.
   - Reason: makes Hermes answer architecture questions without loading every analysis or raw cloned repository.

3. Synthesis records as preferred recommendation source.
   - Reason: prevents treating each source project as a monolith and captures convergence across mature projects.

4. Explicit contradiction records.
   - Reason: many architectural decisions are context-dependent. ArchitectureHarvest should preserve tradeoffs rather than declare premature winners.

5. Outcome-weighted recommendations.
   - Reason: external popularity should not outweigh ProjectForge ecosystem evidence, especially maintenance burden and complexity cost.

6. Lifecycle metadata everywhere relevant.
   - Reason: prevents stale conclusions from looking current and supports future review/retirement without deletion.

## Tradeoffs

- The retrieval layer adds more files and template fields, but avoids heavier infrastructure.
- Seed examples are useful for structure and tests, but are not source-analysis evidence.
- Recommendation quality depends on future discipline: pattern cards, synthesis records, relevance maps, and adoption outcomes must be updated after analyses and project decisions.

## Unresolved questions

- Which initial external repositories should be approved for first real analysis remains unresolved. Current candidates remain candidate-only.
- No ProjectForge ecosystem adoption outcomes exist yet for most seed patterns, so some ecosystem-weighted recommendations remain `insufficient_outcome_history`.
- No automated lifecycle audit tool was added in this task; lifecycle tracking is structural/template-based for now.

## Future extension points

- Add a small file-based validation script for ArchitectureHarvest card schemas.
- Add a retrieval-query helper that reads YAML indexes and emits a compact Markdown recommendation.
- Add scheduled lifecycle review using existing ProjectForge/Hermes mechanisms, not a new scheduler.
- Add real synthesized patterns after approved source analyses.
- Mirror successful/failed generated-project adoption outcomes into `ArchitectureHarvest/adoption_log/`.

## Verification

Dry-run validation:

```text
valid: simulation/dry_runs/20260606_113938-dry-run.md
```

Final checks:

```text
parsed 24 ArchitectureHarvest YAML files
3 passed in 0.26s
66 passed in 4.84s
context_health: blocks [], warnings []
check_coherence: blocks [], warnings []
architecture_reality_audit: blocks [], warnings []
```
