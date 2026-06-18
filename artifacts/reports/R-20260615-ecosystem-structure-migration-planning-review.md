# Ecosystem Structure and Migration Planning Review

Date: 2026-06-15
Status: bounded architecture, naming, ownership, and migration-planning review
Permission level: L4 conceptual review, with bounded terminology alignment only
Scope: EIP/EII terminology, neutral ecosystem root, ProjectForge de-hosting, project-creation location, MetaHarvest extraction/naming, ecosystem ownership, ecosystem infrastructure, and migration sequencing

## Explicit non-actions

This review does not authorize or perform:

- commits;
- staging;
- physical moves;
- directory renames;
- project extraction;
- project creation;
- MacroForge modification;
- ecosystem infrastructure implementation;
- registries;
- interface contracts;
- repository restructuring.

## Governance visibility

FOUNDATIONAL_GOVERNANCE_WARNING
PERMISSION_LEVEL=L4
CATEGORY=FOUNDATIONAL
PROJECT=EIP ecosystem / ProjectForge / MetaHarvest
DECISION=Future ecosystem structure and project-hosting migration

Impact:
Future physical repository structure, ecosystem ownership, and project location assumptions may be affected.

Risk:
Implementation without explicit approval could silently make ProjectForge, MetaHarvest, EII, or another project the de facto ecosystem owner.

Required approval:
STOP. Physical moves, directory renames, project extraction, project creation, ecosystem-root adoption, registry implementation, and contract implementation are prohibited without explicit foundational approval.
END_FOUNDATIONAL_GOVERNANCE_WARNING

## 1. EIP terminology review

The term `EIP` should now mean `Economic Intelligence Platform`, the ecosystem as a whole.

EIP is not a project. It is the future ecosystem boundary that may eventually contain:

- ProjectForge;
- MacroForge;
- MetaHarvest;
- ResearchMemory;
- EII;
- future projects;
- ecosystem infrastructure.

This clarification is important because prior wording treated EIP as a future user-facing project. That creates ownership confusion: if EIP is both the ecosystem and a project, it becomes too easy to assign ecosystem governance, registries, interfaces, or attention-allocation authority to one project by naming accident.

Recommendation: current forward-looking architecture should use `EIP` only for the ecosystem. Historical artifacts need not be rewritten unless they are active guidance surfaces.

## 2. EII terminology review

The future project previously called EIP should now be called `EII` — `Economic Intelligence Initiative`.

Provisional future-project role:

- user-facing intelligence layer;
- synthesis;
- prioritization;
- personalization;
- attention allocation;
- briefing generation;
- consumption of ecosystem outputs.

EII remains a future project only. It is not approved, not created, not designed in detail, and not an implementation target.

Boundary: EII should not own the EIP ecosystem, project purposes, ecosystem infrastructure, registries, interface contracts, or governance authority by default.

## 3. Ecosystem-root assessment

A neutral root structure such as the following is conceptually aligned with project-autonomy doctrine:

```text
EIP/
├── projects/
├── infrastructure/
└── governance/
```

Potential benefits:

- makes ProjectForge one sibling project rather than the ecosystem host;
- clarifies that projects are autonomous peers;
- gives ecosystem infrastructure a neutral place that is not owned by ProjectForge, MetaHarvest, or EII;
- reduces accidental ownership-by-physical-location;
- supports future project creation without assuming ProjectForge ownership;
- makes ecosystem governance and project governance easier to separate.

Risks:

- premature restructuring could create churn without operational value;
- existing paths, scripts, summaries, registries, references, and user habits assume `/home/mkkto/srv/projectforge` as current root;
- nested git/worktree behavior may become confusing;
- neutral root could become a governance dumping ground if responsibilities are not bounded;
- moving too early could break recovery/coherence workflows.

Migration implications:

- path references would need inventory and compatibility strategy;
- ProjectForge creation defaults would need explicit location selection;
- workspace registry semantics would need review;
- MetaHarvest dependencies would need clean interface boundaries before extraction;
- historical artifacts should usually remain historical rather than rewritten.

Governance implications:

- adopting an EIP root is a foundational L4 decision;
- no project should own the root;
- root governance/infrastructure must not imply control over projects;
- root-level artifacts should be descriptive coordination infrastructure unless explicit authority is approved.

Recommendation: conceptually favorable, physically premature.

## 4. ProjectForge de-hosting assessment

Current historical assumption: generated projects default inside ProjectForge.

Proposed future state: ProjectForge is one project among many; project creation location becomes explicit.

Assessment: de-hosting is conceptually aligned with autonomy doctrine because physical containment currently reinforces the false impression that ProjectForge owns generated/autonomous projects.

Benefits:

- reduces ecosystem-host ambiguity;
- prevents ProjectForge from becoming a meta-controller by physical default;
- improves ownership-by-purpose clarity;
- prepares for EIP-root adoption;
- separates framework project concerns from ecosystem placement concerns.

Risks:

- ProjectForge tooling currently assumes workspace defaults;
- registry/coherence tests may assume canonical workspace paths;
- existing generated-project workflows may become more complex;
- explicit location choice adds one more project-creation decision.

Recommendation: de-hosting should be a future migration objective, not immediate implementation. First align terminology and doctrine, then design explicit project-location selection, then adapt tooling only after approval.

## 5. Project-creation workflow assessment

Future project creation should ask for explicit location when location matters.

Candidate question:

```text
Where should this project be created?

Options:
1. Inside an existing project as an approved subproject.
2. As a sibling project under the ecosystem root.
3. Another approved location.
```

Usefulness:

- prevents implicit ecosystem ownership assumptions;
- forces subproject-vs-sibling distinction to be deliberate;
- supports ownership-by-purpose review;
- prepares for neutral EIP root without requiring immediate restructuring.

Risk:

- asking every time may add friction for simple cases;
- users may not know the location until purpose/scope is clearer;
- premature location choice could feel like infrastructure design before project purpose.

Recommendation: future workflow should ask location only when creating a durable project, not during early ideation. The question should appear after purpose/scope are sufficiently clear. Default should be explicit and visible, not hidden.

Do not implement now.

## 6. MetaHarvest extraction assessment

Conceptual separation is justified.

Reasons:

- MetaHarvest has a durable purpose independent of ProjectForge: reusable non-domain knowledge harvesting and advisory recommendations;
- it could reasonably survive if ProjectForge disappeared;
- its governance concerns differ from ProjectForge's framework/scaffold governance;
- it is increasingly relevant to multiple projects, not only ProjectForge.

Physical separation is not yet justified.

Reasons:

- current artifacts, retrieval paths, adoption logs, generated-project placeholders, and instructions still assume `ArchitectureHarvest/` under ProjectForge;
- interface contracts between ProjectForge and MetaHarvest are not explicit enough;
- ecosystem infrastructure ownership remains unresolved;
- physical extraction before naming/path strategy would create avoidable churn;
- no immediate operational blocker requires extraction.

Dependencies still existing:

- ProjectForge docs/instructions consult `ArchitectureHarvest/` directly;
- generated projects receive `architecture/architectureharvest/` placeholders;
- ProjectForge state and constitution describe MetaHarvest as currently hosted;
- recommendation/adoption outcome conventions are still ProjectForge-hosted;
- retrieval path assumptions use ProjectForge-relative paths.

Interfaces required before extraction:

- recommendation artifact contract;
- adoption/rejection outcome contract;
- consultation protocol;
- evidence/retrieval reference protocol;
- project-local relevance-map convention;
- version/compatibility expectations;
- ownership of shared ecosystem metadata.

Recommendation: keep MetaHarvest conceptually separable but physically hosted for now. Prepare extraction only through future interface-contract review and migration inventory.

## 7. MetaHarvest naming assessment

Current physical name: `ArchitectureHarvest/`.

Conceptual name: `MetaHarvest`.

Physical rename trigger conditions:

- active docs consistently use `MetaHarvest (formerly ArchitectureHarvest)`;
- path-reference inventory is complete;
- tests/coherence/recovery references are identified;
- generated-project placeholder naming decision is made;
- extraction decision is either rejected or sequenced;
- migration can be performed in a small, reversible, verified change.

References needing migration before/with rename:

- ProjectForge constitution and AGENTS instructions;
- state files;
- README and architecture docs;
- generated-project templates/placeholders;
- retrieval/adoption paths;
- tests and coherence checks;
- summaries;
- workspace/project registry notes if any;
- skills and durable references;
- scripts using literal paths;
- historical references only when they function as active guidance, not as historical evidence.

Should physical rename happen before or after extraction?

Recommendation: after extraction decision, not automatically before.

Preferred sequence:

1. complete terminology alignment in active docs;
2. inventory path references;
3. decide whether MetaHarvest remains hosted or becomes sibling;
4. if remaining hosted, physical rename can be a local ProjectForge cleanup;
5. if extracting, consider moving and renaming in one carefully planned migration only if verification burden is acceptable.

Avoid two disruptive migrations unless the intermediate state has clear value.

## 8. Ecosystem-ownership assessment

Candidate doctrine: `No project owns the EIP root.`

Assessment: sound and important.

Implications:

- ProjectForge does not own EIP;
- MetaHarvest does not own EIP;
- EII does not own EIP;
- future projects do not own EIP;
- EIP root is ecosystem infrastructure, not a project.

Recommendation: promote to doctrine soon, but not silently as part of this review unless explicitly approved as doctrine implementation. It is strong enough for constitutional doctrine after one more alignment pass because it protects against the central anti-monolith failure mode: one project becoming ecosystem governor by convenience.

Current recommendation: treat as high-confidence doctrine candidate, not yet implemented as constitutional doctrine in this task.

confidence = 0.88
priority = 0.82

## 9. Ecosystem-infrastructure assessment

Future ecosystem infrastructure should remain distinct from projects.

Examples:

- project registries;
- recommendation registries;
- interface contracts;
- lineage records;
- ecosystem metadata;
- ecosystem-level decision indexes.

Recommended ownership boundary:

- infrastructure is not a project by default;
- infrastructure does not imply governance authority;
- infrastructure should not be assigned to EII by default;
- infrastructure should not be assigned to MetaHarvest by default;
- infrastructure should not be assigned to ProjectForge by default long-term;
- temporary hosting by ProjectForge may remain acceptable as a transitional convenience if clearly marked as non-authoritative.

Recommendation: keep ecosystem infrastructure as future-review material until it becomes substantial enough to need explicit ownership. Avoid premature infrastructure project creation.

## 10. Migration sequence recommendation

Safest sequence if restructuring eventually proceeds:

1. Terminology alignment.
   - Use `EIP` for the ecosystem.
   - Use `EII` for the future user-facing intelligence project.
   - Update active guidance surfaces before historical artifacts.

2. Explicit no-root-owner doctrine.
   - Decide whether `No project owns the EIP root` becomes guidance, doctrine, or constitutional doctrine.

3. Project creation location design.
   - Add explicit location selection to project-creation review/design.
   - Do not change default paths until workflow is approved.

4. ProjectForge de-hosting design.
   - Inventory tooling assumptions about `workspace/projects/`.
   - Decide how existing generated projects are treated.
   - Define compatibility/stub strategy.

5. MetaHarvest interface inventory.
   - Identify required consultation, recommendation, adoption, rejection, and retrieval contracts.
   - Do not implement contracts yet.

6. MetaHarvest extraction decision.
   - Decide if sibling status is worth physical separation.
   - If no, keep hosted and only consider physical rename.

7. MetaHarvest physical rename or extraction.
   - Perform only after path inventory, tests, and compatibility plan.
   - Prefer one coherent migration over rename-then-move unless smaller steps are safer.

8. Neutral EIP root adoption.
   - Create/adopt root only after project placement, infrastructure placement, and git/path strategy are decided.

9. Ecosystem infrastructure placement.
   - Move or create registries/contracts/lineage only after ownership and authority boundaries are explicit.

## 11. Conflicts found

Current active docs still contained the older meaning where `EIP` referred to the future user-facing project. That conflicts with the new terminology clarification.

Current ProjectForge structure still places generated/autonomous projects under ProjectForge's workspace by default. This does not violate doctrine if clearly transitional, but it conflicts with the long-term sibling-project conceptual architecture.

MetaHarvest is conceptually separable but physically hosted. This is acceptable as an explicit transitional state, but stale wording should not imply ProjectForge owns MetaHarvest's durable purpose.

## 12. Open questions

- Should `No project owns the EIP root` be promoted directly to constitutional doctrine?
- What exact filesystem root should EIP use if adopted?
- Should existing generated projects be migrated or left in place as historical ProjectForge-managed outputs?
- Should ProjectForge's default project path become configurable before neutral root adoption?
- Should generated-project `architecture/architectureharvest/` placeholders eventually become `architecture/metaharvest/`?
- Should MetaHarvest rename happen before extraction, after extraction, or only if extraction is rejected?
- What is the minimum viable interface contract set before MetaHarvest extraction?
- Should ecosystem infrastructure remain pure files, or eventually require a service/database? No answer is authorized now.
