# MetaHarvest Architecture Consolidation Review

Date: 2026-06-15
Status: review and recommendations only
Scope: conceptual consistency after MetaHarvest evolution
Physical directory: `ArchitectureHarvest/` remains unchanged

## Explicit non-actions

This review does not authorize or perform:

- commits;
- staging;
- directory renaming;
- project splitting;
- project creation;
- MacroForge modification;
- EIP modification;
- governance authority changes;
- interface implementation;
- ecosystem infrastructure implementation;
- new mandatory standards;
- repository restructuring.

## 1. Ownership review

Using ownership-by-purpose, the current MetaHarvest boundary is mostly coherent but needs continued discipline around domain, research-memory, and interface-contract boundaries.

### MetaHarvest

MetaHarvest owns reusable non-domain knowledge whose purpose remains valid across consuming projects:

- architecture patterns;
- interface patterns as knowledge;
- shared concepts and vocabulary as observed meaning;
- shared methodologies;
- decision patterns;
- governance patterns as advisory knowledge;
- heuristics;
- anti-patterns and failure patterns;
- recommendation reasoning and advisory evidence;
- adoption/rejection outcome lessons when generalized across projects.

MetaHarvest should not own the projects that consume this knowledge, the domain conclusions produced by those projects, or active ecosystem infrastructure.

### MacroForge

MacroForge owns economic-domain data, schemas, methods, conclusions, and investment-relevant reasoning:

- GDP/inflation/energy/company/domain analysis;
- macroeconomic interpretations;
- investment theses;
- source-specific and canonical economic modeling decisions;
- domain datasets and derived domain artifacts;
- project-local adoption decisions.

MetaHarvest may preserve a reusable validation workflow discovered in MacroForge, but not the macroeconomic conclusion reached by that workflow.

### ResearchMemory (future)

ResearchMemory, if ever approved, would likely own durable research conclusions, hypotheses, interpretations, literature context, and epistemic history. MetaHarvest should avoid becoming a repository of substantive research conclusions.

Boundary hypothesis:

- MetaHarvest: reusable non-domain method/pattern for how research is conducted, reviewed, classified, or synthesized.
- ResearchMemory: what the research concluded, why, with what evidence, and how the conclusion evolved.

This remains future-context only; no project is created or assumed.

### EIP (future)

EIP, if ever approved, would likely consume ecosystem outputs for user-facing synthesis, prioritization, personalization, briefing generation, and attention allocation.

MetaHarvest should not absorb:

- user-facing synthesis;
- personalized prioritization;
- attention allocation;
- briefing generation;
- command/routing authority over projects.

MetaHarvest can recommend reusable briefing or prioritization patterns, but EIP-like behavior remains outside MetaHarvest.

### Current wording risk

The phrase “projects, systems, architectures, implementations, successes, failures, concepts, methodologies, interfaces, governance structures, decision patterns, and heuristics” is broad. It is acceptable only because current doctrine constrains it to reusable non-domain knowledge and advisory-only behavior.

Risky interpretation to avoid:

- “MetaHarvest preserves all knowledge from projects.”

Correct interpretation:

- “MetaHarvest preserves reusable non-domain lessons extracted from projects.”

Recommendation: keep emphasizing “reusable,” “non-domain,” “advisory,” and “project-local adoption.”

## 2. Ecosystem knowledge review

The ecosystem now implicitly distinguishes five knowledge classes, but the distinction is not yet fully crisp.

### Project knowledge

Owned by the project. Includes project purpose, architecture, tasks, local decisions, implementation, local state, and local adoption decisions.

### Domain knowledge

Owned by domain projects. Includes substantive conclusions about a domain, domain data, domain models, and domain-specific evidence.

### Meta knowledge

Owned by MetaHarvest. Includes reusable non-domain patterns, methods, concepts, decision shapes, governance lessons, heuristics, and anti-patterns.

### User knowledge

Owned outside project governance, normally in Hermes user profile/memory or user-controlled notes. Includes preferences, goals, constraints, habits, personal priorities, and interaction style.

MetaHarvest should not absorb user profile knowledge, although it may preserve non-domain patterns about user-facing systems in abstract form.

### Ecosystem knowledge

Currently partly hosted by ProjectForge as a framework convenience. Includes known projects, descriptive registries, ecosystem lineage, cross-project recommendation status, interface contracts, and ecosystem-level decisions.

This is the least settled category. It is not identical to MetaHarvest. MetaHarvest may preserve patterns about ecosystem knowledge, but should not automatically own active ecosystem registries, active contracts, or ecosystem governance.

### Remaining ambiguity

The largest ambiguity is between meta knowledge and ecosystem knowledge:

- Meta knowledge: “what reusable lesson did we learn?”
- Ecosystem knowledge: “what is currently true about this ecosystem?”

Recommendation: keep MetaHarvest focused on reusable lessons and advisory recommendations. Keep live ecosystem state and active contracts separate, currently as ProjectForge-hosted descriptive infrastructure until future review.

## 3. Interface knowledge vs interface contracts

The distinction is useful and should be preserved.

### Interface knowledge

Interface knowledge is reusable non-domain learning about interfaces:

- recommendation exchange patterns;
- notification patterns;
- review patterns;
- schema-evolution lessons;
- lineage patterns;
- failure modes in contracts;
- examples of good or bad interface separation.

This fits MetaHarvest.

### Interface contracts

Interface contracts are active ecosystem infrastructure:

- the active recommendation schema;
- the active registry contract;
- active ecosystem interface definitions;
- contract versioning policy;
- compatibility commitments;
- producer/consumer obligations.

These should not be owned by MetaHarvest by default. They are operational agreements between projects or ecosystem infrastructure.

### Recommendation

MetaHarvest should own interface knowledge, not active interface contracts.

Active interface contracts should remain ecosystem infrastructure, currently ProjectForge-hosted when necessary, until future review determines whether shared infrastructure needs a dedicated owner.

MetaHarvest may recommend changes to interface contracts but must not impose or implement them automatically.

## 4. Ownership-by-purpose doctrine assessment

Candidate doctrine:

> Capabilities should be owned by the project whose purpose remains valid if all consuming projects disappear.

### Usefulness

High. It prevents ownership-by-history and accidental monolith growth. It is especially useful for separating:

- MetaHarvest-owned advisory knowledge;
- ProjectForge-owned framework creation/governance;
- MacroForge-owned domain knowledge;
- future EIP-owned user-facing synthesis;
- future ecosystem-infrastructure responsibilities.

### Limitations

The test is not sufficient alone. A capability may remain valid without current consumers but still not deserve independent ownership or project creation.

Additional checks remain needed:

- lifecycle difference;
- governance concerns;
- data model difference;
- maintenance burden;
- interface clarity;
- actual recurring need;
- risk of fragmentation.

### Edge cases

- Shared schemas: may remain useful without a consumer, but active contracts require ecosystem coordination.
- Adoption logs: local adoption decisions belong to projects; generalized lessons may belong to MetaHarvest.
- Registries: descriptive live ecosystem state is not the same as reusable knowledge.
- User-facing synthesis: patterns can be MetaHarvest; actual synthesis/personalization would belong elsewhere.
- Research conclusions: research methodology can be MetaHarvest; substantive conclusions likely belong to ResearchMemory or domain projects.

### Relationship to project-autonomy doctrine

Ownership-by-purpose is a useful refinement of project-autonomy and anti-monolith doctrine. It clarifies where capabilities belong when current physical location and development history are misleading.

Recommendation: keep as guidance for now. Consider promotion to doctrine after it is tested against ecosystem infrastructure, interface contracts, MetaHarvest/MacroForge boundaries, and future ResearchMemory/EIP boundaries. Do not promote automatically to constitutional doctrine yet.

## 5. Remaining inconsistencies

### Inconsistency: future ecosystem vision still names ArchitectureHarvest

ProjectForge constitution line-level wording still includes ArchitectureHarvest in the future ecosystem vision. This is not a functional blocker because later text explains ArchitectureHarvest / MetaHarvest, but future wording should eventually say “MetaHarvest (formerly ArchitectureHarvest)” for conceptual consistency.

Recommendation: low-priority bounded doctrine cleanup later.

### Inconsistency: ArchitectureHarvest v1 wording remains in places

Some local docs still say “ArchitectureHarvest v1.” This is acceptable while the physical directory remains unchanged, but future edits should avoid implying architecture-only scope.

Recommendation: use “ArchitectureHarvest / MetaHarvest” when discussing current hosted implementation and “MetaHarvest” when discussing durable purpose.

### Ambiguity: ecosystem knowledge owner

Project registries, recommendation registries, interface contracts, ecosystem lineage, and ecosystem-level decisions are emerging as shared infrastructure. Current doctrine says ProjectForge may host descriptive registry responsibilities temporarily. That remains adequate, but not permanently resolved.

Recommendation: preserve as future-review question only.

### Ambiguity: soft governance

Repeated high-confidence recommendations may become de facto governance through habit, even if formally advisory.

Recommendation: preserve as future-review question only.

### Ambiguity: adoption outcome ownership

A project owns its local adoption decision. MetaHarvest may own generalized cross-project lessons. The boundary should remain explicit in future artifacts.

## 6. Recommendations

1. Keep conceptual name MetaHarvest; defer physical rename.
2. Keep MetaHarvest non-domain and advisory-only.
3. Distinguish reusable knowledge from live ecosystem state.
4. Distinguish interface knowledge from active interface contracts.
5. Keep ownership-by-purpose as guidance, not constitutional doctrine yet.
6. Record ecosystem infrastructure ownership as future review only.
7. Record commit-boundary intelligence as advisory MetaHarvest opportunity only.
8. Record soft-governance risk as future review only.
9. Avoid adding new schemas until concrete repeated use proves existing templates insufficient.
