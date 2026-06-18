# MetaHarvest Conceptual Evolution Review

Date: 2026-06-15
Status: accepted for bounded doctrine/purpose alignment
Scope: conceptual rename and purpose refinement only
Physical name: `ArchitectureHarvest/` remains unchanged
Conceptual name: MetaHarvest, formerly ArchitectureHarvest

## Review question

Does `MetaHarvest` better describe the durable purpose than `ArchitectureHarvest`?

## Finding

Yes, as a conceptual rename. Defer physical repository/directory/package renaming.

ArchitectureHarvest's actual and intended role now extends beyond architecture patterns. It is expected to discover, preserve, organize, analyze, and recommend reusable non-domain knowledge, including architecture patterns, interface patterns, shared concepts/vocabulary, methodologies, decision patterns, governance patterns, and heuristics.

Using ownership-by-purpose, these categories remain one coherent advisory knowledge-harvesting purpose. They do not justify separate projects such as InterfaceHarvest, ConceptHarvest, MethodologyHarvest, DecisionHarvest, GovernanceHarvest, or HeuristicHarvest.

## Refined purpose

MetaHarvest exists to discover, preserve, analyze, organize, and recommend reusable non-domain knowledge extracted from projects, systems, architectures, implementations, successes, failures, concepts, methodologies, interfaces, governance structures, decision patterns, and heuristics.

MetaHarvest is an advisory knowledge source. It provides evidence, patterns, concepts, vocabulary, methodologies, decision lessons, governance lessons, heuristics, and recommendations for project-local review.

MetaHarvest does not govern projects, enforce standards, create tasks inside projects, automatically adopt recommendations, automatically implement changes, or modify target projects. Projects remain autonomous.

## Knowledge category assessment

Recommended explicit categories:

- Architecture Pattern: stable; remains central.
- Interface Pattern: coherent; useful for separation/interface-first design.
- Shared Concept: coherent; preserves meaning without standardizing it.
- Shared Vocabulary: coherent; should record usage and commonality, not mandate terminology.
- Shared Methodology: coherent; captures repeatable workflows and evaluation methods.
- Decision Pattern: coherent; captures recurring decision shapes such as accept/reject/defer/provisional/adopt narrowly.
- Governance Pattern: coherent; captures reusable governance structures such as project autonomy and ownership-by-purpose.
- Heuristic: coherent but should remain lightweight; heuristics are decision aids, not rules.

Recommended missing category:

- Anti-pattern / Failure Pattern: already partially present in ArchitectureHarvest, but should remain explicit because failures often teach more than successes.

Recommended merge guidance:

- Shared Concept and Shared Vocabulary can remain separate in reasoning, but they do not need separate storage yet.
- Governance Pattern and Heuristic overlap. Governance patterns are durable structures; heuristics are lightweight rules of thumb.
- Decision Pattern may be a subtype of methodology in some cases, but it is important enough to name explicitly.

No new storage systems or artifact types are required now.

## Shared concepts and vocabulary

MetaHarvest should preserve reusable ecosystem concepts such as Evidence, Observation, Claim, Confidence, Canonical, Derived, Accepted, Provisional, Review, Mapping, Source, and Artifact.

The goal is preservation of meaning, observed usage, and commonality. It is not standardization or enforcement.

This aligns with project autonomy because consuming projects may evaluate and adopt terminology locally. MetaHarvest may recommend vocabulary alignment when it improves clarity, but it must not impose terms.

## Shared methodology

MetaHarvest should explicitly preserve reusable methodologies such as review workflows, validation workflows, recommendation evaluation processes, experimentation procedures, uncertainty handling approaches, and decision documentation approaches.

These are advisory patterns. They help projects avoid rediscovering reliable workflows but do not become governance mandates unless adopted by the receiving project.

## Decision patterns

Decision-pattern harvesting belongs naturally inside MetaHarvest.

Examples include accept, reject, defer, provisional acceptance, escalation, high-impact review routing, adopt narrowly, supersede, retire, and request more evidence.

Decision patterns are reusable non-domain knowledge. They preserve how projects reason under uncertainty, risk, evidence, governance constraints, and reversibility.

## Governance patterns

Governance-pattern harvesting belongs inside MetaHarvest when bounded as advisory knowledge.

Examples include ownership-by-purpose, advisory-only ecosystems, project autonomy, extraction-before-expansion, interface-first separation, recommendation persistence, and descriptive registries.

Risk: governance patterns can be mistaken for cross-project authority. Boundary: MetaHarvest may preserve and recommend governance patterns, but each project decides whether to adopt them.

## Heuristics

MetaHarvest should preserve reusable heuristics when they are evidence-backed, contextual, and non-mandatory.

Examples include define interfaces before separation, prefer extraction over expansion, avoid ownership-by-history, preserve semantic commit history, and choose the smallest test that reduces architectural uncertainty.

Heuristics are useful because they compress hard-won judgment. They are risky when stripped of context or treated as rules. Each heuristic should retain applicability conditions, failure modes, and confidence where meaningful.

## Non-domain boundary

MetaHarvest must remain non-domain. It should not become a repository for domain knowledge such as GDP analysis, inflation analysis, energy-market conclusions, macroeconomic findings, investment theses, company research, or domain-specific evidence.

Allowed: reusable non-domain patterns discovered while working on domain projects.

Not allowed: the domain conclusions themselves.

Example: A MacroForge workflow for validating canonicalization proposals may become a MetaHarvest methodology pattern. A conclusion about GDP comparability or inflation dynamics remains MacroForge domain knowledge.

## Implementation recommendation

Implement bounded doctrine/purpose wording only:

1. Conceptual rename: `MetaHarvest (formerly ArchitectureHarvest)`.
2. Purpose refinement from architecture-only to reusable non-domain knowledge harvesting.
3. Explicit advisory-only and project-autonomy boundaries.
4. Explicit non-domain boundary.
5. No physical rename, no repository restructuring, no project split, no new projects, no mandatory standards, no governance authority.

## Future doctrine recommendation

Future ecosystem doctrine should eventually consider the guidance:

"MetaHarvest is responsible for discovering and preserving reusable non-domain knowledge across projects, while remaining advisory-only."

Recommendation: keep as guidance now. Consider constitutional doctrine only after the conceptual rename proves useful and after shared-interface and non-domain boundary edge cases are tested.

## Risks

- Conceptual rename may create temporary naming ambiguity while the directory remains `ArchitectureHarvest/`.
- `MetaHarvest` may sound too broad and invite knowledge-hoarding.
- Non-domain boundary must remain explicit to avoid absorbing MacroForge/EIP/domain knowledge.
- Governance-pattern harvesting may be misread as governance authority.
- Heuristics may become slogans if detached from evidence and applicability conditions.
- Future physical rename could create noisy git history and broken references if done prematurely.

## Open questions

- When, if ever, should the physical directory be renamed?
- Should future schemas add a `knowledge_category` field, or is current template metadata sufficient?
- How should shared vocabulary records avoid becoming mandatory standards?
- What review trigger would justify revisiting physical separation or renaming?
- Should MetaHarvest index project-local patterns by pointer rather than copying content?

## Explicit non-actions

This review does not authorize project splitting, physical renaming, repository restructuring, MacroForge changes, EIP changes, cross-project control, mandatory standards, automatic staging, automatic commits, automatic task creation, or automatic implementation.
