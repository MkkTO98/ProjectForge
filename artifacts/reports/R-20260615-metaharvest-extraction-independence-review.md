# MetaHarvest Extraction Independence and Ecosystem-Root Dependency Review

Date: 2026-06-15
Status: bounded architecture and doctrine review
Permission level: L4 conceptual review; no extraction or implementation
Scope: MetaHarvest sibling-project readiness, EIP-root dependency, dependency classification, ownership/interface independence, evolution interface, extraction readiness, and doctrine guidance

## Explicit non-actions

This review does not authorize or perform:

- commits;
- staging;
- directory moves;
- directory renames;
- MetaHarvest extraction;
- project creation;
- ecosystem infrastructure implementation;
- EIP root adoption;
- ProjectForge hosting-behavior changes;
- contract implementation;
- service implementation;
- schema implementation.

## Governance visibility

FOUNDATIONAL_GOVERNANCE_WARNING
PERMISSION_LEVEL=L4
CATEGORY=FOUNDATIONAL
PROJECT=MetaHarvest / EIP ecosystem / ProjectForge
DECISION=MetaHarvest extraction independence from neutral EIP root adoption

Impact:
This review evaluates whether MetaHarvest could become a sibling project before the future EIP ecosystem root exists physically.

Risk:
Treating extraction as dependent on root adoption could create artificial sequencing friction. Treating extraction as independent without operational preparation could create path, evidence, lineage, and authority-boundary breakage.

Required approval:
STOP. This artifact is analysis and doctrine guidance only. Physical extraction, root adoption, directory movement, contracts, services, schemas, infrastructure, and ProjectForge hosting changes are prohibited without explicit foundational approval.
END_FOUNDATIONAL_GOVERNANCE_WARNING

## Executive conclusion

MetaHarvest extraction readiness is logically independent from neutral EIP root adoption.

The two decisions are related but not coupled:

- MetaHarvest becoming a sibling project is primarily a project-boundary decision.
- EIP root adoption is primarily an ecosystem-structure and infrastructure-placement decision.

MetaHarvest may conceptually become a sibling project before adoption of a neutral EIP root if purpose, ownership, authority, and conceptual interfaces are clear and operational migration risks are handled.

However, physical extraction is still not ready today because operational blockers remain: path inventory, compatibility planning, evidence-reference strategy, generated-project placeholder naming, historical-reference interpretation, and verification/rollback planning.

## 1. Extraction-independence assessment

Doctrine candidate:

```text
MetaHarvest may become a sibling project before adoption of a neutral EIP root.
```

Assessment: sound as guidance.

### Benefits

- Avoids artificial dependency between two different architectural decisions.
- Allows MetaHarvest autonomy to be evaluated by purpose and interfaces rather than filesystem idealism.
- Prevents neutral-root adoption from becoming a prerequisite for every project-boundary cleanup.
- Keeps EIP-root adoption as a separate foundational ecosystem decision.
- Allows incremental migration: hosted subsystem -> sibling project in an interim location -> later EIP-root relocation if approved.
- Makes ProjectForge de-hosting easier because MetaHarvest independence can be tested before full ecosystem restructuring.

### Risks

- A sibling without an EIP root may live in an ad hoc location that later needs another move.
- Without root-level doctrine, people may still infer ownership from physical location.
- If placed next to ProjectForge under `/home/mkkto/srv/`, its relationship to the future EIP root may remain ambiguous.
- Extraction before infrastructure ownership is resolved could accidentally make MetaHarvest own active contracts or registries.
- Two-step migration may increase path churn if eventual EIP-root adoption happens later.

### Migration implications

Extraction before EIP-root adoption would require an interim placement decision, such as:

- sibling under `/home/mkkto/srv/`;
- sibling under another approved neutral location;
- remain hosted until EIP root exists.

The key is that interim placement must be explicitly non-authoritative. Physical location must not imply ownership.

### Ownership implications

The already defined ownership boundaries are sufficient conceptually:

- MetaHarvest owns reusable non-domain knowledge and advisory recommendation lineage.
- Consumers own local adoption/rejection/implementation/governance.
- Ecosystem infrastructure owns active shared contracts/registries/compatibility definitions if such infrastructure is approved later.

No EIP root is required for this ownership model to be valid.

### Governance implications

Extraction is still L4 foundational because it changes project boundaries and physical project structure.

EIP-root adoption is also L4, but it is a separate L4 decision.

They can be reviewed independently. Approval for one must not imply approval for the other.

### Ecosystem implications

An extracted MetaHarvest can participate as a sibling using conceptual interfaces before the ecosystem has a physical root. The ecosystem can remain a conceptual governance boundary until root adoption is justified.

Recommendation:
Accept the candidate as migration-planning guidance, not yet constitutional doctrine.

confidence = 0.86
priority = 0.74

## 2. Dependency classification

### EIP root adoption

Classification: Helpful, not required.

Rationale:
A neutral root would provide a clean home and reduce ownership-by-location ambiguity, but MetaHarvest's autonomy depends on purpose, ownership, and interfaces. It can become a sibling in an interim approved location before an EIP root exists.

### Ecosystem infrastructure placement

Classification: Helpful for long-term cleanliness; not required if active infrastructure is not moved or created.

Rationale:
MetaHarvest extraction does not require ecosystem registries, contracts, or metadata infrastructure. It requires avoiding accidental ownership of them. If extraction only moves MetaHarvest-owned knowledge and leaves unresolved infrastructure unresolved, placement can remain deferred.

### Registry ownership decisions

Classification: Helpful; required only if extraction would move or redefine registries.

Rationale:
Current registries are descriptive and ProjectForge-hosted. MetaHarvest extraction does not need registry ownership unless extraction attempts to make MetaHarvest the registry owner or move active/descriptive registry artifacts. Avoid doing that.

### Future EII creation

Classification: Unrelated.

Rationale:
EII is a future user-facing intelligence project. MetaHarvest's boundary is advisory non-domain knowledge. EII creation should not block MetaHarvest extraction.

### Future ResearchMemory creation

Classification: Unrelated.

Rationale:
ResearchMemory would own research conclusions and epistemic history if approved. MetaHarvest owns reusable non-domain methods/patterns. ResearchMemory's future existence does not determine MetaHarvest's extraction readiness.

### Future project-creation workflow changes

Classification: Helpful, not required.

Rationale:
Explicit location selection would make future sibling-project creation cleaner, but MetaHarvest extraction can be approved as a one-off foundational migration before the general workflow is updated. The extraction decision must include its own explicit location choice.

### Active recommendation/adoption contracts

Classification: Helpful; not required if conceptual interfaces remain non-contractual.

Rationale:
Extraction can occur with documented conventions and explicit non-authority boundaries. Contracts become required only if multiple projects must rely on stable machine-readable exchange obligations.

### Path-dependency inventory

Classification: Required.

Rationale:
Physical extraction would break ProjectForge-relative references unless all relevant paths are inventoried and compatibility handled.

### Evidence-reference strategy

Classification: Required.

Rationale:
MetaHarvest's value depends on evidence and lineage. Extraction cannot reasonably occur if evidence pointers become ambiguous, broken, or ownership-violating.

### Verification and rollback plan

Classification: Required.

Rationale:
Physical extraction is filesystem/repository restructuring. It requires clear verification and rollback before execution.

## 3. Ownership-consistency assessment

The current ownership classes are sufficient to support sibling status conceptually.

### MetaHarvest-owned

Stable and coherent:

- reusable non-domain knowledge;
- patterns;
- concepts;
- methodologies;
- heuristics;
- governance patterns;
- decision patterns;
- recommendation rationale;
- recommendation lineage;
- reusable negative knowledge;
- generalized adoption/rejection lessons.

### Consumer-owned

Stable and coherent:

- adoption;
- rejection;
- modification;
- implementation;
- scheduling;
- local governance;
- local priorities;
- local verification;
- project purpose interpretation.

### Ecosystem-owned

Conceptually coherent but operationally unresolved:

- active contracts;
- active registries;
- compatibility definitions;
- ecosystem metadata;
- root-level decision indexes if adopted.

Major remaining ambiguity:
Whether some currently hosted MetaHarvest-adjacent files are actually ecosystem infrastructure rather than MetaHarvest knowledge. This is not a conceptual blocker if extraction scope excludes unresolved infrastructure, but it is an operational inventory blocker.

Recommendation:
Before physical extraction, classify each candidate moved artifact as MetaHarvest-owned, consumer-owned, or ecosystem-owned/transitional.

## 4. Interface-independence assessment

The eight currently identified conceptual interfaces remain valid regardless of repository structure.

### 1. Consultation Interface

Structure-independent.

It requires a consumer to provide bounded problem/project/architecture/context inputs. It does not require ProjectForge hosting.

Potential ProjectForge assumption:
Current consultation triggers and paths are documented in ProjectForge/ArchitectureHarvest docs. Future extraction must restate them in MetaHarvest-owned docs or preserve pointers.

### 2. Recommendation Interface

Structure-independent.

A recommendation can be a file, message, report, or future artifact regardless of repository layout.

Potential ProjectForge assumption:
Current templates and adoption conventions may live under ProjectForge paths.

### 3. Adoption Outcome Interface

Structure-independent.

Consumers can record adoption outcomes locally in any project.

Potential ProjectForge assumption:
Generated projects currently use `architecture/architectureharvest/` placeholders. That path naming is ProjectForge-generated and must be handled before extraction.

### 4. Rejection Memory Interface

Structure-independent.

Local rejection stays local; generalized rejection lessons can flow back to MetaHarvest.

Potential ProjectForge assumption:
Current rejection/retirement files may be ProjectForge-hosted and need ownership classification.

### 5. Evidence Reference Interface

Mostly structure-independent, but operationally sensitive.

The concept is independent. The current evidence pointers may not be. This is the strongest extraction blocker after path inventory.

### 6. Relevance Interface

Structure-independent conceptually.

A consumer can own relevance maps while MetaHarvest owns reusable pattern knowledge and non-authoritative relevance suggestions.

Potential ProjectForge assumption:
ProjectForge templates currently define placeholder structure.

### 7. Staleness Interface

Structure-independent.

MetaHarvest can mark its own knowledge stale; consumers decide local impact.

Potential ProjectForge assumption:
Current staleness audits may assume ProjectForge-relative source locations.

### 8. Authority Boundary Interface

Fully structure-independent.

The rule that MetaHarvest recommends and consumers decide does not depend on filesystem layout.

Conclusion:
No conceptual interface requires ProjectForge hosting. Several current implementations/conventions assume ProjectForge paths, making this an operational rather than logical dependency.

## 5. Evolution-interface assessment

Proposed ninth interface:

### Evolution Interface

Purpose:
Allow projects to contribute reusable lessons back into MetaHarvest without transferring ownership of local history.

Assessment: justified as a distinct conceptual interface.

It is partially covered by adoption outcome, rejection memory, staleness, and evidence-reference interfaces, but naming it separately improves clarity because it describes the learning loop over time, not a single decision outcome.

Examples:

- recommendation issued -> adopted -> succeeded;
- recommendation issued -> adopted -> failed;
- recommendation issued -> rejected -> later reconsidered;
- recommendation issued -> repeatedly rejected under similar conditions;
- pattern adopted in one project -> adapted differently in another;
- recommendation confidence reduced after repeated poor fit;
- recommendation priority increased after repeated successful use.

What the Evolution Interface owns conceptually:

- flow of generalized lessons from consumer outcomes into MetaHarvest;
- distinction between local history and reusable learning;
- updates to fit conditions, confidence, priority, anti-patterns, and revisit triggers;
- preservation of lineage across recommendation generations.

What it must not do:

- transfer local governance history to MetaHarvest;
- force consumers to report every outcome;
- create automatic adoption/rejection propagation;
- make repeated success into authority;
- create active ecosystem infrastructure by default.

Recommendation:
Add Evolution Interface to the conceptual interface set in future doctrine/planning, making the set nine interfaces:

1. Consultation Interface
2. Recommendation Interface
3. Adoption Outcome Interface
4. Rejection Memory Interface
5. Evidence Reference Interface
6. Relevance Interface
7. Staleness Interface
8. Authority Boundary Interface
9. Evolution Interface

Do not implement now.

confidence = 0.84
priority = 0.69

## 6. Extraction-readiness reassessment

### Conceptual readiness

Mostly ready.

Already ready:

- durable independent purpose;
- conceptual separability from ProjectForge;
- advisory-only boundary;
- non-domain boundary;
- ownership classes;
- consumer autonomy boundary;
- minimum conceptual interface set;
- EIP/EII terminology distinction;
- no-root-owner direction as doctrine candidate;
- extraction not logically dependent on EIP root adoption.

Still conceptually missing or incomplete:

- explicit acceptance of Evolution Interface as part of conceptual interface set;
- final doctrine status for `No project owns the EIP root`;
- final doctrine status for `Project extraction decisions should be based primarily on purpose, ownership, and interfaces rather than filesystem structure`;
- exact treatment of ecosystem-owned artifacts currently hosted near MetaHarvest.

### Operational readiness

Not ready.

Required before extraction:

- path inventory for `ArchitectureHarvest`, `MetaHarvest`, `architectureharvest`, and `metaharvest` references;
- artifact ownership classification before move;
- evidence-reference strategy;
- compatibility strategy for old paths;
- generated-project placeholder naming decision;
- migration sequence;
- verification plan;
- rollback plan;
- decision on interim sibling location if no EIP root exists;
- docs update plan to preserve historical interpretability.

Genuine blockers:

- path-dependency inventory;
- evidence-reference stability;
- compatibility/rollback plan;
- artifact ownership classification;
- explicit location approval.

Convenience factors, not blockers:

- EIP root adoption;
- EII creation;
- ResearchMemory creation;
- global project-creation workflow redesign;
- active registry ownership resolution, if extraction avoids registry movement;
- machine-readable contracts/schemas, if conceptual/file-backed conventions remain sufficient.

## 7. EIP-compatibility assessment

Assumed future ecosystem:

```text
EIP
├── ProjectForge
├── MacroForge
├── MetaHarvest
├── ResearchMemory
├── EII
└── future projects
```

The proposed boundaries remain valid whether or not this root exists physically.

Reason:
The boundary model is purpose-based, not path-based.

- ProjectForge remains framework/scaffold infrastructure.
- MacroForge remains economic/investment-relevant domain research.
- MetaHarvest remains reusable non-domain knowledge and advisory recommendation lineage.
- ResearchMemory, if created, owns research conclusions and epistemic history.
- EII, if created, owns user-facing synthesis and attention allocation.
- EIP ecosystem infrastructure, if approved, owns active contracts/registries/metadata.

A physical EIP root would clarify placement but would not change the conceptual ownership model.

## 8. Doctrine-candidate assessment

Doctrine candidate:

```text
Project extraction decisions should be based primarily on purpose, ownership boundaries, and interface boundaries rather than filesystem structure.
```

Assessment: sound and useful.

### Usefulness

- Prevents filesystem layout from becoming pseudo-governance.
- Aligns extraction with autonomy doctrine and ownership-by-purpose guidance.
- Separates conceptual readiness from operational migration readiness.
- Prevents artificial dependency on neutral-root adoption.
- Helps decide whether hosted subsystems are truly projects or just folders.

### Risks

- Could underweight operational migration cost if misread as `purpose is enough`.
- Could encourage premature extraction if interface boundaries are only hand-waved.
- Could ignore tooling, path, evidence, and compatibility risks.

### Overlap with existing doctrine

Overlaps strongly with:

- project autonomy;
- project ownership doctrine;
- scope extraction doctrine;
- anti-monolith doctrine;
- interface-first doctrine;
- governance permission ladder.

It adds one useful clarification:
Filesystem structure is evidence and migration constraint, not primary authority.

Recommendation:
Promote later as doctrine guidance, not constitutional doctrine yet. It should be paired with an operational caveat:

```text
Conceptual extraction readiness depends on purpose, ownership, and interfaces. Physical extraction additionally requires path inventory, compatibility planning, verification, and rollback.
```

confidence = 0.87
priority = 0.76

## 9. Recommended next step

Recommended next task, if approved:

Perform a path-dependency and artifact-ownership inventory for MetaHarvest extraction readiness.

Scope should include references to:

- `ArchitectureHarvest`;
- `MetaHarvest`;
- `architectureharvest`;
- `metaharvest`;
- generated-project placeholders;
- source/evidence paths;
- templates;
- skills;
- state files;
- coherence/audit tools;
- summaries;
- recommendation/adoption artifacts.

The inventory should classify each item as:

- MetaHarvest-owned;
- ProjectForge-owned;
- consumer-owned;
- ecosystem-infrastructure-owned/TBD;
- historical-only;
- compatibility shim candidate.

Still do not move, rename, extract, create projects, implement contracts, or adopt an EIP root during that task.

## 10. Risks, conflicts, and open questions

### Risks

- Interim sibling placement could create another migration later.
- Extraction may accidentally drag ecosystem infrastructure into MetaHarvest.
- Existing path assumptions may be more numerous than expected.
- Evidence pointers may break if moved without indirection or compatibility handling.
- Treating Evolution Interface as mandatory reporting could create bureaucracy.
- Repeated successful recommendations may still create soft-governance pressure if not framed as evidence only.
- Separating before ProjectForge de-hosting may preserve some historical coupling longer than ideal.

### Conflicts found

No hard conceptual conflict.

Soft conflicts:

- Earlier reviews sometimes listed EIP root ownership as an ecosystem criterion for extraction readiness. This review refines that: EIP-root ownership principle is helpful but not logically required for extraction if extraction avoids root/infrastructure changes.
- Current physical hosting still implies ProjectForge locality, while conceptual boundaries support sibling status.
- Current generated-project placeholders use `architectureharvest`, while conceptual name is MetaHarvest.

### Open questions

- What interim location would be acceptable if MetaHarvest became a sibling before EIP-root adoption?
- Should Evolution Interface become formal doctrine or remain migration-planning language?
- Should `No project owns the EIP root` be decided before any sibling extraction, even if root adoption is deferred?
- How much path compatibility is required for historical artifacts versus active docs/tools?
- Which currently hosted MetaHarvest-adjacent artifacts are actually ecosystem infrastructure?
- Should extraction and physical rename occur together or separately if EIP root remains absent?
- What is the minimal acceptable evidence-reference strategy for extraction?

## Final recommendation

Do not extract MetaHarvest now.

But also do not block MetaHarvest extraction on neutral EIP root adoption.

The correct doctrine guidance is:

```text
MetaHarvest extraction readiness is primarily determined by purpose, ownership boundaries, authority boundaries, and conceptual interfaces. Neutral EIP root adoption is helpful for long-term ecosystem organization but is not a logical prerequisite for MetaHarvest becoming a sibling project.
```

Physical extraction remains blocked by operational migration requirements, not by the absence of an EIP root.
