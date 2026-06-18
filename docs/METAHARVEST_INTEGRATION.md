# ProjectForge MetaHarvest Integration Behavior

ProjectForge owns this file. It defines how ProjectForge consumes the external MetaHarvest provider.

## Provider model

Active provider path:

```text
/home/mkkto/srv/EIP/projects/MetaHarvest
```

Current implementation state:

```text
external sibling provider active
```

ProjectForge may be configured for an external MetaHarvest provider. ProjectForge tooling uses `/home/mkkto/srv/EIP/projects/MetaHarvest` as the active provider and does not silently fall back to an embedded MetaHarvest copy while provider status is active.

## ProjectForge-owned responsibilities

ProjectForge owns:

- project scaffolding;
- generated-project templates;
- generated-project coherence checks;
- ProjectForge-local governance and state;
- ProjectForge-local integration behavior;
- generated-project compatibility placeholders under `architecture/architectureharvest/`.

ProjectForge does not own MetaHarvest's autonomous purpose, recommendation authority boundaries, source-analysis knowledge, or long-term artifact lifecycle after extraction.

## Generated-project compatibility

ProjectForge must continue generating this compatibility path:

```text
architecture/architectureharvest/
```

Required generated placeholders:

```text
architecture/architecture_state.md
architecture/architecture_decisions/
architecture/architecture_reviews/
architecture/architectureharvest/relevance_map.yaml
architecture/architectureharvest/adoption_candidates.md
architecture/architectureharvest/rejected_candidates.md
architecture/architectureharvest/review_history.md
architecture/architectureharvest/adoption_outcome.template.yaml
```

This path remains intentionally stable as a generated-project compatibility layer.

## External provider interface

ProjectForge's minimum provider contract is:

```text
README.md
CONSTITUTION.md
INTEGRATION.md
source_registry.yaml
retrieval/problem_catalog.yaml
retrieval/retrieval_index.yaml
retrieval/recommendation_rules.yaml
```

ProjectForge root coherence validates that the active external provider path exists and exposes the required provider interface. When provider status is active, validation must resolve through `/home/mkkto/srv/EIP/projects/MetaHarvest` and must not silently fall back to an embedded ProjectForge copy.

ProjectForge tests should validate the interface contract, not assume ownership of all MetaHarvest internals.

## Source-cache policy

Configured local source cache root:

```text
/home/mkkto/srv/EIP/projects/ProjectForge/external_sources
```

ProjectForge treats this as optional, replaceable storage. MetaHarvest's `source_registry.yaml` may contain absolute local paths to this cache root, but those paths are cache hints rather than canonical source identity. Normal ProjectForge/MetaHarvest consultation must not require the cache directory to exist.

## Authority boundary

MetaHarvest remains advisory only.

ProjectForge may consult MetaHarvest during:

- new project creation;
- architecture definition;
- major architecture modifications;
- introduction of new subsystems;
- creation of new agent roles;
- memory/context system design;
- orchestration design;
- permission system design;
- workflow redesign;
- scheduled architecture reviews;
- repeated implementation failures;
- user-requested improvement scans;
- reusable non-domain concept, vocabulary, methodology, decision-pattern, governance-pattern, or heuristic reviews.

ProjectForge does not require MetaHarvest for:

- bug fixes;
- minor documentation changes;
- test additions;
- small utilities;
- implementation work that does not alter architecture.

MetaHarvest may recommend. ProjectForge decides through ProjectForge governance.

## Compatibility invariant

Normal ProjectForge consumption must not:

- modify MacroForge;
- modify consumer projects;
- stage or commit changes without explicit approval;
- rewrite historical `ArchitectureHarvest` references.
