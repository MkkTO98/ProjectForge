# ProjectForge Constitution

ProjectForge exists to create and improve reusable, durable, agent-assistable project frameworks.

It helps projects begin with a clear purpose, durable structure, continuity across sessions, correctness-oriented workflows, explicit governance, file-backed state, durable decisions, bounded delegation paths, and increasing ability to delegate reliable work from humans to cloud LLMs to local systems while preserving correctness and maintainability.

ProjectForge is a reusable framework. It is not an active project manager, a meta-controller, or the owner of instantiated projects after creation. Generated projects become autonomous at creation time.

ProjectForge canonizes proven architectural patterns. Lessons learned in one project should improve future projects only when they solve recurring framework problems. A framework improvement should answer:

1. What recurring problem caused this improvement?
2. What future projects benefit from it?
3. Why should this become framework behavior instead of project-specific behavior?
4. What implementation evidence shows the pattern has converged beyond one project?

## Non-negotiable rules

1. Project state must be explicit on disk, not hidden in chat memory.
2. Setup answers and deferred specifications must be stored as decision artifacts under `artifacts/decisions/`.
3. Agents must not silently invent project-wide policy. If a decision is absent, ambiguous, or conflicting, use deferred specification and clarification severity rules.
4. GitHub pushes require human approval by default. Auto-commit is allowed only after validation passes and policy permits it.
5. Dry-run/preflight is mandatory according to the risk-scaled dry-run policy in `simulation/dry_run_policy.yaml`.
6. Capability failures escalate to stronger local models before cloud models and before humans. Permission, safety, credential, destructive, monetary, or strategic decisions escalate to humans.
7. Specialized agents are never created silently. ProjectForge may request one with a short explanation; after approval, it may generate the agent automatically.
8. Skills should be small and composable by default. Large playbooks are allowed only for complex domains.
9. Metrics must be used to improve agents, tools, model routing, templates, and task workflows, but not to justify opaque automation.
10. The system must remain understandable from ordinary files: Markdown, YAML, JSON, and JSONL.
11. Raw logs are audit/debug artifacts only and must not be loaded into normal task context.
12. Cloud/Codex model calls require a context audit. Compact governance calls use the configured governance budget; justified project-wide reviews, redesigns, strategic reviews, gap analyses, and architecture audits may use the larger configured project-wide review budget.
13. Framework-level changes must be named explicitly. The user should be told when a change affects framework doctrine, inheritance, templates, governance, questioning, artifact standards, handoff standards, delegation infrastructure, worker infrastructure, or MetaHarvest doctrine.

## Framework boundary

ProjectForge owns reusable framework concerns:

- framework doctrine;
- project creation procedures;
- reusable structure;
- reusable governance;
- reusable standards;
- reusable questioning procedures;
- reusable handoff procedures;
- reusable delegation infrastructure;
- reusable verification and coherence expectations.

ProjectForge does not own instantiated project concerns:

- instantiated project goals;
- instantiated project architecture;
- instantiated project implementation;
- instantiated project task execution;
- instantiated project adoption decisions.

ProjectForge must never silently mutate existing projects. It may modify an instantiated project only when that project is explicitly named as the approved target of a separate task.

## Architecture freeze and canonization doctrine

ProjectForge v1 has five architectural systems:

1. Project Identity.
2. Context and Continuity.
3. Governance and Decision.
4. Work Execution Methodology.
5. Validation and Evidence.

These systems are stable infrastructure. Future architectural work should assume they remain the permanent foundation unless implementation evidence proves otherwise.

No new architectural subsystem may be introduced merely because it appears useful. A sixth subsystem may be created only when repeated implementation evidence from multiple independent generated projects demonstrates that an existing subsystem cannot reasonably own the responsibility. Architectural elegance, theoretical completeness, abstraction opportunities, or anticipated reuse are insufficient evidence.

ProjectForge does not attempt to predict future architecture. Reusable capabilities should first emerge independently in generated projects. Only after repeated convergence should they be promoted into ProjectForge. ProjectForge canonizes patterns, not examples, projects, or domains.

Generated projects remain autonomous after creation. ProjectForge has no ongoing architectural authority over generated projects. Future improvements to ProjectForge do not implicitly modify existing generated projects; adoption is always an explicit generated-project decision.

Every ProjectForge artifact, tool, template, policy, and document should belong clearly to exactly one of the five architectural systems. If ownership cannot be identified, either the artifact is misplaced, the subsystem boundaries need evidence-backed refinement, or the artifact should not exist. Avoid shared miscellaneous infrastructure.

ProjectForge should remain intentionally small. Adding reusable infrastructure carries ongoing maintenance cost, so the burden of proof lies with expansion. When uncertain, leave a capability inside an individual project until repeated evidence demonstrates broader reuse.

## Ecosystem autonomy doctrine

The long-term ProjectForge ecosystem is a set of autonomous projects, not a monolith and not a controller hierarchy. Every project must retain its own purpose, scope, governance, lifecycle, artifacts, and decision history.

Projects may interact through recommendations, notifications, documented interfaces, shared context, manifests, registries, and explicit contracts. Projects may not govern other projects, directly modify other projects, create tasks inside other projects, or assume authority over other projects.

A project owns only its approved purpose. When new functionality appears adjacent but not clearly inside the current purpose, Hermes must ask whether it still belongs to the current project. If the answer is uncertain, escalate for review instead of expanding scope by default.

Projects may be aware that future projects are envisioned, but they must not optimize for hypothetical future projects. Future projects are architectural context and possible escalation targets only; they are not implementation targets until explicitly approved.

## Permission ladder and escalation doctrine

ProjectForge uses four governance permission levels to protect project purpose, ecosystem architecture, and human attention.

### L1 — Operational

Routine implementation inside the current approved scope.

Examples include tests, reports, documentation updates, small refactors, task creation inside the current project, and implementation of already-approved work.

No special escalation is required beyond normal safety, verification, and task discipline.

### L2 — Architectural

Project-local architectural change.

Examples include a new subsystem, new storage model, major schema change, new integration layer, major workflow change, or project-local permission/model-routing/context architecture change.

Explicit approval is required before implementation. The proposal should state impact, risk, and verification path.

### L3 — Strategic

Scope expansion, ecosystem interaction, or cross-project implications.

Examples include significant cross-project recommendations, project-boundary changes, major governance additions below constitutional level, ecosystem-facing capabilities, extraction recommendations, new long-term responsibilities, or recommendations likely to create implicit authority.

Explicit approval is required before implementation. A structured L3 warning block is mandatory.

### L4 — Foundational

Purpose, doctrine, ecosystem, constitutional, or authority-boundary change.

Examples include project purpose changes, project merges, project splits, new project creation, governance-doctrine changes, constitutional changes, ecosystem ownership changes, and authority-boundary changes.

Implementation must stop until explicit foundational approval is received. A structured L4 warning block is mandatory.

## Project purpose protection doctrine

A project's approved purpose is protected. Purpose is not an implementation detail.

Hermes may identify tensions, identify opportunities, recommend expansions, recommend extraction, and document rationale, expected value, implementation effort, architectural impact, confidence, priority, and lineage.

Hermes may not silently expand a project's purpose, redefine its purpose, substantially reinterpret its purpose, or absorb new responsibilities that materially alter project identity.

Purpose changes require L4 foundational approval.

## Governance warning-block doctrine

L3 and L4 proposals must be visibly marked so high-impact decisions remain obvious when copied into ChatGPT, pasted into another agent, or skimmed quickly.

L3 warning format:

```text
GOVERNANCE_WARNING
PERMISSION_LEVEL=L3
CATEGORY=STRATEGIC
PROJECT=<project-or-scope>
DECISION=<short decision name>

Impact:
<concise impact statement>

Risk:
<concise risk statement>

Required approval:
Explicit approval required before implementation.
END_GOVERNANCE_WARNING
```

L4 warning format:

```text
FOUNDATIONAL_GOVERNANCE_WARNING
PERMISSION_LEVEL=L4
CATEGORY=FOUNDATIONAL
PROJECT=<project-or-scope>
DECISION=<short decision name>

Impact:
Project purpose, doctrine, ecosystem structure, constitutional rule, or authority boundary may be affected.

Risk:
Implementation without explicit approval could silently change project identity, governance authority, or ecosystem architecture.

Required approval:
STOP. Implementation prohibited without explicit foundational approval.
END_FOUNDATIONAL_GOVERNANCE_WARNING
```

For L3 and L4 proposals, include a concise explanation, explicit impact statement, explicit risk statement, and explicit approval request.

## Recommendation authority doctrine

Recommendation confidence, priority, and authority are distinct.

Confidence describes belief that a recommendation is correct or well-supported. Priority describes perceived value, urgency, or sequencing importance. Authority describes permission to decide or implement.

Confidence and priority do not imply authority. Repeated acceptance of high-confidence recommendations is evidence, not governance authority. Recommendations remain advisory until adopted through project-local governance and any required approval level.

Use decimal representation for confidence, priority, likelihood, and uncertainty when meaningful, such as `confidence = 0.83` or `priority = 0.72`. Avoid percentages unless externally required. Avoid false precision; use qualitative labels when numeric estimates would be misleading.

## Scope extraction and anti-monolith doctrine

A capability should be considered for extraction when one or more of the following are strongly true:

- it has its own purpose;
- it has its own lifecycle;
- it has its own governance concerns;
- it has its own data model;
- it could reasonably survive if the originating project disappeared;
- adding it would materially expand the originating project's approved purpose.

When extraction pressure is detected, the output must be a recommendation artifact, not automatic project creation, task creation, or implementation. The recommendation must include rationale, expected value or benefit, implementation effort estimate, architectural impact estimate, confidence when meaningful, priority when meaningful, and lineage.

## Project creation threshold doctrine

Projects may recommend new projects. Projects may not create new projects automatically.

Creating a new project is a foundational ecosystem decision and requires explicit human approval. A project-creation recommendation must include supporting rationale, expected value, implementation effort estimate, architectural impact estimate, and why the responsibility has a distinct purpose, would materially expand the originating project, or could survive if the originating project disappeared.

## Extraction-readiness doctrine

Project extraction decisions should be evaluated in two separate layers.

Conceptual extraction readiness depends primarily on purpose, ownership boundaries, authority boundaries, and interface boundaries. A responsibility is conceptually extraction-ready only when it has a durable purpose, clear ownership of its own knowledge/artifacts, clear limits on its authority over other projects, and explicit ways to exchange context, recommendations, outcomes, evidence, staleness signals, and reusable lessons without taking over consumer-project governance.

Physical extraction additionally requires path inventory, artifact ownership inventory, compatibility planning, verification planning, rollback planning, and evidence-reference stability. Filesystem structure is evidence and migration constraint; it is not governance authority by itself.

Do not confuse architectural readiness with migration readiness. A subsystem may be conceptually ready but operationally blocked by path dependencies, compatibility risks, evidence-reference risks, or unclear artifact ownership. Conversely, an easy filesystem move is not justified unless purpose, ownership, authority, and interface boundaries support independent existence.

## Recommendation persistence doctrine

Recommendations are ecosystem artifacts. They must remain discoverable after review so the ecosystem does not repeatedly rediscover the same idea.

Recommendation records should preserve review outcomes, adoption outcomes, rejection rationale, adoption rationale, and supersession lineage. Review outcome and implementation outcome are distinct. Adoption by one project does not imply adoption by another project.

Rejected recommendations must remain discoverable when meaningful. Preserve the recommendation identifier or title, origin, date, target project or scope, review outcome, rejection rationale, relevant context, and supersession or revisit condition when useful. Rejection memory preserves negative knowledge; it does not imply the rejected recommendation should be revisited automatically.

## Ecosystem registry doctrine

The workspace project registry is descriptive. It helps humans and agents find known projects, purposes, interfaces, dependencies, ownership notes, and ecosystem roles when those fields exist. It is not authoritative governance, does not grant write authority, and does not make ProjectForge the owner of registered projects.

Until a dedicated ecosystem-level owner or neutral infrastructure home is approved, ProjectForge may maintain a descriptive registry as a framework convenience. Long-term ownership is TBD through future ecosystem governance review, not assigned to EII, MetaHarvest, ProjectForge, or any other project by default. EIP refers to the ecosystem, not a project owner.

## EIP-root ownership doctrine

No project owns the EIP root.

ProjectForge, MetaHarvest, MacroForge, EII, ResearchMemory, and future projects may participate in the EIP ecosystem, but none owns the ecosystem root by default. The EIP root represents ecosystem organization and possible neutral infrastructure, not project authority.

Root-level ecosystem artifacts must not be interpreted as granting one project authority over another unless explicit foundational governance says so. Temporary hosting of ecosystem-facing artifacts inside a project remains transitional convenience, not ownership transfer.

The durable ecosystem capability ownership matrix lives at `/home/mkkto/srv/EIP/governance/CAPABILITY_OWNERSHIP.md`. It classifies knowledge storage, publication, retrieval, change discoverability, relevance evaluation, prioritization, notification routing, ecosystem coordination, domain intelligence, and future EII boundaries. If a proposed owner differs from that matrix, treat the proposal as a foundational doctrine change rather than an implementation detail.

## Improvement and adoption doctrine

ProjectForge may improve itself and may improve future inheritance only under the architecture-freeze and canonization doctrine above. ProjectForge improvements affect future inheritance by default.

Existing projects remain autonomous. They may receive improvement notices, recommendations, migration suggestions, or adoption checklists, but they decide relevance and adoption through their own governance.

Preferred flow:

```text
ProjectForge improvement -> improvement notice -> project review -> project decision -> optional adoption
```

ProjectForge does not force adoption and does not silently propagate changes into existing projects.

## Questioning doctrine

Project creation should be a Hermes-led discovery conversation, not merely a questionnaire. `config/setup_questionnaire.yaml` is a coverage map, not a rigid user-facing script.

Hermes should ask focused questions, provide context, explain consequences, identify weak assumptions, challenge unclear goals, explain tradeoffs, reuse known context, and defer implementation details when possible.

Question classes are doctrinally recognized:

- `FOUNDATIONAL`: purpose, success, users, non-goals, correctness standards, and other choices that determine whether ProjectForge is creating the right project. These should usually explain why they matter, what depends on them, what goes wrong if unresolved, and why they should be resolved now.
- `ARCHITECTURAL`: structure, interfaces, storage, runtime, deployment, integrations, trust boundaries, and maintainability choices. Resolve before creation when they affect scaffold shape or safety; otherwise record deferred decisions.
- `IMPLEMENTATION`: libraries, packages, APIs, schemas, providers, commands, or low-level implementation details. Defer whenever possible unless they affect foundational viability or immediate scaffold choice.
- `PREFERENCE`: style, workflow, naming, branch habits, documentation depth, notification channels, and personal defaults. Capture when useful, but do not block creation unless safety or correctness depends on them.

The goal is clarity of purpose, not maximum questioning.

## Automation doctrine

Automation is not a goal. Automation is justified only when it is reliable, understandable, maintainable, testable, coherent, observable, and reversible.

Correctness takes precedence over automation. ProjectForge should encourage movement of bounded work from human to cloud LLM to local systems when reliability improves and recurring human burden decreases.

Useful automation improves correctness, continuity, verification, or maintainability without hiding decisions or bypassing governance.

Automation theater is automation that creates machinery without reliable, understandable, testable value. Automation theater includes systems that create side effects faster than they can be reviewed, scanners with no clear review path, workers that exist before real work requires them, generated tasks without project-local approval, or metrics that justify opaque behavior.

## Server infrastructure doctrine

Infrastructure exists to support ecosystem goals. Servers, GPUs, storage systems, orchestration layers, automation platforms, and local AI hardware are means, not the objective.

Architectural decisions should optimize for research quality, information quality, maintainability, attention allocation, and long-term ecosystem value. Avoid infrastructure-driven development.

## Default operating posture

The default is AI-first project execution under human-designed constraints. Humans specify constitution, risk boundaries, and project intent; agents execute inside those boundaries.

## Future ecosystem vision

EIP means `Economic Intelligence Platform`: the future ecosystem as a whole, not a project. EIP may eventually contain autonomous projects or project concepts such as ProjectForge, MacroForge, MetaHarvest, ResearchMemory, EconGraph, MonitorForge, ReportForge, EII, and future ecosystem infrastructure.

EII means `Economic Intelligence Initiative`: a possible future user-facing intelligence project. EII is provisionally understood as a consumer, synthesizer, prioritizer, personalizer, attention-allocation layer, briefing generator, and recommender of ecosystem outputs, not a governor of projects and not the owner of EIP.

These names are non-binding architectural context only unless separately approved. They are not approved implementation targets, do not grant governance authority, and must not be used to justify scope expansion inside an existing project.

## MetaHarvest / MetaHarvest advisory rule

MetaHarvest is an autonomous sibling EIP project at `/home/mkkto/srv/EIP/projects/MetaHarvest`. ProjectForge consumes MetaHarvest through the configured external provider interface and must not host a full MetaHarvest project tree. The `architecture/architectureharvest/` generated-project path remains a compatibility path for historical ArchitectureHarvest lineage and generated-project artifacts.

MetaHarvest is a librarian, reference system, evidence repository, and advisory knowledge system. It discovers, preserves, analyzes, organizes, and recommends reusable non-domain knowledge including architecture patterns, interface patterns, shared concepts, shared vocabulary, shared methodologies, decision patterns, governance patterns, heuristics, anti-patterns, and failure patterns. It is consulted for architectural and reusable-knowledge judgment, not daily implementation control.

MetaHarvest remains non-domain. Domain conclusions such as GDP analysis, inflation analysis, energy-market knowledge, macroeconomic conclusions, investment theses, and company research belong to domain projects. MetaHarvest may preserve reusable non-domain methods or patterns discovered while working on domain projects.

MetaHarvest consultation starts problem-first: problem catalog, retrieval index, synthesized pattern records, contradiction records, adoption outcomes, and target relevance maps before project/component/deep reports. Recommendations may be strong, but they must separate generic evidence from ProjectForge ecosystem outcomes and explain maturity, evidence strength, local fit, tradeoffs, confidence, and limitations.

MetaHarvest consultation is required for architecture definition, major architecture modifications, introduction of new subsystems, creation of new agent roles, memory/context system design, orchestration design, permission system design, workflow redesign, scheduled architecture reviews, repeated implementation failures, user-requested improvement scans, and reviews of reusable non-domain concepts, vocabulary, methodologies, decision patterns, governance patterns, or heuristics. New project creation should use MetaHarvest when architectural uncertainty or relevant pattern evidence exists; simple projects should not be forced into unnecessary ceremony.

MetaHarvest consultation is not required for bug fixes, minor documentation changes, test additions, small utilities, domain analysis, or implementation work that does not alter architecture or reusable methodology.

MetaHarvest may create recommendations, task recommendation proposals, rejection records, and adoption outcome records, but it may never decide adoption, force implementation, bypass project governance, bypass approval gates, create tasks inside another project, create autonomous refactoring campaigns, create architecture changes without review, continuously scan all projects during ordinary development, enforce standards, or modify target projects directly.
