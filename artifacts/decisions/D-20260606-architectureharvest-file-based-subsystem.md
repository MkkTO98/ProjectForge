# Decision: Create file-based ArchitectureHarvest subsystem

Date: 2026-06-06
Status: accepted-for-scaffold

## Context

ProjectForge needs a reusable way to harvest architectural judgment from mature open-source projects without turning external research into token-heavy notes or an uncontrolled implementation driver.

The user requested `ArchitectureHarvest` as a ProjectForge subsystem focused first on ProjectForge/agent systems, with lightweight MacroForge relevance placeholders where obviously applicable.

## Decision

Create `ArchitectureHarvest/` as a file-based v1 subsystem in the ProjectForge root.

The subsystem will use:

- Markdown constitution, README, indexes, reports, and human summaries
- YAML source registry, templates, cards, relevance maps, and recommendations
- generated JSON audit outputs when tools are added later
- raw third-party clones outside the ProjectForge git-tracked tree, under `/home/mkkto/srv/projectforge/external_sources/`

The initial source list is candidate-only:

- OpenHands
- LangGraph
- Aider
- SWE-agent
- AutoGen

No repository is approved or cloned by this decision.

## Rationale

This keeps ArchitectureHarvest local-first, auditable, token-budget-aware, and compatible with Hermes and GitHub while preventing premature database/vector/UI/dashboard complexity.

It also creates a reusable negative-knowledge path (`rejected/`, `retired/`, `rejected_index.md`) so Hermes does not repeatedly rediscover unsuitable patterns.

## Constraints

- File-based v1 only.
- No database, vector store, UI, dashboard, or autonomous discovery daemon.
- No paid services or mandatory cloud dependency.
- No third-party code execution without separate approval.
- Cloned repositories must live outside the git-tracked ProjectForge tree.
- ArchitectureHarvest may create recommendations but must not directly modify ProjectForge or MacroForge from research findings.

## Consequences

Future major architecture work, new subsystem work, repeated failure cycles, project creation, and scheduled reviews may consult ArchitectureHarvest when relevant.

Implementation of any adoption candidate remains subject to normal ProjectForge approval, dry-run, tests, and coherence gates.
