# Architecture

ProjectForge has six current framework layers. Generated projects are outputs of the framework, not subordinate runtime components owned by ProjectForge.

## 1. Global Foundation
Reusable skills, agent role documents, permissions, logging utilities, project templates, and ProjectForge-level governance.

## 2. Bootstrap Layer
`tools/new_project.py` consumes Hermes-captured answers or a terminal fallback, renders a generated project, records setup decisions, and initializes lightweight architecture review and MetaHarvest participation files when appropriate.

Project creation is a Hermes-led discovery conversation. `config/setup_questionnaire.yaml` is a coverage map, not a rigid script. Questions are doctrinally classified as FOUNDATIONAL, ARCHITECTURAL, IMPLEMENTATION, or PREFERENCE; foundational questions should explain why they matter, what depends on them, and why they should be resolved now. The goal is clarity of purpose, not maximum questioning.

## 3. Generated Project Output Layer
Generated projects include state files, decision/task artifacts, logging, permissions, optional specialized agents, and `architecture/` scaffolding for architecture state, reviews, and MetaHarvest relevance/outcome tracking.

Generated projects become autonomous at creation. ProjectForge improves itself and future inheritance, but it does not own instantiated project goals, architecture, implementation, task execution, or adoption decisions.

## 4. Continuity and Recovery Layer
`tools/recover_session.py`, `recovery/continuity_framework.md`, `context/latest_handoff.md`, concise state pointers, task artifacts, decision artifacts, context health, and coherence checks provide bounded fresh-session recovery and standard closeout. The layer extends existing file-backed governance; it is not a database, vector store, daemon, raw-log index, or parallel state system.

The standard closeout command is sufficient: `Perform standard ProjectForge closeout. Follow the continuity framework. Then stop.` The standard recovery command is sufficient: `Recover project state and continue work.` Generated projects inherit this layer through shared templates; existing projects adopt only through explicit project-local approval or a user-named task.

## 5. Project-Local Task Standard Layer
ProjectForge defines reusable task artifact, state, handoff, summary, and verification standards. Instantiated projects own their own task execution through project-local governance.

Temporary task context is stored in `state/active_goal.md`, `artifacts/tasks/`, and run logs. MetaHarvest is not consulted for ordinary implementation tasks that do not alter architecture.

## 6. Reusable Knowledge Intelligence Layer
`MetaHarvest/` is currently hosted within ProjectForge as a file-backed librarian, reference system, evidence repository, and advisory subsystem. Its conceptual long-term name is MetaHarvest because its durable purpose now covers reusable non-domain knowledge, not architecture patterns alone. It is conceptually separable and potentially capable of future independent operation, but it is not split into a separate project in the current architecture and the physical directory remains `MetaHarvest/`.

MetaHarvest discovers, preserves, analyzes, organizes, and recommends reusable non-domain knowledge: architecture patterns, interface patterns, shared concepts, shared vocabulary, shared methodologies, decision patterns, governance patterns, heuristics, anti-patterns, and failure patterns. It stores problem-first retrieval indexes, synthesized pattern records, contradiction records, outcome models, relevance maps, advisory recommendations, rejection/retirement records, adoption outcomes, audits, and reports.

MetaHarvest remains advisory and non-domain. It may preserve reusable methods discovered while working on domain projects, but domain conclusions such as GDP analysis, inflation analysis, energy-market knowledge, macroeconomic conclusions, investment theses, and company research belong to domain projects. It may recommend task consideration, but it must not create tasks inside target projects, decide adoption, modify projects, enforce standards, force migration, or act as a controller.

The consultation path is compact-first: problem catalog, retrieval index, synthesis, contradictions, outcomes, relevance maps, then deep reports only when necessary. Consultation is required for major architecture decision points and scheduled reviews; during new project creation, consult it when architectural uncertainty or relevant pattern evidence exists.

## Governance permission layer
ProjectForge uses a four-level permission ladder for governance-sensitive work:

- L1 Operational: routine implementation inside approved scope.
- L2 Architectural: project-local architecture changes; explicit approval before implementation.
- L3 Strategic: scope expansion, ecosystem interaction, extraction recommendations, major governance additions, or new long-term responsibilities; approval plus `GOVERNANCE_WARNING` required.
- L4 Foundational: purpose, doctrine, constitution, ecosystem ownership, project creation/split/merge, or authority-boundary changes; stop implementation until explicit foundational approval plus `FOUNDATIONAL_GOVERNANCE_WARNING`.

A project's approved purpose is protected. Hermes may recommend expansion or extraction, but may not silently expand, redefine, substantially reinterpret, or absorb responsibilities that materially alter project identity.

Confidence and priority are advisory metadata, not authority. Repeated high-confidence recommendation acceptance is evidence, not governance authority.

## Framework-change doctrine
A framework change affects inheritance, templates, governance, questioning, artifact standards, handoff standards, delegation infrastructure, worker infrastructure, framework doctrine, or MetaHarvest doctrine. The user should be explicitly informed when a framework-level change is being made.

## Improvement flow
ProjectForge improvements affect future inheritance by default. Existing projects receive recommendations or improvement notices, review them locally, and decide adoption through their own governance. ProjectForge must not silently propagate changes into existing projects.


## Ecosystem autonomy and interfaces
Projects in the ecosystem communicate through explicit interfaces and artifacts where practical: documented contracts, manifests, registries, structured recommendations, and review records. These interfaces preserve autonomy; they do not grant governance authority.

The workspace registry is descriptive, not authoritative. Long-term ownership of an ecosystem-level registry is TBD through future ecosystem governance review. No project owns the EIP root; if adopted later, it represents ecosystem organization and neutral infrastructure, not project authority.

Future concepts such as the EIP ecosystem, ResearchMemory, EconGraph, MonitorForge, ReportForge, EII, and future ecosystem infrastructure are boundary-awareness context only. EIP means Economic Intelligence Platform, the ecosystem as a whole; EII means Economic Intelligence Initiative, a possible future user-facing intelligence project. They are not current implementation targets.

Project extraction readiness has two layers: conceptual readiness depends on purpose, ownership, authority, and interface boundaries; physical extraction additionally requires path inventory, ownership inventory, compatibility planning, verification planning, rollback planning, and stable evidence references. Filesystem structure is a migration constraint, not governance authority.

## Automation doctrine
Automation is not a goal. Automation is justified only when it is reliable, understandable, maintainable, testable, coherent, observable, and reversible. Correctness takes precedence over automation.

Useful automation improves correctness, continuity, verification, or maintainability. Automation theater creates machinery without reliable, understandable, testable value.

## Deferred specification
If a decision cannot be made during setup or architecture analysis, it must be written as a deferred decision artifact. Agents should later ask for specification when that decision becomes relevant.

## Clarification severity
Questions are classified as:

- L1: Silent autonomy. The agent may proceed.
- L2: Batched clarification. Ask later; continue if safe.
- L3: Blocking clarification. Pause and ask immediately.
- L4: Emergency stop. Stop execution and require explicit human action.
