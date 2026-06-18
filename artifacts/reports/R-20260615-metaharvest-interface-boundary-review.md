# MetaHarvest Interface-Boundary Review

Date: 2026-06-15
Status: bounded architecture-boundary and extraction-readiness review
Permission level: L4 conceptual review; no extraction or implementation
Scope: ownership boundaries, conceptual interface boundaries, information flow, recommendation flow, consultation flow, adoption flow, rejection flow, evidence flow, extraction readiness, and future EIP compatibility

## Explicit non-actions

This review does not authorize or perform:

- commits;
- staging;
- directory moves;
- directory renames;
- MetaHarvest extraction;
- project creation;
- MacroForge modification;
- EII modification;
- ecosystem infrastructure modification;
- contract implementation;
- service implementation;
- schema creation;
- protocol creation.

## Governance visibility

FOUNDATIONAL_GOVERNANCE_WARNING
PERMISSION_LEVEL=L4
CATEGORY=FOUNDATIONAL
PROJECT=MetaHarvest / ProjectForge / EIP ecosystem
DECISION=MetaHarvest autonomous sibling extraction readiness

Impact:
The review defines conceptual boundaries that would be required before MetaHarvest could become an autonomous sibling project.

Risk:
Implementing extraction, contracts, services, registries, or active ecosystem infrastructure without explicit foundational approval could silently change project ownership, governance authority, or ecosystem structure.

Required approval:
STOP. This artifact is analysis and interface-boundary definition only. Physical extraction, project creation, directory movement, contract implementation, service implementation, and infrastructure changes are prohibited without explicit foundational approval.
END_FOUNDATIONAL_GOVERNANCE_WARNING

## Executive conclusion

MetaHarvest has a coherent autonomous purpose, but physical extraction should still wait. The minimum conceptual boundary set is now clear enough for planning, but not yet enough for execution.

The essential rule is:

- MetaHarvest owns reusable non-domain knowledge and advisory recommendation lineage.
- Consumer projects own local judgment, adoption, rejection, scheduling, implementation, priorities, and purpose interpretation.
- EIP ecosystem infrastructure, if it emerges, owns active shared contracts, registries, compatibility definitions, and ecosystem metadata; MetaHarvest may describe patterns about these but must not own the active agreements.

Extraction readiness depends less on code movement and more on eliminating ambiguous authority.

## 1. Ownership-boundary assessment

### A — MetaHarvest-owned

MetaHarvest should own knowledge whose value remains valid across projects and whose purpose is reusable non-domain learning.

MetaHarvest-owned responsibilities:

- harvested architecture patterns;
- harvested interface patterns;
- harvested shared concepts and vocabulary;
- harvested methodologies;
- harvested heuristics;
- harvested governance patterns;
- harvested decision patterns;
- anti-patterns and failure patterns;
- external-source evidence summaries;
- pattern comparison records;
- recommendation rationale;
- recommendation evidence links;
- recommendation lineage;
- cross-project lessons generalized from local outcomes;
- reusable negative knowledge;
- confidence assessments about reusable patterns;
- priority assessments for advisory recommendations;
- staleness assessment of MetaHarvest-owned knowledge.

Boundary refinement:
MetaHarvest may preserve that a receiving project rejected a recommendation only insofar as the rejection teaches a reusable lesson, updates fit assumptions, or prevents repeated irrelevant recommendations. The receiving project's actual decision remains consumer-owned.

MetaHarvest should not own:

- project-local decisions;
- project-local implementation plans;
- project-local task status;
- project-local priorities;
- domain conclusions;
- active ecosystem contracts;
- active compatibility obligations;
- ecosystem registry truth;
- project purpose interpretation.

### B — Consumer-owned

A consuming project owns its local governance and local reality.

Consumer-owned responsibilities:

- adoption decisions;
- rejection decisions;
- modification decisions;
- local prioritization;
- local scheduling;
- local implementation;
- local tests and verification;
- local architecture decisions;
- local governance decisions;
- project purpose interpretation;
- local risk tolerance;
- local constraints and tradeoffs;
- local recommendation review outcomes;
- local adoption outcomes;
- local rejection rationale;
- local supersession or revisit conditions;
- whether to open a task;
- whether to ignore a recommendation.

Boundary refinement:
A project may share outcome knowledge with MetaHarvest, but sharing does not transfer ownership of the project's decision history. MetaHarvest can mirror reusable lessons, not absorb the consumer's governance record.

### C — Ecosystem-owned / future infrastructure-owned

Some responsibilities are neither MetaHarvest knowledge nor consumer-project governance. They are potential future EIP ecosystem infrastructure.

Potential ecosystem-owned responsibilities:

- active interface contracts;
- active compatibility definitions;
- ecosystem registries;
- canonical project-location metadata;
- ecosystem-level decision indexes;
- ecosystem metadata;
- project relationship records;
- current project-status registry if adopted;
- cross-project version/compatibility expectations;
- neutral recommendation exchange conventions if standardized;
- authority-boundary indexes if they become active shared infrastructure.

Boundary refinement:
This ownership is currently unresolved. It should not be assigned to ProjectForge, MetaHarvest, EII, or another project by default. Temporary ProjectForge hosting remains a transitional convenience only when clearly descriptive and non-authoritative.

## 2. Consultation-boundary assessment

A project consulting MetaHarvest should provide enough context for recommendation judgment, not full project internals.

Minimum conceptual consultation inputs:

1. Request identity
   - requesting project or scope;
   - requester context if relevant;
   - date/time or review event.

2. Problem statement
   - what decision, architecture issue, recurring failure, design question, or improvement scan is being considered;
   - why MetaHarvest is being consulted now.

3. Project purpose and boundary snapshot
   - approved project purpose;
   - relevant scope constraints;
   - governance level if known;
   - explicit non-goals.

4. Architecture context
   - current relevant architecture summary;
   - relevant subsystem or workflow;
   - current constraints and assumptions;
   - known pain points or failure modes.

5. Decision context
   - what kind of recommendation is desired;
   - whether the project wants options, critique, extraction pressure, simplification, pattern candidates, or rejection evidence;
   - whether implementation is in scope after project-local approval.

6. Local constraints
   - cost constraints;
   - operational constraints;
   - maintainability constraints;
   - local-first/cloud constraints;
   - skill/time constraints;
   - regulatory/security constraints when relevant.

7. Evidence pointers
   - paths, artifacts, decisions, reports, logs, or summaries needed to understand the issue;
   - enough references for MetaHarvest to ground its response.

8. Desired output form
   - recommendation, options, risk review, pattern search, anti-pattern check, or extraction review;
   - required confidence/priority fields if useful.

What is not required:

- full repository access by default;
- authority to modify files;
- project-local task creation permission;
- adoption permission;
- active ecosystem registry writes;
- direct access to all project state.

Consultation boundary rule:
MetaHarvest receives context for advisory reasoning. It does not receive governance authority.

## 3. Recommendation-boundary assessment

MetaHarvest should be allowed to emit advisory outputs only.

Minimum conceptual recommendation outputs:

- recommendation identifier;
- origin project/system: MetaHarvest;
- target project or scope;
- recommendation type;
- concise recommendation;
- rationale;
- evidence references;
- expected benefit;
- implementation-cost estimate;
- architectural-impact estimate;
- risk/tradeoff statement;
- fit assumptions;
- non-fit conditions;
- confidence;
- priority;
- lineage;
- staleness/revisit condition if applicable;
- explicit authority boundary statement.

Useful optional outputs:

- alternatives considered;
- why not to adopt;
- minimum useful extraction;
- reversible first step;
- consumer-local approval gate;
- related prior rejections/adoptions;
- dependency assumptions;
- suggested evaluation criteria.

Required boundary statement:

```text
This is advisory. The receiving project owns acceptance, rejection, modification, prioritization, scheduling, implementation, verification, and purpose interpretation.
```

What MetaHarvest must not emit as authoritative output:

- commands to implement;
- direct task creation in the target project;
- project purpose changes;
- governance changes without approval;
- mandatory standards;
- ecosystem contract updates;
- registry mutations;
- compatibility obligations;
- automatic adoption decisions.

Recommendation boundary rule:
MetaHarvest may recommend strongly, but confidence and priority never imply authority.

## 4. Adoption-boundary assessment

Adoption remains entirely the responsibility of the receiving project.

Consumer-owned adoption decisions include:

- accept;
- reject;
- defer;
- modify;
- partially adopt;
- supersede;
- retire;
- ignore;
- open a local task;
- schedule implementation;
- assign priority;
- choose implementation path;
- run tests and verification;
- record project-local decisions;
- update project-local purpose/scope only through proper approval.

MetaHarvest may help the project think about adoption, but it may not decide adoption.

Adoption flow conceptually:

1. Consumer requests or receives a recommendation.
2. Consumer reviews against local purpose, architecture, constraints, and governance permission level.
3. Consumer records local review outcome if meaningful.
4. Consumer decides whether to open local work.
5. Consumer implements only through local governance and verification.
6. Consumer may report outcome back to MetaHarvest if reusable.

Boundary reinforcement:
Implementation success in one project does not imply adoption in another. Repeated acceptance across projects is evidence, not authority.

## 5. Rejection-boundary assessment

Rejection knowledge has two layers.

### Consumer-local rejection knowledge

Belongs to the receiving project.

Includes:

- local rejection decision;
- local rationale;
- local constraints;
- local timing;
- local risk tolerance;
- local revisit condition;
- local supersession context;
- local decision authority.

This should remain in the consumer's decision/recommendation/adoption artifacts.

### MetaHarvest reusable rejection knowledge

Belongs to MetaHarvest only when generalized or useful for future reasoning.

Includes:

- pattern is a poor fit under certain constraints;
- recommendation failed due to missing assumptions;
- approach is overkill for solo/local-first projects;
- vocabulary caused confusion across projects;
- implementation was rejected because a simpler pattern existed;
- adoption attempts exposed new anti-patterns;
- repeated project-local rejections reduce generic priority;
- rejected source/project should not be rediscovered without changed conditions.

Recommended flow:

1. Consumer records local rejection outcome.
2. Consumer may share a summary or pointer with MetaHarvest.
3. MetaHarvest decides whether the rejection creates reusable non-domain knowledge.
4. MetaHarvest records generalized lesson, evidence pointer, and lineage.
5. MetaHarvest does not overwrite or own the consumer's local decision record.

What should remain local:

- sensitive context;
- project-specific priority tradeoffs;
- project-local politics or resource constraints;
- domain-specific conclusions;
- implementation details not reusable outside the project.

What should be reusable:

- fit/non-fit conditions;
- generalizable failure modes;
- reusable anti-patterns;
- false-assumption corrections;
- evidence that recommendation priority/confidence should change;
- conditions that would justify revisiting.

## 6. Interface knowledge vs interface contract assessment

### Interface knowledge

Owned by MetaHarvest.

Definition:
Reusable lessons about interface design, interface failure modes, communication patterns, adoption/rejection flows, and autonomy-preserving boundaries.

Examples:

- projects should exchange recommendations rather than commands;
- adoption and implementation outcomes should remain separate;
- confidence and priority should not imply authority;
- generated recommendations need lineage;
- direct internal coupling creates extraction risk;
- file-backed artifacts can preserve negative knowledge cheaply;
- interface-first separation avoids discovering boundaries after extraction.

MetaHarvest may recommend interface improvements based on this knowledge.

### Interface contracts

Not owned by MetaHarvest by default.

Definition:
Active ecosystem agreements that define how projects must exchange artifacts, maintain compatibility, version schemas, or interpret canonical fields.

Examples:

- active recommendation schema;
- active adoption-outcome schema;
- active compatibility policy;
- active registry format;
- active cross-project API or artifact contract;
- active versioning/deprecation rules;
- required exchange locations under an EIP root.

Why MetaHarvest should not own active contracts:

- contracts affect multiple projects' obligations;
- contract changes can create governance authority;
- advisory systems should not become standards bodies by convenience;
- active contracts belong to ecosystem infrastructure or explicit project-local adoption.

Refined rule:
MetaHarvest can own knowledge about how interfaces should work. It cannot own the active obligation that projects must use a particular interface unless explicit ecosystem governance grants that authority.

## 7. Extraction-readiness criteria

MetaHarvest is not physically extraction-ready until all of the following are true or explicitly waived through L4 approval.

### Ownership criteria

- MetaHarvest-owned, consumer-owned, and ecosystem-owned responsibilities are documented.
- Consumer projects retain adoption/rejection/implementation authority.
- Domain knowledge boundaries are explicit.
- Active ecosystem infrastructure ownership remains separate from MetaHarvest.

### Consultation criteria

- Minimum consultation inputs are documented.
- Consultation does not require internal ProjectForge path assumptions.
- Consulting projects can provide bounded context without surrendering authority.
- Consultation triggers are clear enough to avoid unnecessary ceremony.

### Recommendation criteria

- Minimum recommendation outputs are documented.
- Authority boundary statement is standard practice.
- Confidence and priority are advisory metadata only.
- Recommendation lineage and evidence pointers survive across project boundaries.

### Adoption/rejection criteria

- Receiving projects have local places to record adoption, rejection, modification, deferral, supersession, and outcomes.
- MetaHarvest has a way to preserve generalized lessons without absorbing local governance.
- Rejection memory distinguishes local rationale from reusable negative knowledge.

### Evidence criteria

- Evidence references can survive physical separation.
- External-source evidence remains accessible or reproducibly locatable.
- Consumer-local evidence can be referenced by pointer without copying sensitive/project-owned content.
- Historical lineage can be retained after move/rename.

### Path-dependency criteria

- All ProjectForge-relative references to `ArchitectureHarvest/` are inventoried.
- Generated-project `architecture/architectureharvest/` placeholder naming is decided.
- Scripts, summaries, tests, recovery docs, and skills that mention ArchitectureHarvest are inventoried.
- Compatibility strategy exists for old paths and historical artifacts.

### Ecosystem criteria

- Future EIP root ownership principle is settled or consciously deferred.
- Active interface contracts are not accidentally assigned to MetaHarvest.
- ProjectForge de-hosting implications are understood.
- Extraction does not create a hidden registry or standards authority.

### Operational criteria

- Verification plan exists before move/rename.
- Rollback plan exists.
- No generated projects break from missing paths.
- Historical artifacts remain interpretable.
- Extraction can be performed as a bounded change with clear diff and tests.

Readiness status today:

- Conceptual ownership boundaries: mostly ready after this review.
- Consultation/recommendation/adoption/rejection boundaries: conceptually defined, not implemented as contracts.
- Path-dependency inventory: not complete.
- Active interface contracts: intentionally not implemented.
- Ecosystem infrastructure ownership: unresolved.
- Physical extraction: not ready.

## 8. Future EIP compatibility assessment

The boundaries generalize beyond ProjectForge if applied consistently.

### ResearchMemory compatibility

ResearchMemory, if created, would likely own research conclusions, hypotheses, literature context, and epistemic history.

MetaHarvest boundary remains valid because MetaHarvest owns reusable non-domain methods and patterns, not substantive research conclusions.

Potential flow:

- ResearchMemory may consult MetaHarvest for methodology, evidence handling, review workflow, or memory-architecture patterns.
- MetaHarvest may recommend reusable research-workflow patterns.
- ResearchMemory decides adoption locally and owns research conclusions.

### EII compatibility

EII, if created, would likely own user-facing synthesis, prioritization, personalization, briefing generation, attention allocation, and ecosystem consumption.

MetaHarvest boundary remains valid because MetaHarvest may recommend reusable briefing/prioritization patterns but does not own EII's product behavior, user model, or attention-allocation decisions.

Potential flow:

- EII may consult MetaHarvest for interface, briefing, synthesis, prioritization, and governance-pattern knowledge.
- MetaHarvest may recommend patterns.
- EII owns adoption, implementation, and user-facing decisions.
- EII does not become the owner of MetaHarvest outputs or ecosystem infrastructure by consuming them.

### Additional future projects

Any future sibling project should be able to use the same pattern:

1. provide bounded consultation context;
2. receive advisory recommendation with evidence and lineage;
3. evaluate locally;
4. record local decision;
5. share generalized outcome if useful;
6. retain project-local authority.

Compatibility conclusion:
The proposed boundaries scale because they are purpose-based rather than ProjectForge-specific.

## 9. Minimum conceptual interface set

The minimum interface set required before physical extraction is:

1. Consultation interface
   - consumer provides bounded problem/project/architecture/context inputs;
   - MetaHarvest returns advisory analysis.

2. Recommendation interface
   - MetaHarvest emits recommendation, rationale, evidence, confidence, priority, lineage, risks, fit conditions, and authority boundary.

3. Adoption-outcome interface
   - consumer records accept/reject/defer/modify/supersede/implement outcomes locally;
   - reusable outcome summary may be shared back.

4. Rejection-memory interface
   - consumer preserves local rejection rationale;
   - MetaHarvest preserves generalized negative knowledge when reusable.

5. Evidence-reference interface
   - MetaHarvest references evidence without assuming ownership of consumer-local artifacts;
   - pointers remain stable enough across extraction.

6. Relevance/context interface
   - consumer maintains local relevance/fits/constraints;
   - MetaHarvest maintains reusable pattern knowledge and may maintain non-authoritative relevance suggestions.

7. Staleness/update interface
   - MetaHarvest marks its recommendations/patterns stale when evidence changes;
   - consumers decide whether stale recommendations matter locally.

8. Authority-boundary interface
   - every cross-project exchange preserves that MetaHarvest recommends and the consumer decides.

These are conceptual interfaces, not contracts, schemas, protocols, services, or implementation artifacts.

## 10. Risks and conflicts

Risks:

- Interface definitions may be mistaken for implemented contracts.
- MetaHarvest could become a de facto standards body if its interface knowledge is treated as mandatory.
- Consumer projects may under-record rejection/adoption outcomes, weakening feedback quality.
- Too much evidence copying could violate project ownership or create context pollution.
- Too little evidence sharing could make MetaHarvest recommendations ungrounded.
- Path references may break if extraction is attempted before inventory.
- EIP ecosystem infrastructure ownership remains unresolved and could be accidentally assigned during extraction.

Conflicts found:

- Current hosted `ArchitectureHarvest/` paths are still ProjectForge-relative, while conceptual purpose is sibling-capable.
- Generated-project placeholder names still use `architectureharvest`, while conceptual name is MetaHarvest.
- Existing docs already include many advisory boundaries, but not a single explicit minimum conceptual interface set.
- Current adoption logs and relevance maps are file-backed conventions, not autonomous-project interfaces.

These conflicts do not require immediate implementation. They are blockers to extraction, not blockers to continued hosted operation.

## 11. Open questions

- Should the minimum conceptual interface set become future constitutional doctrine or remain migration-planning guidance?
- What is the smallest path-dependency inventory needed before extraction approval?
- Should future generated projects use `architecture/metaharvest/`, retain `architecture/architectureharvest/`, or support both for compatibility?
- Should consumer-local adoption/rejection summaries be mirrored to MetaHarvest manually, semi-automatically, or only during scheduled reviews?
- What evidence can be safely referenced across project boundaries without copying project-owned content?
- Who owns active recommendation/adoption schemas if they later become ecosystem contracts?
- Should MetaHarvest extraction wait until a neutral EIP root exists, or can it become a sibling before root adoption?
- How should historical `ArchitectureHarvest` references remain interpretable after eventual rename or extraction?

## Final recommendation

Do not extract MetaHarvest yet.

The conceptual interface boundaries are now sufficiently defined for planning, but extraction should wait until:

1. path dependencies are inventoried;
2. active-contract ownership is resolved or explicitly deferred;
3. evidence-reference strategy is defined;
4. generated-project placeholder naming is decided;
5. ProjectForge-specific assumptions are removed from the intended consultation/recommendation/adoption/rejection flows.

Next best task, if approved later:

- perform a path-dependency and reference-inventory review for `ArchitectureHarvest`, `MetaHarvest`, `architectureharvest`, and `metaharvest`, still without moving or renaming anything.
